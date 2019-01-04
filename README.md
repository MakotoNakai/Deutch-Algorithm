# Deutch-Jozsa Algorithm
Deutch-Jozza algorithm is a one of the simplest quantum algorithm that solves a particular problem faster than its classical counterpart.  

## Problem that this algorithm aims to solve  
Suppose that there is a binary function <img src="https://latex.codecogs.com/gif.latex?f(x)" title="f(x)" />, which can be divided into those two following categories.

1. Constant function <img src="https://latex.codecogs.com/gif.latex?f(0)&space;=&space;f(1)&space;=&space;0&space;\quad&space;f(0)&space;=&space;f(1)&space;=&space;1" title="f(0) = f(1) = 0 \quad f(0) = f(1) = 1" />

2. Balanced function <img src="https://latex.codecogs.com/gif.latex?f(0)&space;\neq&space;f(1)" title="f(0) \neq f(1)" />

If you use this algorithm, you can figure out whether <img src="https://latex.codecogs.com/gif.latex?f(x)" title="f(x)" /> is belonged to which category just by one evaluation, although its classical algorithm takes n trials(n is the binary length of input)

## Implementation
Here, I am going to show quantum circuits and codes that I implemented.

This is the quantum circuit for a constant function


