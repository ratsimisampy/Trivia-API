import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

   # questions = [question.format() for question in selection]
    current_questions = selection[start:end]

    return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO done: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO done: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
      return response

  @app.route('/')
  def index():
    return 'Welcome to Trivia API'

  '''
  @TODO done: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def get_Categories():
    categories = [category.format() for category in Category.query.all()]
    if len(categories) == 0:
      abort(404)

    return jsonify({
            'success': True,
            'categories': categories,
            'total_categories': len(categories)
        })

  '''
  @TODO done: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def get_Questions():
    selection = [ question.format() for question in Question.query.order_by(Question.difficulty).all()    ]

    # if categ:
    #   selection = questions.filter(Category.category == categ).one_or_none()

    current_questions = paginate_questions(request, selection)

    return jsonify({
            'Success': True,
           # 'category': categ,
            'List of questions': current_questions,
            'Total_questions': len(Question.query.all())
        })



  '''
  @TODO done: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.get(question_id)

      if question:
        Question.delete(question)
      # Re select all then pagination
        selection = Question.query.order_by(Question.difficulty).all()
        current_questions = paginate_questions(request, selection)

    except:
      abort(422)

    return jsonify({
            'Success': True,
            'List of questions': current_questions,
            'Deleted question id': question_id,
            'Total_questions': len(Question.query.all())
        })

  '''
  @TODO: a tester
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/books', methods=['POST'])
  def create_question():
    body = request.get_json()

    new_question = body.get('question',  None)
    new_answer = body.get('answer', None)
    new_category = body.get('category', None)
    new_difficulty = body.get('difficulty', None)


    try:
      if request.method == 'POST':
        question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
        question.insert()

        selection = Question.query.order_by(difficulty).all()
        current_questions = paginate_questions(request, selection)
        # ???
        import pdb; pdb.set_trace            

      return jsonify({
            'Success': True,
            'List of questions': current_questions,          
            'Total_questions': len(Question.query.all())
        })
    
    except:
      abort(422)

  '''
  @TODO: a tester
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions/search', methods=['POST'])
  def submit_Search():
    search_term = request.form.get('search','')
    search_results = Question.query.filter(Question.question.ilike('%{}%'.format(search_term))).all()
    questions = []

    if len(current_books) == 0:
            abort(404)
      
    for result in search_results:
      questions.append({
        "question": result.question,
        "answer": result.answer,
        "category": result.category,
        "difficulty": result.difficulty
      })

    return jsonify({
            'Success': True,
            'List of questions': questions,          
            'Total_questions': len(questions)
        })

  '''
  @TODO: a tester
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/category/<category_id>/questions')
  def get_by_category(category):
    selection = Question.query.all()

    if category_id:
      selection = Question.query.filter_by(category_id).all()

    current_questions = paginate_questions(request, selection)

    return jsonify({
            'Success': True,
            'List of questions': current_questions,          
            'Total_questions': len(Question.query.all())
        })

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
        return jsonify({
            "success": False, 
            "error": 404,
            "message": "resource not found"
        }), 404

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False, 
          "error": 422,
          "message": "unprocessable"
      }), 422

  return app

    