from flask import Flask, jsonify, request, render_template, abort
# from utils import ClassificationModelBuilder # Uncomment only if you want to re-train your model
from api.predict import predict_api
from jinja2 import TemplateNotFound

app = Flask(__name__ , template_folder='templates')
app.register_blueprint(predict_api, url_prefix='/titanic-survival-classification-model')


# Loading home page
@app.route('/', defaults={'page': 'index'})
@app.route('/<page>')
def show(page):

    try:
        print('home route')
        return render_template(f'{page}.html', app_name='Titanic Survival: Classification Problem')
    
    except TemplateNotFound:
        abort(404)


# Handling 400 Error
@app.errorhandler(400)
def bad_request(error=None):

	message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url + '--> Please check your data payload...',
	}
	resp = jsonify(message)
	resp.status_code = 400

	return resp


# run application
if __name__ == "__main__":
    app.run()