#!/bin/bash

# Create project directory
mkdir my_flask_app
cd my_flask_app


# Create requirements.txt
echo "Flask==2.1.0" > requirements.txt

# Create app.py
cat > app.py << "END"
from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Set up logging configuration
logging.basicConfig(filename='app_logs.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # Log user input
    log_message = f"User submitted form with - Username: {username}, Password: {password}, Confirm Password: {confirm_password}"
    logging.info(log_message)

    # Check for errors in user input
    if password != confirm_password:
        error_message = "Error: Passwords do not match."
        logging.error(error_message)
        return render_template('index.html', error_message=error_message)

    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
END

# Create template directory
mkdir template

# Create index.html in the template directory
cat > template/index.html << "END"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form</title>
</head>
<body>
    <h1>Form</h1>
    {% if error_message %}
        <p style="color: red;">{{ error_message }}</p>
    {% endif %}
    <form action="/submit" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>

        <label for="confirm_password">Confirm Password:</label>
        <input type="password" id="confirm_password" name="confirm_password" required><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
END

# Create template.sh
cat >  template.sh << "END"
#!/bin/bash

# Install Python3.9 dependencies
pip install -r requirements.txt

# Run the Python3.9 application
python3.9 app.py
END

# Provide execution permissions to template.sh
chmod +x template.sh

# Inform the user about the completion of the script
echo "Project structure and files created successfully. Navigate to 'my_flask_app' directory to run the application."
