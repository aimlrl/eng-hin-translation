from config import config
from data_loading import data_loading

import numpy as np
from indicnlp.tokenize import indic_tokenize
from transformers import AutoTokenizer



def tokenize_src_dst_lang_sentences():

    tokenizer = AutoTokenizer.from_pretrained(config.SRC_LANG_TOKENIZER_MODEL)

    data = data_loading.load_data()
    data[config.COLUMN_NAMES[1]] = data[config.COLUMN_NAMES[1]].apply(tokenizer.tokenize)

    data[config.COLUMN_NAMES[3]] = data[config.COLUMN_NAMES[3]].apply(lambda x: indic_tokenize.trivial_tokenize(x,lang=config.DST_LANG))

    return data
