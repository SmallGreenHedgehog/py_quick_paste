from setuptools import setup

APP = ['quick_paste.py']
DATA_FILES = ['ui_files']
MODULES = ['quick_paste','quick_base', 'quick_keyboard']
OPTIONS = {
    'iconfile':'ui_files/icon.icns',
}

setup(
    app=APP,
    name='py_quick_paste',
    version='v0.05',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    # py_modules=MODULES,
    license='',
    author='mrJill',
    author_email='jill.overlord@gmail.com',
    description=''
)
