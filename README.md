# Deutch-Jozsa Algorithm
Deutch-Jozza algorithm is a one of the simplest quantum algorithm that solves a particular problem faster than its classical counterpart.  

## Problem that this algorithm aims to solve  
Suppose that there is a binary function <img src="https://latex.codecogs.com/gif.latex?f(x)" title="f(x)" />, which can be divided into those two following categories.

1. Constant function <img src="https://latex.codecogs.com/gif.latex?f(0)&space;=&space;f(1)&space;=&space;0&space;\quad&space;f(0)&space;=&space;f(1)&space;=&space;1" title="f(0) = f(1) = 0 \quad f(0) = f(1) = 1" />

2. Balanced function <img src="https://latex.codecogs.com/gif.latex?f(0)&space;\neq&space;f(1)" title="f(0) \neq f(1)" />
If you use this algorithm, you can figure out whether <img src="https://latex.codecogs.com/gif.latex?f(x)" title="f(x)" /> is belonged to which category just by one evaluation, although its classical algorithm takes n trials(n is the binary length of input)

## Mathematical explanation   
I prepared the oracle <img src="https://latex.codecogs.com/gif.latex?U_f" title="U_f" /> in order to judge the function is constant or balanced.
<img src="https://latex.codecogs.com/gif.latex?|x_0x_1\rangle|y\rangle&space;\xrightarrow{U_f}&space;|x_0x_1\rangle|y\bigoplus&space;x_0x_1\rangle" title="|x_0x_1\rangle|y\rangle \xrightarrow{U_f} |x_0x_1\rangle|y\bigoplus x_0x_1\rangle" />  
If <img src="https://latex.codecogs.com/gif.latex?|x_0x_1\rangle&space;=&space;|00\rangle" title="|x_0x_1\rangle = |00\rangle" />, this function would be constant and it would be balanced otherwise.

## Implementation
Here, I am going to show quantum circuits and codes that I implemented.  
### Constant function
This is the quantum circuit for a constant function  
![dj_constant](https://user-images.githubusercontent.com/45162150/50703672-3ca48880-1098-11e9-8ac6-45d43fa3ca7d.png)

and this is the result on OpenQASM simulator.    
![screen shot 2019-01-05 at 10 41 05 am](https://user-images.githubusercontent.com/45162150/50718777-7bf1ca00-10d6-11e9-8865-e7e77efce261.png)

Also, this is the result on ibmqtokyo20.  
![screen shot 2019-01-05 at 10 45 22 am](https://user-images.githubusercontent.com/45162150/50718839-2c5fce00-10d7-11e9-8036-9b5ad2de9349.png)

Therefore, this is a constant function.  

### Balanced function  
This is the quantum circuit for a balanced function.











