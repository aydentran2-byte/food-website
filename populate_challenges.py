from flaskblog import create_app, db
from flaskblog.models import Post
from datetime import datetime

app = create_app()

with app.app_context():
    # Sample challenges - using existing Post model but marking them as challenges
    # For now, we'll add some challenge-themed recipes
    challenges = [
        {
            'title': '30-Minute Meal Challenge: Speed Cooking',
            'ingredients': '''2 chicken breasts
200g pasta
1 cup cherry tomatoes
2 cups spinach
2 garlic cloves
2 tbsp olive oil
Salt and pepper
Parmesan cheese''',
            'instructions': '''1. Start timer! Bring water to boil for pasta.

2. While water heats, slice chicken and season with salt/pepper.

3. Heat oil in pan, add chicken and cook 3 minutes per side.

4. Add minced garlic and tomatoes, cook 2 minutes.

5. Add spinach, cook until wilted.

6. Drain pasta (should be done by now), add to pan.

7. Toss everything together, top with Parmesan.

8. Stop timer - you did it in 30 minutes or less!''',
            'prep_time': '5 mins',
            'cook_time': '25 mins',
            'servings': '2',
            'cuisine': 'Italian',
            'difficulty': 'Easy',
            'tags': 'challenge, quick, 30-minute',
            'image_file': 'pasta.jpg'
        },
        {
            'title': 'One-Pot Wonder Challenge: Minimal Cleanup',
            'ingredients': '''400g ground beef
1 onion, chopped
2 carrots, sliced
2 potatoes, cubed
1 cup green beans
2 cups beef broth
2 tbsp tomato paste
1 tsp thyme
Salt and pepper''',
            'instructions': '''1. Brown beef in large pot over medium heat.

2. Add onion, cook until softened.

3. Add carrots, potatoes, green beans.

4. Stir in tomato paste, thyme, salt, pepper.

5. Pour in broth, bring to boil.

6. Reduce heat, simmer 25-30 minutes until vegetables are tender.

7. Challenge complete: only one pot to clean!''',
            'prep_time': '10 mins',
            'cook_time': '35 mins',
            'servings': '4',
            'cuisine': 'American',
            'difficulty': 'Easy',
            'tags': 'challenge, one-pot, easy-cleanup',
            'image_file': 'one_pot.jpg'
        },
        {
            'title': 'Vegan Week Challenge: Plant-Based Cooking',
            'ingredients': '''1 block firm tofu
2 cups broccoli florets
1 red bell pepper, sliced
3 tbsp soy sauce
2 tbsp sesame oil
1 tbsp rice vinegar
2 garlic cloves, minced
1 inch ginger, grated
2 cups cooked rice''',
            'instructions': '''1. Press tofu for 10 minutes to remove water, then cube.

2. Mix soy sauce, sesame oil, vinegar, garlic, ginger for marinade.

3. Marinate tofu for 15 minutes.

4. Stir-fry tofu until golden, set aside.

5. In same pan, cook broccoli and pepper until tender-crisp.

6. Return tofu to pan, add remaining marinade.

7. Serve over rice.

8. Vegan challenge: no animal products used!''',
            'prep_time': '15 mins',
            'cook_time': '15 mins',
            'servings': '2',
            'cuisine': 'Asian',
            'difficulty': 'Easy',
            'tags': 'challenge, vegan, plant-based',
            'image_file': 'vegan.jpg'
        },
        {
            'title': 'Budget Cooking Challenge: $10 Meal',
            'ingredients': '''2 cups rice
1 can chickpeas
1 onion
2 carrots
1 potato
2 cups vegetable broth
1 tsp cumin
1 tsp turmeric
Salt and pepper
Fresh cilantro''',
            'instructions': '''1. Chop all vegetables into bite-sized pieces.

2. Heat oil in pot, cook onion until soft.

3. Add carrots and potato, cook 5 minutes.

4. Add spices, cook 1 minute until fragrant.

5. Add rice, chickpeas, broth.

6. Bring to boil, then simmer covered for 20 minutes.

7. Fluff with fork, garnish with cilantro.

8. Challenge met: delicious meal under $10!''',
            'prep_time': '10 mins',
            'cook_time': '30 mins',
            'servings': '4',
            'cuisine': 'Middle Eastern',
            'difficulty': 'Medium',
            'tags': 'challenge, budget, affordable',
            'image_file': 'budget.jpg'
        },
        {
            'title': 'International Cuisine Challenge: Thai Green Curry',
            'ingredients': '''400g chicken thighs
1 can coconut milk
2 tbsp green curry paste
1 cup bamboo shoots
1 red bell pepper
1 cup Thai basil
2 tbsp fish sauce
1 tbsp brown sugar
Jasmine rice for serving''',
            'instructions': '''1. Cut chicken into bite-sized pieces.

2. Heat 2 tbsp thick coconut cream in wok, add curry paste.

3. Fry paste for 2 minutes until fragrant.

4. Add chicken, cook until no longer pink.

5. Add remaining coconut milk, bamboo shoots, pepper.

6. Simmer 10 minutes.

7. Season with fish sauce and sugar.

8. Stir in basil just before serving.

9. Serve with jasmine rice.

10. International challenge: authentic Thai flavors!''',
            'prep_time': '15 mins',
            'cook_time': '20 mins',
            'servings': '4',
            'cuisine': 'Thai',
            'difficulty': 'Easy',
            'tags': 'challenge, international, thai',
            'image_file': 'thai_curry.jpg'
        }
    ]

    for challenge in challenges:
        post = Post(
            title=challenge['title'],
            ingredients=challenge['ingredients'],
            instructions=challenge['instructions'],
            prep_time=challenge['prep_time'],
            cook_time=challenge['cook_time'],
            servings=challenge['servings'],
            cuisine=challenge['cuisine'],
            difficulty=challenge['difficulty'],
            tags=challenge['tags'],
            image_file=challenge['image_file'],
            date_posted=datetime.utcnow(),
            user_id=1
        )
        db.session.add(post)

    db.session.commit()
    print("Sample cooking challenges added!")