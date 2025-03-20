from config import config
from transformers import AutoTokenizer



def convert_src_lang_tokens_to_ids(data):

    tokenizer = AutoTokenizer.from_pretrained(config.SRC_LANG_TOKENIZER_MODEL)
    data[config.COLUMN_NAMES[1]] = data[config.COLUMN_NAMES[1]].apply(tokenizer.convert_tokens_to_ids)

    return data



def create_dst_language_vocab():

    Vd = set()
    for tokenized_hindi_sentence in data[config.COLUMN_NAMES[3]]:
        Vd.update(tokenized_hindi_sentence)

    hindi_vocab = dict()
    for idx, token in enumerate(Vd):
        hindi_vocab[token] = idx + 3

    hindi_vocab["<PAD>"] = config.EXTRA_TOKENS_DICT["<PAD>"]
    hindi_vocab["<SOS>"] = config.EXTRA_TOKENS_DICT["<SOS>"]
    hindi_vocab["<EOS>"] = config.EXTRA_TOKENS_DICT["<EOS>"]

    Vd = hindi_vocab

    return Vd



def save_vocabulary(file_name,vocabulary):


