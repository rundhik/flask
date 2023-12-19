# Tutorial Flask

### Prasyarat Pustaka
- Flask 3.+

## Basic Simple App

Masuk ke dalam environment Python.

        > venv\Scripts\activate
        (venv) >

Install Flask.

        (venv) > pip install Flask

Buat file ```app.py```.

        from flask import Flask

        app = Flask(__name__)

        @app.route('/')
        def index():
            return '''
            <h1>Tutorial Flask</h1>
            <p>Selamat datang di tutorial aplikasi web menggunakan Flask</p>
            '''

        if __name__ == '__main__':
            app.run()

Jalankan file ```app.py```.

        (venv) > python app.py
        * Serving Flask app 'app'
        * Debug mode: off
        WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
        * Running on http://127.0.0.1:5000
        Press CTRL+C to quit

Akses ```http://127.0.0.1:5000``` melalui browser.
