import os

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app with the name of the module and set the folder for templates
app = Flask(__name__, template_folder='templates')

# Configuration settings for the Flask app, including database URI and secret key for secure sessions
app.config['SECRET_KEY'] = '1234'  # Secret key for securing Flask sessions and flash messages
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://flask_Todo_user:password@localhost/flask_Todo')  # Database connection string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disables modification tracking to save resources

# Initialize SQLAlchemy with the Flask app for ORM capabilities
db = SQLAlchemy(app)

# Define the Todo model for the database, representing tasks in our to-do list
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each task
    task = db.Column(db.String(128), nullable=False)  # The task description
    done = db.Column(db.Boolean, default=False)  # Whether the task is completed
    
# Define the ContactSubmission model, representing contact form submissions
class ContactSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each submission
    name = db.Column(db.String(100), nullable=False)  # Submitter's name
    phone = db.Column(db.String(20), nullable=False)  # Submitter's phone number
    email = db.Column(db.String(100), nullable=False)  # Submitter's email
    message = db.Column(db.Text, nullable=False)  # Submitter's message

# Database setup function that ensures all tables are created based on the models defined
def setup_database(app):
    with app.app_context():
        db.create_all()

# Call the database setup function to prepare our database
setup_database(app)

# Route for the homepage and to-do list management, fetching all to-dos for display
@app.route('/')
@app.route('/home')
def home():
    todos = Todo.query.all()  # Retrieve all to-do items from the database
    return render_template('home.html', todos=todos)  # Render the homepage with to-dos

# Route for managing tasks, similar to the home route but possibly with additional management capabilities
@app.route('/manage')
def manage():
    todos = Todo.query.all()  # Retrieve all to-do items from the database
    return render_template('manage.html', todos=todos)  # Render the management page with to-dos

# Route for the contact page, simply renders the contact form template
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for the about page, providing information about the application
@app.route('/about')
def about():
    return render_template('about.html')

# Route to add a new task, using POST method to handle form submission
@app.route('/add', methods=['POST'])
def add():
    todo_text = request.form['todo']  # Get the task description from the form
    new_todo = Todo(task=todo_text, done=False)  # Create a new Todo object
    db.session.add(new_todo)  # Add the new task to the session
    db.session.commit()  # Commit the session to save the task to the database
    return redirect(url_for('manage'))  # Redirect back to the manage page

# Route to edit an existing task, supports both GET (to display the form) and POST (to submit changes)
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    todo = Todo.query.get_or_404(id)  # Retrieve the task by id or return 404 error
    if request.method == 'POST':
        todo.task = request.form['todo']  # Update the task description from the form
        db.session.commit()  # Commit the changes to the database
        return redirect(url_for('manage'))  # Redirect back to the manage page
    else:
        return render_template('edit.html', todo=todo, id=id)  # Render the edit form for the task

# Route to toggle the completion status of a task
@app.route('/check/<int:id>')
def check(id):
    todo = Todo.query.get_or_404(id)  # Retrieve the task by id or return 404 error
    todo.done = not todo.done  # Toggle the 'done' status of the task
    db.session.commit()  # Commit the changes to the database
    return redirect(url_for('manage'))  # Redirect back to the manage page

# Route to delete a task from the database
@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)  # Retrieve the task by id or return 404 error
    db.session.delete(todo)  # Delete the task from the session
    db.session.commit()  # Commit the session to remove the task from the database
    return redirect(url_for('manage'))  # Redirect back to the manage page

# Route to handle contact form submissions
@app.route('/submit-contact-form', methods=['POST'])
def submit_contact_form():
    # Retrieve form data
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    message = request.form['idea']

    # Create a new contact submission object
    new_submission = ContactSubmission(name=name, phone=phone, email=email, message=message)
    db.session.add(new_submission)  # Add the new submission to the session
    db.session.commit()  # Commit the session to save the submission to the database

    flash('Your contact information has been submitted successfully!', 'success')  # Show success message
    return redirect(url_for('home'))  # Redirect back to the homepage

# The main entry point of the application, running the app on the specified port
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Enable debug mode for development purposes
