import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


firebaseconfig ={ 
    "apiKey": "AIzaSyAvIpxCm8gr_nj4lyfzSksIGpE8bWbobcA",

  "authDomain": "flask-keefe.firebaseapp.com",

  "databaseURL": "https://flask-keefe-default-rtdb.asia-southeast1.firebasedatabase.app",

  "projectId": "flask-keefe",

  "storageBucket": "flask-keefe.appspot.com",

  "messagingSenderId": "576714286217",

  "appId": "1:576714286217:web:144f7e60c583ba96a91258"

}

firebase = pyrebase.initialize_app(firebaseconfig)
storage = firebase.storage()


