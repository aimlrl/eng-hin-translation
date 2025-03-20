SRC_LANG = "eng"

SRC_LANG_TOKENIZER_MODEL = "google-T5/T5-base"

DATASET = "Sentence pairs in English-Hindi - 2025-02-11.tsv"

DATASET_DIR = "dataset"

DST_LANG = "hi"

EXTRA_TOKENS_DICT = {"<PAD>":0, "<SOS>":1, "<EOS>":2}

SRC_LANG_VOCAB_FILENAME = "src_lang_vocab.pkl"

DST_LANG_VOCAB_FILENAME = "dst_lang_vocab.pkl"

LONGEST_SRC_SENT_LENGTH = 68

LONGEST_DST_SENT_LENGTH = 68

TRAINING_DATA_FRAC = 0.98

TEST_DATA_FRAC = (1 - TRAIN_DATA_FRAC)

COLUMN_NAMES = ["SrcSentenceID","SrcSentence","DstSentenceID","DstSentence"]
