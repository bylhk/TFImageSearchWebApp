import gc
import os
import pandas as pd
from tqdm import tqdm

from config import image_dir, parquet_path, styles_path
from lib.extractor import Vgg16Extractor
from lib.utils import read_styles

vgg = Vgg16Extractor()

if os.path.exists(parquet_path):
    styles = pd.read_parquet(parquet_path)
else:
    styles = read_styles(styles_path)
    styles['feature'] = [[]] * styles.shape[0]


for idx, row in tqdm(styles.iterrows(), total=styles.shape[0]):
    if row['feature'] != []:
        continue

    image_path = os.path.join(image_dir, f"{row['id']}.jpg")
    if os.path.exists(image_path):
        styles.at[idx, 'feature'] = vgg.predict(image_path)

    if idx % 5000 == 0:
        styles.to_parquet(parquet_path)
        gc.collect()

styles.to_parquet(parquet_path)
