from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_movies = movies_data[['original_title','poster_link','release_date','runtime','weighted_rating']]

# variables to store data
liked_movie = []
not_liked_movie = []
did_not_watch = []

# method to fetch data from database
def assign_val():
  m_data = {
    'original_title':all_movies.iloc[0,0],
    'poster_link':all_movies.iloc[0,1],
    'release_data':all_movies.iloc[0,2],
    'runtime':all_movies.iloc[0,3],
    'weighted_rating':all_movies.iloc[0,4]/2
  }
  return m_data

# /movies api
@app.route('/movies')
def get_movie():
  movie_data = assign_val()
  return jsonify({

    'data':movie_data,
    'status':'success'
  })

# /like api
@app.route('/liked_movies')
def liked_movies():
  global all_movies
  movie_data = assign_val()
  liked_movie.append(movie_data)
  all_movies.drop([0],inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
    "status":"success"
  })

# /dislike api
@app.route('/not_liked_movies')
def not_liked_movies():
  global all_movies
  movie_data = assign_val()
  not_liked_movie.append(movie_data)
  all_movies.drop([0],inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
    'status':'success'
  })

# /did_not_watch api
@app.route('/did_not_watch')
def did_not_watched():
  global all_movies
  movie_data = assign_val()
  did_not_watch.append(movie_data)
  all_movies.drop([0],inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
    'status':'success'
  })

if __name__ == "__main__":
  app.run()