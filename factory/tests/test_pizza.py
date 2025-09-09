import pytest
from abstract_factory.store import NYPizzaStore, ChicagoPizzaStore
from abstract_factory.ingredients import Clams


def test_NYPizzaStore_create_NYPizzaStyle():
    # Arrange
    store = NYPizzaStore()
    # Act
    pizza = store.order_pizza("cheese")
    # Assert
    assert pizza.name == "NY Style Cheese Pizza"
    
def test_ChicagoPizzaStore_create_ChicagoPizzaStyle():
    # Arrange
    store = ChicagoPizzaStore()
    # Act
    pizza = store.order_pizza("cheese")
    # Assert
    assert pizza.name == "Chicago Style Cheese Pizza"
    
def test_ny_cheese_pizza_has_correct_dough_and_sauce():
    # Arrange
    store = NYPizzaStore()
    # Act
    pizza = store.order_pizza("cheese")
    # Assert
    assert pizza.sauce.name == "Marinara Sauce"
    assert pizza.dough.name == "Thin Crust Dough"
    
def test_chicago_clam_pizza_has_correct_ingredients():
    store = ChicagoPizzaStore()
    # Act
    pizza = store.order_pizza("clam")
    # Assert
    assert isinstance(pizza.clam, Clams)
    
    
    
#correr con \factory> python -m pytest tests/test_pizza.py