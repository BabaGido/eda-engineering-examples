# EDA Engineering Examples

This repository contains small examples demonstrating circuit simulation, PCB design concepts, and engineering analysis using open-source tools.

Tools demonstrated include:
- Ngspice
- LibrePCB
- Qucs-S
- Python engineering simulations

The purpose of this repository is to showcase fundamental electronics design reasoning, circuit simulation workflows, and analysis methods commonly used in hardware development.

---

## Example Projects

### 1. RC Low-Pass Filter Simulation
This example demonstrates a simple RC filter simulated using Ngspice. The simulation shows the transient charging response of a capacitor and illustrates the RC time constant.

Key concept:

τ = RC

---

### 2. Basic PCB Design Concept
A simple PCB schematic demonstrating voltage regulation and decoupling capacitor placement. The example highlights best practices such as minimizing trace inductance and placing decoupling capacitors close to IC power pins.

---

### 3. Engineering Analysis with Python
Python scripts demonstrating analytical modeling of circuit behavior such as capacitor charging curves and time-domain responses.
---
### 4. Python-Based Engineering Plot
`analysis/rc_charging_curve.py`  
`analysis/rc_charging_curve.png`

This example shows the analytical charging response of a capacitor in an RC circuit and includes a generated voltage-versus-time plot.
---
## 5. Frequency Response Example

The script `rc_frequency_response.py` computes the frequency response of an RC low-pass filter.

It generates a Bode-style magnitude plot showing attenuation versus frequency.

Key concept:

The cutoff frequency for an RC filter is given by:

fc = 1 / (2πRC)

For the example circuit:
R = 1 kΩ  
C = 1 µF  

fc ≈ 159 Hz

---
## Purpose

These examples demonstrate practical engineering reasoning used in:

- electronics design
- circuit simulation
- PCB design fundamentals
- engineering analysis workflows

---

## Disclaimer

All examples are generic demonstrations using publicly available tools and do not contain any proprietary or confidential information.
