from flask import Flask

# Create the Flask application
app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My First Flask App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding: 50px;
            }

            .container {
                background: white;
                width: 500px;
                margin: auto;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px gray;
            }

            h1 {
                color: #2c3e50;
            }

            a {
                text-decoration: none;
                color: white;
                background: #3498db;
                padding: 10px 20px;
                border-radius: 5px;
                margin: 5px;
                display: inline-block;
            }

            a:hover {
                background: #2980b9;
            }
        </style>
    </head>

    <body>

        <div class="container">
            <h1>🚀 Welcome to My First Flask Web App</h1>

            <p>
                This entire website is written inside a single Python file!
            </p>

            <hr>

            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>

        </div>

    </body>
    </html>
    """


# About Page
@app.route("/about")
def about():
    return """
    <h1>About</h1>

    <p>I am learning Flask.</p>

    <a href="/">Go Home</a>
    """


# Contact Page
@app.route("/contact")
def contact():
    return """
    <h1>Contact</h1>

    <p>Email: fidahussain@email.com</p>

    <a href="/">Go Home</a>
    """


# Start the server
if __name__ == "__main__":
    app.run(debug=True)