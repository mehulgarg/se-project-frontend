flaskjsonstring = r"""{
  "frameworkId": 12,
  "numberOfModules": 5,
  "modules": [
    {
      "moduleName": "Flask - Home",
      "moduleTopic": [
        "Flask Tutorial",
        "Audience",
        "Prerequisites"
      ],
      "moduleContent": [
        [
          "Flask Tutorial",
          "Flask is a web application framework written in Python. Armin Ronacher, who leads an international group of Python enthusiasts named Pocco, develops it. Flask is based on Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects."
        ],
        [
          "Audience",
          "This tutorial has been prepared for anyone who has a basic knowledge of Python and has an urge to develop websites. After completing this tutorial, you will find yourself at a moderate level of expertise in developing websites using Flask."
        ],
        [
          "Prerequisites",
          "Before you start proceeding with this tutorial, we are assuming that you have hands-on experience on HTML and Python. If you are not well aware of these concepts, then we will suggest you to go through our short tutorials on HTML and Python."
        ]
      ]
    },
    {
      "moduleName": "Flask - Overview",
      "moduleTopic": [
        "What is Web Framework?",
        "What is Flask?",
        "WSGI",
        "Werkzeug",
        "Jinja2"
      ],
      "moduleContent": [
        [
          "What is Web Framework?",
          "Web Application Framework or simply Web Framework represents a collection of libraries and modules that enables a web application developer to write applications without having to bother about low-level details such as protocols, thread management etc."
        ],
        [
          "What is Flask?",
          "Flask is a web application framework written in Python. It is developed by Armin Ronacher, who leads an international group of Python enthusiasts named Pocco. Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects."
        ],
        [
          "WSGI",
          "Web Server Gateway Interface (WSGI) has been adopted as a standard for Python web application development. WSGI is a specification for a universal interface between the web server and the web applications."
        ],
        [
          "Werkzeug",
          "It is a WSGI toolkit, which implements requests, response objects, and other utility functions. This enables building a web framework on top of it. The Flask framework uses Werkzeug as one of its bases."
        ],
        [
          "Jinja2",
          "Jinja2 is a popular templating engine for Python. A web templating system combines a template with a certain data source to render dynamic web pages."
        ]
      ]
    },
    {
      "moduleName": "Flask - Environment",
      "moduleTopic": [
        "Prerequisite",
        "Install virtualenv for development environment",
        "The following command installs virtualenv",
        "This command needs administrator privileges. Add sudo before pip on Linux/Mac OS. If you are on Windows, log in as Administrator. On Ubuntu virtualenv may be installed using its package manager.",
        "Once installed, new virtual environment is created in a folder.",
        "To activate corresponding environment, on Linux/OS X, use the following ",
        "On Windows, following can be used",
        "We are now ready to install Flask in this environment."
      ],
      "moduleContent": [
        [
          "Prerequisite",
          "Python 2.6 or higher is usually required for installation of Flask. Although Flask and its dependencies work well with Python 3 (Python 3.3 onwards), many Flask extensions do not support it properly. Hence, it is recommended that Flask should be installed on Python 2.7."
        ],
        [
          "Install virtualenv for development environment",
          "virtualenv is a virtual Python environment builder. It helps a user to create multiple Python environments side-by-side. Thereby, it can avoid compatibility issues between the different versions of the libraries."
        ],
        [
          "The following command installs virtualenv",
          "pip install virtualenv"
        ],
        [
          "This command needs administrator privileges. Add sudo before pip on Linux/Mac OS. If you are on Windows, log in as Administrator. On Ubuntu virtualenv may be installed using its package manager.",
          "Sudo apt-get install virtualenv"
        ],
        [
          "Once installed, new virtual environment is created in a folder.",
          "mkdir newproj<br>cd newproj<br>virtualenv venv"
        ],
        [
          "To activate corresponding environment, on Linux/OS X, use the following ",
          "venv/bin/activate"
        ],
        [
          "On Windows, following can be used",
          "venv\\scripts\\activate"
        ],
        [
          "We are now ready to install Flask in this environment.",
          "pip install Flask"
        ]
      ]
    },
    {
      "moduleName": "Flask - Application",
      "moduleTopic": [
        "In order to test Flask installation, type the following code in the editor as Hello.py",
        "Importing flask module in the project is mandatory. An object of Flask class is our WSGI application.",
        "Flask constructor takes the name of current module (__name__) as argument.",
        "The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.",
        "Finally the run() method of Flask class runs the application on the local development server.",
        "The above given Python script is executed from Python shell.",
        "A message in Python shell informs you that",
        "The Debug mode is enabled by setting the debug property of the application object to True before running or passing the debug parameter to the run() method."
      ],
      "moduleContent": [
        [
          "In order to test Flask installation, type the following code in the editor as Hello.py",
          "from flask import Flask<br>app = Flask(__name__)<br><br>@app.route('/')<br>def hello_world():<br>   return 'Hello World<br><br>if __name__ == '__main__':<br>   app.run()"
        ],
        [
          "Importing flask module in the project is mandatory. An object of Flask class is our WSGI application.",
          ""
        ],
        [
          "Flask constructor takes the name of current module (__name__) as argument.",
          ""
        ],
        [
          "The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.",
          "app.route(rule, options)"
        ],
        [
          "Finally the run() method of Flask class runs the application on the local development server.",
          "app.run(host, port, debug, options)"
        ],
        [
          "The above given Python script is executed from Python shell.",
          "Python Hello.py"
        ],
        [
          "A message in Python shell informs you that",
          "* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)"
        ],
        [
          "The Debug mode is enabled by setting the debug property of the application object to True before running or passing the debug parameter to the run() method.",
          "app.debug = True<br>app.run()<br>app.run(debug = True)"
        ]
      ]
    },
    {
      "moduleName": "Flask - Routing",
      "moduleTopic": [
        "Modern web frameworks use the routing technique to help a user remember application URLs. It is useful to access the desired page directly without having to navigate from the home page.",
        "The route() decorator in Flask is used to bind URL to a function. For example ",
        "Here, URL '/hello' rule is bound to the hello_world() function. As a result, if a user visits http://localhost:5000/hello URL, the output of the hello_world() function will be rendered in the browser.",
        "The add_url_rule() function of an application object is also available to bind a URL with a function as in the above example, route() is used.",
        "A decorators purpose is also served by the following representation "
      ],
      "moduleContent": [
        [
          "Modern web frameworks use the routing technique to help a user remember application URLs. It is useful to access the desired page directly without having to navigate from the home page.",
          ""
        ],
        [
          "The route() decorator in Flask is used to bind URL to a function. For example ",
          "@app.route('/hello')<br>def hello_world():<br>   return 'hello world'"
        ],
        [
          "Here, URL '/hello' rule is bound to the hello_world() function. As a result, if a user visits http://localhost:5000/hello URL, the output of the hello_world() function will be rendered in the browser.",
          ""
        ],
        [
          "The add_url_rule() function of an application object is also available to bind a URL with a function as in the above example, route() is used.",
          ""
        ],
        [
          "A decorators purpose is also served by the following representation ",
          "def hello_world():<br>   return 'hello world'<br>app.add_url_rule('/','hello','hello_world')"
        ]
      ]
    }
  ]
}"""