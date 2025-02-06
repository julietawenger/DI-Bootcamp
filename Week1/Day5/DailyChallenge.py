""" Challenge 1 : Sorting


Instructions

    Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
    Use List Comprehension

Example:

Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world """

print("\nChallenge 1\n")
def sortingfunc(sequence):
    return ','.join(sorted(sequence.split(','), key= lambda x: x[0]))

print(sortingfunc('without,hello,bag,world'))


""" Challenge 2 : Longest Word
Instructions

    Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
    Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

Examples

longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

longest_word("A thing of beauty is a joy forever.") ➞ "forever."

longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"
"""

print("\nChallenge 2\n")

def longest_word(sentence):
    return max(sentence.split(' '), key= lambda x: len(x))

print(longest_word("Forgetfulness is by all means powerless!"))
print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))