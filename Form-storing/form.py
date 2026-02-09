from flask import Flask
from db.index import db
from routes.addUsers import add_user_bp
from routes.ShowUser import show_users_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db.init_app(app)

app.register_blueprint(add_user_bp)
app.register_blueprint(show_users_bp, url_prefix = "/users")



if __name__  == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)