"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    Parameters:
        dish_name (str): The name of the dish.
        dish_ingredients (list): The ingredients for the dish.

    Returns:
        tuple: Containing (dish name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.

    """
    return (dish_name,set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    Parameters:
        drink_name (str): Name of the drink.
        drink_ingredients (list): Ingredients in the drink.

    Returns:
        str: `drink_name` appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
    has_alcohol = False
    for drink_ingredient in drink_ingredients:
        if drink_ingredient in ALCOHOLS:
            has_alcohol = True
            break

    return drink_name + (" Cocktail" if has_alcohol else " Mocktail")


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    Parameters:
        dish_name (str): The dish to be categorized.
        dish_ingredients (set): The ingredients for the dish.

    Returns:
        str: The dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    """

    IS_VEGAN = all(ingredient in VEGAN for ingredient in dish_ingredients)
    IS_VEGETARIAN = all(ingredient in VEGETARIAN for ingredient in dish_ingredients)
    IS_PALEO = all(ingredient in PALEO for ingredient in dish_ingredients)
    IS_KETO = all(ingredient in KETO for ingredient in dish_ingredients)
    IS_OMNIVORE = all(ingredient in OMNIVORE for ingredient in dish_ingredients)

    DISH_CATEGORY = ''
    if IS_VEGAN:
        DISH_CATEGORY = "VEGAN"
    if IS_VEGETARIAN:
        DISH_CATEGORY = "VEGETARIAN"
    if IS_PALEO:
        DISH_CATEGORY = "PALEO"
    if IS_KETO:
        DISH_CATEGORY = "KETO"
    if IS_OMNIVORE:
        DISH_CATEGORY = "OMNIVORE"

    return dish_name + ": " + DISH_CATEGORY
    


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    Parameters:
        dish (tuple): (dish name, list of dish ingredients).

    Returns:
        tuple: Containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    dish_name, dish_ingredients = dish
    special_ingredient_set = set()
    for dish_ingredient in dish_ingredients:
        if dish_ingredient in SPECIAL_INGREDIENTS:
            special_ingredient_set.add(dish_ingredient)

    return dish_name, special_ingredient_set


def compile_ingredients(dishes):
    """Create a master list of ingredients.

    Parameters:
        dishes (list): Dish ingredient sets.

    Returns:
        set: Ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """

    master_set = set()
    for dish in dishes:
      master_set.update(dish)

    return master_set

def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    Parameters:
        dishes (list): Group of dish names.
        appetizers (list): Group of appetizer names.

    Returns:
        list: Group of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    dish_set = set(dishes)
    appetizers_set = set(appetizers)
    return list(dish_set - appetizers_set)


def singleton_ingredients(dishes, intersection):
    """Find singleton ingredients within the group of dishes (ingredients that only appear once across dishes).

    Parameters:
        dishes (list): Group of ingredient sets.
        intersection (set): Can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.

    Returns:
        set: Containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """

    seen = set()
    duplicates = set()

    for dish in dishes:
        for ingredient in dish:
            if ingredient in seen:
                duplicates.add(ingredient)
            else:
                seen.add(ingredient)

    # Singletons are ingredients seen once minus those that appeared multiple times
    return seen - duplicates
