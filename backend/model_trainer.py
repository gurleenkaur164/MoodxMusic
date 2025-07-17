import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import json

df= pd.read_csv('data.csv')

#valence score: 
def valence_to_mood(val):
    if val> 0.7:
        return 'happy'
    elif val> 0.4:
        return 'neutral'
    else:
        return 'sad'
    
df['mood']= df['valence'].apply(valence_to_mood)
mood_to_songs={}
for mood in df['mood'].unique():
    #select all the rows that match the current mood
    subset= df[df['mood']==mood]
    mood_to_songs[mood] =[
        f"{row['song_title']}-{row['artist']}"
        for _, row in subset.sample(min(10, len(subset))).iterrows()
    ] 

with open("songs.json",'w') as f:
    json.dump(mood_to_songs,f)      

#training data:
texts=["I am very happy today", "I just want to relax",
       "I am so sad and broken", "Let's party!",
       "Feeling low", "Quiet and peaceful evening"]
labels=["happy", "chill", "sad", "happy","sad","neutral"]
vectorizer= TfidfVectorizer()
X= vectorizer.fit_transform(texts)
y= labels
model=LogisticRegression()
model.fit(X,y)
joblib.dump(model, 'mood_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')  