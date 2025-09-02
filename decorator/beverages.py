# beverages.py
# Contiene el Componente y los Componentes Concretos del patrón.

from abc import ABC, abstractmethod

# --- Componente Abstracto ---
class Beverage(ABC):
    """
    La clase base para todas las bebidas. Utiliza el módulo abc para
    definir que es una clase abstracta.
    """
    SIZE_COST = {"Tall": 0.0, "Grande": 0.10, "Venti": 0.20}

    def __init__(self, size="Tall"):
        self.description = "Bebida Desconocida"
        self.size = size  # Nuevo atributo para el tamaño

    def get_description(self) -> str:
        """
        Devuelve la descripción de la bebida.
        """
        return self.description
    
    #Agrego get_size y set_size para el nivel 2 de la entrega 
    def set_size(self, size: str):
        """
        Cambia el tamaño de la bebida.
        Preferimos valores explícitos para evitar typos.
        """
        if size not in ("Tall", "Grande", "Venti"):
            raise ValueError("Size debe ser 'Tall', 'Grande' o 'Venti'")
        self.size = size

    def get_size(self) -> str:
        """
        Devuelve el tamaño de la bebida.
        """
        return self.size 
    
    #Nuevo método de costo así no repito lógica en cada bebida
    def cost_for_size(self, base_cost:float) -> float:
        """
        Método para que el aumento de costo según tamaño se de en todas 
        las bebidas.
        """
        return base_cost + self.SIZE_COST[self.size]


# --- Componentes Concretos ---
class HouseBlend(Beverage):
    """
    Café de la casa, un tipo específico de bebida.
    """
    def __init__(self, size="Tall"):
        super().__init__(size)
        self.description = "Café House Blend"

    def cost(self) -> float:
        base_cost = 0.89
        return self.cost_for_size(base_cost)
    
class DarkRoast(Beverage):
    """
    Café Dark Roast, un tipo específico de bebida.
    """
    def __init__(self, size="Tall"):
        super().__init__(size)
        self.description = "Café Dark Roast"

    def cost(self) -> float:
        base_cost = 0.99
        return self.cost_for_size(base_cost)

class Decaf(Beverage):
    """
    Café Descafeinado, un tipo específico de bebida.
    """
    def __init__(self, size="Tall"):
        super().__init__(size)
        self.description = "Café Descafeinado"

    def cost(self) -> float:
        base_cost = 1.05
        return self.cost_for_size(base_cost)

class Espresso(Beverage):
    """
    Café Espresso, un tipo específico de bebida.
    """
    def __init__(self, size="Tall"):
        super().__init__(size)
        self.description = "Espresso"

    def cost(self) -> float:
        base_cost = 1.99
        return self.cost_for_size(base_cost)
