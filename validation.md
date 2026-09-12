
## Validation criteria

The implementation is considered correct only when it passes independent checks.

**Equity put–call parity**

$$
C-P=S_0e^{-qT}-Ke^{-rT}.
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

Included: European calls and puts, continuous equity dividend yield, analytical Greeks, implied volatility, parity tests, and Monte Carlo validation.

Excluded: American exercise, volatility smiles, stochastic volatility, transaction costs, and production market-data infrastructure.



## part 7:

GPT recommended take:

## 7. Volatility surfaces and local volatility

This is a stronger progression than adding another pricing formula. 

You already invert one option price into one implied volatility; now turn an entire grid of European option quotes into a calibrated, arbitrage-aware surface.


* It introduces actual market data and quote conventions.
* It demonstrates calibration and constrained optimization.
* It connects put–call parity, implied volatility, Greeks and Monte Carlo.
* It exposes numerical issues such as sparse strikes, bid–ask spreads and unstable derivatives.
* It is relevant to derivatives quant, quant developer, model-validation and trading-analytics roles.

I would do this before Heston. Otherwise, you would be calibrating a sophisticated model without first understanding the market object to which it is calibrated.

### The two university assignments

1. [NYU Courant — Derivative Securities, Assignment 8](https://math.nyu.edu/~goodman/teaching/DerivSec09/assignments/assignment8.pdf)

   Do Question 2. It asks you to:

   * simulate a state-dependent volatility model;
   * price European puts over a range of strikes;
   * invert those prices into Black–Scholes implied volatilities;
   * explain why local volatility and implied volatility are not the same function.

   This is an excellent conceptual bridge from your existing Monte Carlo and implied-volatility work. The associated course explicitly describes itself as preparation for the sell-side quantitative-finance industry. [NYU course page](https://math.nyu.edu/~goodman/teaching/DerivSec09/index.html)

2. [Imperial College London — Constructing the SSVI Local Volatility](https://www.ma.imperial.ac.uk/~ajacquie/IC_AMDP/IC_AMDP_Docs/AMDPProblemClassSSVI.pdf)

   This should be the main implementation. It asks you to:

   * calibrate the ATM total-variance term structure;
   * calibrate the SSVI skew parameters;
   * compare observed and fitted surfaces;
   * recover risk-neutral densities;
   * test for arbitrage;
   * compute Dupire local volatility;
   * validate the result using Monte Carlo repricing.

   It is almost exactly the project you need.

### Theoretical exercises

From the [Oxford sheet](https://people.maths.ox.ac.uk/howison/o10/exercises.pdf):

* **7(f):** understand a butterfly spread—the portfolio behind butterfly-arbitrage tests.
* **8(c–d):** derive monotonicity conditions across strikes and maturities.
* **35:** prove option prices increase with volatility, which supports implied-volatility inversion.
* **37:** derive digital-option prices.
* **40:** synthesize general payoffs from European calls across strikes.
* **41:** derive the forward equation for call prices as a function of strike.

Exercises 37, 40 and 41 are particularly valuable because they connect strike derivatives of call prices to digital prices and risk-neutral densities.

### Implementation scope

Keep it disciplined:

1. Use European index-option data, such as SPX-style contracts—not American single-stock options.
2. Convert quotes to forward log-moneyness \(k=\log(K/F_T)\).
3. Use OTM calls and puts, with put–call parity to normalize them.
4. Reject crossed, zero-bid and obvious arbitrage-violating quotes.
5. Compute implied volatility and total variance \(w(k,T)=\sigma_{\text{imp}}^2T\).
6. Fit SVI smiles and then an SSVI surface with explicit parameter constraints.

7. Test:
   * call-price monotonicity and convexity in strike;
   * nonnegative risk-neutral density;
   * calendar monotonicity of total variance;
   * calibration error relative to bid–ask width;
   * parameter stability under different initial guesses;
   * Monte Carlo repricing under the extracted local-volatility model.

Do not judge the fit only with implied-volatility RMSE. Report price error, volatility error and error measured relative to the bid–ask spread.

### Resulting CV bullet

> Built and calibrated an arbitrage-aware SSVI implied-volatility surface for European index options; extracted risk-neutral densities and Dupire local volatility and validated repricing through Monte Carlo simulation.


