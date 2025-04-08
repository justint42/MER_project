import os
import polars as pl

features_dir = "path/to/your/features"
all_feature_dfs = []

for fname in os.listdir(features_dir):
    if fname.endswith(".csv"):
        song_id = int(fname.replace(".csv", ""))
        path = os.path.join(features_dir, fname)
        df = pl.read_csv(path, separator=';', has_header=True)
        df = df.with_columns(pl.lit(song_id).alias("song_id"))
        all_feature_dfs.append(df)

features_df = pl.concat(all_feature_dfs, how="vertical")
features_df.write_csv("frame_level_features_raw.csv")