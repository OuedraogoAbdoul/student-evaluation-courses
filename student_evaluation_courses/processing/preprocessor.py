import os
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
import nltk
# nltk.download('stopwords')
# stop_words = stopwords.words('english')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


class Preprocessor:
    """ A class that clean the raw text files
    Parameters:
    ___________




    Return
    _________

    """
    def __init__(self, is_cleaned=False):
        self.df = ""
        self.preprocesses_all = is_cleaned

    # def test():
    #     print("###################")
    #     pass

    def load_data(self):
        """
        docstring
        """
        self.df = pd.read_csv(r"C:\Users\admin\Desktop\EducTech\student-evaluation-courses\student_evaluation_courses\datasets\RLFall2019.csv", parse_dates=["created_ch", "bucket_name_ch"])

        return self.df

    def remove_html_tags(self):
        """ Remove html and end of line tags """
        self.df.subject_ch = self.df.subject_ch.map(lambda x: BeautifulSoup(str(x), 'html.parser' ).get_text())
        self.df.subject_ch = self.df.subject_ch.str.replace('\d+', '')
        self.df.subject_ch = self.df.subject_ch.str.replace("https", '')
        return self.df

 
    def normalization(self):
        """ remove special characters, convert to lower case  """
        self.df.subject_ch = self.df.subject_ch.map(lambda x: re.sub("[^a-zA-Z0-9], https", ' ', str(x).lower()))

        return self.df

    def tokenizations(self):
        """  Converts all the sentneces into individual words """
        nltk.download('punkt')
        # self.df.subject_ch = self.df.subject_ch.map(lambda x: word_tokenize(str(x)))
        self.df["subject_ch"] = self.df["subject_ch"].apply(word_tokenize)
        self.df.subject_ch = self.df.subject_ch.map(lambda x: re.sub("[^a-zA-Z0-9]", ' ', str(x).lower()))

        return self.df

    def stop_word_remover(self):
        """Remove stop word """
        nltk.download("stopwords")
        print(stopwords.words("english"))
        nltk.data.path.append(os.path.join(r"C:\Users\admin\Desktop\EducTech\Private", "NLTK"))
        stop_words = stopwords.words("english")
        self.df["subject_ch"] = self.df["subject_ch"].apply(lambda words: ' '.join(word.lower() for word in words.split() if word not in stop_words))        
        
        return self.df

    # def part_of_speech(self):
    #     """
    #     docstring
    #     """
    #     return self.df

    # def name_entity_recognization(self, df):
    #     """
    #     docstring
    #     """
    #     return self.df

    def stemming_lemmatization(self):
        """
        docstring
        """
        # process stemming
        self.df["subject_ch"] = [PorterStemmer().stem(w) for w in self.df["subject_ch"]] 

        # process lemmatizatio
        self.df["subject_ch"] = [WordNetLemmatizer().lemmatize(w) for w in self.df["subject_ch"]] 

        return self.df
