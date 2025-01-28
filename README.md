# Flask SQL Query Correction and Generation API

This project is a Flask-based API that integrates Google Gemini AI to analyze, correct, and generate SQL queries. Users can send SQL queries via a POST request, and the system will either return a syntactically corrected version or generate a relevant query based on the given problem statement.

## Features
- Supports GET and POST requests
- Renders an HTML template for the homepage
- Accepts JSON input containing an SQL query
- Uses Google Gemini AI to correct SQL syntax and generate relevant queries
- Provides a user-friendly HTML interface for inputting SQL queries
- Enhances SQL query structure and optimizes its correctness and intent

## Prerequisites
Ensure you have the following installed:
- Python 3.9+
- Flask
- `google-generativeai` package
- `python-dotenv` package

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/sanjay14073/sqlQueryCorrectorGenerator.git
   cd sql-query-corrector
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Google Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage
### Running the Server
Start the Flask application using:
```sh
python app.py
```

The application will be accessible at `http://0.0.0.0:5000`.

### API Endpoints
#### `GET /`
Renders the `index.html` page, which provides a user interface for entering SQL queries.

#### `POST /`
Accepts a JSON request with the following format:
```json
{
  "sql_query": "SELECT * FROM users WHERE age > 25"
}
```
Response:
```json
{
  "message": "SELECT * FROM users WHERE age > 25;"
}
```
If the provided query contains syntax errors, the API corrects them. If the query is incomplete or unclear, the API generates an improved version that better matches the problem statement.

## Project Structure
```
.
├── app.py
├── genresponse.py
├── templates/
│   ├── index.html
├── static/
│   ├── styles.css
│   ├── script.js
├── .env
├── requirements.txt
└── README.md
```

## Author
Sanjay M - [Github](https://github.com/sanjay14073)


