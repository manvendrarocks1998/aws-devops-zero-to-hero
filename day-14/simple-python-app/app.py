from flask import Flask, render_template_string

app = Flask(__name__)

# Simple HTML template with Bootstrap styling
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Flask Showcase</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container py-5">
        <div class="card shadow-lg">
            <div class="card-body text-center">
                <h1 class="display-4 text-primary">🚀 Welcome to My Flask App!</h1>
                <p class="lead">This app is running inside a Docker container on AWS EC2.</p>
                <hr>
                <p>It’s a simple demo, but it shows how cloud + containers + Python can deliver web apps quickly.</p>
                <a href="https://www.linkedin.com" class="btn btn-success btn-lg">Connect with me on LinkedIn</a>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

