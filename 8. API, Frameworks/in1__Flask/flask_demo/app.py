from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

'''
An Application Programming Interface is a way for two or more computer programs to communicate with each other.
It is a type of software interface, offering a service to other pieces of software.
A document or standard that describes how to build or use such a connection or interface is called an API specification.

POSTMAN is trying to invoke our methods. Acting as an API tester.

Postman is an API client that makes it easy for developers to create, share, test and document APIs. 
This is done by allowing users to create and save simple and complex HTTP/s requests, as well as read their responses.

Note: Whatever function will be there under @app.route, only that function will be called through http request.
(following the architecture, y'know!)
'''


@app.route('/', methods=['GET', 'POST'])  # To render Homepage
def home_page():
    return render_template('index.html')


@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if (operation == 'add'):
            r = num1 + num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html', result=result)


@app.route('/post1', methods=['POST'])  # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if operation == 'add':
            r = num1 + num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'subtract':
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'multiply':
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'divide':
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)


@app.route('/post2', methods=['POST'])  # for calling the API from Postman/SOAPUI
def return_mail():
    if request.method == 'POST':
        name = request.json['Name']
        birth_year = request.json['Birth Year']
        domain = request.json['Domain']
        return jsonify(name + str(birth_year) + '@' + domain)


@app.route('/through_browser_itself')
def url_test():
    test1 = request.args.get('val1')
    test2 = request.args.get('val2')

    return f'''<h1>The resul  is : {test1 + test2}</h1>'''


# __main__ Class is super class of all the classes.
# main method is required so that any type of constructor or object can be called in python.
if __name__ == '__main__':
    app.run(debug=True)
