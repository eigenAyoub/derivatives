# European Option Pricing: BSM and Black–76

An educational implementation of European option pricing. The aim is to learn the mathematics by following the same cycle for every result:

\[
\text{derive it} \rightarrow \text{implement it} \rightarrow \text{test it independently}.
\]

This is not a production trading library. The code is intended to make the assumptions, formulas, numerical methods, and failure modes visible enough to teach from.

## Project goals

- Implement Black–Scholes–Merton for European equity options and Black–76 for European options on commodity futures, including closed-form Greeks and implied-volatility inversion.
- Validate closed-form prices using put–call parity, Monte Carlo confidence intervals, and convergence tests.

Black–Scholes–Merton takes the equity spot price \(S_0\) and dividend yield \(q\) as inputs. Black–76 takes the futures price \(F_0\) as its underlying. The project does not treat a commodity futures option as an ordinary spot-equity option.

## Learning progression

| Stage | Read | Solve | Implement |
|---|---|---|---|
| 1. Stochastic model | [MIT 18.642: stochastic calculus](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_lec19_1.pdf) | [Oxford exercises](https://people.maths.ox.ac.uk/howison/o10/exercises.pdf), 15 and 18–20 | Exact geometric-Brownian-motion terminal sampler |
| 2. BSM prices | [MIT 18.642: Black–Scholes PDE](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_lec24.pdf) | Oxford 19, 28 and 43 | [BU FE459 Assignment 7, Task 1](https://cs-people.bu.edu/azs/fe459/assignments/a7.html): calls, puts and delta |
| 3. Greeks | [Imperial: dependence of the BSM price on its parameters](https://www.ma.imperial.ac.uk/~bin06/ULL/ull4a.pdf) | Oxford 30–31 and [UT Austin Homework 6](https://web.ma.utexas.edu/users/mcudina/m339w-hw6-impl-vol.pdf) | Delta, gamma, vega, theta and rho; verify each with finite differences |
| 4. Implied volatility | Imperial notes above | UT Homework 6, problems 6.1–6.2 | [BU FE459 Assignment 7, Task 2](https://cs-people.bu.edu/azs/fe459/assignments/a7.html): inversion; extend it with safeguarded Newton and bisection |
| 5. Black–76 | [NYU Futures and Options notes](https://people.stern.nyu.edu/sfiglews/documents/Figlewski%20Class%20Notes%20for%20Futures%20and%20Options%20UG%20Spring18-full%20set.pdf), pp. 97–103 | Oxford 51–52 | Black–76 calls, puts, Greeks and implied volatility |
| 6. Validation | Review the model identities below | [UT Austin Homework 5](https://web.ma.utexas.edu/users/mcudina/m339d-hw5.pdf) and Oxford 19, 52 | [BU FE459 Assignment 8](https://cs-people.bu.edu/azs/fe459/assignments/a8.html): Monte Carlo pricing and standard errors; extend it to confidence intervals and convergence tests |

The published programming assignment directly implements BSM, delta, implied volatility, and Monte Carlo pricing. Full Greeks, Black–76, Black–76 implied volatility, and formal convergence experiments are deliberate extensions completed in this repository.

## Validation criteria

The implementation is considered correct only when it passes independent checks.

**Equity put–call parity**

\[
C-P=S_0e^{-qT}-Ke^{-rT}.
\]

**Futures put–call parity**

\[
C-P=e^{-rT}(F_0-K).
\]

**Greek verification**

Closed-form Greeks are compared with central finite differences over multiple strikes, maturities, and bump sizes.

**Implied-volatility round trip**

\[
\sigma \rightarrow V(\sigma) \rightarrow \widehat\sigma,
\qquad \widehat\sigma \approx \sigma.
\]

**Monte Carlo validation**

The closed-form price should lie inside the simulated confidence interval at the expected frequency. Across increasing path counts \(M\), ordinary Monte Carlo error should scale approximately as

\[
O(M^{-1/2}).
\]

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
