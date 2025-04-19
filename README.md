# Flask App Test Branch

This branch contains a simple Flask application with the following features:

* `/read` endpoint that takes a `name` parameter and returns a greeting
* Tests for the application endpoints
* Simple home page endpoint

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Run tests:
   ```
   python -m unittest test_app.py
   ```

## API Endpoints

- `GET /` - Returns a status check message
- `GET /read?name=YourName` - Returns a greeting with the provided name (defaults to "World")

## Development

This is a demo app for testing MCP servers.
