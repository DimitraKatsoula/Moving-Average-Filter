# Moving Average Filter – Python Code Examples

This repository contains simple Python scripts that demonstrate how a **Moving Average Filter** works in signal processing. These scripts are ideal for beginners in physics, engineering, or data analysis who want to understand basic filtering techniques using NumPy and Matplotlib.

## What is a Moving Average Filter?
A Moving Average Filter is a simple low-pass filter used to smooth noisy signals. It works by averaging a window of consecutive values in the input signal, effectively reducing high-frequency noise.

---

## Files in this Repository

### 1. moving_average_basic.py
- Applies a basic moving average filter to a noisy sine wave.
- Plots both the original noisy signal and the filtered result.
- Window size is set to 5.

### 2. moving_average_with_error_plot.py
- Expands on the basic filter example.
- Plots the **difference between the ideal signal** (sin(t)) and the filtered signal to visualize the error.
- Useful for understanding how closely the filter approximates the noise-free signal.

---

## How to Run
1. Make sure you have Python 3 installed.
2. Install required libraries (numpy for numerical calculations, matplotlib for plotting)

if you haven’t already, run this in the command line window: pip install numpy matplotlib


3. Run the scripts:
python moving_average_basic.py
python moving_average_with_error_plot.py

---

## Output
The scripts will generate simple plots showing:
- The input noisy signal
- The smoothed/filtered signal
- The approximation error (in the second script)

---

## Author
[Dimitra Katsoula]  
Physics graduate learning signal processing with Python.

---

## License
This code is open source under the MIT License.
