from flask import Flask

app = Flask(__name__)

@app.route('/run_my_python_code')
def run_my_python_code():
    # Your Python code here
    result = "Hello from Python!"
    return result

if __name__ == '__main__':
    app.run(debug=True)
