# Mi Aplicación de Registro de Empleados

Este proyecto es una aplicación de escritorio desarrollada en Python que permite registrar empleados y visualizar sus datos en una matriz. La aplicación utiliza Kivy para la interfaz gráfica y está estructurada en varios módulos para una mejor organización del código.

## Estructura del Proyecto

```
mi-aplicacion
├── src
│   ├── main.py          # Punto de entrada de la aplicación
│   ├── ui
│   │   └── __init__.py  # Definiciones de la interfaz de usuario
│   ├── models
│   │   └── __init__.py  # Estructuras de datos para los empleados
│   ├── controllers
│   │   └── __init__.py  # Lógica de controladores
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación del proyecto
```

## Instalación

1. Clona este repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Instala las dependencias necesarias ejecutando:

```
pip install -r requirements.txt
```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python src/main.py
```

## Características

- Registro de empleados con nombre, cédula, ID, cargo y sueldo.
- Visualización de todos los empleados registrados en una matriz.
- Interfaz de usuario intuitiva con botones centrados.
- Pantalla emergente cuadrada para mostrar mensajes de éxito y error.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.