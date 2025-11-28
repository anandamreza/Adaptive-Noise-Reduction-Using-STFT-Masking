Here is a complete, polished **README.md** for your GitHub repository. Everything is already formatted and ready to upload.

---

# **Adaptive Noise Reduction Using STFT Masking**

This project applies noise reduction to speech audio using a **Short-Time Fourier Transform (STFT)**–based masking algorithm. The method extracts a noise sample from the first few seconds of the recording, estimates its frequency distribution, and constructs a thresholded mask to suppress noise while preserving speech content.

The repository includes:

* `filtering.py` — main processing script
* `before.wav` — raw audio input
* `after.wav` — filtered output
* `Noice Reduction Graph.png` — visualization of time & frequency domain comparison

This implementation serves as a simple baseline for experimenting with speech enhancement, audio denoising, and digital signal processing using Python.

---

## **Features**

* Automatic noise estimation from the first 3 seconds of the audio
* STFT-based spectral masking
* Clean reconstruction using inverse STFT
* Time-domain and frequency-domain visual analysis
* Output audio file generation for comparison

---

## **Dependencies**

Install the required Python packages:

```bash
pip install numpy
pip install scipy
pip install matplotlib
```

This project uses:

* **NumPy** for numerical operations
* **SciPy** for reading WAV files, STFT, and ISTFT
* **Matplotlib** for plotting visualizations

Your working directory must contain:

```
before.wav
filtering.py
```

The script will output:

```
after.wav
```

---

## **How to Execute**

1. Place `filtering.py` and `before.wav` in the same folder.
2. Ensure the beginning of `before.wav` contains at least **3 seconds of noise**, as the algorithm uses this section for noise modeling.
3. Run the script:

```bash
python filtering.py
```

After running:

* A cleaned audio file named **after.wav** will be generated.
* A visualization window will display the **Time Domain** and **Frequency Domain** comparison.
* You may upload these outputs to your repo as examples.

---

## **Limitations**

This STFT-based noise removal technique is simple and works best for stable background noise. Several constraints apply:

* If the initial 3-second segment contains speech or other foreground sounds, the noise model becomes inaccurate.
* The method struggles with **non-stationary noise** (e.g., sudden clicks, keyboard presses).
* Strong suppression may produce **musical noise artifacts**, a common issue in classic spectral subtraction.
* Soft speech components can be unintentionally attenuated if they resemble noise.
* This approach does not perform adaptive learning or deep-feature separation like modern neural models.

For higher-quality results, you may explore methods such as RNNoise, Demucs, or statistical Wiener filtering.
