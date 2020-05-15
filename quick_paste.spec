# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['src/quick_paste.py'],
             pathex=['/Volumes/Data/Users/user/PycharmProjects/py_quick_paste'],
             binaries=[],
             datas=[('./src/ui_files', './')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='quick_paste',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='src/ui_files/icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='quick_paste')
app = BUNDLE(coll,
             name='quick_paste.app',
             icon='./src/ui_files/icon.icns',
             bundle_identifier=None)
