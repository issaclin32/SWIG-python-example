#include <cmath>
#include <vector>
#include "find_nearest.h"
#include "numpy/ndarrayobject.h"
#include <omp.h>
#include <iostream>

using std::sqrt;

// 1: white of eye, 0: skin
std::vector<int> find(std::vector<int> x, std::vector<int> y,
			std::vector<int> wx, std::vector<int> wy,
			std::vector<int> sx, std::vector<int> sy,
			bool show_message){
				
	std::vector<int> ret;
	omp_set_num_threads(omp_get_max_threads());
	
	if(show_message){
		std::cout << "c++ (input info): undetermined pixels (total pixels to be handled): " << x.size() << std::endl;
		std::cout << "c++ (input info): white_of_eye pixels: " << wx.size() << std::endl;
		std::cout << "c++ (input info): skin pixels: " << sx.size() << std::endl;
		std::cout << "c++ (system info): running with " << omp_get_max_threads() << " parallel threads." << std::endl;
	}

	for(int i=0; i<x.size(); i++){
		double min_dist_w = 99999999.0, min_dist_s = 99999999.0;
		if(show_message){
			if(i % 10000 == 0) std::cout << "c++: handling pixel " << i << "/" << x.size() << std::endl;
		}
		
		#pragma omp parallel for
		for(int j=0; j<wx.size(); j++){
			double dist = sqrt((wx[j]-x[i])*(wx[j]-x[i]) + (wy[j]-y[i])*(wy[j]-y[i]));
			if(dist < min_dist_w) min_dist_w = dist;
		}
		
		#pragma omp parallel for
		for(int j=0; j<sx.size(); j++){
			double dist = sqrt((sx[j]-x[i])*(sx[j]-x[i]) + (sy[j]-y[i])*(sy[j]-y[i]));
			if(dist < min_dist_s) min_dist_s = dist;
		}
		
		if(min_dist_w < min_dist_s) ret.push_back(1);
		else ret.push_back(0);
		
	}
	return ret;
}

void yell(){
	std::cout << "Ahhhhh!" << std::endl;
	return;
}
