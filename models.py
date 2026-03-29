from datetime import datetime
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin
import secrets

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(255), nullable=False)
    
    # Two-Factor Authentication Fields
    totp_secret = db.Column(db.String(32), nullable=True)
    is_2fa_enabled = db.Column(db.Boolean, default=False)
    backup_codes = db.Column(db.String(500), nullable=True)
    
    # Relationships
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    ratings = db.relationship('Rating', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, max_age=1800)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def generate_backup_codes(self, num_codes=5):
        """Generate secure backup codes for 2FA"""
        backup_codes = [secrets.token_hex(4) for _ in range(num_codes)]
        self.backup_codes = ','.join(backup_codes)
        return backup_codes

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.ut
