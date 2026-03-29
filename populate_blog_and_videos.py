from flaskblog import create_app, db
from flaskblog.models import BlogPost, Post, User
from datetime import datetime

app = create_app()

with app.app_context():
    # Get the admin user
    user = User.query.filter_by(username='BonnyriggChef').first()
    if not user:
        user = User(username='BonnyriggChef', email='admin@bonnyrigg.com', password='password')
        db.session.add(user)
        db.session.commit()

    # Clear existing blog posts
    BlogPost.query.delete()
    db.session.commit()

    # Create popular blog posts with YouTube video links
    blog_posts = [
        {
            'title': 'Knife Skills 101',
            'content': '''
            <h3>Master the Fundamentals of Kitchen Knife Work</h3>
            <p>Proper knife skills are the foundation of good cooking. Learn the essential techniques that every home cook should know.</p>

            <h4>Essential Cuts to Master:</h4>
            <ul>
                <li><strong>Julienne:</strong> Thin, matchstick-sized strips perfect for stir-fries</li>
                <li><strong>Brunoise:</strong> Tiny, uniform cubes for fine diced vegetables</li>
                <li><strong>Chiffonade:</strong> Thin ribbons of leafy greens and herbs</li>
                <li><strong>Batonnet:</strong> Thick matchsticks for hearty vegetables</li>
            </ul>

            <h4>Safety First:</h4>
            <ul>
                <li>Always use a sharp knife - dull knives are more dangerous</li>
                <li>Keep your fingers curled under (claw grip) when chopping</li>
                <li>Use a stable cutting board that won't slip</li>
                <li>Never try to catch a falling knife</li>
            </ul>

            <p>Watch the video below for a complete demonstration of these techniques:</p>
            '''
        },
        {
            'title': 'Winter Comfort Foods',
            'content': '''
            <h3>Warm Up with Hearty Winter Dishes</h3>
            <p>As the temperatures drop, nothing beats a comforting bowl of homemade soup or a rich, hearty stew. Discover recipes that will warm you from the inside out.</p>

            <h4>Why Winter Comfort Foods Work:</h4>
            <ul>
                <li><strong>Rich Flavors:</strong> Slow-cooked meats and vegetables develop deep, complex tastes</li>
                <li><strong>Warming Spices:</strong> Cinnamon, nutmeg, and cloves add cozy aromas</li>
                <li><strong>Substantial Ingredients:</strong> Root vegetables and grains provide lasting satisfaction</li>
                <li><strong>Soul-Satisfying:</strong> These dishes nourish both body and spirit</li>
            </ul>

            <h4>Popular Winter Comfort Foods:</h4>
            <ul>
                <li>Beef Stew with Root Vegetables</li>
                <li>Chicken Pot Pie</li>
                <li>Butternut Squash Soup</li>
                <li>Irish Beef Stew</li>
                <li>Macaroni and Cheese</li>
                <li>Hot Chocolate with Marshmallows</li>
            </ul>

            <p>Learn how to make the perfect winter comfort meal:</p>
            ''',
            'video_url': 'https://www.youtube.com/watch?v=8r8EpNFjK7w'
        },
        {
            'title': 'Herb Storage Guide',
            'content': '''
            <h3>Keep Your Herbs Fresh and Flavorful</h3>
            <p>Fresh herbs can transform a dish, but they don't last forever. Learn the best ways to store herbs to maximize their shelf life and flavor.</p>

            <h4>Storing Fresh Herbs:</h4>
            <ul>
                <li><strong>Soft Herbs (Basil, Cilantro, Parsley):</strong> Store in water like flowers, or wrap in damp paper towel</li>
                <li><strong>Hard Herbs (Rosemary, Thyme, Oregano):</strong> Store in a damp paper towel in the refrigerator</li>
                <li><strong>Green Onions:</strong> Stand upright in a glass of water in the fridge</li>
                <li><strong>Mint:</strong> Keep in water on the countertop away from direct sunlight</li>
            </ul>

            <h4>Drying and Freezing Methods:</h4>
            <ul>
                <li><strong>Air Drying:</strong> Bundle herbs and hang upside down in a dark, dry place</li>
                <li><strong>Oven Drying:</strong> Low heat (200°F) for 1-2 hours</li>
                <li><strong>Freezing:</strong> Chop and freeze in ice cube trays with water or oil</li>
                <li><strong>Microwave Drying:</strong> Quick method for small batches</li>
            </ul>

            <h4>Herb Substitution Guide:</h4>
            <ul>
                <li>1 tsp dried herbs = 1 tbsp fresh herbs</li>
                <li>Basil → Oregano or thyme</li>
                <li>Cilantro → Parsley or mint</li>
                <li>Rosemary → Thyme or sage</li>
            </ul>

            <p>Master herb storage with these professional techniques:</p>
            '''
        },
        {
            'title': 'Sous Vide Basics',
            'content': '''
            <h3>Perfect Cooking with Sous Vide Technology</h3>
            <p>Sous vide cooking delivers restaurant-quality results with precise temperature control. Learn the fundamentals of this revolutionary cooking method.</p>

            <h4>What is Sous Vide?</h4>
            <p>Sous vide (French for "under vacuum") involves cooking vacuum-sealed food in a water bath at precise temperatures. This method ensures:</p>
            <ul>
                <li>Perfect doneness every time</li>
                <li>Maximum moisture retention</li>
                <li>Enhanced flavor development</li>
                <li>Food safety through pasteurization</li>
            </ul>

            <h4>Essential Equipment:</h4>
            <ul>
                <li><strong>Immersion Circulator:</strong> Maintains precise water temperature</li>
                <li><strong>Vacuum Sealer:</strong> Removes air and seals food</li>
                <li><strong>Vacuum Bags:</strong> Food-safe plastic bags</li>
                <li><strong>Container:</strong> Holds water and food safely</li>
            </ul>

            <h4>Basic Technique:</h4>
            <ol>
                <li>Season your food</li>
                <li>Vacuum seal in a bag</li>
                <li>Cook in water bath at precise temperature</li>
                <li>Finish with a quick sear for texture</li>
            </ol>

            <h4>Temperature Guide:</h4>
            <ul>
                <li>Steak (Rare): 129°F (54°C)</li>
                <li>Steak (Medium): 135°F (57°C)</li>
                <li>Chicken Breast: 149°F (65°C)</li>
                <li>Fish: 140°F (60°C)</li>
                <li>Eggs: 147°F (64°C)</li>
            </ul>

            <p>Get started with sous vide cooking:</p>
            ''',
            'video_url': 'https://www.youtube.com/watch?v=8r8EpNFjK7w'
        }
    ]

    for blog_post in blog_posts:
        post = BlogPost(
            title=blog_post['title'],
            content=blog_post['content'],
            date_posted=datetime.utcnow(),
            user_id=user.id
        )
        db.session.add(post)

    db.session.commit()
    print("Popular blog posts added!")