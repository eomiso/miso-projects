// models/calc.js
class Calculator {
  a: number;
  b: number;

  constructor(a: number, b: number) {
    this.a = a;
    this.b = b;
  }

  sum() {
    return this.a + this.b;
  }
}

export default Calculator;
