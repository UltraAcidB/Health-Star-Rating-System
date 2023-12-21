import hsr_calculator
import hsr_food 

item1 = hsr_food.HSR_food(
    name="Camembert cheese",
    category="3D",
    energy=1750,
    saturated_fat=22.5,
    total_sugars=0.5,
    sodium=652,
    concentrated_fnvl=0,
    fnvl=0,
    fibre=0,
    protein=16.4,
)

item2 = hsr_food.HSR_food(
    name="Instant chicken soup",
    category="2",
    energy=65,
    saturated_fat=0.1,
    total_sugars=0.5,
    sodium=290,
    concentrated_fnvl=0,
    fnvl=0,
    fibre=0.5,
    protein=0.3,
)

item3 = hsr_food.HSR_food(
    name="Fruit and nut muesli bar",
    category="2",
    energy=1735,
    saturated_fat=4.5,
    total_sugars=36.4,
    sodium=30,
    concentrated_fnvl=27,
    fnvl=43,
    fibre=5.0,
    protein=12.5,
)

item4 = hsr_food.HSR_food(
    name="Orange juice",
    category="1",
    energy=188.28,
    saturated_fat=0.2,
    total_sugars=8.4,
    sodium=1,
    concentrated_fnvl=100,
    fnvl=0,
    fibre=0.2,
    protein=0.7,
)

item5 = hsr_food.HSR_food(
    name="Milk",
    category="1D",
    energy=209,
    saturated_fat=1.3,
    total_sugars=5.1,
    sodium=47,
    concentrated_fnvl=0,
    fnvl=0,
    fibre=0,
    protein=3.3,
)

grocery_list = [item1, item2, item3, item4, item5]
for item in grocery_list:
    hsr_calculator.get_health_star_rating(item)
