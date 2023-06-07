from setuptools import setup

setup(
    name='paquete_de_prueba',
    description='Código fuente para publicar en PYPI el ejemplo de un paquete para la clases de módulos y paquetes del bootcamp de Python avanzado para Código Facilito',
    version='0.0.1',
    install_requires=[
        'importlib-metadata; python_version == "3.8"',
    ],
)