from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to print a string
@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'{param}'

# Route to count numbers
@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param)) + '\n'
    return numbers

# Route to perform math operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
