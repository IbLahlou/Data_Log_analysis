from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Set up logging configuration
logging.basicConfig(filename='../spool/log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Check if the file is present in the request
        if 'log_file' not in request.files:
            error_message = "Error: No file provided."
            logging.error(error_message)
            return render_template('index.html', error_message=error_message)

        file = request.files['log_file']

        # Check if the file name is empty
        if file.filename == '':
            error_message = "Error: Empty file name."
            logging.error(error_message)
            return render_template('index.html', error_message=error_message)

        # Read and log the content of the uploaded file
        log_content = file.read().decode('utf-8')
        logging.info("Importing logs from the uploaded file.")
        logging.info(log_content)

        return render_template('index.html', logs=log_content)

    except Exception as e:
        error_message = f"Error: {str(e)}"
        logging.error(error_message)
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
