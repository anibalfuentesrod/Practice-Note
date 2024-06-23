from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
import json
import os
from uuid import uuid4

app = Flask(__name__)

# File to store notes
NOTES_FILE = 'notes.json'

# Function to load notes from JSON file
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            try:
                data = json.load(file)
                return data.get("notes", {})
            except json.JSONDecodeError:
                return {}
    return {}

# Function to save notes to JSON file
def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump({"notes": notes}, file, indent=4)

# Load existing notes
notes = load_notes()

@app.route('/')
def index():
    return render_template('index.html', notes=notes.values())

@app.route('/add_note', methods=['POST'])
def add_note():
    note_text = request.form['note']
    if note_text:
        note_id = str(uuid4())
        note = {'id': note_id, 'text': note_text}
        notes[note_id] = note
        save_notes(notes)
    return redirect(url_for('index'))

@app.route('/add_note', methods=['GET'])
def get_notes():
    return jsonify({"notes": notes})

if __name__ == '__main__':
    app.run(debug=True, port=5001)