# routes/content.py
from flask import Blueprint, render_template, request, redirect
from app.model import Content, db

content = Blueprint('content', __name__)

@content.route('/')
def home():
    contents = Content.query.all()
    return render_template('home.html', contents=contents)

@content.route('/dashboard')
def dashboard():
    contents = Content.query.all()
    return render_template('dashboard.html', contents=contents)

@content.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        c = Content(
            title=request.form['title'],
            description=request.form['description'],
            image=request.form['image'],
            video_url=request.form['video']
        )
        db.session.add(c)
        db.session.commit()
        return redirect('/dashboard')

    return render_template('create.html')