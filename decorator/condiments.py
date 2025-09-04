# condiments.py
# Contiene el Decorador Abstracto y los Decoradores Concretos.

from abc import ABC, abstractmethod

from sklearn import base
from beverages import Beverage

# --- Decorador Abstracto ---
class CondimentDecorator(Beverage, ABC):
    """
    Clase base para los decoradores de condimentos.
    Hereda de Beverage para tener el mismo tipo.
    Mantiene una referencia a la bebida que está envolviendo.
    """
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_size(self):
        return self._beverage.get_size()

    @abstractmethod
    def get_description(self) -> str:
        pass

# --- Decoradores Concretos ---
class Milk(CondimentDecorator):
    """
    Decorador para añadir Leche a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Leche"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10

class Mocha(CondimentDecorator):
    """
    Decorador para añadir Mocha a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20

class Soy(CondimentDecorator):
    """
    Decorador para añadir Soja a una bebida.
    """

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soja"

    def cost(self) -> float:
        return self._beverage.cost() + 0.15

class Whip(CondimentDecorator):
    """
    Decorador para añadir Crema a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Crema"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10

#Agrego el nuevo condimento Caramel
class Caramel(CondimentDecorator):
    """
    Decorador para añadir Caramel a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Caramel"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20

#Agrego el pretty print 
class PrettyPrint(CondimentDecorator):
    """
    Decorador de presentación que agrupa condimentos repetidos en la descripcion sin afectar el costo. 
    """
    def get_description(self) -> str:
        description = self._beverage.get_description()
        cost = round(self._beverage.cost(), 2)

        pedido = [p.strip() for p in description.split(",")] 

        base = pedido[:2]

        if len(pedido) <= 2:
            return f"{description} ${cost}"

        condimentos = {}
        for caracteristica in pedido[2:]:
            condimentos[caracteristica] = condimentos.get(caracteristica, 0) + 1
        

        desc_final = ", ".join(base)
        for condimento, cantidad in condimentos.items():
            if cantidad == 1:
                desc_final += f", {condimento}"
            elif cantidad == 2:
                desc_final += f", Double {condimento}"
            elif cantidad == 3:
                desc_final += f", Triple {condimento}"
            else:
                desc_final += f", {cantidad}x {condimento}"

        return f"{desc_final} ${cost}"

   
    