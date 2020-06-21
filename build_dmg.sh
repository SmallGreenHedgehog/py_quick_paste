#!/bin/sh
rm dist/py_quick_past*.dmg
vers=`cat ./src/version`
appdmg appdmg.json dist/py_quick_paste_v$vers.dmg