
# coding: utf-8

from qiskit import IBMQ, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.qasm import pi
from qiskit.tools.visualization import plot_histogram, circuit_drawer
import numpy as np

APItoken = "replace me"
url = "replace me"
IBMQ.enable_account(APItoken, url)

IBMQ.backends()

# this is the oracle
def dj_constant(qci,n):
    qci.x(q[n])

#The number of qubits    
bn = 3
# The number of classical bits
cn = 2

q = QuantumRegister(bn)
c = ClassicalRegister(cn)
qc = QuantumCircuit(q,c)

#Flip the last bit
qc.x(q[2])

#Put hadamard gates on all the qubits
for i in range(bn):
    qc.h(q[i])
    
#Put the oracle
dj_constant(qc,2)

#Put hadamard gates on all the qubits again.
for i in range(bn):
    qc.h(q[i])
    
for j in range(cn):
    qc.measure(q[cn-j-1],c[j])
    
#Put backends you can use.  I put ibmq20tokyo because this is the only real device I'm allowed to use.   
backends = ['ibmq_20_tokyo', 'qasm_simulator']

#Use this for the actual machine
backend_sim = IBMQ.get_backend(backends[0]) #{'11': 5, '00': 3937, '10': 96, '01': 58}

#Use this for the simulation
#backend_sim = Aer.get_backend(backends[1]) #{'00': 4096}

result = execute(qc, backend_sim, shots=4096).result() 

# You can get the quantum circuit in latex format.
circuit_drawer(qc).show()

#The command below does not work in command line, so I recommend you to execute it in a different cell in Jupyter Notebook.
#plot_histogram(result.get_counts(qc))

print(result.get_counts(qc))

