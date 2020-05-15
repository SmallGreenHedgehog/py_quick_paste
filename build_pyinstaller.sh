#!/bin/bash
rm -R build dist
pyinstaller --noupx --onedir --onefile --noconsole  --name py_quick_paste -i ./src/ui_files/icon.icns ./src/quick_paste.py