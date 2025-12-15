<div align="center"><img src="https://github.com/vtiquet/holbertonschool-resources/blob/main/image/Holberton-Logo.svg" width=40% height=40%/></div>

# Resources

## Table of Contents :

  - [0. Keep every promise you make and only make promises you can keep](#subparagraph0)
  - [1. Don't make a promise...if you know you can't keep it](#subparagraph1)
  - [2. Catch me if you can!](#subparagraph2)
  - [3. Handle multiple successful promises](#subparagraph3)
  - [4. Simple promise](#subparagraph4)
  - [5. Reject the promises](#subparagraph5)
  - [6. Handle multiple promises](#subparagraph6)
  - [7. Load balancer](#subparagraph7)
  - [8. Throw an error](#subparagraph8)
  - [9. Throw error / try catch](#subparagraph9)
  - [10. Await / Async](#subparagraph10)

## Resources
### Read or watch:
* [Promise](/rltoken/aNukpnQLStWa6kqBScmZuA)
* [JavaScript Promise: An introduction](/rltoken/oE70cO9HPu1lOGuPFzYXXw)
* [Await](/rltoken/7IuGsWrFjpvdJkNJ2nVhNg)
* [Async](/rltoken/dA3jsQCVsvT1tslyo_8HJQ)
* [Throw / Try](/rltoken/J7MhpGC9WLbQXe4Jc5hb8Q)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* Promises (how, why, and what)
* How to use thethen,resolve,catchmethods
* How to use every method of the Promise object
* Throw / Try
* The await operator
* How to use anasyncfunction

## Requirements
### General
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS usingnode 20.x.xandnpm 9.x.x
* Allowed editors:vi,vim,emacs,Visual Studio Code
* All your files should end with a new line
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use thejsextension
* Your code will be tested usingJestand the commandnpm run test
* Your code will be verified against lint using ESLint
* All of your functions must be exported

## Task
### 0. Keep every promise you make and only make promises you can keep <a name='subparagraph0'></a>

Return a Promise using this prototype <code>function getResponseFromAPI()</code>

```
bob@dylan:~$ cat 0-main.js
import getResponseFromAPI from "./0-promise.js";

const response = getResponseFromAPI();
console.log(response instanceof Promise);

bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-main.js 
true
bob@dylan:~$
```

---

### 1. Don't make a promise...if you know you can't keep it <a name='subparagraph1'></a>

Using the prototype below, return a <code>promise</code>. The parameter is a <code>boolean</code>.

```
getFullResponseFromAPI(success)
```

When the argument is:

* <code>true</code>

  * resolve the promise by passing an object with 2 attributes:


    * <code>status</code>: <code>200</code>
    * <code>body</code>: <code>'Success'</code>
* <code>false</code>

  * reject the promise with an error object with the message <code>The fake API is not working currently</code>

Try testing it out for yourself

```
bob@dylan:~$ cat 1-main.js
import getFullResponseFromAPI from './1-promise';

console.log(getFullResponseFromAPI(true));
console.log(getFullResponseFromAPI(false));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 1-main.js 
Promise { { status: 200, body: 'Success' } }
Promise {
  <rejected> Error: The fake API is not working currently
    ...
    ...
bob@dylan:~$
```

---

### 2. Catch me if you can! <a name='subparagraph2'></a>

Using the function prototype below

```
function handleResponseFromAPI(promise)
```

Append three handlers to the function:

* When the Promise resolves, return an object with the following attributes


  * <code>status</code>: <code>200</code>
  * <code>body</code>: <code>success</code>
* When the Promise rejects, return an empty <code>Error</code> object
* For every resolution, log <code>Got a response from the API</code> to the console

```
bob@dylan:~$ cat 2-main.js
import handleResponseFromAPI from "./2-then";

const promise = Promise.resolve();
handleResponseFromAPI(promise);

bob@dylan:~$ 
bob@dylan:~$ npm run dev 2-main.js 
Got a response from the API
bob@dylan:~$
```

---

### 3. Handle multiple successful promises <a name='subparagraph3'></a>

In this file, import <code>uploadPhoto</code> and <code>createUser</code> from <code>utils.js</code>

Knowing that the functions in <code>utils.js</code> return promises, use the prototype below to collectively resolve all promises and log <code>body firstName lastName</code> to the console.

```
function handleProfileSignup()
```

In the event of an error, log <code>Signup system offline</code> to the console

```
bob@dylan:~$ cat 3-main.js
import handleProfileSignup from "./3-all";

handleProfileSignup();

bob@dylan:~$ 
bob@dylan:~$ npm run dev 3-main.js 
photo-profile-1 Guillaume Salva
bob@dylan:~$
```

---

### 4. Simple promise <a name='subparagraph4'></a>

Using the following prototype

```
function signUpUser(firstName, lastName) {
}
```

That returns a resolved promise with this object:

```
{
  firstName: value,
  lastName: value,
}
```

```
bob@dylan:~$ cat 4-main.js
import signUpUser from "./4-user-promise";

console.log(signUpUser("Bob", "Dylan"));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 4-main.js 
Promise { { firstName: 'Bob', lastName: 'Dylan' } }
bob@dylan:~$
```

---

### 5. Reject the promises <a name='subparagraph5'></a>

Write and export a function named <code>uploadPhoto</code>. It should accept one argument <code>fileName</code> (string).

The function should return a Promise rejecting with an Error and the string <code>$fileName cannot be processed</code>

```
export default function uploadPhoto(filename) {

}
```

```
bob@dylan:~$ cat 5-main.js
import uploadPhoto from './5-photo-reject';

console.log(uploadPhoto('guillaume.jpg'));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 5-main.js 
Promise {
  <rejected> Error: guillaume.jpg cannot be processed
  ..
    ..
bob@dylan:~$
```

---

### 6. Handle multiple promises <a name='subparagraph6'></a>

Import <code>signUpUser</code> from <code>4-user-promise.js</code> and <code>uploadPhoto</code> from <code>5-photo-reject.js</code>.

Write and export a function named <code>handleProfileSignup</code>. It should accept three arguments <code>firstName</code> (string), <code>lastName</code> (string), and <code>fileName</code> (string). The function should call the two other functions. When the promises are all settled it should return an array with the following structure:

```
[
    {
      status: status_of_the_promise,
      value: value or error returned by the Promise
    },
    ...
  ]
```

```
bob@dylan:~$ cat 6-main.js
import handleProfileSignup from './6-final-user';

console.log(handleProfileSignup("Bob", "Dylan", "bob_dylan.jpg"));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 6-main.js 
Promise { <pending> }
bob@dylan:~$
```

---

### 7. Load balancer <a name='subparagraph7'></a>

Write and export a function named <code>loadBalancer</code>. It should accept two arguments <code>chinaDownload</code> (Promise) and <code>USDownload</code> (Promise).

The function should return the value returned by the promise that resolved the first.

```
export default function loadBalancer(chinaDownload, USDownload) {

}
```

```
bob@dylan:~$ cat 7-main.js
import loadBalancer from "./7-load_balancer";

const ukSuccess = 'Downloading from UK is faster';
const frSuccess = 'Downloading from FR is faster';

const promiseUK = new Promise(function(resolve, reject) {
    setTimeout(resolve, 100, ukSuccess);
});

const promiseUKSlow = new Promise(function(resolve, reject) {
    setTimeout(resolve, 400, ukSuccess);
});

const promiseFR = new Promise(function(resolve, reject) {
    setTimeout(resolve, 200, frSuccess);
});

const test = async () => {
    console.log(await loadBalancer(promiseUK, promiseFR));
    console.log(await loadBalancer(promiseUKSlow, promiseFR));
}

test();

bob@dylan:~$ 
bob@dylan:~$ npm run dev 7-main.js 
Downloading from UK is faster
Downloading from FR is faster
bob@dylan:~$
```

---

### 8. Throw an error <a name='subparagraph8'></a>

Write a function named <code>divideFunction</code> that will accept two arguments: <code>numerator</code> (Number) and <code>denominator</code> (Number).

When the <code>denominator</code> argument is equal to 0, the function should throw a new error with the message <code>cannot divide by 0</code>. Otherwise it should return the numerator divided by the denominator.

```
export default function divideFunction(numerator, denominator) {

}
```

```
bob@dylan:~$ cat 8-main.js
import divideFunction from './8-try';

console.log(divideFunction(10, 2));
console.log(divideFunction(10, 0));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 8-main.js 
5
..../8-try.js:15
  throw Error('cannot divide by 0');
  ^
.....

bob@dylan:~$
```

---

### 9. Throw error / try catch <a name='subparagraph9'></a>

Write a function named <code>guardrail</code> that will accept one argument <code>mathFunction</code> (Function).

This function should create and return an array named <code>queue</code>.

When the <code>mathFunction</code> function is executed, the value returned by the function should be appended to the queue. 
If this function throws an error, the error message should be appended to the queue. 
In every case, the message <code>Guardrail was processed</code> should be added to the queue.

Example:

```
[
  1000,
  'Guardrail was processed',
]
```

```
bob@dylan:~$ cat 9-main.js
import guardrail from './9-try';
import divideFunction from './8-try';

console.log(guardrail(() => { return divideFunction(10, 2)}));
console.log(guardrail(() => { return divideFunction(10, 0)}));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 9-main.js 
[ 5, 'Guardrail was processed' ]
[ 'Error: cannot divide by 0', 'Guardrail was processed' ]
bob@dylan:~$
```

---

### 10. Await / Async <a name='subparagraph10'></a>

Import <code>uploadPhoto</code> and <code>createUser</code> from <code>utils.js</code>

Write an async function named <code>asyncUploadUser</code> that will call these two functions and return an object with the following format:

```
{
  photo: response_from_uploadPhoto_function,
  user: response_from_createUser_function,
}
```

If one of the async function fails, return an empty object. Example:

```
{
  photo: null,
  user: null,
}
```

```
bob@dylan:~$ cat 100-main.js
import asyncUploadUser from "./100-await";

const test = async () => {
    const value = await asyncUploadUser();
    console.log(value);
};

test();

bob@dylan:~$ 
bob@dylan:~$ npm run dev 100-main.js 
{
  photo: { status: 200, body: 'photo-profile-1' },
  user: { firstName: 'Guillaume', lastName: 'Salva' }
}
bob@dylan:~$
```

---


## Authors
vtiquet - [GitHub Profile](https://github.com/vtiquet)
