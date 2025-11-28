import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import stft, istft

# Load audio
sr, y = wavfile.read("before.wav")

# Pastikan mono
if y.ndim == 2:
    y = y.mean(axis=1)  # ubah stereo ke mono

y = y.astype(np.float32)
y /= np.max(np.abs(y))  # Normalisasi

# Mengambil sample noise pada 3 detik pertama.
noise_duration = 3
noise_sample = y[:int(sr * noise_duration)]

# STFT
n_fft = 1024
f, t, Zxx = stft(y, fs=sr, nperseg=n_fft)
_, _, Zxx_noise = stft(noise_sample, fs=sr, nperseg=n_fft)

# Magnitudo noise
noise_mag = np.abs(Zxx_noise).mean(axis=1, keepdims=True)  # (freq, 1)

# Masking
threshold_factor = 4
mask = np.abs(Zxx) > (noise_mag * threshold_factor)
Zxx_filtered = Zxx * mask

# Rekonstruksi sinyal
_, y_filtered = istft(Zxx_filtered, fs=sr)

# Simpan ke file kalau mau:
from scipy.io.wavfile import write
write("after.wav", sr, (y_filtered * 32767).astype(np.int16))

# Visualisasi
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(y, label="Original", alpha=0.5)
plt.plot(y_filtered, label="Filtered", linewidth=0.8)
plt.legend()
plt.title("Time Domain")

plt.subplot(2, 1, 2)
f_fft = np.fft.rfftfreq(len(y), d=1/sr)
Y_orig = np.abs(np.fft.rfft(y))
Y_filt = np.abs(np.fft.rfft(y_filtered))
plt.semilogy(f_fft, Y_orig, label="Original", alpha=0.5)
plt.semilogy(f_fft, Y_filt, label="Filtered", linewidth=0.8)
plt.title("Frequency Domain")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.legend()
plt.tight_layout()
plt.show()
