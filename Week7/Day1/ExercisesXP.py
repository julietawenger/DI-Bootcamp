#%%

data = {
    'Review': [
        'At McDonald\'s the food was ok and the service was bad.',
        'I would not recommend this Japanese restaurant to anyone.',
        'I loved this restaurant when I traveled to Thailand last summer.',
        'The menu of Loving has a wide variety of options.',
        'The staff was friendly and helpful at Google\'s employees restaurant.',
        'The ambiance at Bella Italia is amazing, and the pasta dishes are delicious.',
        'I had a terrible experience at Pizza Hut. The pizza was burnt, and the service was slow.',
        'The sushi at Sushi Express is always fresh and flavorful.',
        'The steakhouse on Main Street has a cozy atmosphere and excellent steaks.',
        'The dessert selection at Sweet Treats is to die for!'
    ]
}

import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
#nltk.download('wordnet')
#nltk.download('omw-1.4')
#nltk.download('punkt')

""" Exercise 1.1. Create a function preprocess_text() wich will receive the data as argument and:

    convert all the text in lower case and tokanize it
    remove punctuation
    apply a lemmatizer
    return the preprocessed strings
"""

def preprocess_text(data):
    preprocessed = []
    for review in data['Review']:
        lemmatizer = WordNetLemmatizer()
        review_l = review.lower()
        tokens = word_tokenize(review_l)
        tokens = [i for i in tokens if i.isalpha()]
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        preprocessed.append(' '.join(lemmatized_tokens))
    return preprocessed


"""Exercise 1.2. Create a new dataset with the cleaned text

hint: keep two datasets: the raw data and the preprocessed data"""

cleaned_data = preprocess_text(data)

#%%
"""Exercise 1.3. Create a function perform_ner() that will receive the text as argument and perform NER tagging on it. Use spacy en_core_web_sm

hint: the function should return the entities text and label_ (example of _labels: ORG, GPE, DATE) """

#nltk.download('averaged_perceptron_tagger_eng')
#nltk.download('maxent_ne_chunker') 
#nltk.download('maxent_ne_chunker_tab')
#nltk.download('words')

from nltk import pos_tag, ne_chunk
from nltk.tree import Tree
def perform_ner(data):
    ner = []
    for review in data:
        tokens = word_tokenize(review)
        tagged = pos_tag(tokens)
        entities = ne_chunk(tagged)
        tree = ne_chunk(tagged)

        entities = []
        for subtree in tree:
            if isinstance(subtree, Tree):
                entity = " ".join([token for token, _ in subtree.leaves()])
                label = subtree.label()
                entities.append((entity, label))
        
        ner.append(entities)
    return ner

print("NER raw data results: ", perform_ner(data["Review"]))
print("NER cleaned data results: ", perform_ner(cleaned_data))

#%%
"""Exercise 1/4. Create a function perform_pos_tagging() that will receive the text as argument and perform POS tagging on it.

hint: use nltk pos_tag method """

def perform_pos_tagging(data):
    pos = []
    for review in data:
        tokens = word_tokenize(review)
        tagged = pos_tag(tokens)
        pos.append(tagged)
    return pos  

print("Pos tagging raw data results: ", perform_pos_tagging(data['Review']))
print("Pos tagging cleaned data results: ", perform_pos_tagging(cleaned_data))

#%%
""" Exercise 2: Plotting the word embeddings

Exercise 2.1. Create the word embeddings using Word2Vec model to vectorize the text.

hint: use the preprocessed and tokenized dataset and use Word2Vec model from gensim.models

Print the dimensions of the Word2Vec object and analyze it. What is the vector dimensions? What does it mean? """

def preprocess_text(data):
    preprocessed = []
    for review in data['Review']:
        lemmatizer = WordNetLemmatizer()
        review_l = review.lower()
        tokens = word_tokenize(review_l)
        tokens = [i for i in tokens if i.isalpha()]
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        preprocessed.append(lemmatized_tokens)
    return preprocessed
cleaned_data = preprocess_text(data)


from gensim.models import Word2Vec
import gensim.downloader as api
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

model = Word2Vec(sentences=cleaned_data, window=5, min_count=1, workers=4, epochs = 100)
print("Word2Vec vector dimensions:", model.wv.vector_size)
print("The length of the vector represents the size of the vector used to represent each word in the vocabulary.")
""" 
Exercise 2.2. Create a function plot_word_embeddings() that receives the word2vec object as argument and plots the embeddings dimensions in a grided plot. Use a scatter plot. Loop through the words and use annotate() method to add text labels to each point on the scatter plot.
Finally call this function to see the plots and analyze it:

    Are the related words close to each other?
    What can be the possible reasons for this output? """



def plot_word_embeddings(model):
    # Get the words in the vocabulary
    words = list(model.wv.index_to_key)
    
    # Get the embeddings for each word
    embeddings = [model.wv[word] for word in words]
    
    # Reduce dimensions to 2D using PCA
    pca = PCA(n_components=2)
    reduced_embeddings = pca.fit_transform(embeddings)
    
    # Create scatter plot
    plt.figure(figsize=(12, 8))
    plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1])
    
    # Annotate words
    for i, word in enumerate(words):
        plt.annotate(word, (reduced_embeddings[i, 0], reduced_embeddings[i, 1]))
    
    plt.title("Word Embeddings Visualization")
    plt.show()

# Plot the embeddings
plot_word_embeddings(model)

# Similar words are not too close to one another. Training the model better will produce better results.