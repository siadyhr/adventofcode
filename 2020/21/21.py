import sys
import re
import functools
import copy

# http://adventofcode.com/2020/day/21

possible_allergens = {}
all_ingredients = {}
foods = []
for rawin in sys.stdin:
    rawin = rawin[:-1] # newlinestrip
#    print('"' + rawin + '"')
    if rawin:
        ingredients, rest = rawin.split("(")
        ingredients = ingredients.split()
        for ingredient in ingredients:
            if not ingredient in all_ingredients:
                all_ingredients[ingredient] = 1
            else:
                all_ingredients[ingredient] += 1

        rest = [x.strip(",") for x in rest[8:-1].split()]
        foods.append([ingredients, rest])
        for allergen in rest:
            if allergen not in possible_allergens:
                possible_allergens[allergen] = set()
            possible_allergens[allergen] |= set(ingredients)
        print(ingredients)
#        print(rawin)
    else:
        pass

print(possible_allergens)
print(all_ingredients)
print(foods)
print()

def intersect_allergens(foods):
    possibilities = {}
    for allergen in possible_allergens.keys():
        possibilities[allergen] = possible_allergens[allergen]
        for food in foods:
            if allergen in food[1]:
                possibilities[allergen] &= set(food[0])
    return possibilities

def thin_allergens(possible_allergens):
    key_list = sorted(
            list(possible_allergens),
            key = lambda key: len(possible_allergens[key])
        )
    for allergen in key_list:
        ingredients = possible_allergens[allergen]
        if len(ingredients) == 1:
            for allergen2 in possible_allergens:
                if allergen2 != allergen:
                    possible_allergens[allergen2] -= ingredients
                    
    for ingredients in possible_allergens.values():
        if len(ingredients) > 1:
            print("!!!", ingredients)
    return possible_allergens

def sum_ingredients(ingredients):
    result = 0
    for food in foods:
        for ingredient in ingredients:
            if ingredient in food[0]:
                result += 1
    return result

intersected_allergens = intersect_allergens(foods)
print(intersected_allergens)
print("--")
thinned_allergens = thin_allergens(thin_allergens(intersected_allergens))
print("--")
print("Udtyndede allergener")
print(thinned_allergens)
bad_ingredients = set.union(*list(thinned_allergens.values()))
print("Dårlige ingredienser")
print(bad_ingredients)
good_ingredients = set(all_ingredients.keys()) - bad_ingredients
print("Gode ingredienser")
print(good_ingredients)
print("Sum af forekomst af gode ingredienser")
print(sum_ingredients(good_ingredients))
ingredient_allergen_pairs = {
        list(value)[0] : key for key, value in thinned_allergens.items()
    }
print("Ingrediens-allergen-par:")
print(ingredient_allergen_pairs)
canonical_dangerous_ingredient_list = sorted(
    bad_ingredients,
    key = lambda key : ingredient_allergen_pairs[key]
)
print(",".join(canonical_dangerous_ingredient_list))
