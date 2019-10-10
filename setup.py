# distutils: language = c++

import platform
from distutils.extension import Extension
from distutils.core import setup
from Cython.Build import cythonize
import numpy

compile_extra_args = []
link_extra_args = []

if platform.system() == "Darwin":
    pass
    # compile_extra_args = ['-DMKL_ILP64', '-m64', '-std=c++11', "-mmacosx-version-min=10.9", "-isysroot/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk"]
# For CONDA
#     link_extra_args = ["-stdlib=libc++",  "-mmacosx-version-min=10.9", '-lmkl_intel_ilp64','-lmkl_sequential', '-lmkl_core', '-lpthread', '-lm', '-ldl']
# For MacPorts
    # link_extra_args = ["-stdlib=libc++", "-L/opt/intel/mkl/lib/", "-L/opt/intel/lib/", "-mmacosx-version-min=10.9", '-lmkl_intel_ilp64','-lmkl_sequential', '-lmkl_core', '-lpthread', '-lm', '-ldl']

elif platform.system() == "Linux":
    pass
    # compile_extra_args = ['-std=c++11']
    # link_extra_args = []

compile_files = ["PyNumPyTest.pyx"]

ext_modules = [Extension("PyNumPyTest", compile_files,
       include_dirs=[numpy.get_include()],
       extra_compile_args=compile_extra_args,
       extra_link_args=link_extra_args)]

setup(ext_modules = cythonize(ext_modules))