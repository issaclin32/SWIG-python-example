#pragma once
#include <vector>
#include <cmath>
#include "numpy/ndarrayobject.h"
#include <omp.h>

std::vector<int> find(std::vector<int>, std::vector<int>,
			std::vector<int>, std::vector<int>,
			std::vector<int>, std::vector<int>,
			bool);
			
void yell();