# complete_quantum_demo.py
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram, plot_bloch_multivector, plot_state_qsphere, circuit_drawer
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=== QUANTUM COMPUTING DEMONSTRATION ===\n")
    
    # ===== PART 1: BASIC QUANTUM CIRCUIT =====
    print("1. BASIC BELL STATE CIRCUIT")
    qc_bell = QuantumCircuit(2, 2)
    qc_bell.h(0)
    qc_bell.cx(0, 1)
    qc_bell.measure([0, 1], [0, 1])
    
    print("Circuit diagram:")
    print(qc_bell.draw(output='text'))
    
    # Simulate
    simulator = AerSimulator()
    compiled_circuit = transpile(qc_bell, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(qc_bell)
    
    print(f"Measurement results: {counts}")
    plot_histogram(counts, title="Bell State Measurement Results")
    plt.show()
    
    # ===== PART 2: ADVANCED CIRCUIT WITH VISUALIZATION =====
    print("\n2. ADVANCED 3-QUBIT CIRCUIT")
    qc_advanced = QuantumCircuit(3, 3)
    
    # Apply various quantum gates
    qc_advanced.h(0)
    qc_advanced.cx(0, 1)
    qc_advanced.ry(np.pi/4, 1)
    qc_advanced.cx(1, 2)
    qc_advanced.x(0)
    qc_advanced.barrier()
    qc_advanced.h(2)
    qc_advanced.t(0)
    qc_advanced.s(1)
    qc_advanced.measure([0, 1, 2], [0, 1, 2])
    
    print("Advanced circuit diagram:")
    fig = circuit_drawer(qc_advanced, output='mpl', style='clifford')
    plt.show()
    
    # Simulate advanced circuit
    compiled_advanced = transpile(qc_advanced, simulator)
    job_advanced = simulator.run(compiled_advanced, shots=2000)
    result_advanced = job_advanced.result()
    counts_advanced = result_advanced.get_counts(qc_advanced)
    
    print(f"Advanced circuit results: {counts_advanced}")
    plot_histogram(counts_advanced, title="Advanced Circuit Results", figsize=(10, 6))
    plt.show()
    
    # ===== PART 3: QUANTUM STATE VISUALIZATION =====
    print("\n3. QUANTUM STATE VISUALIZATIONS")
    
    # Create circuits for state visualization (no measurements)
    qc_bell_state = QuantumCircuit(2)
    qc_bell_state.h(0)
    qc_bell_state.cx(0, 1)
    
    qc_super_position = QuantumCircuit(2)
    qc_super_position.h(0)
    qc_super_position.h(1)
    
    # Get statevectors
    state_bell = Statevector.from_instruction(qc_bell_state)
    state_super = Statevector.from_instruction(qc_super_position)
    
    print("Bloch Sphere - Bell State:")
    plot_bloch_multivector(state_bell)
    plt.show()
    
    print("Bloch Sphere - Double Superposition:")
    plot_bloch_multivector(state_super)
    plt.show()
    
    print("Q-Sphere - Bell State:")
    plot_state_qsphere(state_bell)
    plt.show()
    
    # ===== PART 4: QUANTUM ALGORITHMS =====
    print("\n4. QUANTUM ALGORITHMS")
    
    # Grover's Algorithm implementation
    def grovers_algorithm():
        qc = QuantumCircuit(2, 2)
        
        # Initialize superposition
        qc.h([0, 1])
        
        # Oracle for |11> state
        qc.cz(0, 1)
        
        # Grover diffusion operator
        qc.h([0, 1])
        qc.z([0, 1])
        qc.cz(0, 1)
        qc.h([0, 1])
        
        qc.measure([0, 1], [0, 1])
        return qc
    
    grover_circuit = grovers_algorithm()
    print("Grover's Algorithm Circuit:")
    print(grover_circuit.draw(output='text'))
    
    # Simulate Grover's algorithm
    compiled_grover = transpile(grover_circuit, simulator)
    job_grover = simulator.run(compiled_grover, shots=1000)
    result_grover = job_grover.result()
    grover_counts = result_grover.get_counts(grover_circuit)
    
    print(f"Grover's algorithm results: {grover_counts}")
    plot_histogram(grover_counts, title="Grover's Search Results")
    plt.show()
    
    print("\n=== DEMONSTRATION COMPLETE ===")
    print("This demonstrates:")
    print("✓ Basic quantum circuits")
    print("✓ Advanced multi-qubit operations") 
    print("✓ Circuit visualization")
    print("✓ Quantum state visualization (Bloch sphere, Q-sphere)")
    print("✓ Quantum algorithm implementation")
    print("✓ Measurement and statistical analysis")

if __name__ == "__main__":
    main()