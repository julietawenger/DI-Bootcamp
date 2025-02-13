def word_dict(word):
    dictionary = {}
    for letter in word:    
        dictionary[letter] = word.count(letter)
    return dictionary
    
def is_anagram(word1, word2):
    return word_dict(word1) == word_dict(word2)

class AnagramChecker:

    def __init__(self):
        f = open(r'sowpods.txt')
        word_list = (f.read().lower()).split()
        self.word_list = word_list
    
    def is_valid_word(self, word):
        if word.lower() in self.word_list:
            return True
        else:
            return False
        
    def get_anagrams(self, word):
        if self.is_valid_word(word):
            pass
        else:
            print("Word not found. Try again.")
            exit()
        anagrams =[]    
        for x in self.word_list:
            if is_anagram(word, x):
                anagrams.append(x)
        anagrams.remove(word)        
        return anagrams        


        
