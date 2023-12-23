import hsr_calculator
import hsr_food 
import image_predictor

item_1 = hsr_food.HSR_food(
    name="Banh cuon",
    category="2",
    calories = 118*4.184,
    saturated_fat = 1.2,
    total_sugars = 1.2,
    sodium = 720,
    concentrated_fnvl = 0,
    fnvl = 0,
    fibre = 0.6,
    protein = 3,
)

item_2 = hsr_food.HSR_food(
    name = "Banh mi",
    category = "2",
    calories = 180*4.184,
    saturated_fat = 1.9,
    total_sugars = 1.7,
    sodium = 239,
    concentrated_fnvl = 0,
    fnvl = 20,
    fibre = 0.8,
    protein = 15,
)

item_3 = hsr_food.HSR_food(
    name = "Fried rice",
    category = "2",
    calories = 174*4.184,
    saturated_fat = 0.5,
    total_sugars = 0.6,
    sodium = 387,
    concentrated_fnvl=0,
    fnvl=0,
    fibre = 1.1,
    protein = 4.1,
)

item_4 = hsr_food.HSR_food(
    name = "Com tam",
    category = "2",
    calories = 178*4.184,
    saturated_fat = 2.1,
    total_sugars = 0.1,
    sodium = 135,
    concentrated_fnvl = 0,
    fnvl = 0,
    fibre = 0,
    protein= 11.7,
)

item_5 = hsr_food.HSR_food(
    name = "Omelette",
    category = "2",
    calories = 181*4.184,
    saturated_fat = 3.3,
    total_sugars = 0.4,
    sodium = 350,
    concentrated_fnvl=0,
    fnvl = 0,
    fibre = 0.4,
    protein = 12,
)
PATH = "D:/Projects/HealthStarRating/test-image.jpg"
grocery_list = [item_1, item_2, item_3, item_4, item_5]
pred_item = image_predictor.predict_image(PATH)
for item in grocery_list:
    if pred_item == item.name:
        hsr_calculator.get_health_star_rating(item)
