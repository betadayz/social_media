from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user,current_user,logout_user,login_required
from puppycompanyblog import db
from puppycompanyblog.models import User, BlogPost
from puppycompanyblog.users.forms import RegistrationForm,LoginForm,UpdateUserForm
from puppycompanyblog.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)

@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                     username=form.username.data,
                     password=form.password.data)

    db.session.add(user)
    db.session.commit()
    flash('Thans for registration!')
    return redirect(url_for('users.login'))
return render_template('register.htnl',form=form)    


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))