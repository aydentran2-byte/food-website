from flaskblog import create_app, db
from flaskblog.models import Post, User, Rating
from datetime import datetime

app = create_app()

with app.app_context():
    # Create admin user if not exists
    user = User.query.filter_by(username='BonnyriggChef').first()
    if not user:
        user = User(username='BonnyriggChef', email='admin@bonnyrigg.com', password='password')
        db.session.add(user)
        db.session.commit()

    # Clear existing posts
    Post.query.delete()
    db.session.commit()

    # Sample recipes
    recipes = [
        {
            'title': 'Classic Spaghetti Carbonara',
            'ingredients': '''200g spaghetti
100g pancetta or guanciale
2 large eggs
50g grated Pecorino Romano cheese
50g grated Parmesan cheese
Black pepper
Salt''',
            'instructions': '''1. Cook spaghetti in salted boiling water until al dente.

2. In a pan, cook pancetta until crispy.

3. Whisk eggs with cheeses and pepper.

4. Drain pasta, reserving some water.

5. Mix pasta with pancetta, then add egg mixture off heat, tossing quickly.

6. Add pasta water if needed for creaminess.

7. Serve immediately with extra cheese and pepper.''',
            'prep_time': '10 mins',
            'cook_time': '15 mins',
            'servings': '4',
            'cuisine': 'Italian',
            'difficulty': 'Medium',
            'tags': 'pasta, italian, classic',
            'image_file': 'spaghetti_carbonara.jpg'
        },
        {
            'title': 'Chicken Tikka Masala',
            'ingredients': '''500g chicken breast, cubed
200g yogurt
2 tbsp tikka masala paste
1 onion, chopped
2 garlic cloves, minced
1 can (400g) chopped tomatoes
200ml cream
2 tbsp vegetable oil
Fresh coriander
Salt and pepper''',
            'instructions': '''1. Marinate chicken in yogurt and half the tikka paste for 30 minutes.

2. Heat oil, cook onion until soft.

3. Add garlic, remaining paste, cook for 1 minute.

4. Add tomatoes, simmer for 10 minutes.

5. Grill or fry marinated chicken until cooked.

6. Add chicken to sauce, stir in cream.

7. Simmer for 5 minutes, garnish with coriander.

8. Serve with rice or naan.''',
            'prep_time': '15 mins',
            'cook_time': '25 mins',
            'servings': '4',
            'cuisine': 'Indian',
            'difficulty': 'Medium',
            'tags': 'chicken, curry, indian',
            'image_file': 'chicken_tikka_masala.jpg'
        },
        {
            'title': 'Chocolate Chip Cookies',
            'ingredients': '''225g butter, softened
200g brown sugar
100g white sugar
2 eggs
1 tsp vanilla extract
300g plain flour
1 tsp baking soda
1/2 tsp salt
300g chocolate chips''',
            'instructions': '''1. Preheat oven to 180°C.

2. Cream butter and sugars until fluffy.

3. Beat in eggs and vanilla.

4. Mix flour, baking soda, and salt.

5. Gradually add dry ingredients to wet.

6. Stir in chocolate chips.

7. Drop spoonfuls onto baking sheet.

8. Bake for 10-12 minutes until golden.

9. Cool on wire rack.''',
            'prep_time': '15 mins',
            'cook_time': '12 mins',
            'servings': '24',
            'cuisine': 'American',
            'difficulty': 'Easy',
            'tags': 'cookies, dessert, chocolate',
            'image_file': 'chocolate_chip_cookies.jpg'
        },
        {
            'title': 'Greek Salad',
            'ingredients': '''4 tomatoes, chopped
1 cucumber, sliced
1 red onion, thinly sliced
200g feta cheese, cubed
100g Kalamata olives
4 tbsp olive oil
2 tbsp red wine vinegar
1 tsp oregano
Salt and pepper''',
            'instructions': '''1. Combine tomatoes, cucumber, onion, feta, and olives in a bowl.

2. Whisk together olive oil, vinegar, oregano, salt, and pepper.

3. Pour dressing over salad.

4. Toss gently to combine.

5. Let sit for 10 minutes to meld flavors.

6. Serve chilled.''',
            'prep_time': '15 mins',
            'cook_time': '0 mins',
            'servings': '4',
            'cuisine': 'Greek',
            'difficulty': 'Easy',
            'tags': 'salad, healthy, mediterranean',
            'image_file': 'greek_salad.jpg'
        },
        {
            'title': 'Beef Stir Fry',
            'ingredients': '''400g beef strips
2 bell peppers, sliced
1 broccoli head, cut into florets
2 carrots, sliced
3 tbsp soy sauce
2 tbsp oyster sauce
1 tbsp sesame oil
2 garlic cloves, minced
1 inch ginger, grated
2 tbsp vegetable oil''',
            'instructions': '''1. Heat vegetable oil in a wok or large pan.

2. Stir fry beef until browned, remove.

3. Add garlic and ginger, cook for 30 seconds.

4. Add vegetables, stir fry for 3-4 minutes.

5. Return beef to pan.

6. Add soy sauce, oyster sauce, and sesame oil.

7. Cook for another 2 minutes.

8. Serve with rice.''',
            'prep_time': '15 mins',
            'cook_time': '10 mins',
            'servings': '4',
            'cuisine': 'Chinese',
            'difficulty': 'Easy',
            'tags': 'beef, stir fry, quick',
            'image_file': 'beef_stir_fry.jpg'
        },
        {
            'title': 'Mr Smith\'s Classic Osso Buco',
            'ingredients': '''4 veal shanks
1 onion, chopped
2 carrots, chopped
2 celery stalks, chopped
2 garlic cloves, minced
1 cup white wine
2 cups beef broth
1 can (400g) crushed tomatoes
2 tbsp olive oil
2 tbsp butter
Flour for dredging
Salt and pepper
Fresh parsley, chopped
Lemon zest''',
            'instructions': '''1. Season veal shanks with salt and pepper, dredge in flour.

2. Heat olive oil and butter in a large pot.

3. Brown veal shanks on all sides, remove.

4. Add onion, carrots, celery, cook until softened.

5. Add garlic, cook for 1 minute.

6. Add wine, reduce by half.

7. Add broth and tomatoes, bring to simmer.

8. Return veal to pot, cover and simmer for 2-3 hours until tender.

9. Garnish with parsley and lemon zest.

10. Serve with risotto or polenta.''',
            'prep_time': '20 mins',
            'cook_time': '160 mins',
            'servings': '4',
            'cuisine': 'Italian',
            'difficulty': 'Hard',
            'tags': 'veal, italian, classic, osso buco',
            'image_file': 'osso_buco.jpg'
        },
        {
            'title': 'Mr Zhukov\'s Beef Stroganoff',
            'ingredients': '''500g beef sirloin, sliced
1 onion, sliced
200g mushrooms, sliced
2 tbsp butter
1 cup sour cream
1 cup beef broth
2 tbsp flour
2 tbsp tomato paste
Salt and pepper
Fresh dill, chopped
Egg noodles for serving''',
            'instructions': '''1. Season beef with salt and pepper.

2. Heat butter in a large pan, brown beef in batches.

3. Remove beef, add onion and mushrooms, cook until softened.

4. Add flour, cook for 1 minute.

5. Stir in broth and tomato paste, bring to simmer.

6. Return beef to pan, simmer for 10 minutes.

7. Stir in sour cream, heat through but don't boil.

8. Garnish with dill.

9. Serve over egg noodles.''',
            'prep_time': '15 mins',
            'cook_time': '25 mins',
            'servings': '4',
            'cuisine': 'Other',
            'difficulty': 'Medium',
            'tags': 'beef, russian, stroganoff',
            'image_file': 'beef_stroganoff.jpg'
        },
        {
            'title': 'Mr Elafrost\'s Moussaka',
            'ingredients': '''2 eggplants, sliced
500g ground lamb
1 onion, chopped
2 garlic cloves, minced
1 can (400g) crushed tomatoes
1 tsp cinnamon
1 tsp oregano
2 cups milk
3 tbsp butter
3 tbsp flour
2 eggs
1 cup feta cheese, crumbled
Salt and pepper
Olive oil''',
            'instructions': '''1. Salt eggplant slices, let drain for 30 minutes, rinse and pat dry.

2. Fry eggplant slices in olive oil until golden, set aside.

3. Cook lamb with onion and garlic until browned.

4. Add tomatoes, cinnamon, oregano, simmer for 20 minutes.

5. Make béchamel: melt butter, add flour, cook for 2 minutes.

6. Gradually add milk, cook until thickened.

7. Remove from heat, stir in eggs and half the feta.

8. Layer eggplant, meat sauce, béchamel, remaining feta in baking dish.

9. Bake at 180°C for 45 minutes until golden.

10. Let rest for 15 minutes before serving.''',
            'prep_time': '45 mins',
            'cook_time': '115 mins',
            'servings': '8',
            'cuisine': 'Greek',
            'difficulty': 'Hard',
            'tags': 'lamb, greek, moussaka, eggplant',
            'image_file': 'moussaka.jpg'
        },
        {
            'title': 'Korean Kimchi Jjigae (Kimchi Stew)',
            'ingredients': '''2 cups kimchi, chopped
200g pork belly or tofu
1 onion, sliced
2 green onions, chopped
2 cups water or broth
1 tbsp gochujang
1 tbsp gochugaru
1 tbsp soy sauce
1 tsp sesame oil
2 garlic cloves, minced''',
            'instructions': '''1. Heat sesame oil in a pot, cook pork until browned.

2. Add onion and garlic, cook for 2 minutes.

3. Add kimchi, cook for 3 minutes.

4. Add water, gochujang, gochugaru, soy sauce.

5. Bring to boil, then simmer for 15-20 minutes.

6. Add green onions, cook for 2 more minutes.

7. Serve hot with rice.''',
            'prep_time': '10 mins',
            'cook_time': '30 mins',
            'servings': '4',
            'cuisine': 'Korean',
            'difficulty': 'Medium',
            'tags': 'kimchi, korean, stew, spicy',
            'image_file': 'kimchi_jjigae.jpg'
        },
        {
            'title': 'Authentic Japanese Ramen from Scratch',
            'ingredients': '''For broth:
2 kg pork bones
1 chicken carcass
2 onions, halved
1 carrot, chopped
1 inch ginger, sliced
4 garlic cloves
4 liters water
Soy sauce, mirin, sake for seasoning

For noodles:
200g bread flour
200g all-purpose flour
2 eggs
100ml water
Salt

For toppings:
Chashu pork
Soft-boiled eggs
Green onions
Nori
Bamboo shoots''',
            'instructions': '''1. Roast bones and vegetables for 30 minutes at 200°C.

2. Place in large pot with water, simmer for 12-24 hours, skimming foam.

3. Strain broth, season with soy sauce, mirin, sake.

4. Make noodles: mix flours, make well, add eggs and water, knead for 10 minutes.

5. Rest dough for 30 minutes, roll out thin, cut into noodles.

6. Cook noodles in boiling water for 2-3 minutes.

7. Assemble bowls with hot broth, noodles, and toppings.''',
            'prep_time': '60 mins',
            'cook_time': '780 mins',
            'servings': '4',
            'cuisine': 'Japanese',
            'difficulty': 'Expert',
            'tags': 'ramen, japanese, noodles, broth',
            'image_file': 'ramen.jpg'
        },
        {
            'title': 'Ethiopian Doro Wat (Spicy Chicken Stew)',
            'ingredients': '''1 kg chicken pieces
2 onions, finely chopped
4 garlic cloves, minced
1 inch ginger, grated
1/4 cup berbere spice
2 cups chicken broth
4 hard-boiled eggs
2 tbsp vegetable oil
Salt
Injera for serving''',
            'instructions': '''1. Cook onions in oil over low heat for 30 minutes until caramelized.

2. Add garlic, ginger, berbere, cook for 5 minutes.

3. Add chicken, brown on all sides.

4. Add broth, simmer for 45 minutes until chicken is tender.

5. Add peeled eggs in last 10 minutes.

6. Serve with injera.''',
            'prep_time': '20 mins',
            'cook_time': '70 mins',
            'servings': '6',
            'cuisine': 'African',
            'difficulty': 'Medium',
            'tags': 'chicken, ethiopian, spicy, doro wat',
            'image_file': 'doro_wat.jpg'
        },
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
            'image_file': 'speed_cooking.jpg'
        },
        {
            'title': 'One-Pot Wonder Challenge: Minimal Cleanup',
            'ingredients': '''400g ground beef
1 onion
2 carrots
2 potatoes
1 cup green beans
2 cups beef broth
2 tbsp tomato paste
1 tsp thyme
Salt and pepper''',
            'instructions': '''1. Brown beef in large pot over medium heat.

2. Add onion, cook until soft.

3. Add carrots and potato, cook 5 minutes.

4. Add spices, cook 1 minute until fragrant.

5. Add rice, chickpeas, broth.

6. Bring to boil, then simmer covered for 20 minutes.

7. Fluff with fork, garnish with cilantro.

8. Challenge complete: only one pot to clean!''',
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
1 red bell pepper
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
            'difficulty': 'Medium',
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
            'difficulty': 'Easy',
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
            'difficulty': 'Medium',
            'tags': 'challenge, international, thai',
            'image_file': 'thai_curry.jpg'
        },
        {
            'title': 'Authentic Pad Thai',
            'ingredients': '''200g rice noodles
200g shrimp or chicken
2 eggs
100g bean sprouts
50g peanuts, crushed
2 tbsp fish sauce
1 tbsp tamarind paste
1 tbsp palm sugar
2 cloves garlic, minced
2 tbsp vegetable oil
Lime wedges
Fresh coriander''',
            'instructions': '''1. Soak rice noodles in hot water for 10 minutes, then drain.

2. Heat oil in a wok, cook garlic and protein until done.

3. Push to side, scramble eggs in the pan.

4. Add drained noodles, toss with fish sauce, tamarind, and sugar.

5. Add bean sprouts, cook for 2 minutes.

6. Serve with peanuts, lime, and coriander.''',
            'prep_time': '15 mins',
            'cook_time': '10 mins',
            'servings': '4',
            'cuisine': 'Thai',
            'difficulty': 'Medium',
            'tags': 'thai, noodles, seafood',
            'image_file': 'pad_thai.jpg'
        },
        {
            'title': 'Creamy Butter Chicken',
            'ingredients': '''500g chicken breast, cubed
200g yogurt
2 tbsp butter chicken masala
1 onion, chopped
2 garlic cloves, minced
1 can (400g) crushed tomatoes
200ml cream
2 tbsp butter
Fresh coriander
Salt and pepper''',
            'instructions': '''1. Marinate chicken in yogurt and half the masala for 30 minutes.

2. Heat butter, cook onion until soft.

3. Add garlic and remaining masala, cook for 1 minute.

4. Add tomatoes, simmer for 10 minutes.

5. Cook marinated chicken separately until done.

6. Add chicken to sauce, stir in cream.

7. Simmer for 5 minutes, garnish with coriander.

8. Serve with rice or naan.''',
            'prep_time': '15 mins',
            'cook_time': '25 mins',
            'servings': '4',
            'cuisine': 'Indian',
            'difficulty': 'Medium',
            'tags': 'indian, chicken, curry',
            'image_file': 'butter_chicken.jpg'
        },
        {
            'title': 'Classic Lasagna',
            'ingredients': '''12 lasagna sheets
500g ground beef
1 onion, chopped
2 garlic cloves, minced
1 can (800g) crushed tomatoes
200g ricotta cheese
200g mozzarella cheese
100g parmesan cheese
2 tbsp olive oil
Salt and pepper
Fresh basil''',
            'instructions': '''1. Preheat oven to 180°C.

2. Cook beef with onion and garlic until browned.

3. Add tomatoes, simmer for 20 minutes. Season.

4. Cook lasagna sheets according to package.

5. Layer: sauce, pasta, ricotta, mozzarella, repeat.

6. Top with parmesan and remaining mozzarella.

7. Bake for 30-35 minutes until golden.

8. Let rest 10 minutes before serving.''',
            'prep_time': '20 mins',
            'cook_time': '45 mins',
            'servings': '6',
            'cuisine': 'Italian',
            'difficulty': 'Medium',
            'tags': 'italian, pasta, comfort',
            'image_file': 'lasagna.jpg'
        },
        {
            'title': 'Caesar Salad',
            'ingredients': '''1 romaine lettuce
100g croutons
50g parmesan cheese
2 tbsp caesar dressing
1 tbsp olive oil
Salt and pepper
Anchovies (optional)''',
            'instructions': '''1. Wash and chop romaine lettuce.

2. Toss lettuce with olive oil, salt, and pepper.

3. Add croutons and parmesan.

4. Drizzle with caesar dressing.

5. Toss gently to combine.

6. Serve immediately.''',
            'prep_time': '10 mins',
            'cook_time': '0 mins',
            'servings': '4',
            'cuisine': 'American',
            'difficulty': 'Easy',
            'tags': 'salad, quick, healthy',
            'image_file': 'caesar_salad.jpg'
        },
        {
            'title': 'Fish Tacos',
            'ingredients': '''400g white fish fillets
8 small tortillas
1 cup cabbage slaw
1 avocado, sliced
Lime wedges
2 tbsp vegetable oil
1 tbsp chili powder
Salt and pepper
Fresh cilantro''',
            'instructions': '''1. Season fish with chili powder, salt, and pepper.

2. Heat oil in a pan, cook fish for 3-4 minutes per side.

3. Warm tortillas in a dry pan.

4. Flake cooked fish.

5. Assemble tacos: fish, slaw, avocado, cilantro.

6. Serve with lime wedges.''',
            'prep_time': '15 mins',
            'cook_time': '10 mins',
            'servings': '4',
            'cuisine': 'Mexican',
            'difficulty': 'Easy',
            'tags': 'mexican, fish, tacos',
            'image_file': 'fish_tacos.jpg'
        },
        {
            'title': 'Vegetable Curry',
            'ingredients': '''2 potatoes, cubed
1 cauliflower, florets
2 carrots, sliced
1 onion, chopped
2 garlic cloves, minced
1 can (400g) coconut milk
2 tbsp curry paste
1 tbsp vegetable oil
Fresh coriander
Salt and pepper''',
            'instructions': '''1. Heat oil, cook onion and garlic until soft.

2. Add curry paste, cook for 1 minute.

3. Add vegetables and coconut milk.

4. Simmer for 20-25 minutes until tender.

5. Season with salt and pepper.

6. Garnish with coriander.

7. Serve with rice.''',
            'prep_time': '15 mins',
            'cook_time': '25 mins',
            'servings': '4',
            'cuisine': 'Indian',
            'difficulty': 'Easy',
            'tags': 'vegetarian, curry, healthy',
            'image_file': 'vegetable_curry.jpg'
        },
        {
            'title': 'Fluffy Pancakes',
            'ingredients': '''200g flour
2 eggs
300ml milk
2 tbsp sugar
1 tbsp baking powder
2 tbsp melted butter
Pinch of salt
Maple syrup''',
            'instructions': '''1. Mix dry ingredients: flour, sugar, baking powder, salt.

2. Whisk eggs, milk, and melted butter.

3. Combine wet and dry ingredients.

4. Heat non-stick pan over medium heat.

5. Pour batter for each pancake.

6. Cook until bubbles form, then flip.

7. Cook until golden on both sides.

8. Serve with maple syrup.''',
            'prep_time': '10 mins',
            'cook_time': '15 mins',
            'servings': '4',
            'cuisine': 'American',
            'difficulty': 'Easy',
            'tags': 'breakfast, sweet, pancakes',
            'image_file': 'pancakes.jpg'
        },
        {
            'title': 'Fudgy Brownies',
            'ingredients': '''200g dark chocolate
150g butter
200g sugar
3 eggs
100g flour
30g cocoa powder
Pinch of salt
1 tsp vanilla extract''',
            'instructions': '''1. Preheat oven to 180°C. Grease 8x8 inch pan.

2. Melt chocolate and butter together.

3. Whisk in sugar, then eggs one by one.

4. Add vanilla extract.

5. Fold in flour, cocoa, and salt.

6. Pour into pan, bake for 25-30 minutes.

7. Cool completely before cutting.''',
            'prep_time': '15 mins',
            'cook_time': '30 mins',
            'servings': '9',
            'cuisine': 'American',
            'difficulty': 'Easy',
            'tags': 'dessert, chocolate, brownies',
            'image_file': 'brownies.jpg'
        },
        {
            'title': 'Quinoa Buddha Bowl',
            'ingredients': '''100g quinoa
1 sweet potato, cubed
1 avocado, sliced
100g chickpeas
50g spinach
2 tbsp tahini
1 tbsp olive oil
Lemon juice
Salt and pepper''',
            'instructions': '''1. Cook quinoa according to package.

2. Roast sweet potato at 200°C for 20 minutes.

3. Drain and rinse chickpeas.

4. Arrange quinoa, sweet potato, avocado, chickpeas, spinach in bowl.

5. Drizzle with tahini and olive oil.

6. Season with salt, pepper, and lemon juice.''',
            'prep_time': '15 mins',
            'cook_time': '20 mins',
            'servings': '2',
            'cuisine': 'Healthy',
            'difficulty': 'Easy',
            'tags': 'healthy, vegetarian, bowl',
            'image_file': 'quinoa_bowl.jpg'
        },
        {
            'title': 'Homemade Pizza',
            'ingredients': '''300g pizza dough
100g tomato sauce
200g mozzarella cheese
50g pepperoni
1 bell pepper, sliced
1 onion, sliced
2 tbsp olive oil
Fresh basil''',
            'instructions': '''1. Preheat oven to 220°C.

2. Roll out pizza dough on floured surface.

3. Spread tomato sauce, leaving border.

4. Add cheese, toppings.

5. Drizzle with olive oil.

6. Bake for 12-15 minutes until crust is golden.

7. Garnish with fresh basil.''',
            'prep_time': '15 mins',
            'cook_time': '15 mins',
            'servings': '4',
            'cuisine': 'Italian',
            'difficulty': 'Medium',
            'tags': 'italian, pizza, homemade',
            'image_file': 'pizza.jpg'
        },
        {
            'title': 'California Rolls',
            'ingredients': '''200g sushi rice
4 nori sheets
100g imitation crab
1 cucumber, julienned
1 avocado, sliced
Rice vinegar
Soy sauce
Wasabi''',
            'instructions': '''1. Cook sushi rice, season with vinegar.

2. Place nori on sushi mat, shiny side down.

3. Spread rice evenly, leaving 1 inch border.

4. Add crab, cucumber, avocado in line.

5. Roll tightly using mat.

6. Slice into 6-8 pieces.

7. Serve with soy sauce and wasabi.''',
            'prep_time': '30 mins',
            'cook_time': '20 mins',
            'servings': '4',
            'cuisine': 'Japanese',
            'difficulty': 'Medium',
            'tags': 'japanese, sushi, seafood',
            'image_file': 'sushi.jpg'
        },
        {
            'title': 'Street Tacos',
            'ingredients': '''400g skirt steak
8 small corn tortillas
1 onion, diced
Fresh cilantro
Lime wedges
2 tbsp vegetable oil
1 tbsp chili powder
Salt and pepper''',
            'instructions': '''1. Season steak with chili powder, salt, pepper.

2. Heat oil in grill pan, cook steak 3-4 minutes per side.

3. Rest steak, then slice thinly against grain.

4. Warm tortillas.

5. Fill with steak, onion, cilantro.

6. Serve with lime wedges.''',
            'prep_time': '10 mins',
            'cook_time': '10 mins',
            'servings': '4',
            'cuisine': 'Mexican',
            'difficulty': 'Easy',
            'tags': 'mexican, tacos, beef',
            'image_file': 'tacos.jpg'
        },
        {
            'title': 'Pasta Primavera',
            'ingredients': '''300g pasta
1 zucchini, sliced
1 bell pepper, sliced
100g cherry tomatoes
2 garlic cloves, minced
3 tbsp olive oil
50g parmesan cheese
Fresh basil
Salt and pepper''',
            'instructions': '''1. Cook pasta according to package.

2. Heat olive oil, sauté garlic and vegetables.

3. Cook until tender but crisp.

4. Drain pasta, reserve some water.

5. Toss pasta with vegetables.

6. Add parmesan and basil.

7. Season with salt and pepper.''',
            'prep_time': '10 mins',
            'cook_time': '15 mins',
            'servings': '4',
            'cuisine': 'Italian',
            'difficulty': 'Easy',
            'tags': 'italian, pasta, vegetarian',
            'image_file': 'pasta_primavera.jpg'
        },
        {
            'title': 'Chicken Parmesan',
            'ingredients': '''4 chicken breasts
100g breadcrumbs
50g parmesan cheese
2 eggs
200g mozzarella cheese
200g tomato sauce
2 tbsp olive oil
Fresh basil
Salt and pepper''',
            'instructions': '''1. Preheat oven to 200°C.

2. Pound chicken breasts thin.

3. Bread chicken: flour, egg, breadcrumbs.

4. Fry in olive oil until golden.

5. Place in baking dish, top with sauce and cheeses.

6. Bake for 15 minutes until cheese melts.

7. Garnish with basil.''',
            'prep_time': '15 mins',
            'cook_time': '25 mins',
            'servings': '4',
            'cuisine': 'Italian',
            'difficulty': 'Medium',
            'tags': 'italian, chicken, parmesan',
            'image_file': 'chicken_parmesan.jpg'
        },
        {
            'title': 'Falafel Wraps',
            'ingredients': '''200g chickpeas
1 onion, chopped
2 garlic cloves
2 tbsp flour
1 tbsp cumin
Fresh parsley
4 pita breads
Tahini sauce
Lettuce, tomato, cucumber''',
            'instructions': '''1. Blend chickpeas, onion, garlic, spices, parsley.

2. Mix in flour, form balls.

3. Deep fry or bake at 200°C for 20 minutes.

4. Warm pita breads.

5. Fill with falafel, veggies, tahini.

6. Roll up and serve.''',
            'prep_time': '15 mins',
            'cook_time': '20 mins',
            'servings': '4',
            'cuisine': 'Middle Eastern',
            'difficulty': 'Medium',
            'tags': 'middle eastern, vegetarian, wraps',
            'image_file': 'falafel.jpg'
        },
        {
            'title': 'Mushroom Risotto',
            'ingredients': '''200g arborio rice
200g mushrooms, sliced
1 onion, chopped
2 garlic cloves, minced
1L vegetable stock
100ml white wine
50g parmesan cheese
2 tbsp butter
Fresh thyme
Salt and pepper''',
            'instructions': '''1. Heat stock, keep warm.

2. Sauté onion and garlic in butter.

3. Add mushrooms, cook until soft.

4. Add rice, toast for 2 minutes.

5. Add wine, stir until absorbed.

6. Add stock gradually, stirring constantly.

7. Cook 18-20 minutes until creamy.

8. Stir in parmesan and thyme.''',
            'prep_time': '10 mins',
            'cook_time': '25 mins',
            'servings': '4',
            'cuisine': 'Italian',
            'difficulty': 'Medium',
            'tags': 'italian, risotto, mushrooms',
            'image_file': 'risotto.jpg'
        },
        {
            'title': 'Gourmet Burgers',
            'ingredients': '''400g ground beef
4 burger buns
4 cheese slices
Lettuce, tomato, onion
2 tbsp BBQ sauce
1 tbsp Worcestershire sauce
Salt and pepper
Pickles''',
            'instructions': '''1. Mix beef with Worcestershire, salt, pepper.

2. Form 4 patties.

3. Grill or pan-fry 4-5 minutes per side.

4. Add cheese in last minute.

5. Toast buns.

6. Assemble: bun, patty, cheese, veggies, sauce.

7. Serve immediately.''',
            'prep_time': '10 mins',
            'cook_time': '10 mins',
            'servings': '4',
            'cuisine': 'American',
            'difficulty': 'Easy',
            'tags': 'american, burgers, beef',
            'image_file': 'burgers.jpg'
        },
        {
            'title': 'Classic Tomato Soup',
            'ingredients': '''800g tomatoes
1 onion, chopped
2 garlic cloves, minced
500ml vegetable stock
100ml cream
2 tbsp olive oil
Fresh basil
Salt and pepper''',
            'instructions': '''1. Heat oil, sauté onion and garlic.

2. Add tomatoes and stock.

3. Simmer for 20 minutes.

4. Blend until smooth.

5. Stir in cream.

6. Season with salt, pepper, basil.

7. Serve hot.''',
            'prep_time': '10 mins',
            'cook_time': '25 mins',
            'servings': '4',
            'cuisine': 'American',
            'difficulty': 'Easy',
            'tags': 'soup, tomato, comfort',
            'image_file': 'soup.jpg'
        },
        {
            'title': 'Vegetable Stir Fry',
            'ingredients': '''1 broccoli, florets
1 bell pepper, sliced
1 carrot, sliced
100g snow peas
2 garlic cloves, minced
3 tbsp soy sauce
1 tbsp sesame oil
1 tbsp vegetable oil
Sesame seeds''',
            'instructions': '''1. Heat vegetable oil in wok.

2. Add garlic, stir for 30 seconds.

3. Add vegetables, stir fry for 5-7 minutes.

4. Add soy sauce and sesame oil.

5. Cook for another 2 minutes.

6. Garnish with sesame seeds.

7. Serve with rice.''',
            'prep_time': '10 mins',
            'cook_time': '10 mins',
            'servings': '4',
            'cuisine': 'Asian',
            'difficulty': 'Easy',
            'tags': 'asian, vegetarian, stir fry',
            'image_file': 'stir_fry.jpg'
        },
        {
            'title': 'Chicken Enchiladas',
            'ingredients': '''300g chicken breast, cooked
8 flour tortillas
200g enchilada sauce
200g cheese, shredded
1 onion, chopped
1 bell pepper, chopped
Sour cream
Fresh cilantro''',
            'instructions': '''1. Preheat oven to 180°C.

2. Mix chicken, onion, pepper, half the cheese.

3. Roll mixture in tortillas.

4. Place in baking dish, cover with sauce and cheese.

5. Bake for 20-25 minutes.

6. Serve with sour cream and cilantro.''',
            'prep_time': '15 mins',
            'cook_time': '25 mins',
            'servings': '4',
            'cuisine': 'Mexican',
            'difficulty': 'Medium',
            'tags': 'mexican, chicken, enchiladas',
            'image_file': 'enchiladas.jpg'
        },
        {
            'title': 'Seafood Paella',
            'ingredients': '''200g paella rice
200g mixed seafood
1 onion, chopped
2 garlic cloves, minced
1 bell pepper, chopped
500ml fish stock
100g peas
1 tsp saffron
2 tbsp olive oil
Lemon wedges''',
            'instructions': '''1. Heat oil, sauté onion, garlic, pepper.

2. Add rice, toast for 2 minutes.

3. Add saffron and stock.

4. Simmer for 10 minutes.

5. Add seafood and peas.

6. Cook for another 10 minutes.

7. Rest for 5 minutes.

8. Serve with lemon.''',
            'prep_time': '15 mins',
            'cook_time': '25 mins',
            'servings': '4',
            'cuisine': 'Spanish',
            'difficulty': 'Medium',
            'tags': 'spanish, seafood, paella',
            'image_file': 'paella.jpg'
        },
        {
            'title': 'Lamb Curry',
            'ingredients': '''500g lamb, cubed
1 onion, chopped
2 garlic cloves, minced
2 tbsp curry powder
1 can (400g) coconut milk
2 potatoes, cubed
2 tbsp vegetable oil
Fresh coriander
Salt and pepper''',
            'instructions': '''1. Heat oil, brown lamb cubes.

2. Add onion and garlic, cook until soft.

3. Add curry powder, cook for 1 minute.

4. Add coconut milk and potatoes.

5. Simmer for 45-50 minutes until tender.

6. Season with salt and pepper.

7. Garnish with coriander.

8. Serve with rice.''',
            'prep_time': '15 mins',
            'cook_time': '50 mins',
            'servings': '4',
            'cuisine': 'Indian',
            'difficulty': 'Medium',
            'tags': 'indian, lamb, curry',
            'image_file': 'curry.jpg'
        },
        {
            'title': 'Caprese Salad',
            'ingredients': '''4 tomatoes, sliced
200g mozzarella, sliced
Fresh basil leaves
3 tbsp olive oil
2 tbsp balsamic vinegar
Salt and pepper''',
            'instructions': '''1. Arrange tomato and mozzarella slices alternately.

2. Tuck basil leaves between slices.

3. Drizzle with olive oil and balsamic.

4. Season with salt and pepper.

5. Let sit for 10 minutes before serving.''',
            'prep_time': '10 mins',
            'cook_time': '0 mins',
            'servings': '4',
            'cuisine': 'Italian',
            'difficulty': 'Easy',
            'tags': 'italian, salad, fresh',
            'image_file': 'salad.jpg'
        },
        {
            'title': 'Club Sandwich',
            'ingredients': '''8 slices bread
200g turkey or chicken
4 slices bacon, cooked
Lettuce leaves
2 tomatoes, sliced
4 slices cheese
Mayonnaise
Salt and pepper''',
            'instructions': '''1. Toast bread slices.

2. Spread mayonnaise on one side of each slice.

3. Layer: bread, turkey, bacon, lettuce, tomato, cheese, bread.

4. Add another layer: bread, turkey, bacon, lettuce, tomato, bread.

5. Secure with toothpicks, cut diagonally.

6. Serve immediately.''',
            'prep_time': '10 mins',
            'cook_time': '5 mins',
            'servings': '2',
            'cuisine': 'American',
            'difficulty': 'Easy',
            'tags': 'american, sandwich, lunch',
            'image_file': 'sandwich.jpg'
        },
        {
            'title': 'Veggie Omelette',
            'ingredients': '''4 eggs
1 bell pepper, diced
1 tomato, diced
50g spinach
50g cheese, grated
2 tbsp milk
1 tbsp butter
Salt and pepper''',
            'instructions': '''1. Whisk eggs with milk, salt, pepper.

2. Heat butter in non-stick pan.

3. Add vegetables, cook for 2 minutes.

4. Pour in egg mixture.

5. Cook until edges set, add cheese.

6. Fold omelette, cook until cheese melts.

7. Serve immediately.''',
            'prep_time': '5 mins',
            'cook_time': '10 mins',
            'servings': '2',
            'cuisine': 'American',
            'difficulty': 'Easy',
            'tags': 'breakfast, eggs, vegetarian',
            'image_file': 'omelette.jpg'
        },
        {
            'title': 'Beef Chili',
            'ingredients': '''500g ground beef
1 onion, chopped
2 garlic cloves, minced
1 can (800g) kidney beans
1 can (400g) diced tomatoes
2 tbsp chili powder
1 tsp cumin
Salt and pepper
Sour cream (optional)''',
            'instructions': '''1. Brown beef in large pot.

2. Add onion and garlic, cook until soft.

3. Add tomatoes, beans, spices.

4. Simmer for 30-40 minutes.

5. Season with salt and pepper.

6. Serve with sour cream if desired.''',
            'prep_time': '10 mins',
            'cook_time': '40 mins',
            'servings': '4',
            'cuisine': 'American',
            'difficulty': 'Easy',
            'tags': 'american, chili, beef',
            'image_file': 'chili.jpg'
        },
        {
            'title': 'Dan Dan Noodles',
            'ingredients': '''200g Chinese noodles
200g ground pork
2 tbsp Sichuan chili oil
2 tbsp soy sauce
1 tbsp sesame paste
2 garlic cloves, minced
1 inch ginger, grated
Green onions
Peanuts''',
            'instructions': '''1. Cook noodles according to package.

2. Brown pork in a pan.

3. Add garlic and ginger, cook for 1 minute.

4. Mix chili oil, soy sauce, sesame paste.

5. Toss noodles with sauce and pork.

6. Garnish with green onions and peanuts.

7. Serve immediately.''',
            'prep_time': '10 mins',
            'cook_time': '15 mins',
            'servings': '4',
            'cuisine': 'Chinese',
            'difficulty': 'Medium',
            'tags': 'chinese, noodles, spicy',
            'image_file': 'noodles.jpg'
        },
        {
            'title': 'Pork Dumplings',
            'ingredients': '''200g ground pork
30 dumpling wrappers
1 cabbage, finely chopped
2 garlic cloves, minced
1 inch ginger, grated
2 tbsp soy sauce
1 tbsp sesame oil
Green onions''',
            'instructions': '''1. Mix pork, cabbage, garlic, ginger, soy sauce, sesame oil.

2. Place 1 tsp filling in each wrapper.

3. Moisten edges, fold and pleat.

4. Steam for 8-10 minutes or pan-fry.

5. Serve with dipping sauce.

6. Garnish with green onions.''',
            'prep_time': '20 mins',
            'cook_time': '10 mins',
            'servings': '4',
            'cuisine': 'Chinese',
            'difficulty': 'Medium',
            'tags': 'chinese, dumplings, pork',
            'image_file': 'dumplings.jpg'
        },
        {
            'title': 'Cheese Quesadilla',
            'ingredients': '''4 flour tortillas
200g cheese, shredded
1 bell pepper, sliced
1 onion, sliced
2 tbsp butter
Salsa
Sour cream
Fresh cilantro''',
            'instructions': '''1. Heat butter in pan.

2. Place tortilla, add cheese and veggies.

3. Top with another tortilla.

4. Cook until golden, flip.

5. Cook until cheese melts.

6. Cut into wedges.

7. Serve with salsa and sour cream.''',
            'prep_time': '5 mins',
            'cook_time': '10 mins',
            'servings': '4',
            'cuisine': 'Mexican',
            'difficulty': 'Easy',
            'tags': 'mexican, cheese, quick',
            'image_file': 'quesadilla.jpg'
        },
        {
            'title': 'Breakfast Burrito',
            'ingredients': '''4 flour tortillas
4 eggs
200g chorizo or sausage
1 potato, diced
100g cheese, shredded
Salsa
Sour cream
Fresh cilantro''',
            'instructions': '''1. Cook potato until tender.

2. Brown chorizo in pan.

3. Scramble eggs with chorizo and potato.

4. Warm tortillas.

5. Fill with egg mixture and cheese.

6. Roll up tightly.

7. Serve with salsa and sour cream.''',
            'prep_time': '10 mins',
            'cook_time': '15 mins',
            'servings': '4',
            'cuisine': 'Mexican',
            'difficulty': 'Easy',
            'tags': 'mexican, breakfast, burrito',
            'image_file': 'burrito.jpg'
        },
        {
            'title': 'Pesto Pasta',
            'ingredients': '''300g pasta
50g pine nuts
50g parmesan cheese
2 garlic cloves
100ml olive oil
50g fresh basil
Salt and pepper
Cherry tomatoes''',
            'instructions': '''1. Cook pasta according to package.

2. Blend basil, pine nuts, garlic, parmesan, oil.

3. Season pesto with salt and pepper.

4. Drain pasta, reserve some water.

5. Toss pasta with pesto.

6. Add pasta water if needed.

7. Serve with halved cherry tomatoes.''',
            'prep_time': '10 mins',
            'cook_time': '10 mins',
            'servings': '4',
            'cuisine': 'Italian',
            'difficulty': 'Easy',
            'tags': 'italian, pasta, pesto',
            'image_file': 'pasta.jpg'
        },
        {
            'title': 'Grilled Steak',
            'ingredients': '''400g ribeye steak
2 tbsp olive oil
2 garlic cloves, minced
Fresh rosemary
Salt and pepper
Butter''',
            'instructions': '''1. Season steak generously with salt and pepper.

2. Heat grill or cast-iron pan to high.

3. Sear steak 4 minutes per side for medium-rare.

4. Add butter, garlic, rosemary in last minute.

5. Baste steak with melted butter.

6. Rest for 5 minutes before slicing.''',
            'prep_time': '5 mins',
            'cook_time': '10 mins',
            'servings': '2',
            'cuisine': 'American',
            'difficulty': 'Easy',
            'tags': 'american, steak, grilled',
            'image_file': 'steak.jpg'
        },
        {
            'title': 'Baked Salmon',
            'ingredients': '''400g salmon fillets
2 tbsp olive oil
1 lemon, sliced
Fresh dill
Salt and pepper
Garlic powder''',
            'instructions': '''1. Preheat oven to 200°C.

2. Season salmon with salt, pepper, garlic powder.

3. Place on baking sheet, drizzle with oil.

4. Top with lemon slices and dill.

5. Bake for 12-15 minutes.

6. Serve immediately.''',
            'prep_time': '5 mins',
            'cook_time': '15 mins',
            'servings': '4',
            'cuisine': 'Healthy',
            'difficulty': 'Easy',
            'tags': 'healthy, salmon, baked',
            'image_file': 'salmon.jpg'
        },
        {
            'title': 'Chicken Noodle Soup',
            'ingredients': '''400g chicken breast
100g egg noodles
1 onion, chopped
2 carrots, sliced
2 celery stalks, sliced
1L chicken stock
2 garlic cloves, minced
Fresh parsley
Salt and pepper''',
            'instructions': '''1. Cook chicken in stock until tender.

2. Remove chicken, shred when cool.

3. Add onion, carrots, celery, garlic to stock.

4. Simmer for 15 minutes.

5. Add noodles, cook for 5 minutes.

6. Return shredded chicken to pot.

7. Season and garnish with parsley.''',
            'prep_time': '10 mins',
            'cook_time': '30 mins',
            'servings': '4',
            'cuisine': 'American',
            'difficulty': 'Easy',
            'tags': 'soup, chicken, comfort',
            'image_file': 'chicken_soup.jpg'
        },
        {
            'title': 'Vegetable Fried Rice',
            'ingredients': '''200g rice, cooked
1 carrot, diced
1 bell pepper, diced
50g peas
2 eggs
2 garlic cloves, minced
3 tbsp soy sauce
1 tbsp sesame oil
Green onions''',
            'instructions': '''1. Heat oil in wok or large pan.

2. Add garlic, cook for 30 seconds.

3. Add vegetables, stir fry for 3 minutes.

4. Push to side, scramble eggs.

5. Add rice, soy sauce.

6. Stir fry for 3-4 minutes.

7. Garnish with green onions.''',
            'prep_time': '10 mins',
            'cook_time': '10 mins',
            'servings': '4',
            'cuisine': 'Chinese',
            'difficulty': 'Easy',
            'tags': 'chinese, rice, vegetarian',
            'image_file': 'fried_rice.jpg'
        },
        {
            'title': 'Mac and Cheese',
            'ingredients': '''300g macaroni
200g cheddar cheese
50g parmesan cheese
500ml milk
2 tbsp butter
2 tbsp flour
Salt and pepper
Breadcrumb topping''',
            'instructions': '''1. Cook macaroni according to package.

2. Make roux: melt butter, add flour, cook 1 minute.

3. Gradually add milk, whisk until thick.

4. Add cheeses, stir until melted.

5. Season with salt and pepper.

6. Mix with drained pasta.

7. Top with breadcrumbs, bake at 180°C for 15 minutes.''',
            'prep_time': '10 mins',
            'cook_time': '25 mins',
            'servings': '4',
            'cuisine': 'American',
            'difficulty': 'Medium',
            'tags': 'american, pasta, cheese',
            'image_file': 'mac_cheese.jpg'
        },
        {
            'title': 'Swedish Meatballs',
            'ingredients': '''400g ground beef
50g breadcrumbs
1 egg
1 onion, finely chopped
200ml cream
2 tbsp butter
1 tbsp flour
Salt and pepper
Lingonberry jam''',
            'instructions': '''1. Mix beef, breadcrumbs, egg, onion, salt, pepper.

2. Form small meatballs.

3. Brown meatballs in butter.

4. Remove meatballs, make gravy with flour and cream.

5. Return meatballs to gravy.

6. Simmer for 10 minutes.

7. Serve with lingonberry jam.''',
            'prep_time': '15 mins',
            'cook_time': '20 mins',
            'servings': '4',
            'cuisine': 'Swedish',
            'difficulty': 'Medium',
            'tags': 'swedish, meatballs, comfort',
            'image_file': 'meatballs.jpg'
        },
        {
            'title': 'Chicken Shawarma',
            'ingredients': '''500g chicken thighs
4 pita breads
Tahini sauce
Shredded lettuce
Tomato, sliced
Pickles
2 tbsp shawarma spice
2 tbsp yogurt
Olive oil''',
            'instructions': '''1. Marinate chicken in yogurt, spice, oil for 2 hours.

2. Grill or bake chicken at 200°C for 20 minutes.

3. Slice chicken thinly.

4. Warm pita breads.

5. Fill with chicken, veggies, tahini.

6. Roll up and serve.''',
            'prep_time': '15 mins',
            'cook_time': '20 mins',
            'servings': '4',
            'cuisine': 'Middle Eastern',
            'difficulty': 'Medium',
            'tags': 'middle eastern, chicken, shawarma',
            'image_file': 'shawarma.jpg'
        },
        {
            'title': 'Bibimbap',
            'ingredients': '''200g rice, cooked
100g beef, thinly sliced
2 carrots, julienned
100g spinach
2 eggs
2 tbsp gochujang
1 tbsp sesame oil
Sesame seeds
Kimchi''',
            'instructions': '''1. Cook rice.

2. Stir fry beef with sesame oil.

3. Cook carrots and spinach separately.

4. Fry eggs sunny-side up.

5. Arrange everything over rice.

6. Top with gochujang and sesame seeds.

7. Mix before eating.''',
            'prep_time': '15 mins',
            'cook_time': '15 mins',
            'servings': '2',
            'cuisine': 'Korean',
            'difficulty': 'Medium',
            'tags': 'korean, rice, bibimbap',
            'image_file': 'bibimbap.jpg'
        },
        {
            'title': 'Pho',
            'ingredients': '''200g rice noodles
400g beef sirloin, thinly sliced
1L beef broth
1 onion, sliced
2 star anise
1 cinnamon stick
Fresh basil
Bean sprouts
Lime wedges
Hoisin sauce''',
            'instructions': '''1. Simmer broth with onion, star anise, cinnamon for 30 minutes.

2. Cook noodles according to package.

3. Strain broth.

4. Divide noodles into bowls.

5. Top with raw beef slices.

6. Pour hot broth over beef to cook it.

7. Add basil, bean sprouts, lime, hoisin.''',
            'prep_time': '15 mins',
            'cook_time': '35 mins',
            'servings': '4',
            'cuisine': 'Vietnamese',
            'difficulty': 'Medium',
            'tags': 'vietnamese, soup, pho',
            'image_file': 'pho.jpg'
        }
    ]

    for recipe in recipes:
        post = Post(
            title=recipe['title'],
            ingredients=recipe['ingredients'],
            instructions=recipe['instructions'],
            prep_time=recipe['prep_time'],
            cook_time=recipe['cook_time'],
            servings=recipe['servings'],
            cuisine=recipe['cuisine'],
            difficulty=recipe['difficulty'],
            tags=recipe['tags'],
            image_file=recipe['image_file'],
            date_posted=datetime.utcnow(),
            user_id=user.id
        )
        db.session.add(post)

    db.session.commit()
    print("Sample recipes added!")