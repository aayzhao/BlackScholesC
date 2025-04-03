"""Location of the main method for demonstration."""

import ctypes as ct
from blackScholesCLibWrapper import calcCallPriceC, calcPutPriceC
import timeit

def main():
    # setup
    blackScholesLib = ct.WinDLL("x64/Debug/BlackScholesImpl.dll")

    # call options
    blackScholesLib.blackScholesCall.argtypes = [ct.c_double, ct.c_double, ct.c_double, ct.c_double, ct.c_double]
    blackScholesLib.blackScholesCall.restype = ct.c_double

    # put options
    blackScholesLib.blackScholesPut.argtypes = [ct.c_double, ct.c_double, ct.c_double, ct.c_double, ct.c_double]
    blackScholesLib.blackScholesPut.restype = ct.c_double

    ## End of Setup ##
    
    # testing
    callPrice = calcCallPriceC(100.0, 100.0, 0.05, 0.20, 1.0)
    putPrice = calcPutPriceC(100.0, 100.0, 0.05, 0.20, 1.0)
    print(f"Black-Scholes Call Price: {callPrice}")
    print(f"Black-Scholes Put Price: {putPrice}")
    print("__________________________\n\n")

    # speed tests (ignore the switch in naming conventions)
    setup_code = """
from blackScholesCLibWrapper import largeCalcVolC, calcCallPriceC
from blackScholesPython import calcCallPricePython
S, K, r, sigma, T = 100.0, 100.0, 0.05, 0.20, 1.0
"""
    cdll_time = timeit.timeit('calcCallPriceC(S, K, r, sigma, T)', setup=setup_code, number=1)
    cdll_avg = cdll_time / 10000
    print("Total time for 10,000 DLL calls:", cdll_time)
    print("Average time per DLL call:", cdll_avg)
    print("__________________________\n\n")

    python_time = timeit.timeit('calcCallPricePython(S, K, r, sigma, T)', setup=setup_code, number=10000)
    python_avg = python_time / 10000
    print("Total time for 10,000 Python calls:", python_time)
    print("Average time per Python call:", python_avg)
    print("__________________________\n\n")
    
    cdll_time = timeit.timeit('largeCalcVolC', setup=setup_code, number=1)
    cdll_avg = cdll_time / 10000
    print("Total time for 10,000 DLL calls:", cdll_time)
    print("Average time per DLL call:", cdll_avg)
    print("__________________________\n\n")

if __name__ == "__main__":
    main()