#!/bin/bash
rm -R build dist
pyinstaller --noconsole --add-data './src/config.db:.' --add-data './src/ui_files:ui_files' --name py_quick_paste -i ./src/ui_files/icon.icns ./src/quick_paste.py