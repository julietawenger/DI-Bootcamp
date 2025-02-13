"""
Daily Challenge: text analysis

Instructions :

The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like 
“Today, is a happy day” or it can be an external text file.

Part I

First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

    1. Create a class called Text that takes a string as an argument and store the text in an attribute.
    Hint: You need to manually copy-paste the text, straight into the code

    2.Implement the following methods:
        a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
        a method that returns the most common word in the text.
        a method that returns a list of all the unique words in the text.

"""
class Text:
    def __init__(self, string):
        self.string = string

    def frecuency(self, word):
        word = word.lower()
        string_list = (self.string.lower()).split()   
        if word in string_list:
            freq = string_list.count(word)
            print(f"The word {word} appears {freq} times in the text.")
            return freq
        else:
            return None
        
    def most_common(self):
        string_list = (self.string.lower()).split()           
        most_common_word = max(set(string_list), key=string_list.count)
        print(f"The most common word in the text is '{most_common_word}'.")
        return most_common_word
    
    def unique_words(self):
        string_list = (self.string.lower()).split()           
        return [x for x in string_list if string_list.count(x) ==1]    
    def from_file(self,file):
        f = open(file)
        self.string = f
        return self.string
    
    @classmethod
    def from_file(cls,filename):
        with open(filename, 'r') as file:
            text = file.read().lower()  
        return cls(text)

text = Text("Hola, qué tal, me llamo Julieta. Qué lindo día. Saludos.")
text.frecuency("qué")
text.most_common()
print(text.unique_words())

""" 
Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

    1. Implement a classmethod that returns a Text instance but with a text file:

        >>> Text.from_file('the_stranger.txt')

    Hint: You need to open and read the text from the text file.

    2. Now, use the provided the_stranger.txt file and try using the class you created above.
"""

the_stranger = Text.from_file('the_stranger.txt')
the_stranger.frecuency("stranger")
the_stranger.most_common()
print(the_stranger.unique_words())