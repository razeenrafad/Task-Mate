from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production

# Initialize SQLAlchemy database
db = SQLAlchemy(app)

# Task model - represents a single task in the database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Task {self.title}>'

# Home route - displays all tasks
@app.route('/')
def index():
    # Fetch all tasks from database, ordered by creation date
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

# Add new task route
@app.route('/add', methods=['POST'])
def add_task():
    # Get task data from form
    title = request.form['title']
    description = request.form.get('description', '')
    
    # Validate that title is not empty
    if not title.strip():
        flash('Task title cannot be empty!', 'error')
        return redirect(url_for('index'))
    
    # Create new task object
    new_task = Task(title=title.strip(), description=description.strip())
    
    # Add to database
    db.session.add(new_task)
    db.session.commit()
    
    # Flash success message
    flash('Task added successfully!', 'success')
    return redirect(url_for('index'))

# Edit task route
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    # Find task by ID
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'POST':
        # Update task with new data from form
        task.title = request.form['title'].strip()
        task.description = request.form.get('description', '').strip()
        
        # Validate title is not empty
        if not task.title:
            flash('Task title cannot be empty!', 'error')
            return redirect(url_for('edit_task', task_id=task_id))
        
        # Save changes to database
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('index'))
    
    # Render edit form with current task data
    return render_template('edit.html', task=task)

# Toggle task completion status
@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    # Find task by ID
    task = Task.query.get_or_404(task_id)
    
    # Toggle completion status
    task.completed = not task.completed
    
    # Save changes to database
    db.session.commit()
    
    # Flash appropriate message
    status = 'completed' if task.completed else 'marked as incomplete'
    flash(f'Task {status}!', 'success')
    return redirect(url_for('index'))

# Delete task route
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    # Find task by ID
    task = Task.query.get_or_404(task_id)
    
    # Delete task from database
    db.session.delete(task)
    db.session.commit()
    
    # Flash success message
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))

# Create database tables
with app.app_context():
    db.create_all()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
