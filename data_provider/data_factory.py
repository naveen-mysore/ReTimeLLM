import os
import pandas as pd
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

class Dataset_ETT_hour(Dataset):
    def __init__(self):
        self.data = None
        self.__read_data__()

    
    def __read_data__(self):
        data_path = os.path.join("dataset","ETT-small/ETTh1.csv")
        df_raw = pd.read_csv(data_path)
        print(df_raw.head())
        print(df_raw.shape)
        self.data = df_raw.values

    def __getitem__(self, index):
        return self.data
    
    def __len__(self):
        return 10
                                        


def data_provider():

    data_set = Dataset_ETT_hour()

    # Dataloader from pytorch: https://pytorch.org/docs/stable/data.html
    data_loader = DataLoader(
        dataset=data_set,
        batch_size=1,
        shuffle=False,
        num_workers=1,
        drop_last=False
    )

    return data_loader