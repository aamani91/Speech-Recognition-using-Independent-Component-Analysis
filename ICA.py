PATH=r"C:\Users\LENOVO\Downloads\sound1.wav.wav"
PATH2=r"C:\Users\LENOVO\Downloads\sound1.wav.wav"
#import necessary libraries
from pydub import AudioSegment
import IPython
import numpy as np
import wave

mix_1_wave = wave.open(PATH)
print(mix_1_wave.getparams())

# Extract Raw Audio from Wav File
signal_1_raw = mix_1_wave.readframes(-1)
signal_1 = np.fromstring(signal_1_raw, 'Int16')
'length: ', len(signal_1) , 'first 100 elements: ',signal_1[:100]
import matplotlib.pyplot as plt

fs = mix_1_wave.getframerate()
timing = np.linspace(0, len(signal_1)/fs, num=len(signal_1))


plt.figure(figsize=(12,2))
plt.title('Recording 1')
plt.plot(timing,signal_1, c="#3ABFE7")
plt.ylim(-35000, 35000)
plt.show()
IPython.display.Audio(PATH)
X = list(zip(signal_1))
X[:10]
from sklearn.decomposition import FastICA

# Initializing FastICA with n_components=1 and whitening
ica = FastICA(n_components=1,whiten=True)

# Running the FastICA algorithm using fit_transform on dataset X
ica_result = ica.fit_transform(X)
ica_result.shape
# Independent Component #1
plt.figure(figsize=(12,2))
plt.title('Result')
plt.plot(result_signal_1, c="#df8efd")
plt.ylim(-0.010, 0.010)
plt.show()
from scipy.io import wavfile

# Converting to int, mapping the appropriate range, and increasing the volume a little bit
result_signal_1_int = np.int16(result_signal_1*32767*100)
# Writing wave files
wavfile.write("result_signal_1.wav", fs, result_signal_1_int)
IPython.display.Audio("result_signal_1.wav")
