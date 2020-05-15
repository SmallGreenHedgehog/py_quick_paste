from setuptools import setup

APP = ['quick_paste.py']
DATA_FILES = ['ui_files']
OPTIONS = {
    'iconfile':'ui_files/Icon.icns',
}

setup(
    app=APP,
    name='py_quick_paste',
    version='v0.03',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    packages=[''],
    url='',
    license='',
    author='mrJill',
    author_email='',
    description=''
)