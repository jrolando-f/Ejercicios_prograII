from beverages import Espresso, DarkRoast, HouseBlend
from condiments import Mocha, Whip, Soy, Caramel
from builder import build_beverage
import pytest

def test_espresso_tall_soy_soy():
    b = build_beverage("Espresso", "Tall", ["Soy","Soy"])
    assert b.get_description() == "Espresso, tamaño: Tall, Soja, Soja"
    assert round(b.cost(), 2) == 1.99 + 0.0 + 0.15 + 0.15
    
def test_decaf_grande_caramel_caramel_whip():
    b= build_beverage("Decaf", "Grande", ["Caramel","Caramel","Whip"])
    assert b.get_description() == "Café Descafeinado, tamaño: Grande, Caramel, Caramel, Crema"
    assert round(b.cost(), 2) == 1.65 #1.05 + 0.10 + 0.20 + 0.20 + 0.10
    
def test_houseblend_venti_mocha_mocha_leche():
    b= build_beverage("HouseBlend", "Venti", ["Mocha","Mocha","Milk"])
    assert b.get_description() == "Café House Blend, tamaño: Venti, Mocha, Mocha, Leche"
    assert round(b.cost(), 2) == 0.89 + 0.20 + 0.20 + 0.20 + 0.10
