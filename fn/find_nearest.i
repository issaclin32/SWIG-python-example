/* find_nearest.i */
%module find_nearest  /*module name*/

%inline %{
#include "find_nearest.h"
%}

%include <std_vector.i>
%include <std_complex.i>
%template(vector_int) std::vector<int>;
%template(vector_double) std::vector<double>;


%include "./numpy.i"
%inline %{
#define SWIG_FILE_WITH_INIT
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
%}
%init %{
import_array();
%}

%include "find_nearest.h"


