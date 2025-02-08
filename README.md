# Book Search App

This is a Flask application that allows users to search for books using the Libgen API.

## Setup

1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment:
    - For PowerShell:
        ```sh
        .\venv\Scripts\Activate
        ```
    - For Command Prompt:
        ```sh
        venv\Scripts\activate
        ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set the `FLASK_APP` environment variable:
    - For PowerShell:
        ```sh
        $env:FLASK_APP = "book_search_app/app.py"
        ```
    - For Command Prompt:
        ```sh
        set FLASK_APP=book_search_app/app.py
        ```

5. Run the application:
    ```sh
    flask run
    ```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. Enter a search query and click "Search".
3. View the search results and navigate through the pages.