#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("startWord")
parser.add_argument("endWord")
parser.add_argument("length", type=int)
args = parser.parse_args()

"""Takes 3 parameters: startWord (the given first word of the ladder),
endWord (the given last word of the ladder), and length (excluding the first and
last words).Create a ladder which only includes startWord and add it to a list
of ladders. For each ladder, check if it's a word longer than length, skip it if
it is, else iterate through fourLetterWords and use checker() to see
if it's just one letter off from the last word in the ladder. If so, create a
new ladder that starts with everything in the current ladder followed by the
word that we found. Add that new ladder to the list of ladders. This will
result in a list of ladders where the first one only includes startWord, the
next few are only two letters long, then are 3 letters long, etc. The last
few will have the startWord followed by a list of words each one letter
diffrent from the last which is one word longer than the given length. When
it reaches the end of the list of ladders, the eliminator() will eliminate
any ladders that don't include the given endWord as the last word. The end
result will be all the successful ladders."""
import os
from os.path import dirname
cur_dir = dirname(__file__)
fourLetterWords = list()

# Tries to open the file fourLetterWords.txt, if it doesn't exist then creates
# a list of 4-letter words and saves it with the name above.
try:
    with open(os.path.join(cur_dir, "fourLetterWords.txt")) as wordsfile:
        for line in wordsfile:
            fourLetterWords += [line[:4]]
            # print(fourLetterWords)
except Exception:
    with open(os.path.join(cur_dir, "wlist_match11.txt")) as wordsfile:
        for line in wordsfile:
            if len(line) == 5:
                fourLetterWords += [line[:4]]
        with open(os.path.join(cur_dir, "fourLetterWords.txt"),
                  'w') as wordsfile:
            for word in fourLetterWords:
                wordsfile.write(word + "\n")


def check(word1, word2):
    """Checks if word1 is one letter different from word2. Returns True if one
    letter diffrent, else returns False"""
    if word1 != word2:
        diffrences = 0
        for i in range(len(word2)):
            if word1[i] != word2[i]:
                diffrences += 1
        if diffrences != 1:
            return False
        else:
            return True
    else:
        return False


def solve(startWord, endWord, length):
    """Takes 3 parameters: startWord (the given first word of the ladder)
    endWord (the given last word of the ladder), and length (of the ladder)."""
    # Create a ladder which only includes startWord and add it to a list of
    # ladders.
    ladders = list([[startWord]])
    # For each ladder, check if it's a word longer than length, if it is, check
    # if endWord is one letter different from the last word in the ladder.
    # Else iterate through fourLetterWords and use checker() to see
    # if it's just one letter off from the last word in the ladder.
    for ladd in ladders:
        if len(ladd) == length + 1:
            if check(ladd[-1], endWord):
                ladder = ladd + [endWord]
                print(ladder)
        else:
            # If so, create a
            # new ladder that starts with everything in the current ladder
            # followed by the
            # word that we found.
            for word in fourLetterWords:
                if check(word, ladd[-1]):
                    ladder = ladd + [word]
                    ladders.append(ladder)
# Add that new ladder to the list of ladders. This will
# result in a list of ladders where the first one only includes startWord, the
# next few are only two letters long, then are 3 letters long, etc. The last
# few will have the startWord followed by a list of words each one letter
# diffrent from the last which is one word longer than the given length. When
# it reaches the end of the list of ladders, the eliminator() will eliminate
# any ladders that don't include the given endWord as the last word. The end
# result will be all the successful ladders.


solve(args.startWord, args.endWord, args.length)
