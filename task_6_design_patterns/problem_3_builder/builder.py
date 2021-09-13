class Builder():

    def get_flavor(self):
        pass

    def get_ingredients(self):
        pass

    def get_pasteurization_level(self):
        pass

    def get_homogenization_level(self):
        pass

    def get_creaming_level(self):
        pass


class ChocolateIceCreamBuilder(Builder):

    def get_flavor(self):
        flavor = "Chocolate"
        return flavor

    def get_ingredients(self):
        ingredients = ["Chocolate chips", "Cream"]
        return ingredients

    def get_pasteurization_level(self):
        pasteurization_level = 8
        return pasteurization_level

    def get_homogenization_level(self):
        pasteurization_level = 7
        return pasteurization_level

    def get_creaming_level(self):
        pasteurization_level = 9
        return pasteurization_level


class BerryIceCreamBuilder(Builder):

    def get_flavor(self):
        flavor = "Strawberry"
        return flavor

    def get_ingredients(self):
        ingredients = ["Cherry", "Strawberries", "Blue berry", "Red apples", "Greek yogurt", "Icing sugar", "Lemon juice"]
        return ingredients

    def get_pasteurization_level(self):
        pasteurization_level = 8
        return pasteurization_level

    def get_homogenization_level(self):
        pasteurization_level = 7
        return pasteurization_level
