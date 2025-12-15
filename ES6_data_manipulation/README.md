<div align="center"><img src="https://github.com/vtiquet/holbertonschool-resources/blob/main/image/Holberton-Logo.svg" width=40% height=40%/></div>

# Resources

## Table of Contents :

  - [0. Basic list of objects](#subparagraph0)
  - [1. More mapping](#subparagraph1)
  - [2. Filter](#subparagraph2)
  - [3. Reduce](#subparagraph3)
  - [4. Combine](#subparagraph4)
  - [5. Typed Arrays](#subparagraph5)
  - [6. Set data structure](#subparagraph6)
  - [7. More set data structure](#subparagraph7)
  - [8. Clean set](#subparagraph8)
  - [9. Map data structure](#subparagraph9)
  - [10. More map data structure](#subparagraph10)
  - [11. Weak link data structure](#subparagraph11)

## Resources
### Read or watch:
* [Array](/rltoken/fXeF-M30vPa-VR4qdM1hbQ)
* [Typed Array](/rltoken/K8YavMi9P0JsBDS4W8PXvw)
* [Set Data Structure](/rltoken/47KxkohflmsBUjMCzRxMkQ)
* [Map Data Structure](/rltoken/c01xzbbE1CXwbXEW8jS0gQ)
* [WeakMap](/rltoken/f-CLehBUa4LvtJt5c_tEUw)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* How to use map, filter and reduce on arrays
* Typed arrays
* The Set, Map, and Weak link data structures

## Requirements
### General
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS usingnode 20.x.xandnpm 9.x.x
* Allowed editors:vi,vim,emacs,Visual Studio Code
* All your files should end with a new line
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use thejsextension
* Your code will be tested usingJestand the commandnpm run test
* Your code will be verified against lint using ESLint
* Your code needs to pass all the tests and lint. You can verify the entire project runningnpm run full-test
* All of your functions must be exported

## Task
### 0. Basic list of objects <a name='subparagraph0'></a>

Create a function named <code>getListStudents</code> that returns an array of objects.

Each object should have three attributes: <code>id</code> (Number), <code>firstName</code> (String), and <code>location</code> (String).

The array contains the following students in order:

* <code>Guillaume</code>, id: <code>1</code>, in <code>San Francisco</code>
* <code>James</code>, id: <code>2</code>, in <code>Columbia</code>
* <code>Serena</code>, id: <code>5</code>, in <code>San Francisco</code>

```
bob@dylan:~$ cat 0-main.js
import getListStudents from "./0-get_list_students.js";

console.log(getListStudents());

bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-main.js 
[
  { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
  { id: 2, firstName: 'James', location: 'Columbia' },
  { id: 5, firstName: 'Serena', location: 'San Francisco' }
]
bob@dylan:~$
```

---

### 1. More mapping <a name='subparagraph1'></a>

Create a function <code>getListStudentIds</code> that returns an array of ids from a list of object.

This function is taking one argument which is an array of objects - and this array is the same format as <code>getListStudents</code> from the previous task.

If the argument is not an array, the function is returning an empty array.

You must use the <code>map</code> function on the array.

```
bob@dylan:~$ cat 1-main.js
import getListStudentIds from "./1-get_list_student_ids.js";
import getListStudents from "./0-get_list_students.js";

console.log(getListStudentIds("hello"));
console.log(getListStudentIds(getListStudents()));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 1-main.js 
[]
[ 1, 2, 5 ]
bob@dylan:~$
```

---

### 2. Filter <a name='subparagraph2'></a>

Create a function <code>getStudentsByLocation</code> that returns an array of objects who are located in a specific city.

It should accept a list of students (from <code>getListStudents</code>) and a <code>city</code> (string) as parameters.

You must use the <code>filter</code> function on the array.

```
bob@dylan:~$ cat 2-main.js
import getListStudents from "./0-get_list_students.js";
import getStudentsByLocation from "./2-get_students_by_loc.js";

const students = getListStudents();

console.log(getStudentsByLocation(students, 'San Francisco'));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 2-main.js 
[
  { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
  { id: 5, firstName: 'Serena', location: 'San Francisco' }
]
bob@dylan:~$
```

---

### 3. Reduce <a name='subparagraph3'></a>

Create a function <code>getStudentIdsSum</code> that returns the sum of all the student ids.

It should accept a list of students (from <code>getListStudents</code>) as a parameter.

You must use the <code>reduce</code> function on the array.

```
bob@dylan:~$ cat 3-main.js
import getListStudents from "./0-get_list_students.js";
import getStudentIdsSum from "./3-get_ids_sum.js";

const students = getListStudents();
const value = getStudentIdsSum(students);

console.log(value);

bob@dylan:~$ 
bob@dylan:~$ npm run dev 3-main.js 
8
bob@dylan:~$
```

---

### 4. Combine <a name='subparagraph4'></a>

Create a function <code>updateStudentGradeByCity</code> that returns an array of students for a specific city with their new grade

It should accept a list of students (from <code>getListStudents</code>), a <code>city</code> (String), and <code>newGrades</code> (Array of “grade” objects) as parameters.

<code>newGrades</code> is an array of objects with this format:

```
{
    studentId: 31,
    grade: 78,
  }
```

If a student doesn’t have grade in <code>newGrades</code>, the final grade should be <code>N/A</code>.

You must use <code>filter</code> and <code>map</code> combined.

```
bob@dylan:~$ cat 4-main.js
import getListStudents from "./0-get_list_students.js";
import updateStudentGradeByCity from "./4-update_grade_by_city.js";

console.log(updateStudentGradeByCity(getListStudents(), "San Francisco", [{ studentId: 5, grade: 97 }, { studentId: 1, grade: 86 }]));

console.log(updateStudentGradeByCity(getListStudents(), "San Francisco", [{ studentId: 5, grade: 97 }]));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 4-main.js 
[
  {
    id: 1,
    firstName: 'Guillaume',
    location: 'San Francisco',
    grade: 86
  },
  { id: 5, firstName: 'Serena', location: 'San Francisco', grade: 97 }
]
[
  {
    id: 1,
    firstName: 'Guillaume',
    location: 'San Francisco',
    grade: 'N/A'
  },
  { id: 5, firstName: 'Serena', location: 'San Francisco', grade: 97 }
]
bob@dylan:~$
```

---

### 5. Typed Arrays <a name='subparagraph5'></a>

Create a function named <code>createInt8TypedArray</code> that returns a new <code>ArrayBuffer</code> with an <code>Int8</code> value at a specific position.

It should accept three arguments: <code>length</code> (Number), <code>position</code> (Number), and <code>value</code> (Number).

If adding the value is not possible the error <code>Position outside range</code> should be thrown.

```
bob@dylan:~$ cat 5-main.js
import createInt8TypedArray from "./5-typed_arrays.js";

console.log(createInt8TypedArray(10, 2, 89));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 5-main.js 
DataView {
  byteLength: 10,
  byteOffset: 0,
  buffer: ArrayBuffer {
    [Uint8Contents]: <00 00 59 00 00 00 00 00 00 00>,
    byteLength: 10
  }
}
bob@dylan:~$
```

---

### 6. Set data structure <a name='subparagraph6'></a>

Create a function named <code>setFromArray</code> that returns a <code>Set</code> from an array.

It accepts an argument (Array, of any kind of element).

```
bob@dylan:~$ cat 6-main.js
import setFromArray from "./6-set.js";

console.log(setFromArray([12, 32, 15, 78, 98, 15]));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 6-main.js 
Set { 12, 32, 15, 78, 98 }
bob@dylan:~$
```

---

### 7. More set data structure <a name='subparagraph7'></a>

Create a function named <code>hasValuesFromArray</code> that returns a boolean if all the elements in the array exist within the set.

It accepts two arguments: a <code>set</code> (Set) and an <code>array</code> (Array).

```
bob@dylan:~$ cat 7-main.js
import hasValuesFromArray from "./7-has_array_values.js";

console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1]));
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [10]));
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1, 10]));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 7-main.js 
true
false
false
bob@dylan:~$
```

---

### 8. Clean set <a name='subparagraph8'></a>

Create a function named <code>cleanSet</code> that returns a string of all the set values that start with a specific string (<code>startString</code>).

It accepts two arguments: a <code>set</code> (Set) and a <code>startString</code> (String).

When a value starts with <code>startString</code> you only append the rest of the string. The string contains all the values of the set separated by <code>-</code>.

```
bob@dylan:~$ cat 8-main.js
import cleanSet from "./8-clean_set.js";

console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), 'bon'));
console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), ''));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 8-main.js 
jovi-aparte-appetit

bob@dylan:~$
```

---

### 9. Map data structure <a name='subparagraph9'></a>

Create a function named <code>groceriesList</code> that returns a map of groceries with the following items (name, quantity):

```
Apples, 10
Tomatoes, 10
Pasta, 1
Rice, 1
Banana, 5
```

Result:

```
bob@dylan:~$ cat 9-main.js
import groceriesList from "./9-groceries_list.js";

console.log(groceriesList());

bob@dylan:~$ 
bob@dylan:~$ npm run dev 9-main.js 
Map {
  'Apples' => 10,
  'Tomatoes' => 10,
  'Pasta' => 1,
  'Rice' => 1,
  'Banana' => 5
}
bob@dylan:~$
```

---

### 10. More map data structure <a name='subparagraph10'></a>

Create a function named <code>updateUniqueItems</code> that returns an updated map for all items with initial quantity at 1.

It should accept a map as an argument. The map it accepts for argument is similar to the map you create in the previous task.

For each entry of the map where the quantity is 1, update the quantity to 100. 
If updating the quantity is not possible (argument is not a map) the error <code>Cannot process</code> should be thrown.

```
bob@dylan:~$ cat 10-main.js
import updateUniqueItems from "./10-update_uniq_items.js";
import groceriesList from "./9-groceries_list.js";

const map = groceriesList();
console.log(map);

updateUniqueItems(map)
console.log(map);

bob@dylan:~$ 
bob@dylan:~$ npm run dev 10-main.js 
Map {
  'Apples' => 10,
  'Tomatoes' => 10,
  'Pasta' => 1,
  'Rice' => 1,
  'Banana' => 5
}
Map {
  'Apples' => 10,
  'Tomatoes' => 10,
  'Pasta' => 100,
  'Rice' => 100,
  'Banana' => 5
}
bob@dylan:~$
```

---

### 11. Weak link data structure <a name='subparagraph11'></a>

Export a <code>const</code> instance of <code>WeakMap</code> and name it <code>weakMap</code>.

Export a new function named <code>queryAPI</code>. It should accept an endpoint argument like so:

```
{
    protocol: 'http',
    name: 'getUsers',
  }
```

Track within the <code>weakMap</code> the number of times <code>queryAPI</code> is called for each endpoint.

When the number of queries is >= 5 throw an error with the message <code>Endpoint load is high</code>.

```
bob@dylan:~$ cat 100-main.js
import { queryAPI, weakMap } from "./100-weak.js";

const endpoint = { protocol: 'http', name: 'getUsers' };
weakMap.get(endpoint);

queryAPI(endpoint);
console.log(weakMap.get(endpoint));

queryAPI(endpoint);
console.log(weakMap.get(endpoint));

queryAPI(endpoint);
queryAPI(endpoint);
queryAPI(endpoint);
queryAPI(endpoint);

bob@dylan:~$ 
bob@dylan:~$ npm run dev 100-main.js 
1
2
.../100-weak.js:16
    throw new Error('Endpoint load is high');
   ...
bob@dylan:~$
```

---


## Authors
vtiquet - [GitHub Profile](https://github.com/vtiquet)
