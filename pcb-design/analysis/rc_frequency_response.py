import numpy as np
import matplotlib.pyplot as plt

# RC parameters
R = 1000        # ohms
C = 1e-6        # farads

# Frequency range
f = np.logspace(1, 6, 500)   # 10 Hz to 1 MHz

# Angular frequency
w = 2 * np.pi * f

# Transfer function magnitude for RC low-pass
H = 1 / np.sqrt(1 + (w * R * C)**2)

# Convert to dB
H_db = 20 * np.log10(H)

# Plot
plt.figure(figsize=(8,5))
plt.semilogx(f, H_db)
plt.title("RC Low-Pass Filter Frequency Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True, which="both")

plt.tight_layout()
plt.savefig("rc_frequency_response.png", dpi=300)
plt.show()
