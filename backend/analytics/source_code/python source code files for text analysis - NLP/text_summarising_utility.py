# -*- coding: utf-8 -*-
"""text_summarising_utility.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lZIkJVtK6lDYonCmgALUyA4GEfAZbVsc
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

! pip install simplet5 -q

from sklearn.model_selection import train_test_split
import random
import torch
import re
import os
import string

import pandas as pd

from simplet5 import SimpleT5

class Settings:
#     PROJ_NAME = 'Text-Summarization-Using-T5'
#     root_path = os.getcwd().split(PROJ_NAME)[0] + PROJ_NAME + "\\"
#     APPLICATION_PATH = root_path + "backend\\services\\text_summarization\\application\\"
    # setting up logs path
#     LOGS_DIRECTORY = root_path + "backend\\services\\text_summarization\\logs\\logs.txt"

    MODEL_TYPE = "t5"
    MODEL_NAME = "t5-base"

    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # training data directory
    TRAIN_DATA = "/kaggle/input/news-summary/news_summary.csv"

    Columns = ['headlines', 'text']

    USE_GPU = None
    if str(DEVICE) == "cuda":
        USE_GPU=True
    else:
        USE_GPU = False

    EPOCHS = 5

    encoding = 'latin-1'
    columns_dict = {"headlines": "target_text", "text": "source_text"}
    df_column_list = ['source_text', 'target_text']
    SUMMARIZE_KEY = "summarize: "
    SOURCE_TEXT_KEY = 'source_text'
    TEST_SIZE = 0.2
    BATCH_SIZE = 8
    source_max_token_len = 128
    target_max_token_len = 50
    train_df_len = 5000
    test_df_len = 100

class Preprocess:
    def __init__(self):
        self.settings = Settings

    def clean_text(self, text):
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        return text

    def preprocess_data(self, data_path):
        df = pd.read_csv(data_path, encoding=self.settings.encoding, usecols=self.settings.Columns)
        # simpleT5 expects dataframe to have 2 columns: "source_text" and "target_text"
        df = df.rename(columns=self.settings.columns_dict)
        df = df[self.settings.df_column_list]
        # T5 model expects a task related prefix: since it is a summarization task, we will add a prefix "summarize: "
        df[self.settings.SOURCE_TEXT_KEY] = self.settings.SUMMARIZE_KEY + df[self.settings.SOURCE_TEXT_KEY]

        return df

class T5Model:
    def __init__(self, model_type, model_name):
        self.model = SimpleT5()
        self.model.from_pretrained(model_type=model_type,
                                   model_name=model_name)

    def load_model(self, model_type, model_path, use_gpu: bool):
        try:
            self.model.load_model(
                model_type=model_type,
                model_dir=model_path,
                use_gpu=use_gpu
            )

        except BaseException as ex:
            print("error occurred while loading model ", str(ex))

class Train:
    def __init__(self):
        # initialize required class
        self.settings = Settings
        self.preprocess = Preprocess()

        # initialize required variables
        self.t5_model = None

    def __initialize(self):
        try:
            self.t5_model = T5Model(model_name=self.settings.MODEL_NAME,
                                    model_type=self.settings.MODEL_TYPE)

        except BaseException as ex:
            print("error occurred while loading model ", str(ex))

    def set_seed(self, seed_value=42):
        random.seed(seed_value)
        np.random.seed(seed_value)
        torch.manual_seed(seed_value)
        torch.cuda.manual_seed_all(seed_value)

    def train(self, df):
        try:
            train_df, test_df = train_test_split(df, test_size=self.settings.TEST_SIZE)

            self.t5_model.model.train(train_df=train_df[:self.settings.train_df_len],
                                      eval_df=test_df[:self.settings.test_df_len],
                                      source_max_token_len=self.settings.source_max_token_len,
                                      target_max_token_len=self.settings.target_max_token_len,
                                      batch_size=self.settings.BATCH_SIZE, max_epochs=self.settings.EPOCHS,
                                      use_gpu=self.settings.USE_GPU)

        except BaseException as ex:
            print("error occurred while loading model ", str(ex))

    def run(self):
        try:
            print("Loading and Preparing the Dataset-----!! ")
            df = self.preprocess.preprocess_data(self.settings.TRAIN_DATA)
            print(df.head())
            print("Dataset Successfully Loaded and Prepared-----!! ")
            print("Loading and Initializing the T5 Model -----!! ")
            self.__initialize()
            print("Model Successfully Loaded and Initialized-----!! ")

            print("------------------Starting Training-----------!!")
            self.set_seed()
            self.train(df)
            print("Training complete-----!!!")

        except BaseException as ex:
            print("Following Exception Occurred---!! ", str(ex))

print(Settings.USE_GPU)
print(Settings.DEVICE)

t= Train()
t.run()

"""## Inference"""

! ( cd outputs; ls )

#src = https://www.thehindu.com/business/Industry/twitter-interim-grievance-officer-for-india-quits/article35004295.ece
text_to_summarize="""summarize: Twitter’s interim resident grievance officer for India has stepped down, leaving the micro-blogging site without a grievance official as mandated by the new IT rules to address complaints from Indian subscribers, according to a source.

The source said that Dharmendra Chatur, who was recently appointed as interim resident grievance officer for India by Twitter, has quit from the post.

The social media company’s website no longer displays his name, as required under Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules 2021.

Twitter declined to comment on the development.

The development comes at a time when the micro-blogging platform has been engaged in a tussle with the Indian government over the new social media rules. The government has slammed Twitter for deliberate defiance and failure to comply with the country’s new IT rules.
"""

best_weight = "./outputs/SimpleT5-epoch-4-train-loss-0.6182"

t5_model = T5Model(model_name=Settings.MODEL_NAME,model_type=Settings.MODEL_TYPE)
t5_model.load_model(model_type=Settings.MODEL_TYPE,
                   use_gpu=Settings.USE_GPU,
                   model_path=best_weight
                   )

t5_model.model.predict(text_to_summarize)

