import os
import json
import unittest

from flask_sqlalchemy import SQLAlchemy
from app import create_app
from database.models import setup_db, Actors, Movies




class AgencyTestCase(unittest.TestCase):
    """This class represents the agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.CASTING_ASSISTANT = os.environ['CASTING_ASSISTANT']
        self.CASTING_DIRECTOR =  os.environ['CASTING_DIRECTOR']
        self.EXECUTIVE_PRODUCER = os.environ['EXECUTIVE_PRODUCER']    
        
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agency_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        
        self.new_actor = {
        'name': 'new_name',
        'age': 50,
        'gender': 'F',
        }
        
        self.new_invalid_actor = {
        'name': 'new_name',
        'gender': 1,
        }
        
        self.new_movie = {
        'title': 'new_title',
        'release_year': 2022,
        'duration': '2:30',
        }
        
        self.new_invalid_movie = {
        'title': 'new_title',
        'release_year': '2022',
    
        }
        
        self.valid_patch_actor = {
            'release_year': 2006
        }
        
        self.invalid_patch_actor = {
        
        }
        
        self.valid_patch_movie = {
            'title': 'Titanic',
            'release_year': 2006,
            'duration': 9
        }
        
        self.invalid_patch_movie = {
            
        }


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
            
            
    def tearDown(self):
        """Executed after reach test"""
        pass
    
    
    def test_home(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], 'Healthy')
        
    #get actors w/o token
    def test_actors_without_token_get(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, 200)
        
    #get actor with token
    def test_get_actors_with_valid_token(self):
        res = self.client().get(
            '/actors',
            headers={
                "Authorization": "Bearer {}".format(self.EXECUTIVE_PRODUCER)})
        self.assertEqual(res.status_code, 200)
    
    #get specific actor w/o token
    def test_specific_actor_without_token_get(self):
        res = self.client().get('/actors/2')
        self.assertEqual(res.status_code, 200)
        
    #get specific actor with token 
    # def test_specific_actor_without_token_get(self):
    #     res = self.client().get(
    #         '/actors/2',
    #         headers={'Authorization': "Bearer {}".format(self.EXECUTIVE_PRODUCER)})
    #     self.assertEqual(res.status_code, 200)
        
        
    #post actor w/o token
    def test_actor_without_token_post(self):
        new_actor_data = {
            'name': "New actor name worked.",
            'age': 20,
            'gender': "female"
        } 

        res = self.client().post('/actors', data=json.dumps(new_actor_data), headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor']['name'], new_actor_data['name'])
        self.assertEqual(data['actor']['age'], new_actor_data['age'])
        self.assertEqual(data['actor']['gender'], new_actor_data['gender'])


    #post actor with token
    def test_actor_with_token_post(self):
        res = self.client().post(
            '/actor', 
            headers={'Authorization': "Bearer {}".format(self.EXECUTIVE_PRODUCER)},
            json=self.new_actor)
        
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    
    #patch actor w/o token
    def test_actor_without_token_patch(self):
        actor = Actors(name="Megan Fox", age=50, gender="female")
        actor.insert()

        actor_data_patch = {
            'age': 37
        } 

        res = self.client().patch('/actors/13',
            data=json.dumps(actor_data_patch),
            headers={'Content-Type': 'application/json'})
        
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertFalse(data['success'])





    #patch actor w/o token
    def test_actor_with_token_patch(self):
        res = self.client().patch(
            '/actor/10', 
            headers={'Authorization': "Bearer {}".format(self.EXECUTIVE_PRODUCER)},
            json=self.valid_patch_actor)
        self.assertEqual(res.status_code, 200)
        
    delete actor w/o token
    def test_actor_without_token_delete(self):
        res = self.client().delete('/actor/15')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    delete actor w/o token
    def test_actor_with_token_delete(self):
        res = self.client().delete(
            '/actor/19', 
            headers={'Authorization': "Bearer {}".format(self.EXECUTIVE_PRODUCER)})
        self.assertEqual(res.status_code, 200)
        
        


#----------
#Movie test 
#----------

    #get movies w/o token
    def test_movies_without_token_get(self):
        res = self.client().get('/movies')
        self.assertEqual(res.status_code, 200)
        
    #get movie with token
    def test_movies_with_token_get(self):
        res = self.client().get(
            '/movies', 
            headers={'Authorization': "Bearer {}".format(self.EXECUTIVE_PRODUCER)})
        self.assertEqual(res.status_code, 200)

    #get specific movie w/o token
    def test_specific_movie_without_token_get(self):
        res = self.client().get('/movie/2')
        self.assertEqual(res.status_code, 404)
        
    #get specific movie with token 
    def test_specific_movie_without_token_get(self):
        res = self.client().get(
            '/movie/2',
            headers={'Authorization': "Bearer {}".format(self.EXECUTIVE_PRODUCER)})
        self.assertEqual(res.status_code, 200)
    
    
    #post movie w/o token
    def test_movie_without_token_post(self):
        res = self.client().post('/movies', json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
    


    #post movie w/o token
    def test_movie_with_token_post(self):
        res = self.client().post(
            '/movies', 
            headers={'Authorization': "Bearer {}".format(self.EXECUTIVE_PRODUCER)},
            json=self.new_movie)
        self.assertEqual(res.status_code, 200)
    
    
    #patch movie w/o token
    def test_movie_without_token_patch(self):
        movie = Movies(title="Rocky I", release_year=1976, duration=2)
        movie.insert()

        movie_data_patch = {
            'release_year': 2020
        } 

        res = self.client().patch('/movies/4',
            data=json.dumps(movie_data_patch),
            headers={'Content-Type': 'application/json'}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    

    #patch movie w/o token
    def test_movie_with_token_patch(self):
        res = self.client().patch(
            '/movies/1', 
            headers={'Authorization': "Bearer {}".format(self.EXECUTIVE_PRODUCER)},
            json=self.valid_patch_movie)
        self.assertEqual(res.status_code, 200)
        
        
    #delete movie w/o token
    def test_movie_without_token_delete(self):
        res = self.client().delete('/movies/4')
        self.assertEqual(res.status_code, 200)
    

    #delete movie w/o token
    def test_movie_with_token_delete(self):
        res = self.client().delete(
            '/movies/10', 
            headers={'Authorization': "Bearer {}".format(self.EXECUTIVE_PRODUCER)})
        self.assertEqual(res.status_code, 200)
        
        
if __name__ == "__main__":
    unittest.main()