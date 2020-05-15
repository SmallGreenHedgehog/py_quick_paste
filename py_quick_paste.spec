# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['src/quick_paste.py'],
             pathex=['/Volumes/Data/Users/user/PycharmProjects/py_quick_paste'],
             binaries=[],
             datas=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='py_quick_paste',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='src/ui_files/icon.icns')
app = BUNDLE(exe,
             name='py_quick_paste.app',
             icon='./src/ui_files/icon.icns',
             bundle_identifier=None)
