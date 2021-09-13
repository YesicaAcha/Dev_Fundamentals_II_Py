from task_6_design_patterns.problem_3_builder.builder import ChocolateIceCreamBuilder, BerryIceCreamBuilder
from task_6_design_patterns.problem_3_builder.director import Director

if __name__ == '__main__':
    chocolate_ice_cream_builder = ChocolateIceCreamBuilder()

    director = Director()

    print("Chocolate Ice Cream")
    director.set_builder(chocolate_ice_cream_builder)
    chocolate_ice_cream = director.get_ice_cream()
    chocolate_ice_cream.deliver_ice_cream()

    berry_ice_cream_builder = BerryIceCreamBuilder()

    print("Berry Ice Cream")
    director.set_builder(berry_ice_cream_builder)
    berry_ice_cream = director.get_ice_cream()
    berry_ice_cream.deliver_ice_cream()
