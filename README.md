
# Simple Note App

A simple Flask application to add and store notes in a JSON file.

## Prerequisites

- Python 3.x
- Virtualenv

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/simple-note-app.git
   cd simple-note-app
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install flask
   ```

4. Initialize the `notes.json` file:

   ```bash
   echo '{"notes": {}}' > notes.json
   ```

## Running the Application

1. Ensure your virtual environment is activated:

   ```bash
   source venv/bin/activate
   ```

2. Run the Flask application:

   ```bash
   flask run --port=5001
   ```

3. Open your browser and navigate to `http://127.0.0.1:5001`.

## Usage

- Add a note: Enter your note in the input field and click "Add Note".
- View notes: Notes will be displayed below the input field.
- Get notes in JSON format: Access the `/add_note` endpoint to get all notes in JSON format.

## Project Structure

```
simple-note-app/
├── app.py
├── notes.json
├── templates/
│   └── index.html
├── static/
│   └── styles.css
└── venv/
```

## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.
