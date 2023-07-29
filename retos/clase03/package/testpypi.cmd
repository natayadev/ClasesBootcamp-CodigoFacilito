@ECHO OFF
ECHO -----------------------------------------------------
ECHO Making and upload the Package to TestPyPI
ECHO -----------------------------------------------------
py -m pip install --upgrade build
pause
py -m build
pause
py -m pip install --upgrade twine
pause
py -m twine upload --repository testpypi dist/*
pause
ECHO -----------------------------------------------------
ECHO Finished!
ECHO -----------------------------------------------------
pause