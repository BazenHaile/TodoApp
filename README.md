# TodoApp

A simple yet powerful to-do list web application designed to help users manage their tasks efficiently. Built with a robust stack including Flask, PostgreSQL for the backend, and HTML, CSS, JavaScript for a responsive and interactive frontend.

## Features

- Task Management: Easily add, delete, edit, and mark tasks as complete.
- Interactive UI: Engage with tasks through a user-friendly web interface.
- Data Persistence: Tasks are stored in a PostgreSQL database, ensuring data is saved between sessions.

## Technology Stack

- Backend: Flask, a lightweight WSGI web application framework in Python, offering simplicity and scalability. PostgreSQL is used as the database to store tasks, providing robustness and reliability.
- Frontend: HTML and CSS for structuring and styling the application, with JavaScript enhancing the interactivity, especially in form validation and dynamic content updates.
- Deployment: Hosted on Render.com, leveraging its straightforward deployment process and integration with GitHub for continuous deployment.

## Navigation Planning and Website Flow

### Website Structure and Navigation

- Homepage: Introduces the application with a carousel and provides access to all functionalities.
- Manage To-Dos: A dedicated interface for task management—view, add, edit, delete, and toggle completion status.
- About Us: Shares the mission, features, and team behind the application.
- Contact Us: A form for inquiries, feedback, or support, incorporating JavaScript for client-side validation.

### User Flow Outline

- Entry Point (Homepage): Users land here. Offers navigation to Manage To-Dos, Contact Us, and About Us.
- Task Management (Manage To-Dos): The core of the application where users interact with their tasks.
- Learn More (About Us): Provides detailed background information about the app and its creators.
- Reach Out (Contact Us): Includes a contact form with validation, improving engagement and support.

## Deployment on Render

### Pre-Deployment Checklist

- Ensured code is managed in a GitHub repository.
- Included a `requirements.txt` for Python package management.
- Utilized a `.gitignore` to maintain repository cleanliness.
- Synchronized the local and GitHub repositories.

### Render Configuration

- Service Name: TodoApp
- Region: Europe
- Runtime: Python3
- Build Command: Auto-detected (`pip install -r requirements.txt`)
- Start Command: `gunicorn -w 4 -b :$PORT app:app`

### Deployment Steps

1. Created a new web service on Render and connected the GitHub account.
2. Selected the TodoApp repository and configured the service settings.
3. Initiated deployment and monitored the process via Render's dashboard.
4. Confirmed the application was live and operational at `https://todoapp-p94g.onrender.com`.

## Getting Started

To run the TodoApp locally, follow these steps:

1. Clone the repository: `git clone [repository URL]`
2. Navigate to the project directory: `cd TodoApp`
3. Install dependencies: `pip install -r requirements.txt`
4. Set environment variables: `export FLASK_APP=app` and `export FLASK_ENV=development`
5. Initialize the database: `flask db upgrade`
6. Run the application: `flask run`

Open a web browser and navigate to `http://127.0.0.1:5000/` or `http://127.0.0.1:5001/` to start managing your tasks with TodoApp.
