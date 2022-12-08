# write a function and call this from different location
from flask import Flask , request , jsonify

app = Flask(__name__) # object of flask class

@app.route('/xyz', methods = ['GET' , 'POST']) # get-send thorough url, post-through body.
def test():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
    return jsonify(str(result))

if __name__ == '__main__' :
    app.run()

#----------------------------------------------------------------------------------------

# Another example of calculator :

from flask import Flask , request , jsonify

app = Flask(__name__)


@app.route('/postmanii', methods= ['POST'])
def calculation():
    if (request.method == 'POST'):
        operation = request.json["operation"]
        a = int(request.json["num1"])
        b = int(request.json["num2"])
        if(operation == 'add'):
            r = a + b
            result = "addition of " + str(a) + " and " + str(b) + " is " + str(r)
        elif (operation == 'subtract'):
            r = a - b
            result = "subtract of " + str(a) + " and " + str(b) + " is " + str(r)
        elif (operation == 'multiply'):
            r = a * b
            result = "multiply of " + str(a) + " and " + str(b) + " is " + str(r)
        elif (operation == 'division'):
            r = a / b
            result = "division of " + str(a) + " and " + str(b) + " is " + str(r)
        else :
            result = "could not found....."
        return jsonify(result)

if __name__ == '__main__' :
    app.run()