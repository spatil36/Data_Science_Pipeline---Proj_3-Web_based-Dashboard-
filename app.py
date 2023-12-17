#!/usr/bin/python3  # Replace this with the path to your Python interpreter

import subprocess
from flask import Flask, render_template
from pymongo import MongoClient
from collections import defaultdict


app = Flask(__name__, static_folder='static')


client = MongoClient('mongodb://localhost:27017/')  
db = client['chestnut'] 
collection = db['artists_details']

@app.route('/')
def index():
    subprocess.run(['jupyter', 'nbconvert', '--execute', '--inplace', 'FinalAnalysis.ipynb'])

    artists_data = list(collection.find())

    artist_popularity = [{'name': artist['name'], 'popularity_score': artist['popularity']} for artist in artists_data if 'popularity' in artist]


    graph_urls = {
        'research1': 'static/research1.png',
        'research2': 'static/research2.png',  
        'research3': 'static/research3.png',
        'research4': 'static/research4.png',
        'research5': 'static/research5.png',
        'research6': 'static/research6.png',
    }

    collection_demo = db['artists_posts']
    artists_posts_data = list(collection_demo.find())

    # artists_data_name = [post.get("artist") for post in artists_posts_data if post.get("artist")]

    artist_post_counts = defaultdict(int)
    artists_data_name = set()

    for post in artists_posts_data:
        artist_name = post.get("artist")
        if artist_name:
            artists_data_name.add(artist_name)
            artist_post_counts[artist_name] += 1

    return render_template('dashboard.html', artists=artists_data, graph_urls=graph_urls, artists1=artists_data_name, artist_post_counts=dict(artist_post_counts), artist_popularity=artist_popularity)

@app.route("/demo")
def demo():
    subprocess.run(['jupyter', 'nbconvert', '--execute', '--inplace', 'FinalAnalysis.ipynb'])

    artists_details_data = list(collection.find())
    artist_popularity = [{'name': artist['name'], 'popularity_score': artist['popularity']} for artist in artists_details_data if 'popularity' in artist]

    collection_demo = db['artists_posts']
    artists_posts_data = list(collection_demo.find())

    artist_post_counts = defaultdict(int)
    artists_data_name = set()

    for post in artists_posts_data:
        artist_name = post.get("artist")
        if artist_name:
            artists_data_name.add(artist_name)
            artist_post_counts[artist_name] += 1

    return render_template('demo.html', artists=artists_data_name, artist_post_counts=dict(artist_post_counts), artist_popularity=artist_popularity)
    

if __name__ == '__main__':
    app.run(debug=True)
