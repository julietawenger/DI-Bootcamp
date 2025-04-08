""" Text preprocessing

For this exercises we will be using NLTK and spaCy

The corpus will be the Lewis Carrol books:

    Alice’s Adventures in Wonderland

    THROUGH THE LOOKING-GLASS And What Alice Found There

    A Tangled Tale

    Using requests to access the contents online, create a function load_texts().This function should recive a list of urls, load them, clean non-words using regular expressions and append the cleaned text to the corpus that will be returned.

    print the first 200 characteres of each text.
    Are there parts of the text that are not relevant to the analysis? If so, you need to remove them.
    hint:* you can use slicing to start and stop the text where you need (ignoring autoral credits in the begining and end) looking for the following phrases:
    ‘ START’
    ‘*** END’

    tokenize the text and print the first 150 tokens of each book

    remove stopwords using NLTK. Check that they were removed using count() and looking for some of the stop words like: ‘i’, ‘me’, ‘my’, ‘myself’, ‘we’, ‘our’, ‘ours’, ‘ourselves’, etc.
    Using PorterStemmer(), print the first 50 stemmed tokens
    Using spaCy pre-trained model ‘en_core_web_sm’ to load and print the first 50 lemmatized tokens. Hint: in spaCy the lemmatized token can be accessed as attribute.
    Analyse the difference between the stemmed and lemmatized tokens. What is different and why?
    using NLTK, identify POS tags of each text.
    using NLTK identify all the entities of each text """

import requests
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, ne_chunk
from nltk.tree import Tree

# Function to load texts from a list of URLs
def load_texts(urls):
    corpus = []
    
    # Loop over each URL in the list
    for url in urls:
        # Retrieve the content from the URL
        response = requests.get(url)
        
        if response.status_code == 200:  # Check if the request was successful
            text = response.text
        else:
            print(f"Failed to retrieve text from {url}. Status code: {response.status_code}")
            continue
        
        # Clean the text: remove non-words using regular expressions
        text_cleaned = clean_text(text)
        
        # Append the cleaned text to the corpus
        corpus.append(text_cleaned)
    
    # Return the cleaned corpus as a single string (or list of strings)
    return corpus

def clean_text(text):
    # Remove everything except alphabetic characters and spaces
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra spaces between words (if any)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    
    cleaned_text = cleaned_text.lower()
    
    return cleaned_text

urls = [
    'https://www.gutenberg.org/cache/epub/11/pg11.txt',  # Alice’s Adventures in Wonderland
    'https://www.gutenberg.org/cache/epub/12/pg12.txt',  # THROUGH THE LOOKING-GLASS And What Alice Found There
    'https://www.gutenberg.org/cache/epub/29042/pg29042.txt'  # A Tangled Tale
]


alice, looking_glass, tangled = load_texts(urls)
alice = alice[1265:1265+200]  
looking_glass = looking_glass[3248:3248 + 200]  
tangled = tangled[2582:2582+200]

print("Alice’s Adventures in Wonderland:\n", alice)
alice_token = word_tokenize(alice)[:150]
print(alice_token)
print("\nTHROUGH THE LOOKING-GLASS And What Alice Found There:\n", looking_glass)
looking_glass_token = word_tokenize(looking_glass)[:150]
print(looking_glass_token)
print("\nA Tangled Tale:\n", tangled)
tangled_token = word_tokenize(tangled)[:150]
print(tangled_token)


stop_words = set(stopwords.words('english'))

def remove_stopwords(token):
    filtered_words=[]
    count = 0
    for tok in token:
        if tok in stop_words:
            count+=1
        else:
            filtered_words.append(tok)    
    return filtered_words, count

alice_filtered, alice_stopwords = remove_stopwords(alice_token)
lg_filtered, lg_stopwords = remove_stopwords(looking_glass_token)
tangled_filtered, tangled_stopwords = remove_stopwords(tangled_token)

print("Alice’s Adventures in Wonderland filtered:\n", alice_filtered)
print(f"Stopword count: {alice_stopwords}")

print("\nTHROUGH THE LOOKING-GLASS And What Alice Found There, filtered:\n", lg_filtered)
print(f"Stopword count: {lg_stopwords}")

print("\nA Tangled Tale filtered:\n", tangled_filtered)
print(f"Stopword count: {tangled_stopwords}")


def apply_stemmer(tokens):
    porter_stemmer = PorterStemmer()
    stemmed_tokens = [porter_stemmer.stem(token) for token in tokens]
    return stemmed_tokens

print("Alice’s Adventures in Wonderland Stemmer:\n", apply_stemmer(alice_token))
print("\nTHROUGH THE LOOKING-GLASS And What Alice Found There, Stemmer:\n", apply_stemmer(looking_glass_token))
print("\nA Tangled Tale Stemmer:\n", apply_stemmer(tangled_token))

def apply_lemmatizer(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

print("Alice’s Adventures in Wonderland Lemmatizer:\n", apply_lemmatizer(alice_token))
print("\nTHROUGH THE LOOKING-GLASS And What Alice Found There, Lemmatizer:\n", apply_lemmatizer(looking_glass_token))
print("\nA Tangled Tale Lemmatizer:\n", apply_lemmatizer(tangled_token))

# A stemmer removes prefixes and suffixes from words to get to their "stem" or root form, which may or may not be a valid word in the language.
# A lemmatizer reduces words to their dictionary form (also called a "lemma"), ensuring that the result is always a valid word in the language.

def perform_ner(tokens):
    tagged = pos_tag(tokens)
    entities_tree = ne_chunk(tagged)
    
    entities = []
    for subtree in entities_tree:
        if isinstance(subtree, Tree):
            entity = " ".join([word for word, _ in subtree.leaves()])
            label = subtree.label()  # The entity type (e.g., PERSON, ORGANIZATION)
            entities.append((entity, label))
    return tagged, entities

alice_tag, alice_entities = perform_ner(alice_token)
lg_tag, lg_entities = perform_ner(looking_glass_token)
tangled_tag, tangled_entities = perform_ner(tangled_token)

print("Alice tagged: ", alice_tag)
print("Alice Entitites: ", alice_entities)

print("\nLooking Glass tagged:", lg_tag)
print("Looking Glass Entities: ", lg_entities)

print("\nTangled tagged: ", tangled_tag)
print("Tangled Entities: ", tangled_entities)


""" Using wordcloud and matplotlib, display a word cloud of each book.
Use BoW method to check the five most frequent words in all the books
hint: What will be the best text from the preprocess step? (raw text, stemmed, lemmarized, etc)?
print the BoW and identify the numbers: What is the document number? What is the index and what is how many times the word was found?
Display a pie plot of the 5 most frequent words in the text. Add the word and its frequence as labels.
Analyze the outputs: Are those words informative? Are they insightful or expected? 
"""
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

def get_most_frequent_words(corpus, top_n=5):
    stop_words = list(stopwords.words('english'))
    vectorizer = CountVectorizer(stop_words=stop_words)  # Use NLTK stopwords as a list
    X = vectorizer.fit_transform(corpus)
    word_counts = X.toarray().sum(axis=0)
    words = vectorizer.get_feature_names_out()
    word_count_dict = dict(zip(words, word_counts))
    sorted_word_count = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_count[:top_n]

print(f"Top 5 Most Frequent Words in Alice: {get_most_frequent_words([alice])}")
print(f"Top 5 Most Frequent Words in Looking Glass: {get_most_frequent_words([looking_glass])}")
print(f"Top 5 Most Frequent Words in Tangled: {get_most_frequent_words([tangled])}")

def plot_top_words_pie(top_words):
    words, frequencies = zip(*top_words)  # Unzip the list of tuples into two lists
    plt.figure()
    plt.pie(frequencies, labels=words, autopct='%1.1f%%', startangle=90)
    plt.title('Top Words Frequency Distribution')
    plt.show()


plot_top_words_pie(get_most_frequent_words([alice]))
plot_top_words_pie(get_most_frequent_words([looking_glass]))
plot_top_words_pie(get_most_frequent_words([tangled]))



"""     
Create another BoW, now using TF-IDF as vectorizer.
    hint: You need to pass min_df=1, max_df=2 as arguments of the TfidfVectorizer(), because we are using a small dataset.
    Create again the pie plots with the new 5 most relevant words from each document.
"""
from sklearn.feature_extraction.text import TfidfVectorizer


def get_most_relevant_words_tfidf(book, top_n=5):

    vectorizer = TfidfVectorizer(stop_words='english', min_df=1, max_df=2)
    X = vectorizer.fit_transform([book])
    tfidf_scores = X.toarray()
    words = vectorizer.get_feature_names_out()
    doc_tfidf = tfidf_scores[0]
    sorted_indices = doc_tfidf.argsort()[::-1]
    top_words = [(words[index], doc_tfidf[index]) for index in sorted_indices[:top_n]]
    
    return top_words

plot_top_words_pie(get_most_relevant_words_tfidf(alice))
plot_top_words_pie(get_most_relevant_words_tfidf(looking_glass))
plot_top_words_pie(get_most_relevant_words_tfidf(tangled))

