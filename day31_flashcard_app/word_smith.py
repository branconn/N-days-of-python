import pandas as pd
import random as r


class Words:
    def __init__(self):
        try:
            word_df = pd.read_csv("./data/words_2_learn.csv")
        except FileNotFoundError:
            word_df = pd.read_csv("./data/french_words.csv")
        self.all_word_list = word_df.to_dict(orient="records")
        self.word_list = self.all_word_list[:]
        self.num_tot = len(self.word_list)
        self.num_words = self.num_tot
        self.now = r.choice(self.word_list)

    def cycle(self):
        self.now = r.choice(self.word_list)
        return self.now

    def current(self):
        return self.now

    def count(self):
        return self.num_words

    def exile(self):
        self.word_list.remove(self.now)
        self.save()
        self.num_words = len(self.word_list)
        if self.num_words == 0:
            return False
        else:
            return True

    def save(self):
        to_learn_df = pd.DataFrame(self.word_list)
        to_learn_df.to_csv("./data/words_2_learn.csv", index=False)



