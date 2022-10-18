#!/usr/bin/env python
# encoding: utf-8
import pandas as pd
import os.path as osp
import torch
from torch.utils.data.dataset import Dataset
from torchvision.io import read_image, ImageReadMode


class MusicDataset(Dataset):
    def __init__(self, data_dir: str, trainval: str):
        self.data_dir = data_dir
        self.trainval = trainval

        if self.trainval == 'train':
            df = pd.read_csv(osp.join(data_dir, 'train.csv'))
        else:
            df = pd.read_csv(osp.join(data_dir, 'test.csv'))

        self.df = df.set_index('index')

    def __getitem__(self, index):
        row = self.df.iloc[index]
        image_path = osp.join(self.data_dir, 'mel_spec', f'{str(row.name).zfill(4)}.png')
        return {
            'name': row.name,
            'image': read_image(image_path, ImageReadMode.RGB).type(torch.float32),
            'target': torch.tensor(row.to_numpy(), dtype=torch.float32),
        }

    def __len__(self):
        return self.df.shape[0]

    def make_dataloader(self, batch_size, shuffle, drop_last, nr_workers):
        from jactorch.data.dataloader import JacDataLoader
        from jactorch.data.collate import VarLengthCollateV2

        collate_guide = {
            'name': 'skip',
        }

        return JacDataLoader(
            self, batch_size=batch_size, shuffle=shuffle, drop_last=drop_last,
            num_workers=nr_workers, pin_memory=True,
            collate_fn=VarLengthCollateV2(collate_guide)
        )
