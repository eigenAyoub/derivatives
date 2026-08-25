
## Validation criteria

The implementation is considered correct only when it passes independent checks.

**Equity put–call parity**

$$
C-P=S_0e^{-qT}-Ke^{-rT}.
$$

**Futures put–call parity**

$$
C-P=e^{-rT}(F_0-K).
$$

**Greek verification**

Closed-form Greeks are compared with central finite differences over multiple strikes, maturities, and bump sizes.

**Implied-volatility round trip**

$$
\sigma \rightarrow V(\sigma) \rightarrow \widehat\sigma,
\qquad \widehat\sigma \approx \sigma.
$$

**Monte Carlo validation**

The closed-form price should lie inside the simulated confidence interval at the expected frequency. Across increasing path counts \(M\), ordinary Monte Carlo error should scale approximately as

$$
O(M^{-1/2}).
$$

## Suggested structure

```text
src/
  bsm.py
  black76.py
  implied_vol.py
  monte_carlo.py
tests/
  test_prices.py
  test_greeks.py
  test_implied_vol.py
  test_parity.py
notebooks/
  model_validation.ipynb
```

## Scope

Included: European calls and puts, continuous equity dividend yield, options on commodity futures, analytical Greeks, implied volatility, parity tests, and Monte Carlo validation.

Excluded: American exercise, volatility smiles, stochastic volatility, transaction costs, futures rolling, physical storage and convenience-yield modelling, and production market-data infrastructure.