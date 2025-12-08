export default class Car {
  constructor(brand, motor, color) {
    this.brand = brand;
    this.motor = motor;
    this.color = color;
  }

  get brand() {
    return this._brand;
  }

  set brand(newBrand) {
    if (newBrand !== undefined && typeof newBrand !== 'string') {
      throw new TypeError('Brand must be a string');
    }
    this._brand = newBrand;
  }

  get motor() {
    return this._motor;
  }

  set motor(newMotor) {
    if (newMotor !== undefined && typeof newMotor !== 'string') {
      throw new TypeError('Motor must be a string');
    }
    this._motor = newMotor;
  }

  get color() {
    return this._color;
  }

  set color(newColor) {
    if (newColor !== undefined && typeof newColor !== 'string') {
      throw new TypeError('Color must be a string');
    }
    this._color = newColor;
  }

  cloneCar() {
    const Species = this.constructor[Symbol.species] || this.constructor;
    return new Species();
  }
}
