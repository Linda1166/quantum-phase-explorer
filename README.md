# ✦ Quantum Phase Explorer ✦

**Quantum phase interference and the Bloch sphere ⚛️🧑‍💻**

The H–P(φ)–H sequence turns relative phase into observable interference: P(0) = cos²(φ/2). Direct Z measurement remains 50/50. The notebook compares |+〉 and |−〉, visualizes Bloch coordinates and checks global-phase invariance. Baseline 65 phase settings and 2,048 simulated samples per setting.

## Run

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. Then run:

```bash
python -m pip install -r requirements.txt
python phase_explorer.py --shots 2048 --seed 42
python -m unittest discover -s tests -v
```

 References: [Qiskit Statevector](https://quantum.cloud.ibm.com/docs/en/api/qiskit/2.2/qiskit.quantum_info.Statevector), [Qiskit QuantumCircuit](https://quantum.cloud.ibm.com/docs/en/api/qiskit/2.2/qiskit.circuit.QuantumCircuit), [QWorld Bronze](https://qworld.net/workshop-bronze/), [QWorld Silver](https://qworld.net/qsilver/).
