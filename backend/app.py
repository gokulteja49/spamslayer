

import logging
from flask import Flask, redirect, request, session, url_for, jsonify
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
import html2text
import requests
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)
app.secret_key = 'your_secret_key'

CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'http://localhost:5000/oauth2callback'
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

logging.basicConfig(level=logging.DEBUG)

# Load ML model and vectorizer
with open('vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_spam(email_text, tfidf, model, threshold=0.5):
    vector_input = tfidf.transform([email_text])
    prediction = model.predict_proba(vector_input)
    return 1 if prediction[0][1] >= threshold else 0

def read_emails():
    if 'google_token' in session:
        token_data = session['google_token']
        creds = Credentials(
            token=token_data['access_token'],
            refresh_token=token_data.get('refresh_token'),
            token_uri='https://oauth2.googleapis.com/token',
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            scopes=SCOPES
        )
        
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
        messages = results.get('messages', [])
        messages_data = []
        
        for msg in messages[:10]:  # Limit to 10 messages for quick testing
            message = service.users().messages().get(userId='me', id=msg['id']).execute()
            headers = message['payload'].get('headers', [])
            subject = next((header['value'] for header in headers if header['name'] == 'Subject'), 'No Subject')
            snippet = message.get('snippet', '')
            spam_alert = predict_spam(snippet, tfidf, model)
            
            messages_data.append({
                'id': msg['id'],
                'from': next((header['value'] for header in headers if header['name'] == 'From'), 'Unknown'),
                'subject': subject,
                'snippet': snippet,
                'spam_alert': spam_alert
            })
        
        return messages_data
    return []

@app.route('/api/emails')
def get_emails():
    if 'google_token' in session:
        emails = read_emails()
        return jsonify(emails)
    return jsonify({'error': 'User not authenticated'}), 401

@app.route('/login')
def login():
    scopes = ' '.join(SCOPES)
    auth_url = (f'https://accounts.google.com/o/oauth2/v2/auth?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}'
                f'&response_type=code&scope={scopes}&access_type=offline')
    return redirect(auth_url)

@app.route('/oauth2callback')
def oauth2callback():
    code = request.args.get('code')
    token_response = requests.post('https://oauth2.googleapis.com/token', data={
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }).json()
    
    if 'access_token' in token_response:
        session['google_token'] = token_response
        return redirect('http://localhost:3000')  # Redirect to React frontend
    return jsonify({'error': 'Authorization failed'}), 400

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect('http://localhost:3000')

if __name__ == '__main__':
    app.run(debug=True)
