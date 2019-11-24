djangojsonstring = r"""{
  "frameworkId": 14,
  "numberOfModules": 6,
  "modules": [
    {
      "moduleName": "Django - Home",
      "moduleTopic": [
        "Django Tutorial",
        "Audience",
        "Prerequisites"
      ],
      "moduleContent": [
        [
          "Django Tutorial",
          "Django is a web development framework that assists in building and maintaining quality web applications. Django helps eliminate repetitive tasks making the development process an easy and time saving experience. This tutorial gives a complete understanding of Django."
        ],
        [
          "Audience",
          "This tutorial is designed for developers who want to learn how to develop quality web applications using the smart techniques and tools offered by Django."
        ],
        [
          "Prerequisites",
          "Before you proceed, make sure that you understand the basics of procedural and object-oriented programming: control structures, data structures and variables, classes, objects, etc."
        ]
      ]
    },
    {
      "moduleName": "Django - Basics",
      "moduleTopic": [
        "MVC Pattern",
        "DJANGO MVC - MVT Pattern"
      ],
      "moduleContent": [
        [
          "MVC Pattern",
          "When talking about applications that provides UI (web or desktop), we usually talk about MVC architecture. And as the name suggests, MVC pattern is based on three components: Model, View, and Controller. Check our MVC tutorial here to know more."
        ],
        [
          "DJANGO MVC - MVT Pattern",
          "The Model-View-Template (MVT) is slightly different from MVC. In fact the main difference between the two patterns is that Django itself takes care of the Controller part (Software Code that controls the interactions between the Model and View), leaving us with the template. The template is a HTML file mixed with Django Template Language (DTL)."
        ]
      ]
    },
    {
      "moduleName": "Django - Overview",
      "moduleTopic": [
        "Django development environment consists of installing and setting up Python, Django, and a Database System. Since Django deals with web application, it's worth mentioning that you would need a web server setup as well.",
        "Step 1 Installing Python",
        "If you're on one of the latest Linux or Mac OS X distribution, you probably already have Python installed. You can verify it by typing python command at a command prompt. If you see something like this, then Python is installed.",
        "Step 2 - Installing Django",
        "UNIX/Linux and Mac OS X Installation",
        "You can test your installation by running this command ",
        "Windows Installation",
        "Next, install Django by running the following command for which you will need administrative privileges in windows shell cmd ",
        "To test your installation, open a command prompt and type the following command ",
        "Step 3 Database Setup",
        "Step 4  Web Server"
      ],
      "moduleContent": [
        [
          "Django development environment consists of installing and setting up Python, Django, and a Database System. Since Django deals with web application, it's worth mentioning that you would need a web server setup as well.",
          ""
        ],
        [
          "Step 1 Installing Python",
          "Django is written in 100% pure Python code, so you'll need to install Python on your system. Latest Django version requires Python 2.6.5 or higher "
        ],
        [
          "If you're on one of the latest Linux or Mac OS X distribution, you probably already have Python installed. You can verify it by typing python command at a command prompt. If you see something like this, then Python is installed.",
          "$ python<br>Python 2.7.5 (default, Jun 17 2014, 18:11:42)<br>[GCC 4.8.2 20140120 (Red Hat 4.8.2-16)] on linux2<br>"
        ],
        [
          "Step 2 - Installing Django",
          "Installing Django is very easy, but the steps required for its installation depends on your operating system. Since Python is a platform-independent language, Django has one package that works everywhere regardless of your operating system."
        ],
        [
          "UNIX/Linux and Mac OS X Installation",
          "$ tar xzvf Django-x.xx.tar.gz<br>$ cd Django-x.xx<br>$ sudo python setup.py install<br>"
        ],
        [
          "You can test your installation by running this command ",
          "$ django-admin.py --version<br>"
        ],
        [
          "Windows Installation",
          "c:\\>cd c:\\Django-x.xx<br>"
        ],
        [
          "Next, install Django by running the following command for which you will need administrative privileges in windows shell cmd ",
          "c:\\Django-x.xx>python setup.py install<br>"
        ],
        [
          "To test your installation, open a command prompt and type the following command ",
          "c:\\>python -c \"import django; print(django.get_version())\"<br>"
        ],
        [
          "Step 3 Database Setup",
          "Django supports several major database engines and you can set up any of them based on your comfort.MySQL PostgreSQL SQLite3 Oracle MongoDb"
        ],
        [
          "Step 4  Web Server",
          "Django comes with a lightweight web server for developing and testing applications. This server is pre-configured to work with Django, and more importantly, it restarts whenever you modify the code.However, Django does support Apache and other popular web servers such as Lighttpd. We will discuss both the approaches in coming chapters while working with different examples."
        ]
      ]
    },
    {
      "moduleName": "Django - Environment",
      "moduleTopic": [
        "Now that we have installed Django, let's start using it. In Django, every web app you want to create is called a project; and a project is a sum of applications. An application is a set of code files relying on the MVT pattern. As example let's say we want to build a website, the website is our project and, the forum, news, contact engine are applications. This structure makes it easier to move an application between projects since every application is independent.",
        "Create a Project",
        "This will create a 'myproject' folder with the following structure ",
        "The Project Structure",
        "Setting Up Your Project",
        "Your project is set up in the subfolder myproject/settings.py. Following are some important options you might need to set ",
        "This option lets you set if your project is in debug mode or not. Debug mode lets you get more information about your project's error. Never set it to True for a live project. However, this has to be set to True if you want the Django light server to serve static files. Do it only in the development mode.",
        "Now that your project is created and configured make sure it's working ",
        "You will get something like the following on running the above code "
      ],
      "moduleContent": [
        [
          "Now that we have installed Django, let's start using it. In Django, every web app you want to create is called a project; and a project is a sum of applications. An application is a set of code files relying on the MVT pattern. As example let's say we want to build a website, the website is our project and, the forum, news, contact engine are applications. This structure makes it easier to move an application between projects since every application is independent.",
          ""
        ],
        [
          "Create a Project",
          "$ django-admin startproject myproject<br>"
        ],
        [
          "This will create a 'myproject' folder with the following structure ",
          "myproject/<br>   manage.py<br>   myproject/<br>      __init__.py<br>      settings.py<br>      urls.py<br>      wsgi.py<br>"
        ],
        [
          "The Project Structure",
          "The myproject folder is just your project container, it actually contains two elements manage.py The myproject subfolder with __init__.py,settings.py,urls.py,wsgi.py"
        ],
        [
          "Setting Up Your Project",
          ""
        ],
        [
          "Your project is set up in the subfolder myproject/settings.py. Following are some important options you might need to set ",
          "DEBUG = True<br>"
        ],
        [
          "This option lets you set if your project is in debug mode or not. Debug mode lets you get more information about your project's error. Never set it to True for a live project. However, this has to be set to True if you want the Django light server to serve static files. Do it only in the development mode.",
          "DATABASES = {<br>   'default': {<br>      'ENGINE': 'django.db.backends.sqlite3',<br>      'NAME': 'database.sql',<br>      'USER': '',<br>      'PASSWORD': '',<br>      'HOST': '',<br>      'PORT': '',<br>   }<br>}<br>"
        ],
        [
          "Now that your project is created and configured make sure it's working ",
          "$ python manage.py runserver<br>"
        ],
        [
          "You will get something like the following on running the above code ",
          "Validating models...<br><br>0 errors found<br>September 03, 2015 - 11:41:50<br>Django version 1.6.11, using settings 'myproject.settings'<br>Starting development server at http://127.0.0.1:8000/<br>Quit the server with CONTROL-C.<br>"
        ]
      ]
    },
    {
      "moduleName": "Django - Creating a Project",
      "moduleTopic": [
        "A project is a sum of many applications. Every application has an objective and can be reused into another project, like the contact form on a website can be an application, and can be reused for others. See it as a module of your project.",
        "Create an Application",
        "You just created myapp application and like project, Django create a myapp  folder with the application structure ",
        "Get the Project to Know About Your Application",
        "At this stage we have our 'myapp' application, now we need to register it with our Django project 'myproject'. To do so, update INSTALLED_APPS tuple in the settings.py file of your project (add your app name) "
      ],
      "moduleContent": [
        [
          "A project is a sum of many applications. Every application has an objective and can be reused into another project, like the contact form on a website can be an application, and can be reused for others. See it as a module of your project.",
          ""
        ],
        [
          "Create an Application",
          "$ python manage.py startapp myapp<br>"
        ],
        [
          "You just created myapp application and like project, Django create a myapp  folder with the application structure ",
          "myapp/<br>   __init__.py<br>   admin.py<br>   models.py<br>   tests.py<br>   views.py<br>"
        ],
        [
          "Get the Project to Know About Your Application",
          ""
        ],
        [
          "At this stage we have our 'myapp' application, now we need to register it with our Django project 'myproject'. To do so, update INSTALLED_APPS tuple in the settings.py file of your project (add your app name) ",
          "INSTALLED_APPS = (<br>   'django.contrib.admin',<br>   'django.contrib.auth',<br>   'django.contrib.contenttypes',<br>   'django.contrib.sessions',<br>   'django.contrib.messages',<br>   'django.contrib.staticfiles',<br>   'myapp',<br>)<br>"
        ]
      ]
    },
    {
      "moduleName": "Django - Apps Life Cycle"
    }
  ]
}"""