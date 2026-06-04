# Discrete Math: Sieve-Based Prime Factorization O(log n)

## The Core Problem
Traditional prime factorization via trial division takes $O(\sqrt{n})$ time per query, which introduces massive latency spikes when deployed in high-traffic production backends (e.g., cryptographic token generation or database sharding engines).

## The Engineering Solution
This repository implements a **Pre-computed Smallest Prime Factor (SPF)** lookup array using a modified Sieve of Eratosthenes. 
* **Boot Time Cost:** $O(N \log \log N)$ time to build the static array map.
* **Query Time Performance:** Pure $O(\log n)$ logarithmic runtime to factorize any incoming number.
* **Trade-off Analysis:** We willingly sacrifice $O(N)$ space in RAM at boot time to guarantee ultra-low latency microsecond responses for active users during runtime.
