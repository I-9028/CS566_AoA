# CS566_AoA

[](https://github.com/I-9028/CS566_AoA#cs566_aoa)

This repository contains the project for MET CS 566 for the Spring 2024 semester under Dr. Alexander Belyaev, at Boston University Metropolitan College

## Title
Finding a Solution for [A290250](https://oeis.org/A290250) for n=1

## Description
The sequence [A290250](https://oeis.org/A290250) , for a given n denotes the smallest prime *a(n)* which divides the sum of the $2^n$ powers of factorials from 1 to *a(n)*, i.e.,

$a(n) \mid \sum_{k=1}^{a(n)}(k!)^ {2^n}$ 

I compute the solution for n=1, which is given as, **1248829**.

## Implementation
The problem is broken into two parts, the first part deals with the generation of prime numbers and the second part performs the computation for the sum of the powers of factorials. 

I use Python for the implementation.

### Prime Number Generation
For implementing the generatiion of prime numbers, I utilize three methods, and proceed to benchmark them using **scalene**. The three methods are:

 1. Sieve of Eratosthenes
 2. Croft's Spiral Sieve
 3. Using _primerange(a,b)_ from the _sympy_ module in Python.

### Computation
For this step, two basic algorithms are implemented, and benchmarked.

## Replication
Please install the packages mentioned in the ``requirements.txt`` file to identify the packages required for replicating the results as presented in the notebooks.

## Benchmarking using scalene
Individual functions were copied to temporary files, and *scalene* was used to benchmark them individually.

