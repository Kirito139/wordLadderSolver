from os.path import dirname
import os.path
cur_dir = dirname(__file__)
fourLetterWords = list()
with open(os.path.join(cur_dir, "words_alpha.txt")) as wordsfile:
    for line in wordsfile:
        if len(line) == 5:
            fourLetterWords += [line[:4]]
print(fourLetterWords)
