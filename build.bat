@echo off
FOR /F "delims=" %%B IN ( 'python -c "import __version__;print(__version__.__version__)"') DO ( Set "Version=%%B" )

pyinstaller --noconfirm --onefile --windowed --icon "%cd%\images\logo.ico" --add-data "%cd%\images\logo.ico;.\images" --name "AUE-Python-%VERSION%.py"   "%cd%\AUE-Python.py"

tar.exe -a -c -f dist/AUE-Python-%VERSION%.zip images\logo.ico PySimpleGUI.py data_indexes.py extra.py AUE-Python.py __main__.py