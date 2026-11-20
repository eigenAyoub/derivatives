# European Option Pricing

This is an on-going, educational repo. I intent to dig deep into Europoean option pricing, both theory and implementation. 


## Main project goals

- Implement Black–Scholes–Merton for European equity options, including closed-form Greeks and implied-volatility inversion.

- Validate closed-form prices using put–call parity, Monte Carlo confidence intervals, and convergence tests.


## Learning progression

| Stage | Read | Solve | Implement | Progress |
|---|---|---|---|---|
| **1. Risk-neutral stock model and terminal sampler** | [MIT 18.642, Stochastic Calculus](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_lec19_1.pdf) | Derive the log-price dynamics and expected stock price. [Oxford exercise 15](https://people.maths.ox.ac.uk/howison/o10/exercises.pdf) | Adapt [BU Assignment 8, Task 1](https://cs-people.bu.edu/azs/fe459/assignments/a8.html) to generate stock prices **at expiry**. Use one standard-normal draw per scenario. Check the sample mean against the theoretical mean. | **IN PROGRESS** (sampler pending) |
| **2. Analytical Black-Scholes prices and Delta** | [MIT 18.642, Black-Scholes differential equation](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_lec24.pdf) | Work through the PDE, put-call parity, and the shape of Delta. [Oxford exercises 18–20](https://people.maths.ox.ac.uk/howison/o10/exercises.pdf) | Follow [BU Assignment 7, Task 1](https://cs-people.bu.edu/azs/fe459/assignments/a7.html). Implement European call and put prices and their analytical Deltas. Add a put-call parity test. | **DONE** for prices and Delta (automated parity test pending) |
| **3. Monte Carlo pricing** | [BU Assignment 8, Task 2](https://cs-people.bu.edu/azs/fe459/assignments/a8.html), especially the European call and put examples | Price one contract analytically. Predict what should happen to the Monte Carlo standard error when you quadruple the sample count, then test it. | Follow the European-option portion of [BU Assignment 8](https://cs-people.bu.edu/azs/fe459/assignments/a8.html) using your stage 1 sampler. Return the discounted payoff mean, standard error, and 95% confidence interval. Use independent runs to check coverage against stage 2. | **TODO** |
| **4. Monte Carlo Delta** | [Imperial, The Greeks](https://www.ma.imperial.ac.uk/~bin06/ULL/ull4a.pdf), focusing on Delta | Write the central-difference estimate for Delta. Explain why the up-bump and down-bump valuations should reuse the same random draws. | Extend your stage 3 pricer. Calculate Delta at several bump sizes, repeat across seeds, and plot the error against analytical Delta. **First portfolio milestone.** | **TODO** |
| **5. Remaining analytical Greeks** | [Imperial, The Greeks](https://www.ma.imperial.ac.uk/~bin06/ULL/ull4a.pdf) | Derive Gamma, Vega, Theta, and Rho in [Oxford exercise 30](https://people.maths.ox.ac.uk/howison/o10/exercises.pdf). Exercise 31 is an optional hedging application. | Implement all four for European calls and puts. Check each against finite differences of the **analytical price**. Document Vega units and whether Theta is differentiated with respect to calendar time or time remaining. | **TODO** |
| **6. Implied-volatility inversion** | [Imperial, Implied Volatility and Greeks](https://www.ma.imperial.ac.uk/~bin06/ULL/ull4a.pdf) | [UT Austin Homework 6, problems 6.1–6.2](https://web.ma.utexas.edu/users/mcudina/m339w-hw6-impl-vol.pdf) | Extend [BU Assignment 7, Task 2](https://cs-people.bu.edu/azs/fe459/assignments/a7.html) into a reusable call/put bisection solver with price-bound checks. Test the round trip from volatility to price and back, including a low-Vega example. | **IN PROGRESS** (call example and bisection done) |

### Stage 1:

**The sampler is one Python function that returns an array of possible stock prices at expiry.** For example, `sample_terminal_prices(spot, rate, dividend_yield, volatility, maturity, n_samples, rng)` should return `n_samples` values. Each value comes from one independent standard-normal draw $Z \sim \mathcal{N}(0,1)$.

$$
S_T = S_0 \exp\left[\left(r - q - \frac{\sigma^2}{2}\right)T + \sigma\sqrt{T}\,Z\right].
$$

Check three cases:

- At $T = 0$, every output should equal $S_0$.
- At $\sigma = 0$, every output should equal $S_0 e^{(r-q)T}$.
- With positive time and volatility, the sample mean should approach $S_0 e^{(r-q)T}$ as the sample count grows. Allow for sampling error when comparing the two.


**That function and those checks complete stage 1.** In stage 3, you turn the simulated stock prices into option payoffs. [Oxford exercise 15](https://people.maths.ox.ac.uk/howison/o10/exercises.pdf)

### References: 

- **Stages 1 and 2.** Use MIT for the model and BU for the code. Oxford 15 gives you the expected-value check for the sampler. Oxford 19 gives you the parity check for the pricer. BU Assignment 8, Task 1 covers stock simulation more broadly, so generating only the terminal price is your adaptation. BU Assignment 7, Task 1 covers analytical pricing. [Oxford exercises](https://people.maths.ox.ac.uk/howison/o10/exercises.pdf) · [BU Assignment 8](https://cs-people.bu.edu/azs/fe459/assignments/a8.html) · [BU Assignment 7](https://cs-people.bu.edu/azs/fe459/assignments/a7.html)
- **Stage 3.** BU Task 2 contains European Monte Carlo call and put examples with standard errors and Black-Scholes comparisons. Stop at the heading *Valuing path-dependent (a.k.a. ‘Exotic’) options*. Checking confidence-interval coverage across repeated runs is your project extension. [BU Assignment 8, Task 2](https://cs-people.bu.edu/azs/fe459/assignments/a8.html)
- **Stages 4 and 5.** Read the Imperial Delta section for stage 4. Reusing the same random draws to estimate Delta is your extension of the BU pricer. Save Oxford 30 for stage 5, where it asks for the four Greeks you’ll implement. [Imperial notes](https://www.ma.imperial.ac.uk/~bin06/ULL/ull4a.pdf) · [Oxford exercises 30–31](https://people.maths.ox.ac.uk/howison/o10/exercises.pdf)
- **Stage 6.** Use UT Austin for the problems and BU for the coding exercise. Build on your existing call example by putting bisection in a reusable function, checking its inputs, and adding round-trip tests. [UT Austin Homework 6](https://web.ma.utexas.edu/users/mcudina/m339w-hw6-impl-vol.pdf) · [BU Assignment 7, Task 2](https://cs-people.bu.edu/azs/fe459/assignments/a7.html)