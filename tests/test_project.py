import unittest
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from phase_explorer import phase_state, bloch_coordinates, sample_counts

class Tests(unittest.TestCase):
 def test_interference_formula(self):
  for p in np.linspace(0,2*np.pi,25):
   np.testing.assert_allclose(phase_state(p).probabilities(),[.5,.5],atol=1e-12)
   np.testing.assert_allclose(phase_state(p,True).probabilities(),[np.cos(p/2)**2,np.sin(p/2)**2],atol=1e-12)
 def test_bloch_coordinates(self):
  for p in [0,.7,np.pi/2,np.pi,3*np.pi/2]:
   np.testing.assert_allclose(bloch_coordinates(phase_state(p).data),[np.cos(p),np.sin(p),0],atol=1e-12)
 def test_global_phase_invariance(self):
  state=phase_state(.7); circuit=QuantumCircuit(1); circuit.h(0)
  shifted=Statevector(np.exp(1j*1.3)*state.data)
  np.testing.assert_allclose(state.evolve(circuit).probabilities(),shifted.evolve(circuit).probabilities(),atol=1e-12)
 def test_sampling_reproducible(self):
  a=sample_counts([.3,.7],1000,np.random.default_rng(42))
  b=sample_counts([.3,.7],1000,np.random.default_rng(42))
  np.testing.assert_array_equal(a,b); self.assertEqual(a.sum(),1000)
if __name__=='__main__': unittest.main()
