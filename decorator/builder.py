from beverages import Espresso, DarkRoast, HouseBlend, Decaf
from condiments import Mocha, Milk, Soy, Whip, Caramel

bases = {
    "Espresso": Espresso,
    "DarkRoast": DarkRoast,
    "HouseBlend": HouseBlend,
    "Decaf": Decaf,
}

decorators = {
    "Mocha": Mocha,
    "Milk": Milk,
    "Soy": Soy,
    "Whip": Whip,
    "Caramel": Caramel,
}

def build_beverage(base_name: str, size: str, condiments: list[str]):
    """
    Construye una bebida con la base, tamaño y condimentos especificados.

    :param base_name: Nombre de la bebida base (e.g., "Espresso").
    :param size: Tamaño de la bebida (e.g., "Tall", "Grande", "Venti").
    :param condiments: Lista de nombres de condimentos a añadir (e.g., ["Mocha", "Whip"]).
    :return: Instancia de la bebida con los condimentos aplicados.
    """
    if base_name not in bases:
        raise ValueError(f"Bebida base '{base_name}' no reconocida.")
    
    # Crear la bebida base con el tamaño especificado
    beverage = bases[base_name](size=size)
    
    # Añadir cada condimento en el orden especificado
    for condiment_name in condiments:
        if condiment_name not in decorators:
            raise ValueError(f"Condimento '{condiment_name}' no reconocido.")
        beverage = decorators[condiment_name](beverage)
    
    return beverage