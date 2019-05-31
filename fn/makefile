#Makefile
#-fPIC can be ignored on Windows platform
# This should be compiled using VS Build Tools(x64 native) 2017 or above

PYTHON_PATH = $(USERPROFILE)\Anaconda3
all: _find_nearest.pyd
rebuild: clean _find_nearest.pyd
_find_nearest.pyd: find_nearest.h find_nearest.cpp find_nearest_wrap.cxx
	cl /openmp /O2 /EHsc /LD /Fe:_find_nearest.pyd /I$(PYTHON_PATH)\include /I$(PYTHON_PATH)\Lib\site-packages\numpy\core\include find_nearest.cpp find_nearest_wrap.cxx /link /LIBPATH:$(PYTHON_PATH)\libs /DEFAULTLIB:python3 /DEFAULTLIB:python36
find_nearest_wrap.cxx: find_nearest.i find_nearest.h find_nearest.cpp
	swig -c++ -python -py3 -v find_nearest.i
clean:
	del /f /s _find_nearest.pyd find_nearest_wrap.cxx find_nearest.py *.obj *.lib *.exp