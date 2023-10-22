web framework
web_flask/0-hello_route.py


#!/usr/bin/python3

""" Starts a Flash Web Application """

from flask import Flask

app = Flask(__name__)



@app.route('/', strict_slashes=False)

def hello_hbnb():

    """ Prints a Message when / is called """

    return 'Hello HBNB!'


if __name__ == "__main__":

    """ Main Function """

    app.run(host='0.0.0.0', port=5000)


web_flask/1-hbnb_route.py


#!/usr/bin/python3

""" Starts a Flash Web Application HBNB"""

from flask import Flask

app = Flask(__name__)



@app.route('/', strict_slashes=False)

def hello_hbnb():

    """ Prints a Message when / is called """

    return 'Hello HBNB!'



@app.route('/hbnb', strict_slashes=False)

def hbnb():

    """ Prints a Message when /hbnb is called """

    return 'HBNB'


if __name__ == "__main__":

    """ Main Function """

    app.run(host='0.0.0.0', port=5000)


web_flask/2-c_route.py


#!/usr/bin/python3

""" Starts a Flash Web Application C is FUN"""

from flask import Flask

app = Flask(__name__)



@app.route('/', strict_slashes=False)

def hello_hbnb():

    """ Prints a Message when / is called """

    return 'Hello HBNB!'



@app.route('/hbnb', strict_slashes=False)

def hbnb():

    """ Prints a Message when /hbnb is called """

    return 'HBNB'



@app.route('/c/<text>', strict_slashes=False)

def c_is_fun(text):

    """ Prints a Message when /c is called """

    return "C " + text.replace('_', ' ')


if __name__ == "__main__":

    """ Main Function """

    app.run(host='0.0.0.0', port=5000)


web_flask/3-python_route.py


#!/usr/bin/python3

"""

starts a Flask web application

"""


from flask import Flask

app = Flask(__name__)



@app.route('/', strict_slashes=False)

def index():

    """returns Hello HBNB!"""

    return 'Hello HBNB!'



@app.route('/hbnb', strict_slashes=False)

def hbnb():

    """returns HBNB"""

    return 'HBNB'



@app.route('/c/<text>', strict_slashes=False)

def cisfun(text):

    """display “C ” followed by the value of the text variable"""

    return 'C ' + text.replace('_', ' ')



@app.route('/python', strict_slashes=False)

@app.route('/python/<text>', strict_slashes=False)

def pythoniscool(text='is cool'):

    """display “Python ”, followed by the value of the text variable"""

    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':

    app.run(host='0.0.0.0', port='5000')


web_flask/4-number_route.py


#!/usr/bin/python3

"""

starts a Flask web application

"""


from flask import Flask

app = Flask(__name__)



@app.route('/', strict_slashes=False)

def index():

    """returns Hello HBNB!"""

    return 'Hello HBNB!'



@app.route('/hbnb', strict_slashes=False)

def hbnb():

    """returns HBNB"""

    return 'HBNB'



@app.route('/c/<text>', strict_slashes=False)

def cisfun(text):

    """display “C ” followed by the value of the text variable"""

    return 'C ' + text.replace('_', ' ')



@app.route('/python', strict_slashes=False)

@app.route('/python/<text>', strict_slashes=False)

def pythoniscool(text='is cool'):

    """display “Python ”, followed by the value of the text variable"""

    return 'Python ' + text.replace('_', ' ')



@app.route('/number/<int:n>', strict_slashes=False)

def imanumber(n):

    """display “n is a number” only if n is an integer"""

    return "{:d} is a number".format(n)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port='5000')


web_flask/5-number_template.py


#!/usr/bin/python3

"""

starts a Flask web application

"""


from flask import Flask, render_template

app = Flask(__name__)



@app.route('/', strict_slashes=False)

def index():

    """returns Hello HBNB!"""

    return 'Hello HBNB!'



@app.route('/hbnb', strict_slashes=False)

def hbnb():

    """returns HBNB"""

    return 'HBNB'



@app.route('/c/<text>', strict_slashes=False)

def cisfun(text):

    """display “C ” followed by the value of the text variable"""

    return 'C ' + text.replace('_', ' ')



@app.route('/python', strict_slashes=False)

@app.route('/python/<text>', strict_slashes=False)

def pythoniscool(text='is cool'):

    """display “Python ”, followed by the value of the text variable"""

    return 'Python ' + text.replace('_', ' ')



@app.route('/number/<int:n>', strict_slashes=False)

def imanumber(n):

    """display “n is a number” only if n is an integer"""

    return "{:d} is a number".format(n)



@app.route('/number_template/<int:n>', strict_slashes=False)

def numbersandtemplates(n):

    """display a HTML page only if n is an integer"""

    return render_template('5-number.html', n=n)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port='5000')
