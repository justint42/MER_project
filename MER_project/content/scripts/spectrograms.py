import os
import librosa
import librosa.display
import matplotlib.pyplot as plt

input_dir = "path/to/your/wav_files"
output_dir = "path/to/save/spectrograms"
os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if file.endswith(".wav"):
        song_id = file.replace(".wav", "")
        y, sr = librosa.load(os.path.join(input_dir, file))
        S = librosa.feature.melspectrogram(y=y, sr=sr)
        S_dB = librosa.power_to_db(S, ref=np.max)

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
        plt.colorbar(format='%+2.0f dB')
        plt.title(f'Spectrogram - Song ID {song_id}')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f"{song_id}.png"))
        plt.close()