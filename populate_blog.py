from flaskblog import create_app, db
from flaskblog.models import BlogPost
from datetime import datetime

app = create_app()

with app.app_context():
    # Clear existing blog posts
    BlogPost.query.delete()
    db.session.commit()

    # Sample cooking tips
    tips = [
        {
            'title': 'Essential Kitchen Tools Every Home Cook Needs',
            'content': '''Having the right tools can make cooking more enjoyable and efficient. Here are the must-have items for any kitchen:

**Chef's Knife**: A sharp, versatile knife for chopping, slicing, and dicing.

**Cutting Board**: Use separate boards for meat, vegetables, and bread to prevent cross-contamination.

**Dutch Oven**: Perfect for slow-cooking stews, braising meats, and even baking bread.

**Cast Iron Skillet**: Great for searing, frying, and oven-to-table serving.

**Microplane Grater**: Essential for zesting citrus, grating cheese, and garlic.

**Digital Scale**: For precise measurements, especially when baking.

**Immersion Blender**: Handy for soups, sauces, and smoothies.

**Tongs**: Multi-purpose tool for flipping, turning, and serving.

Remember, quality over quantity - invest in good tools that will last.''',
            'user_id': 1
        },
        {
            'title': 'The Science of Perfect Pasta Cooking',
            'content': '''Cooking pasta seems simple, but there's real science behind getting it just right:

**Salt the Water Generously**: Use 1-2 tablespoons of salt per gallon of water. This seasons the pasta from within.

**Use Plenty of Water**: At least 4 quarts per pound of pasta ensures even cooking and prevents sticking.

**Boil Vigorously**: Keep the water at a rolling boil throughout cooking.

**Don't Add Oil**: Oil prevents sauce from adhering to the pasta.

**Reserve Pasta Water**: That starchy water is liquid gold for thinning sauces and creating emulsions.

**Test for Doneness**: Taste a piece 2-3 minutes before the package suggests - al dente is key.

**Drain Immediately**: Don't rinse unless making cold pasta salad.

**Sauce Right Away**: Hot pasta + hot sauce = perfect marriage.''',
            'user_id': 1
        },
        {
            'title': 'Mastering Knife Skills: The Foundation of Good Cooking',
            'content': '''Sharp knives and proper technique are essential for safe, efficient cooking:

**The Claw Grip**: Tuck your fingers under and grip the food with your knuckles facing the knife. This protects your fingers.

**The Pinch Grip**: For precision work, pinch the blade between your thumb and forefinger.

**Rocking Motion**: Use your whole arm, letting the knife tip stay on the cutting board.

**Keep Knives Sharp**: A dull knife is more dangerous than a sharp one. Hone regularly, sharpen professionally every 6-12 months.

**Practice Basic Cuts**:
- Brunoise: 1/8" x 1/8" x 1/8" dice
- Small dice: 1/4" cubes
- Medium dice: 1/2" cubes
- Large dice: 3/4" cubes
- Julienne: 1/8" x 1/8" x 2" sticks
- Batonnet: 1/4" x 1/4" x 2" sticks

**Safety First**: Always cut away from your body, use a stable cutting surface, and never catch a falling knife.''',
            'user_id': 1
        },
        {
            'title': 'Building Flavor: The Art of Layering Tastes',
            'content': '''Great cooking is about building complex, balanced flavors through careful layering:

**Start with Aromatics**: Onions, garlic, carrots, celery - the foundation of most savory dishes.

**Add Herbs and Spices**: Fresh herbs for brightness, dried for depth. Add early for mellowing, late for freshness.

**Acidity for Balance**: Lemon juice, vinegar, or wine to cut richness and brighten flavors.

**Salt Strategically**: Salt enhances natural flavors. Add gradually and taste as you go.

**Fat for Mouthfeel**: Butter, oil, or cream adds richness and carries flavors.

**Texture Contrast**: Crisp elements with soft, crunchy with creamy.

**Umami Boost**: Parmesan, mushrooms, soy sauce, or miso add savory depth.

**Rest and Reassess**: Flavors develop over time. Let dishes rest before final seasoning.

Remember: You can always add more seasoning, but you can't take it away!''',
            'user_id': 1
        },
        {
            'title': 'Meal Prep Mastery: Save Time and Eat Better',
            'content': '''Effective meal prep can revolutionize your cooking routine:

**Plan Your Week**: Choose recipes that share ingredients to minimize waste and shopping.

**Prep Staples**: Cook grains, chop vegetables, portion proteins in advance.

**Storage Solutions**: Use clear containers, label everything with dates, store in fridge for 3-4 days.

**Cook Once, Eat Twice**: Make extra portions for lunches or future meals.

**Versatile Ingredients**: Buy items that can be used in multiple dishes.

**Quick Assembly**: Have prepped components ready for fast weeknight meals.

**Freezer Friendly**: Soups, sauces, and baked goods freeze beautifully.

**Safety First**: Cool hot foods quickly, thaw frozen items safely, use within recommended timeframes.

**Variety is Key**: Rotate proteins, vegetables, and cooking methods to avoid boredom.

**Track and Adjust**: Note what works and what doesn't for continuous improvement.''',
            'user_id': 1
        },
        {
            'title': 'The Perfect Steak: From Grill to Plate',
            'content': '''Mastering steak cooking takes practice, but the results are worth it:

**Choose Quality Meat**: Look for well-marbled beef, preferably dry-aged.

**Bring to Room Temperature**: Let steak sit out for 30-60 minutes before cooking.

**Season Generously**: Salt both sides 30-60 minutes ahead for better flavor penetration.

**Pat Dry**: Moisture prevents proper searing.

**Hot Pan/Grill**: Get your cooking surface smoking hot.

**Oil the Steak, Not the Pan**: For better flavor and less smoke.

**Sear First**: 2-3 minutes per side for a good crust.

**Use Thermometer**: Medium-rare: 130-135°F, Medium: 140-145°F, Medium-well: 150-155°F.

**Rest Before Cutting**: Let juices redistribute for 5-10 minutes.

**Finish with Butter**: Compound butter with herbs adds amazing flavor.

**Don't Overcook**: Better slightly under than over.''',
            'user_id': 1
        }
    ]

    for tip in tips:
        blog_post = BlogPost(
            title=tip['title'],
            content=tip['content'],
            user_id=tip['user_id'],
            date_posted=datetime.utcnow()
        )
        db.session.add(blog_post)

    db.session.commit()
    print("Sample cooking tips added!")