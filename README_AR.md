# ✦ Quantum Phase Explorer ✦

Quantum phase, interference and the Bloch sphere ⊚ 

The H–P(φ)–H sequence turns relative phase into observable interference: P(0) = cos²(φ/2). Direct Z measurement remains 50/50. The notebook compares |+〉 and |−〉, visualizes Bloch coordinates and checks global-phase invariance. Baseline 65 phase settings and 2,048 simulated samples per setting

## التشغيل

ثبت المكتبات وشغل التجربة من هذا المجلد:

```bash
python -m pip install -r requirements.txt
python phase_explorer.py --shots 2048 --seed 42
python -m unittest discover -s tests -v
```

يحتوي "experiment.ipynb" على الشرح والنتايج، ينفتح في Jupyter او Colab لتشغيل الخلايا *ملاحظة مهمة : المحاكاة رح تصير معنا على Qiskit مو على جهاز كمي فعليا !

 References: [Qiskit Statevector](https://quantum.cloud.ibm.com/docs/en/api/qiskit/2.2/qiskit.quantum_info.Statevector), [Qiskit QuantumCircuit](https://quantum.cloud.ibm.com/docs/en/api/qiskit/2.2/qiskit.circuit.QuantumCircuit), [QWorld Bronze](https://qworld.net/workshop-bronze/), [QWorld Silver](https://qworld.net/qsilver/).
