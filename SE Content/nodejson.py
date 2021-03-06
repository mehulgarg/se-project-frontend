import json
nodejsonstring = r"""{
  "frameworkId": 16,
  "numberOfModules": 5,
  "modules": [
    {
      "moduleName": "Node.js - Home",
      "moduleTopic": [
        "Node.js Tutorial",
        "Audience",
        "Prerequisites"
      ],
      "moduleContent": [
        [
          "Node.js Tutorial",
          "Node.js is a very powerful JavaScript-based platform built on Google Chrome's JavaScript V8 Engine. It is used to develop I/O intensive web applications like video streaming sites, single-page applications, and other web applications. Node.js is open source, completely free, and used by thousands of developers around the world."
        ],
        [
          "Audience",
          "This tutorial is designed for software programmers who want to learn the basics of Node.js and its architectural concepts. This tutorial will give you enough understanding on all the necessary components of Node.js with suitable examples."
        ],
        [
          "Prerequisites",
          "Before proceeding with this tutorial, you should have a basic understanding of JavaScript. As we are going to develop web-based applications using Node.js, it will be good if you have some understanding of other web technologies such as HTML, CSS, AJAX, etc."
        ]
      ]
    },
    {
      "moduleName": "Node.js - Introduction",
      "moduleTopic": [
        "What is Node.js?",
        "Node.js also provides a rich library of various JavaScript modules which simplifies the development of web applications using Node.js to a great extent.",
        "Features of Node.js",
        "Following are some of the important features that make Node.js the first choice of software architects.",
        "Who Uses Node.js?",
        "Where to Use Node.js?",
        "Where Not to Use Node.js?"
      ],
      "moduleContent": [
        [
          "What is Node.js?",
          "Node.js is a server-side platform built on Google Chrome's JavaScript Engine (V8 Engine). Node.js was developed by Ryan Dahl in 2009 and its latest version is v0.10.36. The definition of Node.js as supplied by its official documentation is as follows Node.js is an open source, cross-platform runtime environment for developing server-side and networking applications. Node.js applications are written in JavaScript, and can be run within the Node.js runtime on OS X, Microsoft Windows, and Linux."
        ],
        [
          "Node.js also provides a rich library of various JavaScript modules which simplifies the development of web applications using Node.js to a great extent.",
          "Node.js = Runtime Environment + JavaScript Library<br>"
        ],
        [
          "Features of Node.js",
          ""
        ],
        [
          "Following are some of the important features that make Node.js the first choice of software architects.",
          "Asynchronous and Event Driven  All APIs of Node.js library are asynchronous, that is, non-blocking. It essentially means a Node.js based server never waits for an API to return data. The server moves to the next API after calling it and a notification mechanism of Events of Node.js helps the server to get a response from the previous API call.Very Fast Being built on Google Chrome's V8 JavaScript Engine, Node.js library is very fast in code execution.Single Threaded but Highly Scalable  Node.js uses a single threaded model with event looping. Event mechanism helps the server to respond in a non-blocking way and makes the server highly scalable as opposed to traditional servers which create limited threads to handle requests. Node.js uses a single threaded program and the same program can provide service to a much larger number of requests than traditional servers like Apache HTTP Server.No Buffering  Node.js applications never buffer any data. These applications simply output the data in chunks.License  Node.js is released under the MIT license."
        ],
        [
          "Who Uses Node.js?",
          "Following is the link on github wiki containing an exhaustive list of projects, application and companies which are using Node.js. This list includes eBay, General Electric, GoDaddy, Microsoft, PayPal, Uber, Wikipins, Yahoo!, and Yammer to name a few."
        ],
        [
          "Where to Use Node.js?",
          ""
        ],
        [
          "Where Not to Use Node.js?",
          "It is not advisable to use Node.js for CPU intensive applications."
        ]
      ]
    },
    {
      "moduleName": "Node.js - Environment Setup",
      "moduleTopic": [
        "Try it Option Online",
        "Local Environment Setup",
        "Text Editor",
        "The Node.js Runtime",
        "Installation on UNIX/Linux/Mac OS X, and SunOS",
        "Based on your OS architecture, download and extract the archive node-v6.3.1-osname.tar.gz into /tmp, and then finally move extracted files into /usr/local/nodejs directory. For example:",
        "Installation on Windows",
        "Verify installation: Executing a File",
        "Create a js file named main.js on your machine (Windows or Linux) having the following code.",
        "Now execute main.js file using Node.js interpreter to see the result ",
        "If everything is fine with your installation, this should produce the following result "
      ],
      "moduleContent": [
        [
          "Try it Option Online",
          "<br>You really do not need to set up your own environment to start learning Node.js. Reason is very simple, we already have set up Node.js environment online, so that you can execute all the available examples online and learn through practice. Feel free to modify any example and check the results with different options.<br>Try the following example using the Live Demo option available at the top right corner of the below sample code box (on our website) <br><br> Live Demo<br><br>/* Hello World! program in Node.js */<br>console.log(\"Hello World!\");<br><br>For most of the examples given in this tutorial, you will find a Try it option, so just make use of it and enjoy your learning.<br>"
        ],
        [
          "Local Environment Setup",
          "If you are still willing to set up your environment for Node.js, you need the following two softwares available on your computer, (a) Text Editor and (b) The Node.js binary installables."
        ],
        [
          "Text Editor",
          "This will be used to type your program. Examples of few editors include Windows Notepad, OS Edit command, Brief, Epsilon, EMACS, and vim or vi.Name and version of text editor can vary on different operating systems. For example, Notepad will be used on Windows, and vim or vi can be used on windows as well as Linux or UNIX.The files you create with your editor are called source files and contain program source code. The source files for Node.js programs are typically named with the extension \".js\".Before starting your programming, make sure you have one text editor in place and you have enough experience to write a computer program, save it in a file, and finally execute it."
        ],
        [
          "The Node.js Runtime",
          "The source code written in source file is simply javascript. The Node.js interpreter will be used to interpret and execute your javascript code.Node.js distribution comes as a binary installable for SunOS , Linux, Mac OS X, and Windows operating systems with the 32-bit (386) and 64-bit (amd64) x86 processor architectures. Following section guides you on how to install Node.js binary distribution on various OS."
        ],
        [
          "Installation on UNIX/Linux/Mac OS X, and SunOS",
          ""
        ],
        [
          "Based on your OS architecture, download and extract the archive node-v6.3.1-osname.tar.gz into /tmp, and then finally move extracted files into /usr/local/nodejs directory. For example:",
          "$ cd /tmp<br>$ wget http://nodejs.org/dist/v6.3.1/node-v6.3.1-linux-x64.tar.gz<br>$ tar xvfz node-v6.3.1-linux-x64.tar.gz<br>$ mkdir -p /usr/local/nodejs<br>$ mv node-v6.3.1-linux-x64/* /usr/local/nodejs<br>"
        ],
        [
          "Installation on Windows",
          "Use the MSI file and follow the prompts to install the Node.js. By default, the installer uses the Node.js distribution in C:\\Program Files<br>odejs. The installer should set the C:\\Program Files<br>odejs\\bin directory in window's PATH environment variable. Restart any open command prompts for the change to take effect."
        ],
        [
          "Verify installation: Executing a File",
          ""
        ],
        [
          "Create a js file named main.js on your machine (Windows or Linux) having the following code.",
          "/* Hello, World! program in node.js */<br>console.log(\"Hello, World!\")<br>"
        ],
        [
          "Now execute main.js file using Node.js interpreter to see the result ",
          "$ node main.js<br>"
        ],
        [
          "If everything is fine with your installation, this should produce the following result ",
          "Hello, World!<br>"
        ]
      ]
    },
    {
      "moduleName": "Node.js - First Application",
      "moduleTopic": [
        "Before creating an actual \"Hello, World!\" application using Node.js, let us see the components of a Node.js application. A Node.js application consists of the following three important components ",
        "Creating Node.js Application",
        "Step 1 - Import Required Module",
        "Step 2 - Create Server",
        "Step 3 - Testing Request & Response",
        "Now execute the main.js to start the server as follows ",
        "Verify the Output. Server has started.",
        "Make a Request to the Node.js Server"
      ],
      "moduleContent": [
        [
          "Before creating an actual \"Hello, World!\" application using Node.js, let us see the components of a Node.js application. A Node.js application consists of the following three important components ",
          "Import required modules  We use the require directive to load Node.js modules.Create server  A server which will listen to client's requests similar to Apache HTTP Server.Read request and return response  The server created in an earlier step will read the HTTP request made by the client which can be a browser or a console and return the response."
        ],
        [
          "Creating Node.js Application",
          ""
        ],
        [
          "Step 1 - Import Required Module",
          "var http = require(\"http\");<br>"
        ],
        [
          "Step 2 - Create Server",
          "http.createServer(function (request, response) {<br>   // Send the HTTP header <br>   // HTTP Status: 200 : OK<br>   // Content Type: text/plain<br>   response.writeHead(200, {'Content-Type': 'text/plain'});<br>   <br>   // Send the response body as \"Hello World\"<br>   response.end('Hello World<br>');<br>}).listen(8081);<br><br>// Console will print the message<br>console.log('Server running at http://127.0.0.1:8081/');<br>"
        ],
        [
          "Step 3 - Testing Request & Response",
          "var http = require(\"http\");<br><br>http.createServer(function (request, response) {<br>   // Send the HTTP header <br>   // HTTP Status: 200 : OK<br>   // Content Type: text/plain<br>   response.writeHead(200, {'Content-Type': 'text/plain'});<br>   <br>   // Send the response body as \"Hello World\"<br>   response.end('Hello World<br>');<br>}).listen(8081);<br><br>// Console will print the message<br>console.log('Server running at http://127.0.0.1:8081/');<br>"
        ],
        [
          "Now execute the main.js to start the server as follows ",
          "$ node main.js<br>"
        ],
        [
          "Verify the Output. Server has started.",
          "Server running at http://127.0.0.1:8081/<br>"
        ],
        [
          "Make a Request to the Node.js Server",
          "Open http://127.0.0.1:8081/ in any browser and observe the following result."
        ]
      ]
    },
    {
      "moduleName": "Node.js - REPL Terminal",
      "moduleTopic": [
        "REPL stands for Read Eval Print Loop and it represents a computer environment like a Windows console or Unix/Linux shell where a command is entered and the system responds with an output in an interactive mode. Node.js or Node comes bundled with a REPL environment. It performs the following tasks ",
        "Online REPL Terminal",
        "Starting REPL",
        "Simple Expression",
        "Use Variables",
        "Multiline Expression",
        "Underscore Variable",
        "Stopping REPL"
      ],
      "moduleContent": [
        [
          "REPL stands for Read Eval Print Loop and it represents a computer environment like a Windows console or Unix/Linux shell where a command is entered and the system responds with an output in an interactive mode. Node.js or Node comes bundled with a REPL environment. It performs the following tasks ",
          "Read  Reads user's input, parses the input into JavaScript data-structure, and stores in memory.Eval  Takes and evaluates the data structure.Print  Prints the result.Loop  Loops the above command until the user presses ctrl-c twice."
        ],
        [
          "Online REPL Terminal",
          "To simplify your learning, we have set up an easy to use Node.js REPL environment online, where you can practice Node.js syntax  Launch Node.js REPL Terminal "
        ],
        [
          "Starting REPL",
          "$ node<br>"
        ],
        [
          "Simple Expression",
          "$ node<br>> 1 + 3<br>4<br>> 1 + ( 2 * 3 ) - 4<br>3<br>><br>"
        ],
        [
          "Use Variables",
          "$ node<br>> x = 10<br>10<br>> var y = 10<br>undefined<br>> x + y<br>20<br>> console.log(\"Hello World\")<br>Hello World<br>undefined<br>"
        ],
        [
          "Multiline Expression",
          "$ node<br>> var x = 0<br>undefined<br>> do {<br>   ... x++;<br>   ... console.log(\"x: \" + x);<br>   ... } <br>while ( x < 5 );<br>x: 1<br>x: 2<br>x: 3<br>x: 4<br>x: 5<br>undefined<br>><br>"
        ],
        [
          "Underscore Variable",
          "$ node<br>> var x = 10<br>undefined<br>> var y = 20<br>undefined<br>> x + y<br>30<br>> var sum = _<br>undefined<br>> console.log(sum)<br>30<br>undefined<br>><br>"
        ],
        [
          "Stopping REPL",
          "$ node<br>><br>(^C again to quit)<br>><br>"
        ]
      ]
    }
  ]
}"""
print(json.loads(nodejsonstring))