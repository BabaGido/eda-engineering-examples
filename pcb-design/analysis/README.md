# Engineering Analysis Example

This folder contains a simple analytical simulation of an RC charging circuit.

## Files
- rc_charging_curve.py — Python script that computes capacitor voltage over time using the analytical RC charging equation
- rc_charging_curve.png — generated plot of capacitor voltage versus time

## Engineering Principle

For a charging capacitor in an RC circuit:

Vout(t) = Vin * (1 - exp(-t / (R * C)))

Where:
- R = resistance
- C = capacitance
- Vin = input voltage

This example demonstrates transient response behavior and the effect of the RC time constant on circuit charging.
