import pandas as pd
from torch.utils.data import Dataset

class Dataset_ETT_hour(Dataset):
    def __init__():
        self.__read_data__()
    
    def __read_data__():
        df_raw = pd.read_csv(os.path.join(self.root_path,
                                          self.data_path))
        print(df_raw.head)