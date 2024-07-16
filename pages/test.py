import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
key_dict = json.loads(st.secrets["textkey"])

# Fetch the service account key JSON file contents
cred = credentials.Certificate('key_dict')

# Initialize the app with a service account, granting admin privileges
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://camp---2-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
#ref = db.reference('sub')
#st.write(ref.get())
if st.button("setTest") :  
    ref = db.reference('test')
    ref.set({"hi":"hello"})

    ref2 = db.reference('test2')
    ref2.set({"hi":{"hello":"bye", 'good':'bad'}})
if st.button("updateTest"):
    ref = db.reference()
    ref.set({"hi":"HELLo", "bye":"GOOD BYE"})