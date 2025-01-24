import difflib

# Predefined database of recipes
recipes = [
    {
        "name": "Spaghetti with Tomato Sauce",
        "ingredients": ["tomato", "pasta", "garlic", "olive oil"],
        "instructions": "Boil pasta. Saute garlic in olive oil, add tomatoes, and cook into a sauce. Mix pasta with sauce."
    },
    {
        "name": "Garlic Bread",
        "ingredients": ["bread", "garlic", "butter", "parsley"],
        "instructions": "Mix garlic with butter. Spread on bread and bake until golden brown. Sprinkle with parsley."
    },
    {
        "name": "Vegetable Stir Fry",
        "ingredients": ["bell pepper", "onion", "soy sauce", "broccoli"],
        "instructions": "Stir-fry vegetables in a pan with soy sauce."
    },
]

def find_matching_recipes(user_ingredients):
    """
    Finds recipes that match the user's available ingredients.
    :param user_ingredients: List of ingredients user has.
    :return: List of recipes sorted by match percentage.
    """
    matches = []

    for recipe in recipes:
        recipe_ingredients = recipe["ingredients"]
        matched = set(user_ingredients) & set(recipe_ingredients)
        match_percentage = (len(matched) / len(recipe_ingredients)) * 100

        matches.append({
            "name": recipe["name"],
            "match_percentage": match_percentage,
            "missing_ingredients": list(set(recipe_ingredients) - set(user_ingredients)),
            "instructions": recipe["instructions"]
        })

    # Sort recipes by match percentage in descending order
    matches = sorted(matches, key=lambda x: x["match_percentage"], reverse=True)
    return matches

# Main program
def main():
    print("Welcome to the AI Recipe Generator!")
    print("Enter your available ingredients, separated by commas:")
    user_input = input("Ingredients: ").lower()
    user_ingredients = [ingredient.strip() for ingredient in user_input.split(",")]

    # Find matching recipes
    matching_recipes = find_matching_recipes(user_ingredients)

    if matching_recipes:
        print("\nHere are the recipes you can make:")
        for recipe in matching_recipes:
            print(f"\nRecipe: {recipe['name']}")
            print(f"Match: {recipe['match_percentage']:.2f}%")
            if recipe["missing_ingredients"]:
                print(f"Missing Ingredients: {', '.join(recipe['missing_ingredients'])}")
            print(f"Instructions: {recipe['instructions']}")
    else:
        print("\nNo matching recipes found. Try adding more ingredients!")

if __name__ == "__main__":
    main()
