import os
import secrets
from PIL import Image
from flask import current_app, url_for
from flask_mail import Message
from flaskblog import mail, ph

def save_picture(form_picture):
    """Save profile picture with unique filename"""
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    
    # Resize image
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn

def send_reset_email(user):
    """Send password reset email"""
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@bonnyriggpizza.com',
                  recipients=[user.email])
    
    reset_url = url_for('users.reset_token', token=token, _external=True)
    msg.body = f'''To reset your password, visit the following link:
{reset_url}

If you did not make this request, simply ignore this email and no changes will be made.
'''
    
    try:
        mail.send(msg)
        return True
    except Exception as e:
        current_app.logger.error(f"Email send error: {str(e)}")
        return False

def verify_password(stored_password, provided_password):
    """
    Verify password using Argon2 with secure comparison
    
    Args:
        stored_password (str): Hashed password from database
        provided_password (str): Password attempt from user
    
    Returns:
        bool: True if password matches, False otherwise
    """
    try:
        ph.verify(stored_password, provided_password)
        return True
    except:
        return False
