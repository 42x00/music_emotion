import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import soundfile as sf

df = pd.read_csv('../../data/label/MeanCategoryRatingsUSA.csv')

for filename in df['filename']:
    y, sr = sf.read(f'../../data/sample/{filename}')
    y = librosa.to_mono(y.T)

    spec = np.abs(librosa.stft(y.T, n_fft=2048, hop_length=512))
    log_spec = librosa.amplitude_to_db(spec)

    librosa.display.specshow(log_spec, sr=sr, hop_length=512)
    plt.show()
    break
