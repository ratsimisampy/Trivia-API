import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # testing get all questions, for all categories
    def test_paginated_questions(self):
        """Test_______________"""
        res = self.client().get('/questions')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.asserTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    # def test_404_sent_requesting_beyond_request_questions(self):
    #     """Test _____________ """
    #     res = self.client().get('/questions?page=1000')
    #     data = json.loads(res.data)
        
    #     self.assertEqual(res.status_code,404)   
    #     self.assertEqual(data['success'], False)        
    #     self.assertEqual(data['message'],'resource not found')

    # # testing all categories only
    # def test_get_all_categories(self):
    #     """Test_______________"""
    #     res = self.client().get('/categories')
    #     data = json.loads(res.data)        

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.asserTrue(data['total_categories'])
    #     self.assertTrue(len(data['categories']))

    # # testing, No category found
    # def test_404_when_no_categories(self):
    #     """Test_______________"""
    #     res = self.client().get('/categories')
    #     data = json.loads(res.data)        

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], True)
    #     self.asserTrue(data['total_categories'])
    #     self.assertEqual(len(data['categories']), 0)
    #     self.assertEqual(data['message'], 'no category found')

    # def test_delete_questions(self):
    #     """Test_______________"""
    #     res = self.client().delete('/questions/1')
    #     data = json.loads(res.data)

    #     question = Question.query.filter(Question.id == 1).one_or_one()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted'], 1)
    #     self.assertTrue(data['Total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertEqual(question, None)

    # def test_404_if_question_does_not_exist(self):
    #     """Test_______________"""
    #     res = self.client().delete('/questions/1000')
    #     data = json.loads(res.data)        

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')


    # # DOING
    # def test_get_questions_by_category(self):
    #     """Test_______________"""
    #     res = self.client().get('questions/<category>')
    #     data = Question.query.filter(Question.category == 'Science').one_or_one()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['questions']))

    # # ???
    # def test_404_questions_not_found(self):
    #     """Test_______________"""
    #     res = self.client().get('questions/<category>')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')


    # # testing creation of question
    # def test_create_question(self):
    #     """Test_______________"""
    #     res = self.client().post('/questions', json=self.new_question)
    #     data = json.loads(res.data)
        
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['message'],'question is created')

    # # testing fails to create question
    # def test_405_if_creation_is_not_allowed(self):

    #     self.assertEqual(data['success'], False)  

    # # testing search question
    # def test_search_question(self):

    #     self.assertEqual(data['success'], True)

    # # testing surch result is none     
    # def test_404_search_not found(self):

    #     self.assertEqual(data['success'], True)




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()