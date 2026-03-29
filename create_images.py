from PIL import Image, ImageDraw, ImageFont
import os

# Create recipe_images directory if it doesn't exist
os.makedirs('flaskblog/static/recipe_images', exist_ok=True)

from PIL import Image, ImageDraw, ImageFont
import os

# Create recipe_images directory if it doesn't exist
os.makedirs('flaskblog/static/recipe_images', exist_ok=True)

# Extended list of recipe names and their colors (50 recipes)
recipes = [
    ('spaghetti_carbonara.jpg', 'Spaghetti Carbonara', '#D2691E'),
    ('chicken_tikka_masala.jpg', 'Chicken Tikka Masala', '#FF6347'),
    ('chocolate_chip_cookies.jpg', 'Chocolate Chip Cookies', '#8B4513'),
    ('greek_salad.jpg', 'Greek Salad', '#32CD32'),
    ('beef_stir_fry.jpg', 'Beef Stir Fry', '#FF4500'),
    ('osso_buco.jpg', 'Osso Buco', '#8B0000'),
    ('beef_stroganoff.jpg', 'Beef Stroganoff', '#DC143C'),
    ('moussaka.jpg', 'Moussaka', '#9370DB'),
    ('kimchi_jjigae.jpg', 'Kimchi Jjigae', '#FF0000'),
    ('ramen.jpg', 'Authentic Ramen', '#FFD700'),
    ('doro_wat.jpg', 'Doro Wat', '#8B4513'),
    ('speed_cooking.jpg', '30-Minute Meal', '#00CED1'),
    ('one_pot.jpg', 'One-Pot Wonder', '#228B22'),
    ('vegan.jpg', 'Vegan Challenge', '#9ACD32'),
    ('budget.jpg', 'Budget Meal', '#FFDAB9'),
    ('thai_curry.jpg', 'Thai Green Curry', '#FF6347'),
    ('pad_thai.jpg', 'Pad Thai', '#FFA500'),
    ('butter_chicken.jpg', 'Butter Chicken', '#FF69B4'),
    ('lasagna.jpg', 'Classic Lasagna', '#CD853F'),
    ('caesar_salad.jpg', 'Caesar Salad', '#90EE90'),
    ('fish_tacos.jpg', 'Fish Tacos', '#00BFFF'),
    ('vegetable_curry.jpg', 'Vegetable Curry', '#32CD32'),
    ('pancakes.jpg', 'Fluffy Pancakes', '#FFE4B5'),
    ('brownies.jpg', 'Fudgy Brownies', '#654321'),
    ('quinoa_bowl.jpg', 'Quinoa Buddha Bowl', '#DEB887'),
    ('pizza.jpg', 'Homemade Pizza', '#FF4500'),
    ('sushi.jpg', 'California Rolls', '#87CEEB'),
    ('tacos.jpg', 'Street Tacos', '#FF6347'),
    ('pasta_primavera.jpg', 'Pasta Primavera', '#98FB98'),
    ('chicken_parmesan.jpg', 'Chicken Parmesan', '#DC143C'),
    ('falafel.jpg', 'Falafel Wraps', '#F4A460'),
    ('risotto.jpg', 'Mushroom Risotto', '#DDA0DD'),
    ('burgers.jpg', 'Gourmet Burgers', '#8B4513'),
    ('soup.jpg', 'Tomato Soup', '#FF6347'),
    ('stir_fry.jpg', 'Vegetable Stir Fry', '#32CD32'),
    ('enchiladas.jpg', 'Chicken Enchiladas', '#FF8C00'),
    ('paella.jpg', 'Seafood Paella', '#FFD700'),
    ('curry.jpg', 'Lamb Curry', '#8B0000'),
    ('salad.jpg', 'Caprese Salad', '#FF69B4'),
    ('sandwich.jpg', 'Club Sandwich', '#D2691E'),
    ('omelette.jpg', 'Veggie Omelette', '#FFFACD'),
    ('chili.jpg', 'Beef Chili', '#B22222'),
    ('noodles.jpg', 'Dan Dan Noodles', '#FF0000'),
    ('dumplings.jpg', 'Pork Dumplings', '#F5DEB3'),
    ('quesadilla.jpg', 'Cheese Quesadilla', '#FFD700'),
    ('burrito.jpg', 'Breakfast Burrito', '#FFA500'),
    ('pasta.jpg', 'Pesto Pasta', '#9ACD32'),
    ('steak.jpg', 'Grilled Steak', '#8B0000'),
    ('salmon.jpg', 'Baked Salmon', '#FF69B4'),
    ('chicken_soup.jpg', 'Chicken Noodle Soup', '#F0E68C'),
    ('fried_rice.jpg', 'Vegetable Fried Rice', '#32CD32'),
    ('mac_cheese.jpg', 'Mac and Cheese', '#FFD700'),
    ('meatballs.jpg', 'Swedish Meatballs', '#CD853F'),
    ('shawarma.jpg', 'Chicken Shawarma', '#FF6347'),
    ('bibimbap.jpg', 'Bibimbap', '#FF0000'),
    ('pho.jpg', 'Pho', '#FFD700')
]

def create_placeholder_image(filename, title, color):
    # Create a 400x300 image
    img = Image.new('RGB', (400, 300), color=color)
    draw = ImageDraw.Draw(img)

    # Try to use a font, fallback to default if not available
    try:
        font = ImageFont.truetype("arial.ttf", 24)
        small_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Add a subtle pattern
    for x in range(0, 400, 20):
        for y in range(0, 300, 20):
            if (x + y) % 40 == 0:
                draw.rectangle([x, y, x+10, y+10], fill=(255, 255, 255, 30))

    # Add title text
    bbox = draw.textbbox((0, 0), title, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (400 - text_width) // 2
    y = (300 - text_height) // 2

    # Add text shadow
    draw.text((x+2, y+2), title, fill=(0, 0, 0, 128), font=font)
    draw.text((x, y), title, fill='white', font=font)

    # Add "Recipe" subtitle
    subtitle = "Recipe Image"
    bbox_sub = draw.textbbox((0, 0), subtitle, font=small_font)
    sub_width = bbox_sub[2] - bbox_sub[0]
    sub_x = (400 - sub_width) // 2
    sub_y = y + text_height + 10

    draw.text((sub_x+1, sub_y+1), subtitle, fill=(0, 0, 0, 128), font=small_font)
    draw.text((sub_x, sub_y), subtitle, fill=(255, 255, 255, 200), font=small_font)

    # Save the image
    img.save(f'flaskblog/static/recipe_images/{filename}')
    print(f"Created {filename}")

# Create all placeholder images
for filename, title, color in recipes:
    create_placeholder_image(filename, title, color)

print("All placeholder images created!")