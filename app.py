import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import flash, get_flashed_messages

app = Flask(__name__, template_folder='templates')

# My PostgreSQL configuration
app.config['SECRET_KEY'] = '1234'  # used to secure sessions and flash messages.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://flask_Todo_user:password@localhost/flask_Todo')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(128), nullable=False)
    done = db.Column(db.Boolean, default=False)
    
class ContactSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Initialize the database
def setup_database(app):
    with app.app_context():
        db.create_all()

setup_database(app)


# The home and manage routes need to query the database for todos
@app.route('/')
@app.route('/home')
def home():
    todos = Todo.query.all()
    return render_template('home.html', todos=todos)

@app.route('/manage')
def manage():
    todos = Todo.query.all()
    return render_template('manage.html', todos=todos)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

# The add function adds a new todo to the database
@app.route('/add', methods=['POST'])
def add():
    todo_text = request.form['todo']
    new_todo = Todo(task=todo_text, done=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('manage'))

# The edit function fetchs and updates todos by their id
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    todo = Todo.query.get_or_404(id)
    if request.method == 'POST':
        todo.task = request.form['todo']
        db.session.commit()
        return redirect(url_for('manage'))
    else:
        return render_template('edit.html', todo=todo, id=id)

# The check function toggles the done status of a todo
@app.route('/check/<int:id>')
def check(id):
    todo = Todo.query.get_or_404(id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for('manage'))

# The delete function removes a todo from the database
@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('manage'))

@app.route('/submit-contact-form', methods=['POST'])
def submit_contact_form():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    message = request.form['idea']

    new_submission = ContactSubmission(name=name, phone=phone, email=email, message=message)
    db.session.add(new_submission)
    db.session.commit()

    flash('Your contact information has been submitted successfully!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)

