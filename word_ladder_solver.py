# TODO: Save all the 4letter words into a file.
# TODO: Generate a word that is one letter different from startWord and
# continue to endWord
from os.path import dirname
from string import ascii_lowercase
import os.path


def word_checker(word1, word2):
    if word2 not in fourLetterWords:
        return False
    else:
        if word2 != word1:  # exactly one letter different
            diffrences = 0
            for i in range(len(word2)):
                if word2[i] != word1[i]:
                    diffrences += 1
            if diffrences != 1:
                return False
            else:
                return True


cur_dir = dirname(__file__)
fourLetterWords = list()
with open(os.path.join(cur_dir, "words_alpha.txt")) as wordsfile:
    for line in wordsfile:
        if len(line) == 5:
            fourLetterWords += [line[:4]]
print(fourLetterWords)


def solve(startWord, endWord, length):
    for c in ascii_lowercase:
        pass
