from flask import Blueprint, render_template, url_for, flash, redirect, request, session
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, ph, limiter
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm, 
                                   RequestResetForm, ResetPasswordForm, 
                                   TOTPSetupForm, TOTPVerifyForm)
from flaskblog.users.utils import save_picture, send_reset_email
import pyotp
import qrcode
import io
import base64
import secrets

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = ph.hash(form.password.data)
        user = User(username=form.username.data, 
                    email=form.email.data, 
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in', 'success')
        return redirect(url_for('users.login'))
    
    return render_template('register.html', title='Register', form=form)

@users.route("/login", methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user:
            try:
                # Verify password using Argon2
                ph.verify(user.password, form.password.data)
            except:
                flash('Invalid email or password', 'danger')
                return render_template('login.html', title='Login', form=form)
            
            # Check if 2FA is enabled
            if user.is_2fa_enabled:
                # Store user ID in session for 2FA verification
                session['pre_2fa_user_id'] = user.id
                return redirect(url_for('users.verify_2fa'))
            
            # Log in user directly if 2FA is not enabled
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.home'))
        
        flash('Login Unsuccessful. Please check email and password', 'danger')
    
    return render_template('login.html', title='Login', form=form)

@users.route("/2fa/setup", methods=['GET', 'POST'])
@login_required
def setup_2fa():
    form = TOTPSetupForm()
    
    if not current_user.totp_secret:
        # Generate a new secret if not exists
        current_user.totp_secret = pyotp.random_base32()
        db.session.commit()
    
    # Generate QR Code
    totp = pyotp.TOTP(current_user.totp_secret)
    provisioning_url = totp.provisioning_uri(
        name=current_user.email, 
        issuer_name="Bonnyrigg Pizza"
    )
    
    qr = qrcode.make(provisioning_url)
    qr_buffer = io.BytesIO()
    qr.save(qr_buffer, 'PNG')
    qr_buffer.seek(0)
    qr_base64 = base64.b64encode(qr_buffer.getvalue()).decode()
    
    if form.validate_on_submit():
        # Verify the code entered by user
        totp = pyotp.TOTP(current_user.totp_secret)
        if totp.verify(form.token.
