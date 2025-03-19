#pragma once

/*
Standard Normal Probability Density Function implementation
*/
double normalPDF(double x);

/*
Standard Normal Cumulative Distribution Function using the error function (erf)
*/
double normalCDF(double x);

/*
Computes d1 in the Black–Scholes model:
		   ln(S/K) + (r + sigma^2 / 2) * T
	d1 =  ---------------------------------
	              sigma * sqrt(T)
or: 
	d1 = [ln(S/K) + (r + sigma^2 / 2) * T] / [sigma * sqrt(T)]
*/
double computeD1(double S, double K, double r, double sigma, double T);