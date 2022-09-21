import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from database.models import setup_db, Actors, Movies
from flask_cors import CORS

from auth.auth import AuthError, requires_auth



def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)


# --------------------------
# Config
# --------------------------
def create_app(test_config=None):
      
  app = Flask(__name__)
  setup_db(app)
    
  CORS(app)


# --------------------------
# Routes
# --------------------------

  @app.route('/')
  def home():
        return jsonify({
          'success': True,
          'message': 'Healthy'
        })

# ------
# GET 
# -------

  #Get actors 
  @app.route('/actors', methods=['GET'])
  @requires_auth("get:actors")
  def get_actors():
        actors = Actors.query.order_by(Actors.id).all()
        formatted_actors = [actors.format() for actors in actors]
        
        
        return jsonify({
          'success': True,
          'actors': formatted_actors,
        }), 200
  
  #get specific actor 
  @app.route('/actors/<int:actor_id>')  
  @requires_auth('get:actors-details')   
  def get_specific_actor(actor_id):
      #body = request.get_json()
      try:
        actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
        
        if actor is None:
              abort(404)
              
        else:
              return jsonify({
                'success': True,
                'id': actor.id,
                'actor': actor.format()
              }), 200
      except:
        abort(405)
        
        
  #get movies 
  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movies')
  def get_movies():
      movies = Movies.query.order_by(Movies.id).all()
      formatted_movies = [movies.format() for movies in movies]
      
      return jsonify({
        'success': True,
        'movies': formatted_movies,
      }), 200
        
        
  #get specific movie
  @app.route('/movies/<int:movie_id>', methods=['GET'])
  @requires_auth('get:movies-details')
  def get_specific_movie(movie_id):
    try:
      movies = Movies.query.filter(Movies.id == movie_id).one_or_none()
    
      if movies is None:
            abort(404)
            
      else:
            return jsonify({
              'success': True,
              'id': movies.id,
              'movie': movies.format()
            }), 200
    except:
      abort(405)

# ------
# POST
# -------

  #Create Actor 
  @app.route('/actors', methods=['POST'])
  @requires_auth('get:actors')
  def create_actors():
        body = request.get_json()
        actors_list = Actors.query.all
        
        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)
        
      
        actor = Actors(name=new_name, age=new_age, gender=new_gender)
        actor.insert()
        
        return jsonify({
          'success': True,
          'created': actor.id,
          'actor': actor.name,
        }), 200
        

  
  #Create Movie
  @app.route('/movies', methods=['POST'])
  @requires_auth('get:movies')
  def create_movies():
        body = request.get_json()
        movies_list = Movies.query.all()
        
        new_title = body.get('title', None)
        new_release_year = body.get('release_year', None)
        new_duration = body.get('duration', None)
        
        try: 
          movie = Movies(title=new_title, release_year=new_release_year, duration=new_duration)
          movie.insert()
          
          return jsonify({
            'success': True,
            'created': movie.id,
            'movie': movie.title,
            'total_movies': len(movies_list)
          }), 200
          
        except:
          abort(422)

# ------
# PATCH
# -------

  #Update actor 
  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def patch_actor(actor_id):
    actor = Actors.query.get(actor_id)
    body = request.get_json()
    
    name = body.get('name', None)
    age = body.get('age', None)
    gender = body.get('gender', None)
    
    actor = Actors.query.filter_by(actor_id=id).one_or_none() 
    
    if actor is None:
      abort(404)
      
      
    actor.name = name
    actor.age = age
    actor.gender = gender
    actor.update()
      
    return jsonify({
      'success': True,
      'updated_actor': actor
    }), 200

    


  @app.route('/movies/<int:id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def patch_movie(id):
    movie = Movies.query.filter_by(id=id).one_or_none()
    if movie is None:
        abort(404)
    body = request.get_json()
    title = body.get('title', None)
    release_year = body.get('release_year', None)
    duration = body.get('duration', None)

    movie.title = title
    movie.release_year = release_year
    movie.duration = duration

    movie.update()

    return jsonify({
        'success': True,
        'updated_movie': id,
        'total_movies': len(Movies.query.all())
    })
# ------
# DELETE
# -------

  #delete actor
  @app.route('/actors/<int:id>', methods=['DELETE'])
  @requires_auth('delete:actors')

  def delete_actor(id):
    actor = Actors.query.filter_by(id=id).one_or_none()
    
    if not actor:
      abort(404)
  
    try:
      actor.delete()
      
      return jsonify({
        'success': True,
        'deleted_actor': id
      }), 200

    except:
      abort(422)


  #delete movie
  @app.route('/movies/<int:id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(id):
    movie = Movies.query.filter_by(id=id).one_or_none()
    
    if not movie:
      abort(404)
  
    try:
      movie.delete()
      
      return jsonify({
        'success': True,
        'deleted_movie': id
      }), 200

    except:
      abort(422)


#------------------------------------
# Error Handling
#------------------------------------


  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          'success': False,
          'error': 400,
          'message': 'Bad Request'
      }), 400

  @app.errorhandler(401)
  def unauthorized(error):
      return jsonify({
          'success': False,
          'error': 401,
          'message': 'Unauthorized'
      }), 401

  '''
  @TODO implement error handler for 404
      error handler should conform to general task above
  '''
  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          'success': False,
          'error': 404,
          'message': 'Not Found'
      }), 404

  @app.errorhandler(405)
  def method_not_allowed(error):
      return jsonify({
          'success': False,
          'error': 405,
          'message': 'Method Not Allowed'
      }), 405

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "Unprocessable"
      }), 422

  @app.errorhandler(500)
  def internal_server_error(error):
      return jsonify({
          'success': False,
          'error': 500,
          'message': 'Internal Server Error'
      }), 500

  '''
  @TODO implement error handler for AuthError
      error handler should conform to general task above
  '''

  @app.errorhandler(AuthError)
  def auth_error(error):
      return jsonify({
          'success': False,
          'error': error.status_code,
          'message': error.error['description']
      }), error.status_code
      
      
  
  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)