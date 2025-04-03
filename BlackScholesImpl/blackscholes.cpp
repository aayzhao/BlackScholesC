#include "pch.h"
#include "blackscholes.h"
#include <cmath>

double WINAPI normalPDF(double x) {
    static const double INV_SQRT_2PI = 0.3989422804014327;
    return INV_SQRT_2PI * std::exp(-0.5 * x * x);
}

double WINAPI normalCDF(double x) {
    return 0.5 * (1.0 + std::erf(x / std::sqrt(2.0)));
}

double WINAPI computeD1(double S, double K, double r, double sigma, double T) {
    return (std::log(S / K) + (r + 0.5 * sigma * sigma) * T)
        / (sigma * std::sqrt(T));
}

double WINAPI computeD2(double d1, double sigma, double T) {
    return d1 - sigma * std::sqrt(T);
}

double WINAPI blackScholesCall(double S, double K, double r, double sigma, double T) {
    double d1 = computeD1(S, K, r, sigma, T);
    double d2 = computeD2(d1, sigma, T);

    double callPrice = S * normalCDF(d1) - K * std::exp(-r * T) * normalCDF(d2);
    return callPrice;
}

double WINAPI blackScholesPut(double S, double K, double r, double sigma, double T) {
    double d1 = computeD1(S, K, r, sigma, T);
    double d2 = computeD2(d1, sigma, T);

    double putPrice = K * std::exp(-r * T) * normalCDF(-d2) - S * normalCDF(-d1);
    return putPrice;
}