@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing AutoPEP8...
ECHO -----------------------------------------
env\Scripts\autopep8.exe -i -r setup.py
env\Scripts\autopep8.exe -i -r multi_maths\__init__.py
env\Scripts\autopep8.exe -i -r multi_maths\__main__.py
env\Scripts\autopep8.exe -i -r multi_maths\__version__.py
env\Scripts\autopep8.exe -i -r multi_maths\cli.py
env\Scripts\autopep8.exe -i -r multi_maths\core.py
env\Scripts\autopep8.exe -i -r multi_maths\filters.py
env\Scripts\autopep8.exe -i -r multi_maths\info.py
env\Scripts\autopep8.exe -i -r multi_maths\multi_maths.py
env\Scripts\autopep8.exe -i -r multi_maths\tests\__init__.py
env\Scripts\autopep8.exe -i -r multi_maths\tests\test_arithmetic.py
env\Scripts\autopep8.exe -i -r multi_maths\tests\test_core.py
env\Scripts\autopep8.exe -i -r multi_maths\tests\test_filters.py
env\Scripts\autopep8.exe -i -r multi_maths\tests\test_geometry.py
env\Scripts\autopep8.exe -i -r multi_maths\tests\test_info.py
env\Scripts\autopep8.exe -i -r multi_maths\tests\test_statistics.py
env\Scripts\autopep8.exe -i -r multi_maths\mm_arithmetic\__init__.py
env\Scripts\autopep8.exe -i -r multi_maths\mm_arithmetic\mm_arithmetic.py
env\Scripts\autopep8.exe -i -r multi_maths\mm_geometry\__init__.py
env\Scripts\autopep8.exe -i -r multi_maths\mm_geometry\mm_geometry.py
env\Scripts\autopep8.exe -i -r multi_maths\mm_statistics\__init__.py
env\Scripts\autopep8.exe -i -r multi_maths\mm_statistics\mm_statistics.py
pause
ECHO -----------------------------------------
ECHO Runing flake8...
ECHO -----------------------------------------
env\Scripts\flake8.exe setup.py
env\Scripts\flake8.exe multi_maths\__init__.py
env\Scripts\flake8.exe multi_maths\__main__.py
env\Scripts\flake8.exe multi_maths\__version__.py
env\Scripts\flake8.exe multi_maths\cli.py
env\Scripts\flake8.exe multi_maths\core.py
env\Scripts\flake8.exe multi_maths\filters.py
env\Scripts\flake8.exe multi_maths\info.py
env\Scripts\flake8.exe multi_maths\multi_maths.py
env\Scripts\flake8.exe multi_maths\tests\__init__.py
env\Scripts\flake8.exe multi_maths\tests\test_arithmetic.py
env\Scripts\flake8.exe multi_maths\tests\test_core.py
env\Scripts\flake8.exe multi_maths\tests\test_filters.py
env\Scripts\flake8.exe multi_maths\tests\test_geometry.py
env\Scripts\flake8.exe multi_maths\tests\test_info.py
env\Scripts\flake8.exe multi_maths\tests\test_statistics.py
env\Scripts\flake8.exe multi_maths\mm_arithmetic\__init__.py
env\Scripts\flake8.exe multi_maths\mm_arithmetic\mm_arithmetic.py
env\Scripts\flake8.exe multi_maths\mm_geometry\__init__.py
env\Scripts\flake8.exe multi_maths\mm_geometry\mm_geometry.py
env\Scripts\flake8.exe multi_maths\mm_statistics\__init__.py
env\Scripts\flake8.exe multi_maths\mm_statistics\mm_statistics.py
pause
pause
ECHO -----------------------------------------
ECHO Runing PyLint...
ECHO -----------------------------------------
env\Scripts\pylint.exe setup.py
env\Scripts\pylint.exe multi_maths\__init__.py
env\Scripts\pylint.exe multi_maths\__main__.py
env\Scripts\pylint.exe multi_maths\__version__.py
env\Scripts\pylint.exe multi_maths\cli.py
env\Scripts\pylint.exe multi_maths\core.py
env\Scripts\pylint.exe multi_maths\filters.py
env\Scripts\pylint.exe multi_maths\info.py
env\Scripts\pylint.exe multi_maths\multi_maths.py
env\Scripts\pylint.exe multi_maths\tests\__init__.py
env\Scripts\pylint.exe multi_maths\tests\test_arithmetic.py
env\Scripts\pylint.exe multi_maths\tests\test_core.py
env\Scripts\pylint.exe multi_maths\tests\test_filters.py
env\Scripts\pylint.exe multi_maths\tests\test_geometry.py
env\Scripts\pylint.exe multi_maths\tests\test_info.py
env\Scripts\pylint.exe multi_maths\tests\test_statistics.py
env\Scripts\pylint.exe multi_maths\mm_arithmetic\__init__.py
env\Scripts\pylint.exe multi_maths\mm_arithmetic\mm_arithmetic.py
env\Scripts\pylint.exe multi_maths\mm_geometry\__init__.py
env\Scripts\pylint.exe multi_maths\mm_geometry\mm_geometry.py
env\Scripts\pylint.exe multi_maths\mm_statistics\__init__.py
env\Scripts\pylint.exe multi_maths\mm_statistics\mm_statistics.py
pause
pause