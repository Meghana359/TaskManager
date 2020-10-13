'''
Bootstrap program
'''

# import os
from flask import Flask, Blueprint
# from flask import request

from flask_restx import Resource, Api

# from task_manager.routes.tasks import task as task_namespace
# from task_manager.routes.users import user as user_namespace

from routes.tasks import model_get_create_task, model_post_create_task, model_fetch_task, model_get_update_task, model_post_update_task, model_delete_task

app = Flask(__name__)                  # Create a Flask WSGI application
api = Api(app)                          # Create a Flask-RESTPlus API

@api.route('/')
@api.route('/hello')                   # Create a URL route to this resource
class HelloWorld(Resource):            # Create a RESTful resource
	''' HOME PAGE '''
	def get(self):                     # Create GET endpoint
		return {'hello':'world'}

@api.route('/task/create', methods=['GET', 'POST'])
class CreateTask(Resource):
	''' CREATE NEW TASK '''
	def get(self):
		# return {'Show': 'Form'}
		return model_get_create_task()

	def post(self):
		# return {'Create':'Task'}
		return model_post_create_task()


@api.route('/task/')
@api.route('/task/<int:task_id>')
class FetchTask(Resource):
	''' FETCH TASK '''
	def get(self, task_id = -1):
		# return 'Task %d' % task_id
		return model_fetch_task(task_id)


@api.route('/task/edit/<int:task_id>', methods=['GET', 'POST'])
class UpdateTask(Resource):
	''' UPDATE TASK '''
	def get(self, task_id):
		# return {'Show': 'Form'}
		return model_get_update_task(task_id)

	def post(self, task_id):
		# return {'Update':'Task'}
		return model_post_update_task(task_id)


@api.route('/task/delete/<int:task_id>', methods=['PUT', 'DELETE'])
class DeleteTask(Resource):
	''' DELETE TASK '''
	def delete(self, task_id):
		# return 'Task %d' % task_id
		return model_delete_task(task_id)


@api.route('/user/create', methods=['GET', 'POST'])
class CreateUser(Resource):
	''' CREATE USER '''
	def get(self):
		return {'Show':'Form'}

	def post(self):
		return {'create':'user'}


@api.route('/user/')
@api.route('/user/<int:user_id>')
class FetchUser(Resource):
	''' FETCH USER '''
	def get(self, user_id = -1):
		return {'User': user_id}


@api.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
class UpdateUser(Resource):
	''' UPDATE USER '''
	def get(self):
		return {'Show':'Form'}

	def post(self):
		return {'update':'user'}


@api.route('/user/delete/<int:user_id>', methods=['PUT', 'DELETE'])
# I dont know if I want to do DELETE or PUT
class DeleteUser(Resource):
	''' DELETE USER '''
	def delete(self,user_id):
		return 'User %d' % user_id


def initialize_app(flask_app):
	blueprint = Blueprint('api', __name__, url_prefix = '/routes')
	api.init_app(blueprint)
#	api.add_namespace(task_namespace)
#	api.add_namespace(user_namespace)
	flask_app.register_blueprint(blueprint)


def main():
	initialize_app(app)
	app.run(debug=True)  # Start a development server


if __name__ == '__main__':
	#app.run(debug=True)	 # Start a development server
	main()
