import pandas as pd
import requests
from tqdm import tqdm

df = pd.read_csv('../../data/backup/raw.csv')
for i, row in tqdm(df.iterrows(), total=df.shape[0]):
    url = f'https://s3.amazonaws.com/musicemo/Verified_Normed/{row.filename}'
    save_path = f'../../data/audio/{str(row.id).zfill(4)}.mp3'
    doc = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(doc.content)
