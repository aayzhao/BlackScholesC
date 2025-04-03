"""Location of the main method for demonstration."""

import ctypes as ct
from blackScholesCLibWrapper import calcCallPriceC, calcPutPriceC
import time

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

if __name__ == "__main__":
    main()