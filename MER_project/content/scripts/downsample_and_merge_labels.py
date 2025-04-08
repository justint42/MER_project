import polars as pl

df = pl.read_csv("frame_level_features_raw.csv")
df = df.with_columns([
    (pl.col("timestamp") // 1).cast(pl.Int32).alias("timestamp")
])
df = df.groupby(["song_id", "timestamp"]).mean()

arousal = pl.read_csv("arousal.csv").melt(id_vars="song_id", variable_name="timestamp", value_name="arousal")
valence = pl.read_csv("valence.csv").melt(id_vars="song_id", variable_name="timestamp", value_name="valence")
arousal = arousal.with_columns(pl.col("timestamp").cast(pl.Float64))
valence = valence.with_columns(pl.col("timestamp").cast(pl.Float64))

labels = arousal.join(valence, on=["song_id", "timestamp"])
merged = df.join(labels, on=["song_id", "timestamp"])
merged.write_csv("frame_level_with_labels.csv")