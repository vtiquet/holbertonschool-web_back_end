<div align="center"><img src="https://github.com/vtiquet/holbertonschool-resources/blob/main/image/Holberton-Logo.svg" width=40% height=40%/></div>

# Resources

## Table of Contents :

  - [0. You used to attend a place like this at some point](#subparagraph0)
  - [1. Let's make some classrooms](#subparagraph1)
  - [2. A Course, Getters, and Setters](#subparagraph2)
  - [3. Methods, static methods, computed methods names..... MONEY](#subparagraph3)
  - [4. Pricing](#subparagraph4)
  - [5. A Building](#subparagraph5)
  - [6. Inheritance](#subparagraph6)
  - [7. Airport](#subparagraph7)
  - [8. Primitive - Holberton Class](#subparagraph8)
  - [9. Hoisting](#subparagraph9)
  - [10. Vroom](#subparagraph10)
  - [11. EVCar](#subparagraph11)

## Resources
### Read or watch:
* [Classes](/rltoken/AJdJxuoO8o3hwpybQaFSDQ)
* [Metaprogramming](/rltoken/jF42Fw5HNIPnFWKmDzVg1g)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* How to define a Class
* How to add methods to a class
* Why and how to add a static method to a class
* How to extend a class from another
* Metaprogramming and symbols

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

## Task
### 0. You used to attend a place like this at some point <a name='subparagraph0'></a>

Implement a class named <code>ClassRoom</code>:

* Prototype: <code>export default class ClassRoom</code>
* It should accept one attribute named <code>maxStudentsSize</code> (Number) and assigned to <code>_maxStudentsSize</code>

```
bob@dylan:~$ cat 0-main.js
import ClassRoom from "./0-classroom.js";

const room = new ClassRoom(10);
console.log(room._maxStudentsSize)

bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-main.js 
10
bob@dylan:~$
```

---

### 1. Let's make some classrooms <a name='subparagraph1'></a>

Import the <code>ClassRoom</code> class from <code>0-classroom.js</code>.

Implement a function named <code>initializeRooms</code>. It should return an array of 3 <code>ClassRoom</code> objects with the sizes 19, 20, and 34 (in this order).

```
bob@dylan:~$ cat 1-main.js
import initializeRooms from './1-make_classrooms.js';

console.log(initializeRooms());

bob@dylan:~$ 
bob@dylan:~$ npm run dev 1-main.js 
[
  ClassRoom { _maxStudentsSize: 19 },
  ClassRoom { _maxStudentsSize: 20 },
  ClassRoom { _maxStudentsSize: 34 }
]
bob@dylan:~$
```

---

### 2. A Course, Getters, and Setters <a name='subparagraph2'></a>

Implement a class named <code>HolbertonCourse</code>:

* Constructor attributes: 


  * <code>name</code> (String)
  * <code>length</code> (Number)
  * <code>students</code> (array of Strings)
* Make sure to verify the type of attributes during object creation
* Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)
* Implement a getter and setter for each attribute.

```
bob@dylan:~$ cat 2-main.js
import HolbertonCourse from "./2-hbtn_course.js";

const c1 = new HolbertonCourse("ES6", 1, ["Bob", "Jane"])
console.log(c1.name);
c1.name = "Python 101";
console.log(c1);

try {
    c1.name = 12;
} 
catch(err) {
    console.log(err);
}

try {
    const c2 = new HolbertonCourse("ES6", "1", ["Bob", "Jane"]);
}
catch(err) {
    console.log(err);
}

bob@dylan:~$ 
bob@dylan:~$ npm run dev 2-main.js 
ES6
HolbertonCourse {
  _name: 'Python 101',
  _length: 1,
  _students: [ 'Bob', 'Jane' ]
}
TypeError: Name must be a string
    ...
TypeError: Length must be a number
    ...
bob@dylan:~$
```

---

### 3. Methods, static methods, computed methods names..... MONEY <a name='subparagraph3'></a>

Implement a class named <code>Currency</code>:

* - Constructor attributes: 


  * <code>code</code> (String)
  * <code>name</code> (String)
* Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)
* Implement a getter and setter for each attribute.
* Implement a method named <code>displayFullCurrency</code> that will return the attributes in the following format <code>name (code)</code>.

```
bob@dylan:~$ cat 3-main.js
import Currency from "./3-currency.js";

const dollar = new Currency('$', 'Dollars');
console.log(dollar.displayFullCurrency());

bob@dylan:~$ 
bob@dylan:~$ npm run dev 3-main.js 
Dollars ($)
bob@dylan:~$
```

---

### 4. Pricing <a name='subparagraph4'></a>

Import the class <code>Currency</code> from <code>3-currency.js</code>

Implement a class named <code>Pricing</code>:

* Constructor attributes: 


  * <code>amount</code> (Number)
  * <code>currency</code> (Currency)
* Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)
* Implement a getter and setter for each attribute.
* Implement a method named <code>displayFullPrice</code> that returns the attributes in the following format <code>amount currency_name (currency_code)</code>.
* Implement a static method named <code>convertPrice</code>. It should accept two arguments: <code>amount</code> (Number), <code>conversionRate</code> (Number). The function should return the amount multiplied by the conversion rate.

```
bob@dylan:~$ cat 4-main.js
import Pricing from './4-pricing.js';
import Currency from './3-currency.js';

const p = new Pricing(100, new Currency("EUR", "Euro"))
console.log(p);
console.log(p.displayFullPrice());

bob@dylan:~$ 
bob@dylan:~$ npm run dev 4-main.js 
Pricing {
  _amount: 100,
  _currency: Currency { _code: 'EUR', _name: 'Euro' }
}
100 Euro (EUR)
bob@dylan:~$
```

---

### 5. A Building <a name='subparagraph5'></a>

Implement a class named <code>Building</code>:

* Constructor attributes: 


  * <code>sqft</code> (Number)
* Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)
* Implement a getter for each attribute.
* Consider this class as an abstract class. And make sure that any class that extends from it should implement a method named <code>evacuationWarningMessage</code>.


  * If a class that extends from it does not have a <code>evacuationWarningMessage</code> method, throw an error with the message <code>Class extending Building must override evacuationWarningMessage</code>

```
bob@dylan:~$ cat 5-main.js
import Building from './5-building.js';

const b = new Building(100);
console.log(b);

class TestBuilding extends Building {}

try {
    new TestBuilding(200)
}
catch(err) {
    console.log(err);
}

bob@dylan:~$ 
bob@dylan:~$ npm run dev 5-main.js 
Building { _sqft: 100 }
Error: Class extending Building must override evacuationWarningMessage
    ...
bob@dylan:~$
```

---

### 6. Inheritance <a name='subparagraph6'></a>

Import <code>Building</code> from <code>5-building.js</code>.

Implement a class named <code>SkyHighBuilding</code> that extends from <code>Building</code>:

* Constructor attributes: 


  * <code>sqft</code> (Number) (must be assigned to the parent class <code>Building</code>)
  * <code>floors</code> (Number)
* Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)
* Implement a getter for each attribute.
* Override the method named <code>evacuationWarningMessage</code> and return the following string <code>Evacuate slowly the NUMBER_OF_FLOORS floors</code>.

```
bob@dylan:~$ cat 6-main.js
import SkyHighBuilding from './6-sky_high.js';

const building = new SkyHighBuilding(140, 60);
console.log(building.sqft);
console.log(building.floors);
console.log(building.evacuationWarningMessage());

bob@dylan:~$ 
bob@dylan:~$ npm run dev 6-main.js 
140
60
Evacuate slowly the 60 floors
bob@dylan:~$
```

---

### 7. Airport <a name='subparagraph7'></a>

Implement a class named <code>Airport</code>:

* Constructor attributes: 


  * <code>name</code> (String)
  * <code>code</code> (String)
* Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)
* The default string description of the class should return the airport <code>code</code> (example below).

```
bob@dylan:~$ cat 7-main.js
import Airport from "./7-airport.js";

const airportSF = new Airport('San Francisco Airport', 'SFO');
console.log(airportSF);
console.log(airportSF.toString());

bob@dylan:~$ 
bob@dylan:~$ npm run dev 7-main.js 
Airport [SFO] { _name: 'San Francisco Airport', _code: 'SFO' }
[object SFO]
bob@dylan:~$
```

---

### 8. Primitive - Holberton Class <a name='subparagraph8'></a>

Implement a class named <code>HolbertonClass</code>:

* Constructor attributes: 


  * <code>size</code> (Number)
  * <code>location</code> (String)
* Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)
* When the class is cast into a <code>Number</code>, it should return the size.
* When the class is cast into a <code>String</code>, it should return the location.

```
bob@dylan:~$ cat 8-main.js
import HolbertonClass from "./8-hbtn_class.js";

const hc = new HolbertonClass(12, "Mezzanine")
console.log(Number(hc));
console.log(String(hc));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 8-main.js 
12
Mezzanine
bob@dylan:~$
```

---

### 9. Hoisting <a name='subparagraph9'></a>

Fix this code and make it work.

```
const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  get year() {
    return this._year;
  }

  get location() {
    return this._location;
  }
}

const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

export class StudentHolberton {
  constructor(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get holbertonClass() {
    return this.holbertonClass;
  }

  get fullStudentDescription() {
    return `${self._firstName} ${self._lastName} - ${self._holbertonClass.year} - ${self._holbertonClass.location}`;
  }
}


export const listOfStudents = [student1, student2, student3, student4, student5];
```

Result:

```
bob@dylan:~$ cat 9-main.js
import listOfStudents from "./9-hoisting.js";

console.log(listOfStudents);

const listPrinted = listOfStudents.map(
    student => student.fullStudentDescription
);

console.log(listPrinted)

bob@dylan:~$ 
bob@dylan:~$ npm run dev 9-main.js
[
  StudentHolberton {
    _firstName: 'Guillaume',
    _lastName: 'Salva',
    _holbertonClass: HolbertonClass { _year: 2020, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'John',
    _lastName: 'Doe',
    _holbertonClass: HolbertonClass { _year: 2020, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'Albert',
    _lastName: 'Clinton',
    _holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'Donald',
    _lastName: 'Bush',
    _holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'Jason',
    _lastName: 'Sandler',
    _holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
  }
]
[
  'Guillaume Salva - 2020 - San Francisco',
  'John Doe - 2020 - San Francisco',
  'Albert Clinton - 2019 - San Francisco',
  'Donald Bush - 2019 - San Francisco',
  'Jason Sandler - 2019 - San Francisco'
]
bob@dylan:~$
```

---

### 10. Vroom <a name='subparagraph10'></a>

Implement a class named <code>Car</code>:

* Constructor attributes: 


  * <code>brand</code> (String)
  * <code>motor</code> (String)
  * <code>color</code> (String)
* Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)
* Add a method named <code>cloneCar</code>. This method should return a new object of the class.

Hint: Symbols in ES6

```
bob@dylan:~$ cat 10-main.js
import Car from "./10-car.js";

class TestCar extends Car {}

const tc1 = new TestCar("Nissan", "Turbo", "Pink");
const tc2 = tc1.cloneCar();

console.log(tc1);
console.log(tc1 instanceof TestCar);

console.log(tc2);
console.log(tc2 instanceof TestCar);

console.log(tc1 == tc2);

bob@dylan:~$ 
bob@dylan:~$ npm run dev 10-main.js
TestCar { _brand: 'Nissan', _motor: 'Turbo', _color: 'Pink' }
true
TestCar { _brand: undefined, _motor: undefined, _color: undefined }
true
false
bob@dylan:~$
```

---

### 11. EVCar <a name='subparagraph11'></a>

Import <code>Car</code> from <code>10-car.js</code>.

Implement a class named <code>EVCar</code> that extends the <code>Car</code> class:

* Constructor attributes: 


  * <code>brand</code> (String)
  * <code>motor</code> (String)
  * <code>color</code> (String)
  * <code>range</code> (String)
* Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)
* For privacy reasons, when <code>cloneCar</code> is called on a EVCar object, the object returned should be an instance of <code>Car</code> instead of <code>EVCar</code>.

```
bob@dylan:~$ cat 100-main.js
import EVCar from './100-evcar.js';

const ec1 = new EVCar("Tesla", "Turbo", "Red", "250");
console.log(ec1);

const ec2 = ec1.cloneCar();
console.log(ec2);

bob@dylan:~$ 
bob@dylan:~$ npm run dev 100-main.js
EVCar {
  _brand: 'Tesla',
  _motor: 'Turbo',
  _color: 'Red',
  _range: '250'
}
Car { _brand: undefined, _motor: undefined, _color: undefined }
bob@dylan:~$
```

---


## Authors
vtiquet - [GitHub Profile](https://github.com/vtiquet)
