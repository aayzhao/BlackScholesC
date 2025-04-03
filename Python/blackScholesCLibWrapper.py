import ctypes as ct

class BlackScholesCLibWrapper:
    # setup
    _blackScholesLib = ct.WinDLL("x64/Debug/BlackScholesImpl.dll")

    # call options
    _blackScholesLib.blackScholesCall.argtypes = [ct.c_double, ct.c_double, ct.c_double, ct.c_double, ct.c_double]
    _blackScholesLib.blackScholesCall.restype = ct.c_double

    # put options
    _blackScholesLib.blackScholesPut.argtypes = [ct.c_double, ct.c_double, ct.c_double, ct.c_double, ct.c_double]
    _blackScholesLib.blackScholesPut.restype = ct.c_double

    @staticmethod
    def calcCall(S: float, K: float, r: float, sigma: float, T: float) -> float: # some semblance of type safety
        return BlackScholesCLibWrapper._blackScholesLib.blackScholesCall(S, K, r, sigma, T)
    
    @staticmethod
    def calcPut(S: float, K: float, r: float, sigma: float, T: float) -> float:
        return BlackScholesCLibWrapper._blackScholesLib.blackScholesPut(S, K, r, sigma, T)
    
    @staticmethod
    def largeCalcVolume():
        BlackScholesCLibWrapper._blackScholesLib.largeCalculationVolume()
        return

# expose wrapper functions at the module level
calcCallPriceC = BlackScholesCLibWrapper.calcCall
calcPutPriceC = BlackScholesCLibWrapper.calcPut
largeCalcVolC = BlackScholesCLibWrapper.largeCalcVolume