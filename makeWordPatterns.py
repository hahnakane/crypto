# Creates wordPatterns.py based on the words in our dictionary
# text file, dictionary.txt.

import pprint


def getWordPattern(word):
    # Returns a string of the pattern form of the given word.
    # e.g. '0.1.2.3.4.5.6.3.0.1.2.4 for 'PHILADELPHIA'
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])
    return '.'.join(wordPattern)


def main():
    allPatterns = {}

    dict_file = open('dictionary.txt')
    wordList = dict_file.read().split('\n')
    dict_file.close()

    for word in wordList:
        # Get the pattern for each string in wordList.
        pattern = getWordPattern(word)

        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    # This is code that writes code. The wordPatterns.py file contains
    # one very, very large assignment statement.
    pattern_file = open('wordPatterns.py', 'w')
    pattern_file.write('allPatterns = ')
    pattern_file.write(pprint.pformat(allPatterns))
    pattern_file.close()


if __name__ == '__main__':
    main()
