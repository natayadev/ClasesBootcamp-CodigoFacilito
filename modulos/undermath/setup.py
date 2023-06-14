from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except (IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='undermath',
    version='1.1.3',
    description='Este paquete contiene módulos para realizar cálculos \
aritméticos y estadísticos sencillos.',
    long_description=long_description,
    author='Underdoge',
    author_email='eduardo.chapa@gmail.com',
    url='https://github.com/Underdoge/undermath',
    install_requires=[
        'argparse',
        'importlib-metadata; python_version == "3.10"',
    ],
)
