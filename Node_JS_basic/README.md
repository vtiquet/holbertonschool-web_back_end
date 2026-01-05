<div align="center"><img src="https://github.com/vtiquet/holbertonschool-resources/blob/main/image/Holberton-Logo.svg" width=40% height=40%/></div>

# Resources

## Table of Contents :

  - [0. Executing basic javascript with Node JS](#subparagraph0)
  - [1. Using Process stdin](#subparagraph1)
  - [2. Reading a file synchronously with Node JS](#subparagraph2)
  - [3. Reading a file asynchronously with Node JS](#subparagraph3)
  - [4. Create a small HTTP server using Node's HTTP module](#subparagraph4)
  - [5. Create a more complex HTTP server using Node's HTTP module](#subparagraph5)
  - [6. Create a small HTTP server using Express](#subparagraph6)
  - [7. Create a more complex HTTP server using Express](#subparagraph7)
  - [8. Organize a complex HTTP server using Express](#subparagraph8)

## Resources
### Read or watch:
* [Node JS getting started](/rltoken/RqwwGmqIE4M3WwjqXusJ7w)
* [Process API doc](/rltoken/TyodG31Rx3XIiGE7HnxNYw)
* [Child process](/rltoken/Ic5-12q1xFd74_0psW4CdQ)
* [Express getting started](/rltoken/Bi4zX1TeHY2RF5lLYgKspg)
* [Mocha documentation](/rltoken/eBgT_wcT40RgCLtYXuRpvw)
* [Nodemon documentation](/rltoken/rlx9PqRqSQkA6v6ZJmYKNw)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* run javascript using NodeJS
* use NodeJS modules
* use specific Node JS module to read files
* useprocessto access command line arguments and the environment
* create a small HTTP server using Node JS
* create a small HTTP server using Express JS
* create advanced routes with Express JS
* use ES6 with Node JS with Babel-node
* use Nodemon to develop faster

## Requirements
### General
* Allowed editors:vi,vim,emacs,Visual Studio Code
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS usingnode(version 20.x.x)
* All your files should end with a new line
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use thejsextension
* Your code will be tested usingJestand the commandnpm run test
* Your code will be verified against lint using ESLint
* Your code needs to pass all the tests and lint. You can verify the entire project runningnpm run full-test
* All of your functions/classes must be exported by using this format:module.exports = myFunction;
* You must also send the following files to your repository:package.json,babel.config.js,.eslintrc.jsanddatabase.csv

## Task
### 0. Executing basic javascript with Node JS <a name='subparagraph0'></a>

In the file <code>0-console.js</code>, create a function named <code>displayMessage</code> that prints in <code>STDOUT</code> the string argument.

```
bob@dylan:~$ cat 0-main.js
const displayMessage = require('./0-console');

displayMessage("Hello NodeJS!");

bob@dylan:~$ node 0-main.js
Hello NodeJS!
bob@dylan:~$
```

---

### 1. Using Process stdin <a name='subparagraph1'></a>

Create a program named <code>1-stdin.js</code> that will be executed through command line:

* It should display the message <code>Welcome to Holberton School, what is your name?</code> (followed by a new line)
* The user should be able to input their name on a new line
* The program should display <code>Your name is: INPUT</code>
* When the user ends the program, it should display <code>This important software is now closing</code> (followed by a new line)

<strong>Requirements:</strong>

* Your code will be tested through a child process, make sure you have everything you need for that

```
bob@dylan:~$ node 1-stdin.js 
Welcome to Holberton School, what is your name?
Bob
Your name is: Bob
bob@dylan:~$ 
bob@dylan:~$ echo "John" | node 1-stdin.js 
Welcome to Holberton School, what is your name?
Your name is: John
This important software is now closing
bob@dylan:~$
```

---

### 2. Reading a file synchronously with Node JS <a name='subparagraph2'></a>

Using the database <code>database.csv</code> (provided in project description), create a function <code>countStudents</code> in the file <code>2-read_file.js</code>

* Create a function named <code>countStudents</code>. It should accept a path in argument
* The script should attempt to read the database file synchronously
* If the database is not available, it should throw an error with the text <code>Cannot load the database</code>
* If the database is available, it should log the following message to the console <code>Number of students: NUMBER_OF_STUDENTS</code>
* It should log the number of students in each field, and the list with the following format: <code>Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES</code>
* CSV file can contain empty lines (at the end) - and they are not a valid student!

```
bob@dylan:~$ cat 2-main_0.js
const countStudents = require('./2-read_file');

countStudents("nope.csv");

bob@dylan:~$ node 2-main_0.js
2-read_file.js:9
    throw new Error('Cannot load the database');
    ^

Error: Cannot load the database
...
bob@dylan:~$
bob@dylan:~$ cat 2-main_1.js
const countStudents = require('./2-read_file');

countStudents("database.csv");

bob@dylan:~$ node 2-main_1.js
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
bob@dylan:~$
```

---

### 3. Reading a file asynchronously with Node JS <a name='subparagraph3'></a>

Using the database <code>database.csv</code> (provided in project description), create a function <code>countStudents</code> in the file <code>3-read_file_async.js</code>

* Create a function named <code>countStudents</code>. It should accept a path in argument (same as in <code>2-read_file.js</code>)
* The script should attempt to read the database file asynchronously
* The function should return a Promise
* If the database is not available, it should throw an error with the text <code>Cannot load the database</code>
* If the database is available, it should log the following message to the console <code>Number of students: NUMBER_OF_STUDENTS</code>
* It should log the number of students in each field, and the list with the following format: <code>Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES</code>
* CSV file can contain empty lines (at the end) - and they are not a valid student!

```
bob@dylan:~$ cat 3-main_0.js
const countStudents = require('./3-read_file_async');

countStudents("nope.csv")
    .then(() => {
        console.log("Done!");
    })
        .catch((error) => {
        console.log(error);
    });

bob@dylan:~$ node 3-main_0.js
Error: Cannot load the database
...
bob@dylan:~$
bob@dylan:~$ cat 3-main_1.js
const countStudents = require('./3-read_file_async');

countStudents("database.csv")
    .then(() => {
        console.log("Done!");
    })
        .catch((error) => {
        console.log(error);
    });
console.log("After!");

bob@dylan:~$ node 3-main_1.js
After!
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
Done!
bob@dylan:~$
```

<strong>Tips:</strong>

* Using asynchronous callbacks is the preferred way to write code in Node to avoid blocking threads

---

### 4. Create a small HTTP server using Node's HTTP module <a name='subparagraph4'></a>

In a file named <code>4-http.js</code>, create a small HTTP server using the <code>http</code> module:

* It should be assigned to the variable <code>app</code> and this one must be exported
* HTTP server should listen on port 1245
* Displays <code>Hello Holberton School!</code> in the page body for any endpoint as plain text

In terminal 1:

```
bob@dylan:~$ node 4-http.js
...
```

In terminal 2:

```
bob@dylan:~$ curl localhost:1245 && echo ""
Hello Holberton School!
bob@dylan:~$ 
bob@dylan:~$ curl localhost:1245/any_endpoint && echo ""
Hello Holberton School!
bob@dylan:~$
```

---

### 5. Create a more complex HTTP server using Node's HTTP module <a name='subparagraph5'></a>

In a file named <code>5-http.js</code>, create a small HTTP server using the <code>http</code> module:

* It should be assigned to the variable app and this one must be exported
* HTTP server should listen on port 1245
* It should return plain text
* When the URL path is <code>/</code>, it should display <code>Hello Holberton School!</code> in the page body
* When the URL path is <code>/students</code>, it should display <code>This is the list of our students</code> followed by the same content as the file <code>3-read_file_async.js</code> (with and without the database) - the name of the database must be passed as argument of the file
* CSV file can contain empty lines (at the end) - and they are not a valid student!

Terminal 1:

```
bob@dylan:~$ node 5-http.js database.csv
...
```

In terminal 2:

```
bob@dylan:~$ curl localhost:1245 && echo ""
Hello Holberton School!
bob@dylan:~$ 
bob@dylan:~$ curl localhost:1245/students && echo ""
This is the list of our students
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
bob@dylan:~$
```

---

### 6. Create a small HTTP server using Express <a name='subparagraph6'></a>

Install Express and in a file named <code>6-http_express.js</code>, create a small HTTP server using Express module:

* It should be assigned to the variable <code>app</code> and this one must be exported
* HTTP server should listen on port 1245
* Displays <code>Hello Holberton School!</code> in the page body for the endpoint <code>/</code>

In terminal 1:

```
bob@dylan:~$ node 6-http_express.js
...
```

In terminal 2:

```
bob@dylan:~$ curl localhost:1245 && echo ""
Hello Holberton School!
bob@dylan:~$ 
bob@dylan:~$ curl localhost:1245/any_endpoint && echo ""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>Cannot GET /lskdlskd</pre>
</body>
</html> 
bob@dylan:~$
```

---

### 7. Create a more complex HTTP server using Express <a name='subparagraph7'></a>

In a file named <code>7-http_express.js</code>, recreate the small HTTP server using <code>Express</code>:

* It should be assigned to the variable app and this one must be exported
* HTTP server should listen on port 1245
* It should return plain text
* When the URL path is <code>/</code>, it should display <code>Hello Holberton School!</code> in the page body
* When the URL path is <code>/students</code>, it should display <code>This is the list of our students</code> followed by the same content as the file <code>3-read_file_async.js</code> (with and without the database) - the name of the database must be passed as argument of the file
* CSV file can contain empty lines (at the end) - and they are not a valid student!

Terminal 1:

```
bob@dylan:~$ node 7-http_express.js database.csv
...
```

In terminal 2:

```
bob@dylan:~$ curl localhost:1245 && echo ""
Hello Holberton School!
bob@dylan:~$ 
bob@dylan:~$ curl localhost:1245/students && echo ""
This is the list of our students
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
bob@dylan:~$
```

---

### 8. Organize a complex HTTP server using Express <a name='subparagraph8'></a>

Obviously writing every part of a server within a single file is not sustainable. Let’s create a full server in a directory named <code>full_server</code>.

Since you have used ES6 and Babel in the past projects, let’s use <code>babel-node</code> to allow to use ES6 functions like <code>import</code> or <code>export</code>.

* Create 2 directories within:


  * <code>controllers</code>
  * <code>routes</code>
* Create a file <code>full_server/utils.js</code>, in the file create a function named <code>readDatabase</code> that accepts a file path as argument:


  * It should read the database asynchronously
  * It should return a promise
  * When the file is not accessible, it should reject the promise with the error
  * When the file can be read, it should return an object of arrays of the firstname of students per fields

Inside the file <code>full_server/controllers/AppController.js</code>:

* Create a class named <code>AppController</code>. Add a static method named <code>getHomepage</code>
* The method accepts <code>request</code> and <code>response</code> as argument. It returns a 200 status and the message <code>Hello Holberton School!</code>

Inside the file <code>full_server/controllers/StudentsController.js</code>, create a class named <code>StudentsController</code>. Add two static methods:

The first one is <code>getAllStudents</code>:

* The method accepts <code>request</code> and <code>response</code> as argument
* It should return a status 200
* It calls the function <code>readDatabase</code> from the <code>utils</code> file, and display in the page:


  * First line: <code>This is the list of our students</code>
  * And for each field (order by alphabetic order case insensitive), a line that displays the number of students in the field, and the list of first names (ordered by appearance in the database file) with the following format: <code>Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES</code>
* If the database is not available, it should return a status 500 and the error message <code>Cannot load the database</code>

The second one is <code>getAllStudentsByMajor</code>:

* The method accepts <code>request</code> and <code>response</code> as argument
* It should return a status 200
* It uses a parameter that the user can pass to the browser <code>major</code>. The <code>major</code> can only be <code>CS</code> or <code>SWE</code>. If the user is passing another parameter, the server should return a 500 and the error <code>Major parameter must be CS or SWE</code>
* It calls the function <code>readDatabase</code> from the <code>utils</code> file, and display in the page the list of first names  for the students (ordered by appearance in the database file) in the specified field <code>List: LIST_OF_FIRSTNAMES_IN_THE_FIELD</code>
* If the database is not available, it should return a status 500 and the error message <code>Cannot load the database</code>

Inside the file <code>full_server/routes/index.js</code>:

* Link the route <code>/</code> to the <code>AppController</code>
* Link the route <code>/students</code>  and <code>/students/:major</code>to the <code>StudentsController</code>

Inside the file named <code>full_server/server.js</code>, create a small Express server:

* It should use the routes defined in <code>full_server/routes/index.js</code>
* It should use the port <code>1245</code>

If you are starting node from outside of the folder <code>full_server</code>, you will have to update the command <code>dev</code> by: <code>nodemon --exec babel-node --presets babel-preset-env ./full_server/server.js ./database.csv</code>

<strong>Warning:</strong>

* Don’t forget to export your express app at the end of <code>server.js</code> (<code>export default app;</code>)
* The database filename is passed as argument of the <code>server.js</code> BUT, for testing purpose, you should retrieve this filename at the execution (when <code>getAllStudents</code> or <code>getAllStudentsByMajor</code>  are called for example)

In terminal 1:

```
bob@dylan:~$ npm run dev
...
```

In terminal 2:

```
bob@dylan:~$ curl localhost:1245 && echo ""
Hello Holberton School!
bob@dylan:~$ 
bob@dylan:~$ curl localhost:1245/students && echo ""
This is the list of our students
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
bob@dylan:~$ 
bob@dylan:~$ curl localhost:1245/students/SWE && echo ""
List: Guillaume, Joseph, Paul, Tommy
bob@dylan:~$ 
bob@dylan:~$ curl localhost:1245/students/French -vvv && echo ""
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 1245 (#0)
> GET /students/SWES HTTP/1.1
> Host: localhost:1245
> User-Agent: curl/7.58.0
> Accept: */*
>
< HTTP/1.1 500 Internal Server Error
< X-Powered-By: Express
< Date: Mon, 06 Jul 2020 03:29:00 GMT
< Connection: keep-alive
< Content-Length: 33
<
* Connection #0 to host localhost left intact
Major parameter must be CS or SWE
bob@dylan:~$
```

If you want to add test to validate your integration, you will need to add this file: <code>.babelrc</code>
<details>
<summary>Click to show/hide file contents</summary>
<pre>
<code>
{
    "presets": [["env", {"exclude": ["transform-regenerator"]}]]
}
</code>
</pre>
</details>

---


## Authors
vtiquet - [GitHub Profile](https://github.com/vtiquet)
