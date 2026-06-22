# Discrete Math: Sieve-Based Prime Factorization O(log n)

## The Core Problem
Traditional prime factorization via trial division takes $O(\sqrt{n})$ time per query, which introduces massive latency spikes when deployed in high-traffic production backends (e.g., cryptographic token generation or database sharding engines).

## The Engineering Solution
This repository implements a **Pre-computed Smallest Prime Factor (SPF)** lookup array using a modified Sieve of Eratosthenes. 
>>> Boot Time Cost:** $O(N \log \log N)$ time to build the static array map.
* **Query Time Performance:** Pure $O(\log n)$ logarithmic runtime to factorize any incoming number.
* **Trade-off Analysis:** We willingly sacrifice $O(N)$ space in RAM at boot time to guarantee ultra-low latency microsecond responses for active users during runtime.


# High-Precision Fermat Factorization Engine (Sub-Linear)

## Engineering Problem Statement
Standard $O(\sqrt{n})$ trial division algorithms crash with Time Limit Exceeded (TLE) errors when processing massive 64-bit keys ($10^{18}$) in latency-sensitive backends. If factors are located near the square root, iterating from 2 up to $\sqrt{n}$ causes massive CPU spikes.

## Mathematical Architecture
Instead of brute-forcing division loops, this engine utilizes Fermat's algebraic identity:
$$n = x^2 - y^2 = (x - y)(x + y)$$

By initiating the search directly at $x = \lfloor\sqrt{n}\rfloor + 1$ and iterating upwards, the algorithm operates in **sub-linear time**, locating factors in microseconds when they reside close to $\sqrt{n}$.

## Production Safety & Mitigations
* **Floating-Point Degradation Avoided:** Standard `math.sqrt` truncates precision at 15-17 digits, generating catastrophic negative value square root crashes on 64-bit bounds. This implementation exclusively leverages pure integer-arithmetic (`math.isqrt`) for absolute precision.
* **Even Number Guard:** Implements a sub-nanosecond bitwise filter (`n & 1`) to intercept even inputs before entering number-theoretic square loops.


# High-Precision Fermat Factorization Engine

## Problem Statement
Standard $O(\sqrt{n})$ trial division algorithms cause Time Limit Exceeded (TLE) errors on 64-bit integer payloads ($10^{18}$) within low-latency production environments.

## Solution Architecture
This engine utilizes Fermat's difference of squares identity ($n = x^2 - y^2$) to achieve sub-linear execution time when factors are close to $\sqrt{n}$.

### Key Optimizations:
1. **Precision Guard:** Replaced floating-point operations with `math.isqrt` to eliminate 64-bit decimal truncation errors.
2. **Circuit Breaker Pattern:** Integrated an iteration budget (`max_iterations`) to prevent infinite loop execution and CPU throttling when processing non-adjacent factors or primes.


## 6/16/2026 ####### FERMAT FACTORIZATION
HIGH-PRECISION FERMAT FACTORIZATION ENGINE

>>> The system architecture
This engine replaces slow, linear division loops with a sub-linear geometric search based on fermats difference of squares identity:
 *n = x^2 - y^2 = (x - y)(x + y)$*

>>> Structural blue print
1. Precision Boundary: Uses integer-only arithmetic (`math.isqrt`) to stop 64-bit precision loss.
2. Circuit Breaker: Implements a strict iteration cap to prevent server freezes (TLE) when factors are spaced far apart.


## 6/22/2026 ###### PHOLLARDS ALGORITHM FACTOR
>>> Pollard's Rho Factorization Pipeline

1. *Complexity*: $O(n^{1/4})$ sub-linear execution time.
2. *Optimization*: Features a fast primality entry-gate filter to optimize CPU usage and prevent dead-end loop cycles.

*pho_algo_v.py, v2.py, and v3.py*