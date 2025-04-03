#pragma once
#include "pch.h"
#ifdef BLACK_SCHOLES_EXPORTS
#define BLACK_SCHOLES_API __declspec(dllexport)
#else
#define BLACK_SCHOLES_API __declspec(dllimport)
#endif

extern "C" {
	/*
	Standard Normal Probability Density Function implementation.
	Only needed for an approximation of CDF using Abramowitz and Stegun.
	*/
	double normalPDF(double x);

	/*
	Standard Normal Cumulative Distribution Function using the error function (erf)
	*/
	double normalCDF(double x);

	/*
	Computes d1 in the Black–Scholes model:
		d1 = [ln(S/K) + (r + sigma^2 / 2) * T] / [sigma * sqrt(T)]
	*/
	double computeD1(double S, double K, double r, double sigma, double T);

	/*
	Computes d2 in the Black-Scholes model:
		d2 = d1 - sigma * sqrt(T)

	@param d1
	@param sigma volatility (decimal s.t. 0 < sigma < 1)
	@param T time to maturity in years
	*/
	double computeD2(double d1, double sigma, double T);

	/*
	Computes Black-Scholes for the price of a European-style call option.
		Price = S * N(d1) - e^{-rt} * N(d2)

	@param S current underlying security price
	@param K strike price
	@param r risk-free rate (decimal s.t. 0 < r < 1)
	@param sigma volatility (decimal s.t. 0 < sigma < 1)
	@param T time to maturity in years
	@returns theoretical price of the given option
	*/
	BLACK_SCHOLES_API double blackScholesCall(double S, double K, double r, double sigma, double T);

	/*
	Computes Black-Scholes for the price of a European-style call option.
		Price = e^{-rT} * K * N(-d2) - S * N(-d1)

	@param S current underlying security price
	@param K strike price
	@param r risk-free rate (decimal s.t. 0 < r < 1)
	@param sigma volatility (decimal s.t. 0 < sigma < 1)
	@param T time to maturity in years
	@returns theoretical price of the given option
	*/
	BLACK_SCHOLES_API double blackScholesPut(double S, double K, double r, double sigma, double T);
}
