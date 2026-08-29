from BSM import *

import numpy as np

def generate_option_value_table(s, x, t, sigma, rf, div):
    for ss in range(s,s+10):
        call = BSMEuroCallOption(ss, x, t, sigma, rf, div)
        put  = BSMEuroCallOption(ss, x, t, sigma, rf, div)
        print(
        f"${ss:9.2f}"
        f"{call.value:15.4f}"
        f"{put.value:15.4f}"
        f"{call.delta:15.4f}"
        f"{put.delta:15.4f}"
    )



def generate_value_IV(s, x, t, sigma, rf, div, mkt_v):
    negative_call = 222 
    negative_sigma = 222 
    for sig in np.arange(sigma-0.4, sigma+0.4, 0.01):
        call = BSMEuroCallOption(s, x, t, sig, rf, div)
        if call.value - mkt_v < 0 :
            negative_call = call.value
            negative_sigma = sig
        else:
            print(
            f"${negative_sigma:9.2f}"
            f"{negative_call:15.4f}"
            f"{negative_call - mkt_v:15.4f}"
        )
            print(
            f"${sig:9.2f}"
            f"{call.value:15.4f}"
            f"{call.value - mkt_v:15.4f}"
        )
            return sig, negative_sigma

    return sig

s,x,t,sigma,rf,div, mkt_v = 92.76, 90, 100/365, 0.5, 0.01, 0.00, 7.4

p_sig, n_sig = generate_value_IV(s, x, t, sigma, rf, div, mkt_v)


for i in range(100):
    m = (n_sig + p_sig)/2
    new_call_value = BSMEuroCallOption(s, x, t, m, rf, div).value - mkt_v
    if new_call_value < 0:
        n_sig = m 
    else:
        p_sig = m
print(n_sig, p_sig)