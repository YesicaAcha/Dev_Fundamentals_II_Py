class IceCream:

    def __init__(self):
        self.__flavor = None
        self.__toppings = list()
        self.__pasteurization_level = None
        self.__homogenization_level = None
        self.__creaming_level = None

    def set_flavor(self, flavor):
        self.__flavor = flavor

    def set_ingredients(self, toppings):
        self.__toppings = toppings

    def set_pasteurization_level(self, pasteurization_level):
        self.__pasteurization_level = pasteurization_level

    def set_homogenization_level(self, homogenization_level):
        self.__homogenization_level = homogenization_level

    def set_creaming_level(self, creaming_level):
        self.__creaming_level = creaming_level

    def deliver_ice_cream(self):
        print(f"Flavor: {self.__flavor}, Toppings: {self.__toppings}, "
              f"Pasteurization level: {self.__pasteurization_level}, "
              f"Homogenization level: {self.__homogenization_level}, Creaming level: {self.__creaming_level}")
