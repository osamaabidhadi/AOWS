# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('resources/background.png', 'resources'),('resources/ico_menu.png', 'resources'),('resources/img0.png', 'resources'),('resources/img1.png', 'resources'),('resources/img2.png', 'resources'),('resources/img3.png', 'resources'),('resources/img4.png', 'resources'),('resources/img5.png', 'resources'),('resources/no_image.png', 'resources'),('resources/test.png', 'resources')],
    hiddenimports=['PIL'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='AWOZ',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
     icon='ico_menu.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
