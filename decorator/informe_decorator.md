
## 📝 Informe de diseño

### ✔️ Propagación del tamaño (`size`)

Se agregó un atributo `_size` a la clase base `Beverage`, con métodos `set_size(size)` y `get_size()`.  
En vez de duplicar esa información en cada decorador, los condimentos acceden al tamaño directamente desde la bebida que están envolviendo usando:

```python
size = self._beverage.get_size()
```

Esto permite que decoradores como `Soy` cobren precios distintos según el tamaño (`Tall`, `Grande`, `Venti`) sin necesidad de guardar ese estado ellos mismos.

---

## Manejo de tamaños en las bebidas

Para el manejo de los tamaños se decidió centralizar los costos adicionales en la clase base `Beverage`.  
Esto se implementó mediante un diccionario de clase:

```python
SIZE_COST = {"Tall": 0.0, "Grande": 0.10, "Venti": 0.20}
```
Esto permite:

- Mantenibilidad: todos los recargos viven en un único lugar.

- Simplicidad: cada bebida suma precio_base + size_cost() sin condicionales.

- Extensibilidad: agregar o modificar tamaños requiere solo editar el diccionario.

### ✔️ Composición de condimentos (diseño flexible)

Gracias al patrón Decorator, se pueden encadenar múltiples condimentos, incluso del mismo tipo (doble, triple).  
Se implementó una función `build_beverage(base, size, condiments)` para construir bebidas decoradas a partir de un nombre base, un tamaño y una lista de strings con condimentos.  
Esto simplifica el uso y mejora la legibilidad.

---

### ✔️ Pretty Print de descripción

Para mejorar la presentación, se agregó un decorador opcional `PrettyDescriptionDecorator` que analiza la cadena de descripción y reemplaza repeticiones como `"Mocha, Mocha"` por `"Double Mocha"`.  
Este decorador **no afecta el cálculo de costo**, solo modifica el resultado de `get_description()`.

---

### ✔️ Pruebas

Se escribieron tests con `pytest` para validar:
- El costo total de combinaciones con uno o varios condimentos.
- La correcta lectura del tamaño desde decoradores.
- La descripción final.

Los tests están en `test_decorator.py` y cubren al menos 3 casos representativos, incluyendo bebidas grandes, dobles, triples y con decoradores múltiples.
