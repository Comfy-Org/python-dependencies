# -*- mode: python ; coding: utf-8 -*-

import os
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_all, collect_submodules

block_cipher = None

def include_folder(folder_name):
    base_path = os.path.join(os.getcwd(), folder_name)
    files_to_include = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, start=os.getcwd())
            # Ensure the destination path doesn't include the filename as a directory
            destination_path = os.path.dirname(relative_path)
            files_to_inclu
            de.append((full_path, destination_path))
    return files_to_include

spandrel_datas, spandrel_binaries, spandrel_hiddenimports = collect_all('spandrel')
kornia_datas, kornia_binaries, kornia_hiddenimports = collect_all('kornia')

comfy_required_folders = [
        ('output/_output_images_will_be_put_here', 'output'),
        ('custom_nodes/example_node.py.example', 'custom_nodes'),
        *include_folder('web'),
        *include_folder('models'),
        *include_folder('comfy_extras'),
        ('input/example.png', 'input'),
        *include_folder('user'),
    ]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=comfy_required_folders,
    hiddenimports=[
        'spandrel',
        'kornia',
    ],
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
    [],
    exclude_binaries=True,
    name='ComfyUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    argv=['--front-end-version', 'Comfy-Org/ComfyUI_frontend@latest'],
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ComfyUI',
)
