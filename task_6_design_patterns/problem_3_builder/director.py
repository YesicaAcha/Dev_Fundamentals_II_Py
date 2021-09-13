import self as self

from task_6_design_patterns.problem_3_builder.icecream import IceCream


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_ice_cream(self):
        ice_cream = IceCream()

        flavor = self.__builder.get_flavor()
        ice_cream.set_flavor(flavor)

        ingredients = self.__builder.get_ingredients()
        ice_cream.set_ingredients(ingredients)

        pasteurization_level = self.__builder.get_pasteurization_level()
        ice_cream.set_pasteurization_level(pasteurization_level)

        homogenization_level = self.__builder.get_homogenization_level()
        ice_cream.set_homogenization_level(homogenization_level)

        creaming_level = self.__builder.get_creaming_level()
        ice_cream.set_creaming_level(creaming_level)

        return ice_cream
