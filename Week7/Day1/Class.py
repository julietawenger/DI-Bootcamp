#%%
import nltk

# Download the 'punkt_tab' resource
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize, sent_tokenize

text = "Why, sometimes I`ve believed as many as 6 impossible things before breakfast?"
tokens = word_tokenize(text)

print(tokens)

span = tokens[1:7]

print(span)

text = "Why, sometimes I`ve believed as many as 6 impossible things before breakfast? I don't know"

print(sent_tokenize(text)[0:2]) 

#%%
doc = "Linguistics and Natural Language Processing (NLP) are closely linked. \n Linguistics is the scientific study of language, encompassing its structure, meaning, and context. \n It provides foundational knowledge about language syntax, semantics, pragmatics, and phonetics. \n NLP applies this linguistic knowledge in computational algorithms to enable computers to understand, interpret, and generate human language. By leveraging linguistic principles, NLP seeks to bridge the gap between human communication and computer understanding, enabling tasks like translation, sentiment analysis, and voice recognition."

nltk.download('stopwords')

from nltk.corpus import stopwords

tokens = word_tokenize(doc)
print(tokens)
mask = [i in stopwords.words('english') for i in tokens]

print([item for keep, item in zip(mask, tokens) if keep])