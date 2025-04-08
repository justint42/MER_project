import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import librosa.display
import os

# Load data
df = pd.read_csv("data/song_level_dataset.csv")
spectrogram_dir = "path/to/spectrograms"

st.title("🎵 Emotion Recognition Dashboard")

song_id = st.selectbox("Select Song ID", df["song_id"].unique())

# Plot spectrogram
spectrogram_path = os.path.join(spectrogram_dir, f"{song_id}.png")
if os.path.exists(spectrogram_path):
    st.image(spectrogram_path, caption=f"Spectrogram for Song ID {song_id}")

# Plot emotion curves (frame-level)
try:
    frame_df = pd.read_csv("data/frame_level_with_labels.csv")
    curve = frame_df[frame_df["song_id"] == song_id]

    fig, ax = plt.subplots()
    ax.plot(curve["timestamp"], curve["arousal"], label="Arousal", color="red")
    ax.plot(curve["timestamp"], curve["valence"], label="Valence", color="blue")
    ax.set_title("Emotion Curves")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Score")
    ax.legend()
    st.pyplot(fig)
except Exception as e:
    st.warning(f"No frame-level data available for Song ID {song_id}.")