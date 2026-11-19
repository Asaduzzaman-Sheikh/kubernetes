from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        message = f"Hello, {name}! Welcome to our kubernetes application."
        # Process the data (e.g., save to database, send email, etc.)
        # return render_template('thank_you.html', name=name)
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)