from flask import Blueprint,request, render_template, redirect
from db.index import db
from models.users import User

show_users_bp = Blueprint("show_users_bp", __name__)

@show_users_bp.route('/')
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@show_users_bp.route("/delete/<int:id>", methods = ['GET','POST'])
def delete_users(id):
    users_to_delete = User.query.get_or_404(id)
    db.session.delete(users_to_delete)
    db.session.commit()
    return redirect('/')
