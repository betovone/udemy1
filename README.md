# MARKDOWN

# cabecera h1
## cabecera h2
### cabecera h3
#### cabecera h4
##### cabecera h5
###### cabecera h6

underline 1
-----------

underline 2
===========

- *italica*
- _otra italica_
- **bold**
- __otro bold__

# Lista ordenada
1. item1
2. item2
3. item3
4. item4

# Links
- <a href="http;//google.com">Link html (html es soportado en MarkDown</a>
- [Link en Markdown](http://google.com)

# Imágenes
![Logo Github](https://cdn-icons-png.flaticon.com/512/25/25231.png)

# Code Snippets
```python

def calculate(rectangles):
    area = 0
    lista_sets_cuadrados = []
    for rectangle in rectangles:
        cuadrados = buscar_cuadrados(rectangle)
        if lista_sets_cuadrados:
            cuadrados.difference_update(*lista_sets_cuadrados)
            lista_sets_cuadrados.append(cuadrados)            
        else:
            lista_sets_cuadrados.append(cuadrados)
        area += len(cuadrados)
    print(area)
    return area
```

# Tablas
| Cabecera1 | Cabecera2 | Cabecera3 |
| --------- | --------- | --------- |
| registro 1| registro2 | registro3 |
| registro 1| registro2 | registro3 |

# citas
esto es un texto referente a una cita que pondremos abajo
> esto es una cita

# lineas divisoras
este texto será dividido

---
esto es otro texto dividido

---


# saltos de linea
este es el primer parrafo. para hacer salto de linea hay que darle 2 ENTER

este es el primer parrafo. para hacer salto de linea hay que darle 2 ENTER

este es el primer parrafo. para hacer salto de linea hay que darle 2 ENTER

