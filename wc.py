# Aqsa Noreen
# 9/6/2023
# CS-462

import sys
import os
import pickle
import argparse
from string import punctuation

#compute word frequencies
def word_freq(fname, stripPunc, toLower):
    wordDict = {}

    with open(fname) as f:
        words = f.read().split()

        for word in words:
            if stripPunc: #remove punctuation from word if true
                word = word.strip(punctuation)

            if toLower: #cover word to lowercase if true
                word = word.lower()

            #will update word count in dictionary
            if word in wordDict :
                wordDict[word] += 1
            else :
                wordDict[word] = 1

    return wordDict

# to process a file or directory in order to compute the word frequencies
def fileProcess(fileORdir, args):
    # if the provided path is a file
    if os.path.isfile(fileORdir):
        freqDict = word_freq(fileORdir, args.strip, args.lower)
    else: # now if the path is a directory
        freqDict = {}
        #loop to wlak through the directory
        for root, i, files in os.walk(fileORdir):
            #process the .txt files
            for file in files:
                if file.endswith(".txt"):
                    filePath = os.path.join(root, file)
                    word = word_freq(filePath, args.strip, args.lower)
                    # word frequencies are merged
                    freqDict.update(word)

    # load word frequencies from the specified file if --load is being used
    if args.load:
        with open(args.load, 'rb') as f:
            freqDict = pickle.load(f)
    #save word frequencies, if --save is being used
    if args.save:
        with open(args.save, 'wb') as f:
            pickle.dump(freqDict, f)
    # printing frequencies
    printFreq(freqDict, args)

# printing frequencies func
def printFreq(freqDict, args):
    # print word frequencies sorted by the frequency when -s is used
    if args.s:
        for word in sorted(freqDict, key=freqDict.get):
            print(f"{word}: {freqDict[word]}")
    else: # otherwise print dictionary
        print(freqDict)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='File or directory path')
    parser.add_argument('--strip', action='store_true')
    parser.add_argument('--lower', action='store_true')
    parser.add_argument('--load', metavar='FILE') # load frequency from a file
    parser.add_argument('--save', metavar='FILE') # save frequency to a file
    parser.add_argument('-s', action='store_true')

    args = parser.parse_args() # parse the command line

    fileProcess(args.path, args)


