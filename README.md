SpamSlayer: A Machine Learning-based Spam Email Detection Application
SpamSlayer is a powerful web application that utilizes machine learning (ML) techniques to detect spam emails. Built using Flask for the backend and React for the frontend, this project aims to provide users with a user-friendly interface to identify spam emails and protect their inboxes.

Key Features:
Machine Learning Model for Spam Detection: Trains and uses ML models to classify emails as spam or non-spam based on their content.
Real-Time Email Filtering: Users can upload or view emails, and the system will instantly detect if they are spam, displaying alerts with a red background if flagged as spam.
User Interface: The React-based frontend allows easy interaction with the backend, providing users with an intuitive platform to interact with the spam detection model.
Seamless Backend Integration: Flask handles the backend operations, running the spam detection logic and handling API requests.
Tech Stack:
Frontend: React, Bootstrap (for styling)
Backend: Flask, Python
Machine Learning: Scikit-learn, NLTK (for text preprocessing and feature extraction)
APIs: Gmail API (optional integration for real email fetching)
Installation & Setup:
Clone the repository:


git clone https://github.com/gokulteja49/SpamSlayer.git
Backend Setup (Flask):

Install Python dependencies:
cd backend
pip install -r requirements.txt

Run the Flask backend:
python app.py
Frontend Setup (React):

Install Node.js dependencies:
cd frontend
npm install

Start the React development server:
npm start
Run both backend and frontend servers:

Make sure both Flask and React servers are running to see the app in action!

overview of WEB app:
![image](https://github.com/user-attachments/assets/fa3f9c81-238c-4a49-b024-44dd22c50ee5)


