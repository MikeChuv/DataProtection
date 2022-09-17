@echo off
python -m PyQt5.uic.pyuic -x .\ui\about.ui -o .\src\forms\aboutWindow.py
python -m PyQt5.uic.pyuic -x .\ui\admin.ui -o .\src\forms\adminWindow.py
python -m PyQt5.uic.pyuic -x .\ui\mainWindow.ui -o .\src\forms\mainWindow.py
python -m PyQt5.uic.pyuic -x .\ui\newUserDialog.ui -o .\src\forms\newUserDialogWindow.py
python -m PyQt5.uic.pyuic -x .\ui\passwordChangeDialog.ui -o .\src\forms\passwordChangeDialogWindow.py

python .\src\main.py