#
# Code for ruunnning HHL algorithm on defferent input states
# original by rum
#
# Importing QISkit
from qiskit import IBMQ, QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
from qiskit.qasm import pi
from qiskit.tools.visualization import plot_histogram, matplotlib_circuit_drawer
import numpy as np
from numba import jit

IBMQ.load_accounts()
IBMQ.backends()



########## phase estimation ##########

@jit
def U_rotation(qc, q, n, N):
    for i in range(1, N+1):
        qc.h(q[i])
        for j in range(N+1, n):
            for k in range(2**(N-i)):
                print(i, j, k)
                ######## X-rotation #######
                qc.cu3(pi, -pi/2, pi/2, q[i], q[j])


def iQFT(qc, q, n, N):
    for i in range(1, N+1):
        qc.h(q[i])
        for j in range(1, N - i + 1):
            try:
                qc.cu1(pi/(2**(j)), q[i], q[j+i])
            except:
                continue




######### R rotation ##########

def R_rotation(qc, q, N):
    for i in range(1, N+1):
        qc.cu1(_theta, 0, 0, q[i], q[0])



######### uncompute ##########

# def QFT(qc, q, n, N):
#     for i in range(N, 0, -1):
#         for j in range(N-1, 0, -1):
#             try:
#                 qc.cu1(pi/(2**(j)), q[i], q[j])
#                 print(pi/(2**(j)), i, j)
#             except:
#                 continue
#         qc.h(q[i])



def QFT(qc, q, N):
    for j in range(N, 0, -1):
        qc.h(q[j])
        for k in range(j, 0, -1):
            try:
                qc.cu1(pi/float(2**(j-k)), q[j], q[k])
            except:
                continue

def iU_rotation(qc, q, n, N):
    for i in range(1, N+1):
        for j in range(N+1, n):
            for k in range(2**(N-i)):
                print(i, j, k)
                ######## X-rotation #######
                qc.cu3(pi, -pi/2, pi/2, q[j], q[i])
        qc.h(q[i])
# def iQFT(self):
#     q = self.q
#     qc = self.qc
#     for n in range(1, self.qubits-1):
#         qc.h(q[n])
#         # print(n)
#         for t in range(1, self.qubits-n):
#             try:
#                 qc.cu1(pi/(2**(t)), q[n], q[t+n])
#                 # print(pi/(2**(t)), n, t+n)
#             except:
#                       continue
#     qc.h(q[self.qubits-1])


#def QFT(self):

# def QFT(self):
#         q = self.q
#         qc = self.qc
#         qc.h(q[self.qubits-1])
#         for m in range(self.qubits-2, 0, -1):
#             # print(m)
#             for u in range(self.qubits, 0, -1):
#                 try:
#                     qc.cu1(pi/(2**(u)), q[m+u], q[m])
#                     # print(pi/(2**(u)), u+m, m)
#                 except:
#                     continue
#             qc.h(q[m])




######## Let's define the circuit #########
#print("Putting together the circuit...")
n = 11
N = int((n-1)/2)

q = QuantumRegister(n)
c = ClassicalRegister(n)
qc = QuantumCircuit(q, c)

#U_rotation(qc, q, n, N)
#iQFT(qc, q, n, N)
#QFT(qc, q, N)
iU_rotation(qc, q, n, N)
matplotlib_circuit_drawer(qc)
