import os
import re

import pandas as pd
import tensorflow as tf


def labeler(example, index):
    return example, tf.cast(index, tf.int64)


def load_data(directory):
    labeled_data_sets = []
    data = {'page': [], 'result': []}
    for file_path in os.listdir(directory):
        text_dir = tf.keras.utils.get_file(file_path)
        lines_dataset = tf.data.TextLineDataset(file_path)
        labeled_dataset = lines_dataset.map(lambda ex: labeler(ex, i))
        labeled_data_sets.append(labeled_dataset)
    return pd.DataFrame.from_dict(data)
