import numpy as np
import qiskit
from qiskit import QuantumCircuit

circuitb = QuantumCircuit(2,2)
circuitb.h(0)
circuitb.cx(0,1)
circuitb.measure([0,1],[0,1])
Figure1 = circuitb.draw(output='mpl')
Figure1.show()