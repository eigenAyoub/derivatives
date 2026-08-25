# European Option Pricing

This is an on-going, educational repo. I intent to dig deep into Europoean option pricing, both theory and implementation. 

## Main project goals

- Implement Black–Scholes–Merton for European equity options and Black–76 for European options on commodity futures, including closed-form Greeks and implied-volatility inversion.

- Validate closed-form prices using put–call parity, Monte Carlo confidence intervals, and convergence tests.


## Learning progression

| Stage | Read | Solve | Implement | Progress |
|---|---|---|---|---|
| 1. Stochastic model | [MIT 18.642: stochastic calculus](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_lec19_1.pdf) | [Oxford exercises](https://people.maths.ox.ac.uk/howison/o10/exercises.pdf), 15 and 18–20 | Exact geometric-Brownian-motion terminal sampler | IN PROGRESS |
| 2. BSM prices | [MIT 18.642: Black–Scholes PDE](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_lec24.pdf) | Oxford 19, 28 and 43 | [BU FE459 Assignment 7, Task 1](https://cs-people.bu.edu/azs/fe459/assignments/a7.html): calls, puts and delta | DONE |
| 3. Greeks | [Imperial: dependence of the BSM price on its parameters](https://www.ma.imperial.ac.uk/~bin06/ULL/ull4a.pdf) | Oxford 30–31 and [UT Austin Homework 6](https://web.ma.utexas.edu/users/mcudina/m339w-hw6-impl-vol.pdf) | Delta, gamma, vega, theta and rho; verify each with finite differences | TODO |
| 4. Implied volatility | Imperial notes above | UT Homework 6, problems 6.1–6.2 | [BU FE459 Assignment 7, Task 2](https://cs-people.bu.edu/azs/fe459/assignments/a7.html): inversion; extend it with safeguarded Newton and bisection | TODO |
| 5. Black–76 | [NYU Futures and Options notes](https://people.stern.nyu.edu/sfiglews/documents/Figlewski%20Class%20Notes%20for%20Futures%20and%20Options%20UG%20Spring18-full%20set.pdf), pp. 97–103 | Oxford 51–52 | Black–76 calls, puts, Greeks and implied volatility | TODO |
| 6. Validation | Review the model identities below | [UT Austin Homework 5](https://web.ma.utexas.edu/users/mcudina/m339d-hw5.pdf) and Oxford 19, 52 | [BU FE459 Assignment 8](https://cs-people.bu.edu/azs/fe459/assignments/a8.html): Monte Carlo pricing and standard errors; extend it to confidence intervals and convergence tests | TODO |

