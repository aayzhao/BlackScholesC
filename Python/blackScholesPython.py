import math

def cdf(x: float) -> float:
    """Cumulative distribution function for the standard normal distribution."""
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def black_scholes_call(S: float, K: float, r: float, sigma: float, T: float) -> float:
    """
    Calculate the Black-Scholes call option price.

    Parameters:
        S (float): Current stock price.
        K (float): Strike price.
        T (float): Time to maturity (in years).
        r (float): Risk-free interest rate.
        sigma (float): Volatility of the underlying asset.

    Returns:
        float: Call option price.
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    call_price = S * cdf(d1) - K * math.exp(-r * T) * cdf(d2)
    return call_price

calcCallPricePython = black_scholes_call

# Example usage and timing:
if __name__ == "__main__":
    # Parameters
    S = 100.0    # Current stock price
    K = 100.0    # Strike price
    T = 1.0      # Time to maturity (1 year)
    r = 0.05     # Risk-free interest rate (5%)
    sigma = 0.2  # Volatility (20%)

    price = black_scholes_call(S, K, T, r, sigma)
    print("Black-Scholes Call Price:", price)
