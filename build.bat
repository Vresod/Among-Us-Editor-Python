@echo off

pyinstaller --noconfirm --onefile --windowed --icon "%cd%\images\logo.ico" --add-data "%cd%\images\logo.ico;.\images"  "%cd%\AUE-Python.py"

tar.exe -a -c -f dist/AUE-Python.zip images\logo.ico PySimpleGUI.py data_indexes.py extra.py AUE-Python.py __main__.py