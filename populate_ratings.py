from flaskblog import create_app, db
from flaskblog.models import Rating, Post, User
from random import randint, choice
from datetime import datetime, timedelta

app = create_app()

with app.app_context():
    # Create some test users for ratings
    test_users = []
    usernames = ['Foodie123', 'ChefMike', 'HomeCook', 'RecipeLover', 'CulinaryFan', 'TasteTester']

    for username in usernames:
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(
                username=username,
                email=f'{username.lower()}@example.com',
                password='password',
                image_file='default.jpg'
            )
            db.session.add(user)
            test_users.append(user)
        else:
            test_users.append(user)

    db.session.commit()

    # Get all posts
    posts = Post.query.all()

    # Clear existing ratings
    Rating.query.delete()
    db.session.commit()

    # Add random ratings to each post
    for post in posts:
        # Each post gets 3-6 random ratings
        num_ratings = randint(3, 6)

        for _ in range(num_ratings):
            user = choice(test_users)
            # Make sure user hasn't already rated this post
            existing_rating = Rating.query.filter_by(user_id=user.id, post_id=post.id).first()
            if not existing_rating:
                rating_value = randint(3, 5)  # Mostly positive ratings
                rating = Rating(
                    value=rating_value,
                    user_id=user.id,
                    post_id=post.id,
                    date_posted=datetime.utcnow() - timedelta(days=randint(0, 30))
                )
                db.session.add(rating)

    db.session.commit()
    print("Fake ratings added to recipes!")