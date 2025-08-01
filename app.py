from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
reminder_titles = []
reminders = []

# for now use json then server-side storage can be implemented later
if json_file := 'reminders.json':
    try:
        with open(json_file, 'r') as file:
            reminders = json.load(file)
    except FileNotFoundError:
        # If the file does not exist, we create the file
        with open(json_file, 'w') as file:
            json.dump([], file)


@app.route('/')
def index():
    return render_template('index.html', reminders=reminders)


@app.route('/add_reminder', methods=['POST'])
def add_reminder():
    reminder_title = request.form['reminder_title']
    reminder_text = request.form['reminder_text']
    reminder_time = request.form['reminder_time']
    if reminder_title and reminder_text and reminder_time:
        reminders.append({
            'title': reminder_title,
            'text': reminder_text,
            'time': reminder_time
        })
        with open('reminders.json', 'w') as file:
            json.dump(reminders, file)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))