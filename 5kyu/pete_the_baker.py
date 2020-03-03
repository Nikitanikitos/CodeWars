def cakes(recipe, available):
    res = 10000
    for key, item in recipe.items():
        if key not in available:
            return 0
        else:
            if res >= available[key] // item:
                res = available[key] // item
    return res


recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
total = cakes(recipe, available)
print(total)