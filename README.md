# TodoApp

A simple yet powerful to-do list web application designed to help users manage their tasks efficiently. Built with a robust stack including Flask, PostgreSQL for the backend, and HTML, CSS, JavaScript for a responsive and interactive frontend.

**Live Application**: 
[TodoApp on Render](https://todoapp-u0kd.onrender.com/)

## Features

- Task Management: Easily add, delete, edit, and mark tasks as complete.
- Interactive UI: Engage with tasks through a user-friendly web interface.
- Data Persistence: Tasks are stored in a PostgreSQL database, ensuring data is saved between sessions.

## Enhanced User Interaction

- Robust User Engagement and Data Capture: Beyond its core functionality of managing tasks, the application offers a comprehensive platform for users to voice their inquiries, share feedback, and seek support. Utilizing a meticulously designed "Contact Us" interface, each user interaction is securely captured and stored within the PostgreSQL database. This commitment to data integrity ensures no user input is overlooked, allowing for timely and effective responses. More than just enhancing user engagement, this system empowers us to leverage PostgreSQL's powerful querying capabilities. By analyzing the collected data, we can extract meaningful insights, identify trends, and make informed decisions to elevate the overall user experience continuously.

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

## Database and Application Initialization

To ensure that your PostgreSQL tables are set up correctly, the application now includes an initialization function that is run at import time. This ensures that when the application is started by a WSGI server like Gunicorn, the database tables are created properly.

It is critical to set the `DATABASE_URL` environment variable correctly in your Render service's settings. This environment variable should be the internal PostgreSQL database URL provided by Render and not a localhost string.

## Deployment on Render

### Pre-Deployment Checklist

- Ensured code is managed in a GitHub repository.
- Included a `requirements.txt` for Python package management.
- Synchronized the local and GitHub repositories.
- Set the `DATABASE_URL` environment variable in the Render service settings to match the PostgreSQL database provided by Render.

### PostgreSQL Database on Render

- The PostgreSQL database for the application has been provisioned on Render with the following settings:
  - **Name**: `postgresqldb`
  - **Version**: PostgreSQL 16
  - **Region**: Frankfurt (EU Central)
  - **Plan**: Starter (Free Tier with 1GB storage)

Before deploying, make sure that the tables are created by running the application locally or using a migration tool to set up the database schema on Render.

### Render Configuration

- Service Name: TodoApp
- Region: Europe
- Runtime: Python3
- Build Command: Auto-detected (`pip install -r requirements.txt`)
- Start Command: `gunicorn -w 4 app:app`
- Environment: Set the `DATABASE_URL` to the PostgreSQL database, Internal PostgreSQL Database URL provided by Render. This is done in the service's environment variables section.

### Deployment Steps

1. Created a new web service on Render and connected the GitHub account.
2. Selected the TodoApp repository and configured the service settings.
3. Added the necessary environment variables, including `DATABASE_URL`.
4. Initiated deployment and monitored the process via Render's dashboard.
5. Confirmed the application was live and operational at the provided Render subdomain.

## Getting Started

To run the TodoApp locally, follow these steps:

1. Clone the repository: `git clone https://github.com/BazenHaile/TodoApp.git`
2. Navigate to the project directory: `cd TodoApp`
3. Install dependencies: `pip install -r requirements.txt`
4. Set environment variables: `export DATABASE_URL=your_database_uri` replacing `your_database_uri` with your local or cloud PostgreSQL database URI.
5. Start the application: `python app.py`

Open a web browser and navigate to `http://127.0.0.1:5001/` to start managing your tasks with TodoApp.

Replace `your_database_uri` with the actual URI of your PostgreSQL database when running the app locally. For the database URI format, refer to the information provided in your Render PostgreSQL settings. Do not include sensitive information, such as your database URI, directly in your code. Use environment variables to manage sensitive data.
