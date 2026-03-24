import numpy as np
import matplotlib.pyplot as plt

# RC circuit parameters
R = 1000          # ohms
C = 1e-6          # farads
Vin = 5           # volts

# Time vector
t = np.linspace(0, 0.01, 1000)   # 0 to 10 ms

# Capacitor charging equation
Vout = Vin * (1 - np.exp(-t / (R * C)))

# Plot
plt.figure(figsize=(8, 5))
plt.plot(t, Vout, label="Vout(t)")
plt.title("RC Charging Curve")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save image
plt.savefig("rc_charging_curve.png", dpi=300)
plt.show()
