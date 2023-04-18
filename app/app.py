from flask import Flask
from flasgger import Swagger
from routes.players import bp as players_bp

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'My Flask API',
    'uiversion': 3
}
swagger = Swagger(app)

app.register_blueprint(players_bp, url_prefix='/players')

if __name__ == '__main__':
    app.run()