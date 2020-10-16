import pandas as pd
import numpy as np
# from bs4 import BeautifulSoup


class Preprocessor:
    """ A class that clean the raw text files
    Parameters:
    ___________




    Return
    _________

    """
    def __init__(self, dataframe, is_cleaned=False):
        self.df = dataframe
        self.preprocesses_all = is_cleaned

    # def test():
    #     print("###################")
    #     pass

    def load_data(self):
        """
        docstring
        """
        self.df = pd.read_csv("./datasets/RLFall2019.csv")

        return self.df

    def remove_html_tags(self):
        """
        docstring
        """
        return self.df

    def nlp_cleaning(self, df):
        """
        docstring
        """
        return self.df

    def normalization(self, df):
        """
        docstring
        """
        return self.df

    def tokenizations(self, df):
        """
        docstring
        """
        return self.df

    def stop_word_remover(self, df):
        """
        docstring
        """
        return self.df

    def part_of_speech(self, df):
        """
        docstring
        """
        return self.df

    def name_entity_recognization(self, df):
        """
        docstring
        """
        return self.df

    def stemming_lemmatization(self, df):
        """
        docstring
        """
        return self.df

    def fit(self, clean=False):
        clean = self.preprocesses_all
        if (clean):
            self.df = self.load_data()

        return self.df
