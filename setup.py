from setuptools import Extension, setup

# load the C extentsion library
trig = Extension(
    name="pycbf.trig._trig",
    include_dirs=["pycbf/trig"],
    depends=["pycbf/trig/trig.h"],
    sources=["pycbf/trig/trig.c"]
)

# run setup tools
setup(
    name='pyusel-pycbf',
    description="C-Backed beamforming engines",
    author_email="wew12@duke.edu",
    packages=['pycbf', 'pycbf.trig', 'pycbf.trig._trig'],
    package_dir={
        'pycbf':'pycbf', 
        'pycbf.trig':'pycbf/trig',
        'pycbf.trig._trig':'pycbf/trig'
    },
    install_requires = [
        "numpy",
        "pyusel-cinpy @ https://github.com/wewightman/pyusel-cinpy/archive/main.tar.gz",
        "pyusel-interp @ https://github.com/wewightman/pyusel-interp/archive/main.tar.gz",
        "pyusel-types @ https://github.com/wewightman/pyusel-types/archive/main.tar.gz",
    ],
    license="MIT",
    ext_modules=[trig],
    version="0.0.0"
)