
## 📝 Informe de diseño

### ✔️ Propagación del tamaño (`size`)

Se agregó un atributo `_size` a la clase base `Beverage`, con métodos `set_size(size)` y `get_size()`.  
En vez de duplicar esa información en cada decorador, los condimentos acceden al tamaño directamente desde la bebida que están envolviendo usando:

```python
size = self._beverage.get_size()
```

Esto permite que decoradores como `Soy` cobren precios distintos según el tamaño (`Tall`, `Grande`, `Venti`) sin necesidad de guardar ese estado ellos mismos.

---

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

Se escribieron tests con `assert` para validar:
- El costo total de combinaciones con uno o varios condimentos
- La correcta lectura del tamaño desde decoradores
- La descripción final (normal y con pretty print)

Los tests están en `test_decorator.py` y cubren al menos 5 casos representativos, incluyendo bebidas grandes, dobles, triples y con decoradores múltiples.
