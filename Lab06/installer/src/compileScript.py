
import PyInstaller.__main__
import os

sourceDir = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
installerDir = os.path.abspath(os.path.join(sourceDir, os.pardir))
installerDir = os.path.abspath(os.path.join(installerDir, os.pardir))
installerDir = os.path.abspath(os.path.join(installerDir, 'installer-dist\\'))
# print(installerDir)
PyInstaller.__main__.run([  
    '--distpath',
    installerDir,
    f'--name=Lab06 Installer',
    '--windowed',
    '--noconfirm',
    os.path.join(sourceDir, 'main.py'), 
])