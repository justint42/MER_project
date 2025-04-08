import polars as pl

df = pl.read_csv("frame_level_with_labels.csv")
agg_df = df.groupby("song_id").mean()
agg_df.write_csv("song_level_dataset.csv")