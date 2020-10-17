from preprocessor import Preprocessor as PP
import os
import sys
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import re
# Import pandas to read the file 
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize


def convert_emoticons(text):
    for emot in EMOTICONS:
        text = re.sub(u'('+emot+')', "_".join(EMOTICONS[emot].replace(",","").split()), text)
    return text



def remove_unwanted_columns(df):
        """
        Remove unncessary columns
        
        ARgs:
            df: take dataframe as imput
        Return dataframe
        
        """

        return df.drop(columns=["Unnamed: 0", "config_ch"], axis=1)

def run_preprocessor():
    """load the data and clean it """

    prepro = PP()
    df = prepro.load_data()

    df.subject_ch = df.subject_ch.map(lambda x: convert_emoticons(str(x)))

    df = prepro.remove_html_tags()


    df = remove_unwanted_columns(df)
    df["weeks"] = df['created_ch'].dt.week

    # remove characteres
    df = prepro.normalization()

    # run tokenizer
    df = prepro.tokenizations()

    # remove characteres
    df = prepro.stop_word_remover()

    # remove characteres
    df = prepro.stemming_lemmatization()

    return df




    # def replace_week_numbers(df):
    #     """
    #     functiion that change week number from 1 to 19
    #     """
        
    #     return sorted(df.weeks.unique())

    # df["weeks_num"] = df["weeks"].map(lambda x: replace_week_numbers(df).index(x)+1 if(x in replace_week_numbers(df)) else np.nan)

if __name__ == "__main__":
   df = run_preprocessor()
   print(df.sample(100))