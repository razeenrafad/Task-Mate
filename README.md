# 📝 Daily Task Tracker

A simple and elegant Flask web application for managing your daily tasks. Built with Flask, SQLAlchemy, and SQLite database.

## ✨ Features

- **Add Tasks**: Create new tasks with title and optional description
- **Edit Tasks**: Update existing task details
- **Delete Tasks**: Remove tasks you no longer need
- **Mark Complete**: Toggle task completion status
- **Persistent Storage**: All tasks are saved in SQLite database
- **Responsive Design**: Works on desktop and mobile devices
- **Clean UI**: Modern and intuitive user interface

## 🏗️ Project Structure

```
Flask App/
├── app.py                 # Main Flask application file
├── templates/
│   ├── index.html        # Main page template
│   └── edit.html         # Edit task template
├── static/
│   └── style.css         # CSS styling file
├── requirements.txt      # Python dependencies
├── Procfile             # Deployment configuration
└── README.md            # Project documentation
```

## 🚀 Local Setup and Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the project**

   ```bash
   # If you have the project in a folder, navigate to it
   cd "Flask App"
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate

   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:5000`
   - Start adding and managing your tasks!

### Database Setup

The application automatically creates a SQLite database file (`tasks.db`) when you first run it. No additional database setup is required.

## 🌐 Deployment on Render

### Step 1: Prepare Your Repository

1. **Initialize Git repository** (if not already done)

   ```bash
   git init
   git add .
   git commit -m "Initial commit: Daily Task Tracker Flask app"
   ```

2. **Push to GitHub**
   ```bash
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

### Step 2: Deploy on Render

1. **Sign up/Login to Render**

   - Go to [render.com](https://render.com)
   - Sign up or login to your account

2. **Create New Web Service**

   - Click "New +" button
   - Select "Web Service"

3. **Connect Repository**

   - Connect your GitHub account
   - Select your repository containing the Flask app

4. **Configure Deployment Settings**

   - **Name**: `daily-task-tracker` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Python Version**: `3.9` or higher

5. **Advanced Settings (Optional)**

   - **Auto-Deploy**: Enable to automatically deploy on code changes
   - **Branch**: `main` (or your default branch)

6. **Deploy**

   - Click "Create Web Service"
   - Wait for deployment to complete (usually 2-5 minutes)

7. **Access Your App**
   - Once deployed, Render will provide you with a URL like `https://your-app-name.onrender.com`
   - Your Daily Task Tracker is now live!

### Environment Variables (Optional)

If you need to configure environment variables:

- Go to your Render service dashboard
- Navigate to "Environment" tab
- Add any required environment variables

### Database Considerations

- **SQLite**: The app uses SQLite by default, which is file-based
- **Production Database**: For production apps, consider upgrading to PostgreSQL
- **Data Persistence**: Render provides persistent disk storage for SQLite databases

## 🛠️ Development

### Running in Development Mode

```bash
# Set Flask environment to development
export FLASK_ENV=development  # On macOS/Linux
set FLASK_ENV=development     # On Windows

# Run the application
python app.py
```

### Project Structure Explanation

- **`app.py`**: Main Flask application with routes and database models
- **`templates/`**: HTML templates using Jinja2 templating engine
- **`static/`**: Static files like CSS, JavaScript, and images
- **`requirements.txt`**: Python package dependencies
- **`Procfile`**: Deployment configuration for web platforms

### Key Components

1. **Flask Routes**:

   - `/` - Display all tasks
   - `/add` - Add new task
   - `/edit/<id>` - Edit existing task
   - `/toggle/<id>` - Toggle task completion
   - `/delete/<id>` - Delete task

2. **Database Model**:

   - `Task` model with SQLAlchemy ORM
   - Fields: id, title, description, completed, created_at

3. **Templates**:
   - `index.html` - Main page with task list and add form
   - `edit.html` - Task editing form

## 🔧 Customization

### Styling

- Modify `static/style.css` to change the appearance
- The CSS includes responsive design for mobile devices

### Functionality

- Add new features by modifying `app.py`
- Create new templates in the `templates/` directory
- Add static files to the `static/` directory

### Database

- Modify the `Task` model in `app.py` to add new fields
- Run database migrations if you change the model structure

## 📱 Features Overview

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Real-time Updates**: Changes are immediately reflected in the interface
- **User Feedback**: Success and error messages for all actions
- **Data Validation**: Form validation to prevent empty task titles
- **Confirmation Dialogs**: Delete confirmation to prevent accidental deletions

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**

   ```bash
   # Kill process using port 5000
   lsof -ti:5000 | xargs kill -9
   ```

2. **Database Issues**

   ```bash
   # Delete database file to reset
   rm tasks.db
   python app.py
   ```

3. **Dependencies Issues**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```

### Getting Help

- Check the Flask documentation: [flask.palletsprojects.com](https://flask.palletsprojects.com/)
- SQLAlchemy documentation: [sqlalchemy.org](https://www.sqlalchemy.org/)
- Render documentation: [render.com/docs](https://render.com/docs)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

---

**Happy Task Tracking! 🎯**

