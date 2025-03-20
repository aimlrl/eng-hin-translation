import pandas as pd
from config import config
import os

def load_data():

    data = pd.read_csv(os.path.join(config.DATASET_DIR,config.DATASET),sep="\t",header=None,
                   names=config.COLUMN_NAMES)

    return data
