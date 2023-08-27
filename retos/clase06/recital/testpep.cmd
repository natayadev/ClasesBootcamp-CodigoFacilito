@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing AutoPEP8...
ECHO -----------------------------------------
env\Scripts\autopep8.exe -i -r app.py
env\Scripts\autopep8.exe -i -r app\__init__.py
env\Scripts\autopep8.exe -i -r app\controllers\__init__.py
env\Scripts\autopep8.exe -i -r app\controllers\default.py
env\Scripts\autopep8.exe -i -r app\models\__init__.py
env\Scripts\autopep8.exe -i -r app\models\queues.py
env\Scripts\autopep8.exe -i -r app\tests\__init__.py
env\Scripts\autopep8.exe -i -r app\tests\test_default.py
env\Scripts\autopep8.exe -i -r app\views\__init__.py
env\Scripts\autopep8.exe -i -r app\views\default.py
env\Scripts\autopep8.exe -i -r app\views\stage.py
env\Scripts\autopep8.exe -i -r app\views\stage_logo.py
pause
ECHO -----------------------------------------
ECHO Runing flake8...
ECHO -----------------------------------------
env\Scripts\flake8.exe app.py
env\Scripts\flake8.exe app\__init__.py
env\Scripts\flake8.exe app\controllers\__init__.py
env\Scripts\flake8.exe app\controllers\default.py
env\Scripts\flake8.exe app\models\__init__.py
env\Scripts\flake8.exe app\models\queues.py
env\Scripts\flake8.exe app\tests\__init__.py
env\Scripts\flake8.exe app\tests\test_default.py
env\Scripts\flake8.exe app\views\__init__.py
env\Scripts\flake8.exe app\views\default.py
env\Scripts\flake8.exe app\views\stage.py
env\Scripts\flake8.exe app\views\stage_logo.py
pause
pause
ECHO -----------------------------------------
ECHO Runing PyLint...
ECHO -----------------------------------------
env\Scripts\pylint.exe app.py
env\Scripts\pylint.exe app\__init__.py
env\Scripts\pylint.exe app\controllers\__init__.py
env\Scripts\pylint.exe app\controllers\default.py
env\Scripts\pylint.exe app\models\__init__.py
env\Scripts\pylint.exe app\models\queues.py
env\Scripts\pylint.exe app\tests\__init__.py
env\Scripts\pylint.exe app\tests\test_default.py
env\Scripts\pylint.exe app\views\__init__.py
env\Scripts\pylint.exe app\views\default.py
env\Scripts\pylint.exe app\views\stage.py
env\Scripts\pylint.exe app\views\stage_logo.py
pause
pause