
# coding: utf-8

# In[4]:


from qiskit import IBMQ, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.qasm import pi
from qiskit.tools.visualization import plot_histogram, circuit_drawer
import numpy as np

APItoken = "fa84f6833961480e40f615777a497a80f45e9fbf83266bf7431ef468a80d425fbd31080f4483dec301fc05ffe67c178c9b52c4b90bb37b20f10ca68cda09386f"
url = "https://q-console-api.mybluemix.net/api/Hubs/ibm-q-keio/Groups/keio-internal/Projects/qip-students"
IBMQ.enable_account(APItoken, url)

IBMQ.backends()

def oracle_constant(qci,n):
    qci.x(q[n])

bn = 2
cn = 1

q = QuantumRegister(bn)
c = ClassicalRegister(cn)
qc  = QuantumCircuit(q,c)
qc.x(q[1])
for i in range(bn):
    qc.h(q[i])
oracle_constant(qc,1)
for j in range(bn):
    qc.h(q[j])

for l in range(bn):
    qc.measure(q[0],c[0])
    

backends = ['ibmq_20_tokyo', 'qasm_simulator']
#Use this for the actual machine
backend_sim = IBMQ.get_backend(backends[0])
#Use this for the simulation
#backend_sim = Aer.get_backend(backends[1])
result = execute(qc, backend_sim, shots=4096).result()
#{'0': 4096}
circuit_drawer(qc).show()
plot_histogram(result.get_counts(qc))
print(result.get_counts(qc))

