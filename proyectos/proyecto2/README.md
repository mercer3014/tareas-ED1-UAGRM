# 🧮 Gestor de Polinomios - Lista Enlazada

Un proyecto completo que implementa un gestor de polinomios utilizando listas enlazadas y el patrón MVC (Modelo-Vista-Controlador).

## 📋 Características

### ✅ Funcionalidades Implementadas
- **Crear Polinomios**: Construir polinomios P(x) y Q(x) usando listas enlazadas
- **Sumar Polinomios**: Operación P(x) + Q(x) con recorrido simultáneo
- **Multiplicar Polinomios**: Operación P(x) × Q(x) 
- **Evaluar Polinomios**: Calcular el valor del polinomio en un punto específico
- **Interfaz Gráfica**: Aplicación GUI moderna con Tkinter
- **Ordenamiento Automático**: Los términos se mantienen ordenados por exponente descendente

### 🏗️ Arquitectura del Proyecto

```
proyecto2/
├── models/
│   ├── nodo.py              # Clase Nodo para términos de polinomios
│   └── listaEnlazada.py     # Lista enlazada para polinomios
├── controllers/
│   └── controller.py        # Controlador principal (lógica de negocio)
├── view/
│   └── interfaz.py          # Interfaz gráfica con Tkinter
└── README.md               # Documentación del proyecto
```

## 🚀 Cómo Ejecutar

### Opción 1: Interfaz Gráfica (Recomendado)
```bash
python view/interfaz.py
```

### Opción 2: Pruebas de Modelos
```bash
python models/listaEnlazada.py
```

### Opción 3: Pruebas del Controlador
```bash
python controllers/controller.py
```

## 🎯 Uso de la Aplicación

### Interfaz Gráfica
La aplicación presenta una interfaz moderna dividida en dos paneles:

#### Panel Izquierdo - Controles
- **➕ Agregar Término**: Selecciona P(x) o Q(x), ingresa coeficiente y exponente
- **🔢 Evaluar Polinomio**: Evalúa P(x) o Q(x) en un valor específico de x
- **⚡ Operaciones**: Suma y multiplicación entre polinomios
- **🗂️ Gestión**: Ver y limpiar polinomios

#### Panel Derecho - Visualización
- **Visualización en tiempo real** de P(x) y Q(x)
- **Área de resultados** con historial de operaciones
- **Consejos de uso** integrados

## 🔧 Estructura Técnica

### Modelo (models/)
- **`Nodo`**: Representa un término del polinomio (coeficiente, exponente, siguiente)
- **`ListaEnlazada`**: Implementa el polinomio como lista enlazada ordenada

### Controlador (controllers/)
- **`PolinomioController`**: Maneja la lógica de negocio y operaciones
- Validación de entrada y manejo de errores robusto

### Vista (view/)
- **`PolinomioApp`**: Interfaz gráfica moderna con Tkinter
- Diseño responsivo y experiencia de usuario optimizada

## 📚 Ejemplos de Uso

### Crear Polinomios
```python
# P(x) = 3x² + 2x + 1
ctrl.agregar_termino('P', 3, 2)  # 3x²
ctrl.agregar_termino('P', 2, 1)  # 2x
ctrl.agregar_termino('P', 1, 0)  # 1

# Q(x) = x³ - 4x
ctrl.agregar_termino('Q', 1, 3)  # x³
ctrl.agregar_termino('Q', -4, 1) # -4x
```

### Operaciones
```python
# Suma: P(x) + Q(x)
resultado_suma = ctrl.sumar()

# Multiplicación: P(x) × Q(x)
resultado_mult = ctrl.multiplicar()

# Evaluación: P(2)
valor = ctrl.evaluar('P', 2)
```

## 🎨 Características de la Interfaz

- **Diseño Moderno**: Interfaz limpia y profesional
- **Validación en Tiempo Real**: Manejo de errores intuitivo
- **Historial de Operaciones**: Seguimiento completo de todas las operaciones
- **Responsive**: Se adapta a diferentes tamaños de ventana
- **Iconos y Emojis**: Interfaz visual atractiva

## 🔍 Validaciones Implementadas

- ✅ Coeficientes pueden ser decimales
- ✅ Exponentes deben ser enteros
- ✅ Validación de tipos de datos
- ✅ Manejo de errores robusto
- ✅ Confirmación antes de limpiar polinomios

## 🧪 Casos de Prueba

El proyecto incluye ejemplos de prueba en cada módulo:

1. **Modelos**: Prueba de listas enlazadas y operaciones básicas
2. **Controlador**: Prueba de la lógica de negocio
3. **Vista**: Interfaz gráfica completamente funcional

## 📖 Documentación del Código

- **Docstrings completos** en todas las clases y métodos
- **Comentarios explicativos** en código complejo
- **Nombres descriptivos** para variables y funciones
- **Estructura MVC clara** y bien definida

## 🎓 Conceptos Aplicados

- **Listas Enlazadas**: Estructura de datos fundamental
- **Patrón MVC**: Separación de responsabilidades
- **POO**: Programación orientada a objetos
- **GUI**: Interfaz gráfica de usuario
- **Validación de Datos**: Manejo robusto de entrada
- **Algoritmos de Ordenamiento**: Bubble sort para ordenar términos

---

**Desarrollado con ❤️ usando Python, Tkinter y listas enlazadas**
