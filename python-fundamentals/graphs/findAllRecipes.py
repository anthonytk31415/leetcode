# Time: O(n)
# Space: O(n)

def findAllRecipes(recipes, ingredients, supplies):
    recipe_lookup = {}      # given recipe name, return index
    for i , recipe in enumerate(recipes): 
        recipe_lookup[recipe] = i

    supplies = set(supplies)
    visited = [False] *len(recipes)
    res = []

    ## needs to return true or false if you can complete the recipe 
    def dfs(i, res, visited, supplies, recipes, ingredients, recipe_lookup):
        visited[i] = True
        cur_recipe = recipes[i]
        cur_ingredients = ingredients[i]
        needed_ingredients = []

        for ingredient in cur_ingredients:
            if ingredient not in supplies:
                needed_ingredients.append(ingredient)

        for needed_ingredient in needed_ingredients:
            if needed_ingredient in recipe_lookup:
                j = recipe_lookup[needed_ingredient]
                if not visited[j] and dfs(j, res, visited, supplies, recipes, ingredients, recipe_lookup):
                    continue
                else:
                    return False
            else: 
                return False

        res.append(cur_recipe)
        supplies.add(cur_recipe)
        return True

    for i in range(len(recipes)):
        if not visited[i]:
             dfs(i, res, visited, supplies, recipes, ingredients, recipe_lookup)
                        
    return res

# recipes = ["bread"]
# ingredients = [["yeast","flour"]]
# supplies = ["yeast","flour","corn"]

# recipes = ["bread","sandwich"]
# ingredients = [["yeast","flour"],["bread","meat"]]
# supplies = ["yeast","flour","meat"]

# recipes = ["bread","sandwich","burger"]
# ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
# supplies = ["yeast","flour","meat"]

recipes = ["ju","fzjnm","x","e","zpmcz","h","q"]
ingredients = [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],
               ["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],
               ["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]]
supplies = ["f","hveml","cpivl","d"]

print(findAllRecipes(recipes, ingredients, supplies))