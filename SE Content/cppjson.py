cppjsonstring = r"""{
  "frameworkId": "17",
  "numberOfModules": 5,
  "modules": [
    {
      "moduleName": "C++ Home",
      "moduleTopic": [
        "C++ is a middle-level programming language developed by Bjarne Stroustrup starting in 1979 at Bell Labs. C++ runs on a variety of platforms, such as Windows, Mac OS, and the various versions of UNIX. This C++ tutorial adopts a simple and practical approach to describe the concepts of C++ for beginners to advanded software engineers.",
        "Why to Learn C++",
        "C++ is a MUST for students and working professionals to become a great Software Engineer. I will list down some of the key advantages of learning C++:",
        "Hello World using C++",
        "There are many C++ compilers available which you can use to compile and run above mentioned program:",
        "Applications of C++ Programming",
        "Audience",
        "Prerequisites"
      ],
      "moduleContent": [
        [
          "C++ is a middle-level programming language developed by Bjarne Stroustrup starting in 1979 at Bell Labs. C++ runs on a variety of platforms, such as Windows, Mac OS, and the various versions of UNIX. This C++ tutorial adopts a simple and practical approach to describe the concepts of C++ for beginners to advanded software engineers.",
          ""
        ],
        [
          "Why to Learn C++",
          ""
        ],
        [
          "C++ is a MUST for students and working professionals to become a great Software Engineer. I will list down some of the key advantages of learning C++:",
          "You get a chance to work at a low level which gives you lot of control in terms of memory management, better performance and finally a robust software development.C++ programming gives you a clear understanding about Object Oriented Programming.C++ is one of the every green programming languages and loved by millions of software developers.C++ is the most widely used programming languages in application and system programming. C++ really teaches you the difference between compiler, linker and loader, different data types, storage classes, variable types their scopes etc."
        ],
        [
          "Hello World using C++",
          "#include <iostream><br>using namespace std;<br><br>// main() is where program execution begins.<br>int main() {<br>   cout << \"Hello World\"; // prints Hello World<br>   return 0;<br>}<br>"
        ],
        [
          "There are many C++ compilers available which you can use to compile and run above mentioned program:",
          "Apple C++.Xcode,Bloodshed Dev-C++,Clang C++,Cygwin (GNU C++),Mentor Graphics,MINGW - Minimalist GNU for Windows"
        ],
        [
          "Applications of C++ Programming",
          "Application Software Development,Programming Languages Development,Computation Programming,Games Development,Embedded System"
        ],
        [
          "Audience",
          "This C++ tutorial has been prepared for the beginners to help them understand the basic to advanced concepts related to C++."
        ],
        [
          "Prerequisites",
          "Before you start practicing with various types of examples given in this C++ tutorial,we are making an assumption that you are already aware of the basics of computer program and computer programming language."
        ]
      ]
    },
    {
      "moduleName": "C++ Overview",
      "moduleTopic": [
        "Object-Oriented Programming",
        "C++ fully supports object-oriented programming, including the four pillars of object-oriented development ",
        "Standard Libraries",
        "The ANSI Standard",
        "Learning C++",
        "Use of C++"
      ],
      "moduleContent": [
        [
          "Object-Oriented Programming",
          ""
        ],
        [
          "C++ fully supports object-oriented programming, including the four pillars of object-oriented development ",
          "Encapsulation,Data hiding,Inheritance,Polymorphism"
        ],
        [
          "Standard Libraries",
          "The core language giving all the building blocks including variables, data types and literals, etc.The C++ Standard Library giving a rich set of functions manipulating files, strings, etc.The Standard Template Library (STL) giving a rich set of methods manipulating data structures, etc."
        ],
        [
          "The ANSI Standard",
          "The ANSI standard is an attempt to ensure that C++ is portable; that code you write for Microsoft's compiler will compile without errors, using a compiler on a Mac, UNIX, a Windows box, or an Alpha.The ANSI standard has been stable for a while, and all the major C++ compiler manufacturers support the ANSI standard."
        ],
        [
          "Learning C++",
          "The most important thing while learning C++ is to focus on concepts.The purpose of learning a programming language is to become a better programmer; that is, to become more effective at designing and implementing new systems and at maintaining old ones.C++ supports a variety of programming styles. You can write in the style of Fortran, C, Smalltalk, etc., in any language. Each style can achieve its aims effectively while maintaining runtime and space efficiency."
        ],
        [
          "Use of C++",
          "C++ is used by hundreds of thousands of programmers in essentially every application domain.C++ is being highly used to write device drivers and other software that rely on direct manipulation of hardware under realtime constraints.C++ is widely used for teaching and research because it is clean enough for successful teaching of basic concepts.Anyone who has used either an Apple Macintosh or a PC running Windows has indirectly used C++ because the primary user interfaces of these systems are written in C++."
        ]
      ]
    },
    {
      "moduleName": "C++ Environment Setup",
      "moduleTopic": [
        "Local Environment Setup",
        "Text Editor",
        "C++ Compiler",
        "Installing GNU C/C++ Compiler",
        "UNIX/Linux Installation",
        "If you have installed GCC, then it should print a message such as the following ",
        "Mac OS X Installation",
        "Windows Installation"
      ],
      "moduleContent": [
        [
          "Local Environment Setup",
          "If you are still willing to set up your environment for C++, you need to have the following two softwares on your computer."
        ],
        [
          "Text Editor",
          "This will be used to type your program. Examples of few editors include Windows Notepad, OS Edit command, Brief, Epsilon, EMACS, and vim or vi.Name and version of text editor can vary on different operating systems. For example, Notepad will be used on Windows and vim or vi can be used on windows  as well as Linux, or UNIX.The files you create with your editor are called source files and for C++ they typically are named with the extension .cpp, .cp, or .c.A text editor should be in place to start your C++ programming."
        ],
        [
          "C++ Compiler",
          "This is an actual C++ compiler, which will be used to compile your source code into final executable program.Most C++ compilers don't care what extension you give to your source code, but if you don't specify otherwise, many will use .cpp by default.Most frequently used and free available compiler is GNU C/C++ compiler, otherwise you can have compilers either from HP or Solaris if you have the respective Operating Systems."
        ],
        [
          "Installing GNU C/C++ Compiler",
          ""
        ],
        [
          "UNIX/Linux Installation",
          "$ g++ -v<br>"
        ],
        [
          "If you have installed GCC, then it should print a message such as the following ",
          "Using built-in specs.<br>Target: i386-redhat-linux<br>Configured with: ../configure --prefix=/usr .......<br>Thread model: posix<br>gcc version 4.1.2 20080704 (Red Hat 4.1.2-46)<br>"
        ],
        [
          "Mac OS X Installation",
          "If you use Mac OS X, the easiest way to obtain GCC is to download the Xcode development environment from Apple's website and follow the simple installation instructions.Xcode is currently available at developer.apple.com/technologies/tools/."
        ],
        [
          "Windows Installation",
          "To install GCC at Windows you need to install MinGW. To install MinGW, go to the MinGW homepage, www.mingw.org, and follow the link to the MinGW download page. Download the latest version of the MinGW installation program which should be named MinGW-<version>.exe.While installing MinGW, at a minimum, you must install gcc-core, gcc-g++, binutils, and the MinGW runtime, but you may wish to install more.Add the bin subdirectory of your MinGW installation to your PATH environment variable so that you can specify these tools on the command line by their simple names.When the installation is complete, you will be able to run gcc, g++, ar, ranlib, dlltool, and several other GNU tools from the Windows command line."
        ]
      ]
    },
    {
      "moduleName": "C++ Basic Syntax",
      "moduleTopic": [
        "When we consider a C++ program, it can be defined as a collection of objects that communicate via invoking each other's methods. Let us now briefly look into what a class, object, methods, and instant variables mean.",
        "C++ Program Structure",
        "Compile and Execute C++ Program",
        "Semicolons and Blocks in C++",
        "For example, following are three different statements ",
        "A block is a set of logically connected statements that are surrounded by opening and closing braces. For example ",
        "C++ does not recognize the end of the line as a terminator. For this reason, it does not matter where you put a statement in a line. For example ",
        "is the same as",
        "C++ Identifiers",
        "Here are some examples of acceptable identifiers ",
        "Whitespace in C++",
        "Statement 1",
        "Statement 2"
      ],
      "moduleContent": [
        [
          "When we consider a C++ program, it can be defined as a collection of objects that communicate via invoking each other's methods. Let us now briefly look into what a class, object, methods, and instant variables mean.",
          "Object, Class, Methods, Instance Variables"
        ],
        [
          "C++ Program Structure",
          "#include <iostream><br>using namespace std;<br><br>// main() is where program execution begins.<br>int main() {<br>   cout << \"Hello World\"; // prints Hello World<br>   return 0;<br>}<br>"
        ],
        [
          "Compile and Execute C++ Program",
          "Open a text editor and add the code as above.Save the file as: hello.cpp<br>Open a command prompt and go to the directory where you saved the file.<br>Type g++ hello.cpp and press enter to compile your code. If there are no errors in your code the command prompt will take you to the next line and would generate a.out executable file.<br>Now, type a.out to run your program.<br>You will be able to see  Hello World  printed on the window."
        ],
        [
          "Semicolons and Blocks in C++",
          "In C++, the semicolon is a statement terminator. That is, each individual statement must be ended with a semicolon. It indicates the end of one logical entity."
        ],
        [
          "For example, following are three different statements ",
          "x = y;<br>y = y + 1;<br>add(x, y);<br>"
        ],
        [
          "A block is a set of logically connected statements that are surrounded by opening and closing braces. For example ",
          "{<br>   cout << \"Hello World\"; // prints Hello World<br>   return 0;<br>}<br>"
        ],
        [
          "C++ does not recognize the end of the line as a terminator. For this reason, it does not matter where you put a statement in a line. For example ",
          "x = y;<br>y = y + 1;<br>add(x, y);<br>"
        ],
        [
          "is the same as",
          "x = y; y = y + 1; add(x, y);<br>"
        ],
        [
          "C++ Identifiers",
          "A C++ identifier is a name used to identify a variable, function, class, module, or any other user-defined item. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores, and digits (0 to 9)."
        ],
        [
          "Here are some examples of acceptable identifiers ",
          "mohd       zara    abc   move_name  a_123<br>myname50   _temp   j     a23b9      retVal<br>"
        ],
        [
          "Whitespace in C++",
          "A line containing only whitespace, possibly with a comment, is known as a blank line, and C++ compiler totally ignores it.Whitespace is the term used in C++ to describe blanks, tabs, newline characters and comments. Whitespace separates one part of a statement from another and enables the compiler to identify where one element in a statement, such as int, ends and the next element begins."
        ],
        [
          "Statement 1",
          "int age;<br>"
        ],
        [
          "Statement 2",
          "fruit = apples + oranges;   // Get the total fruit<br>"
        ]
      ]
    },
    {
      "moduleName": "C++ Comments",
      "moduleTopic": [
        "Program comments are explanatory statements that you can include in the C++ code. These comments help anyone reading the source code. All programming languages allow for some form of comments.",
        "C++ comments start with /* and end with */. For example ",
        "A comment can also start with //, extending to the end of the line. For example ",
        "When the above code is compiled, it will ignore // prints Hello World and final executable will produce the following result ",
        "Within a /* and */ comment, // characters have no special meaning. Within a // comment, /* and */ have no special meaning. Thus, you can nest one kind of comment within the other kind. For example "
      ],
      "moduleContent": [
        [
          "Program comments are explanatory statements that you can include in the C++ code. These comments help anyone reading the source code. All programming languages allow for some form of comments.",
          "C++ supports single-line and multi-line comments. All characters available inside any comment are ignored by C++ compiler."
        ],
        [
          "C++ comments start with /* and end with */. For example ",
          "/* This is a comment */<br><br>/* C++ comments can also<br>   * span multiple lines<br>*/<br>"
        ],
        [
          "A comment can also start with //, extending to the end of the line. For example ",
          "#include <iostream><br>using namespace std;<br><br>main() {<br>   cout << \"Hello World\"; // prints Hello World<br>   <br>   return 0;<br>}<br>"
        ],
        [
          "When the above code is compiled, it will ignore // prints Hello World and final executable will produce the following result ",
          "Hello World<br>"
        ],
        [
          "Within a /* and */ comment, // characters have no special meaning. Within a // comment, /* and */ have no special meaning. Thus, you can nest one kind of comment within the other kind. For example ",
          "/* Comment out printing of Hello World:<br><br>cout << \"Hello World\"; // prints Hello World<br><br>*/<br>"
        ]
      ]
    }
  ]
}"""