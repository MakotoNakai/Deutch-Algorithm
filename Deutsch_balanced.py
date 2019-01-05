
# coding: utf-8


from qiskit import IBMQ, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.qasm import pi
from qiskit.tools.visualization import plot_histogram, circuit_drawer
import numpy as np

APItoken = "Replace me"
url = "Replace me"
IBMQ.enable_account(APItoken, url)

IBMQ.backends()

# this is the oracle
def oracle_balanced(qci,n1,n2):
    qci.cx(q[n1],q[n2])
    
#The number of qubits
bn = 2
# The number of classical bits
cn = 1

q = QuantumRegister(bn)
c = ClassicalRegister(cn)
qc  = QuantumCircuit(q,c)

#Flip the last bit
qc.x(q[1])

#Put hadamard gates on all the qubits
for i in range(bn):
    qc.h(q[i])
    
#Put the oracle     
oracle_balanced(qc,0,1)

#Put hadamard gates on all the qubits again
for j in range(bn):
    qc.h(q[j])

for l in range(bn):
    qc.measure(q[0],c[0])
    
#Put backends you can use.  I put ibmq20tokyo because this is the only real device I'm allowed to use. 
backends = ['ibmq_20_tokyo', 'qasm_simulator']

#Use this for the actual machine(This code doesn't work on real devices
#backend_sim = IBMQ.get_backend(backends[0])
#Use this for the simulation
backend_sim = Aer.get_backend(backends[1]) #{'1': 4096}
result = execute(qc, backend_sim, shots=4096).result()

# You can get the quantum circuit in latex format.
circuit_drawer(qc).show()

#The command below does not work in command line, so I recommend you to execute it in a different cell in Jupyter Notebook.
plot_histogram(result.get_counts(qc))

print(result.get_counts(qc))

