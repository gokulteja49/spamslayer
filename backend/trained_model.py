import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Function to read emails from text file
def read_emails_from_text(text_file):
    texts = []
    labels = []
    with open(text_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().rsplit(' ', 1)
            if len(parts) == 2:
                texts.append(parts[0].strip())
                labels.append(parts[1].strip())
    return texts, labels


text_file = 'data/SMSSpamCollection.txt'  


texts, labels = read_emails_from_text(text_file)

texts = [text for text in texts if text.strip()]
labels = labels[:len(texts)]  

tfidf = TfidfVectorizer(stop_words='english', lowercase=True, max_df=0.95, min_df=2)


X = tfidf.fit_transform(texts)

model = MultinomialNB()

model.fit(X, labels)


with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf, f)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Training completed. Vectorizer and model saved as vectorizer.pkl and model.pkl.")
