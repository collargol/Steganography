# -*- mode: python -*-

block_cipher = None

hi = ['scipy._lib.messagestream', 'numpy', 'tkinter', 'scipy', 'matplotlib', 'fixtk', 'scipy.signal', 'scipy.signal.bsplines', 'scipy.special', 'scipy.special._ufuncs_cxx',
                        'scipy.linalg.cython_blas',
                        'scipy.linalg.cython_lapack',
                        'scipy.integrate',
                        'scipy.integrate.quadrature',
                        'scipy.integrate.odepack',
                        'scipy.integrate._odepack',
                        'scipy.integrate.quadpack',
                        'scipy.integrate._quadpack',
                        'scipy.integrate._ode',
                        'scipy.integrate.vode',
                        'scipy.integrate._dop', 'scipy._lib', 'scipy._build_utils','scipy.__config__',
                        'scipy.integrate.lsoda', 'scipy.cluster', 'scipy.constants','scipy.fftpack','scipy.interpolate','scipy.io','scipy.linalg','scipy.misc','scipy.ndimage','scipy.odr','scipy.optimize','scipy.setup','scipy.sparse','scipy.spatial','scipy.special','scipy.stats','scipy.version']
a = Analysis(['gui.py'],
             pathex=['C:\\Users\\Piotr\\AppData\\Local\\Programs\\Python\\Python35-32\\Lib\\site-packages\\scipy\\extra-dll', 'F:\\Studia\\Krypto\\Steganography'],
             binaries=[],
             datas=[],
             hiddenimports=hi,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gui',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='key.ico')
