#set up a regular expression that can detect any punctuation
import re
punctuation_regex = re.compile('[\W]')

#open a story that's in this folder, read each line, and split each line into words
#that we add to our list of storyWords
storyFile = open('short-story.txt', 'r') #replace 'short-story.txt' with 'long-story.txt' if you want!
storyWords = []
for line in storyFile:
    lineWords = line.split(' ')     #separate out each word by breaking the line at each space " "
    for word in lineWords:
        cleanedWord = word.strip().lower()      #strip off leading and trailing whitespace, and lowercase it
        cleanedWord = punctuation_regex.sub('', cleanedWord)    #remove all the punctuation
                                                                #(literally, replace all punctuation with nothing)
        storyWords.append(cleanedWord)          #add this clean word to our list

#set up an empty dictionary to hold words and their frequencies
#keys in this dictionary are words
#the value that goes with each key is the number of times that word appears in the dictionary
#Example: a key might be 'cat', and frequency_table['cat'] might be 5 if the word 'cat'
#appears 5 times in the storyWords list
frequency_table = {}
#ALL OF OUR CODE GOES HERE
for word in storyWords:

#if I have not seen any words of this type before, add a new entry
#1 is referring to how many times you've seen it before
    if word not in frequency_table:
        frequency_table[word] = 1

#if I have seen it before, add 1 to its current count
    else:
        frequency_table[word] = 1 + frequency_table[word]

print(frequency_table)

#this is a function that finds the most frequent word
def find_max_frequency():
    #at the start, I haven't seen any words
    #but I want to keep track of the most frequent word I've seen so far
    max_freq = 0
    max_word = ' '

    #look through ALL words in the frequency table
    for word in frequency_table:

        #if the word I'm looking at now has appeared more than any
        #words I've seen so far, update my max
        if frequency_table[word] > max_freq:
            max_freq = frequency_table[word]
            max_word = word

    #at the end of the for loop, we've looked through all entries and max_word has the most frequent word in it
    return max_word

best_word = find_max_frequency()
print("The most frequent word is: " + best_word)

#make a fucntion to find the top 10
#CHALLENGE: modify this so it takes the top N
def top_twenty():
    #take the most frequent word out of the frequency table 10 times
    for count in range(20):
        top_word = find_max_frequency()
        print(top_word + " appears " + str(frequency_table[top_word]))
        del(frequency_table[top_word]) #take that entry out of the table
#call the top ten function
top_twenty()
