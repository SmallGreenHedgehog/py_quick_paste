#!/bin/bash
rm -R build dist
pyinstaller --noconsole --add-data './src/ui_files:ui_files' --add-data './src/version:./' --name py_quick_paste -i ./src/ui_files/icon.icns ./src/quick_paste.py