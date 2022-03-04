# TODO: Generate a word that is one letter different from startWord and
# continue to endWord
# TODO: Try all possible word combinations until a success, not just first one.
"""Takes 3 parameters: startWord (the given first word of the ladder),
endWord (the given last word of the ladder), and length (of the ladder).
Create a ladder which only includes startWord and add it to a list of
ladders. For each ladder, check if it's a word longer than length, skip it if
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
    with open(os.path.join(cur_dir, "words_alpha.txt")) as wordsfile:
        for line in wordsfile:
            if len(line) == 5:
                fourLetterWords += [line[:4]]
        with open(os.path.join(cur_dir, "fourLetterWords.txt"),
                  'w') as wordsfile:
            for word in fourLetterWords:
                wordsfile.write(word + "\n")


def check(word1, word2):
    """Checks if word is one letter
    different from word1"""
    if word1 != word2:
        diffrences = 0
        for i in range(len(word2)):
            if word1[i] != word2[i]:
                diffrences += 1
        if diffrences != 1:
            return False
        else:
            return True


def solve(startWord, endWord, length):
    """Takes 3 parameters: startWord (the given first word of the ladder)
    endWord (the given last word of the ladder), and length (of the ladder)."""
    # Create a ladder which only includes startWord and add it to a list of
    # ladders.
    ladders = list()
    ladder = [startWord]
    ladders.append(ladder)
    # print(ladders)

    # For each ladder, check if it's a word longer than length, skip it if
    # it is, else iterate through fourLetterWords and use checker() to see
    # if it's just one letter off from the last word in the ladder.
    toBRmvd = list()
    for ladd in ladders:
        if len(ladd) == length + 2:
            if ladd[-1] != endWord:
                toBRmvd.append(ladd)
        else:
            # If so, create a
            # new ladder that starts with everything in the current ladder
            # followed by the
            # word that we found.
            toBRmvd.append(ladd)
            for word in fourLetterWords:
                if check(word, ladd[-1]):
                    ladder = ladd + [word]
                    ladders.append(ladder)

    # eliminator()
    for ladd in toBRmvd:
        ladders.remove(ladd)
    print(ladders)

# Add that new ladder to the list of ladders. This will
# result in a list of ladders where the first one only includes startWord, the
# next few are only two letters long, then are 3 letters long, etc. The last
# few will have the startWord followed by a list of words each one letter
# diffrent from the last which is one word longer than the given length. When
# it reaches the end of the list of ladders, the eliminator() will eliminate
# any ladders that don't include the given endWord as the last word. The end
# result will be all the successful ladders.


solve("core", "seed", 4)
