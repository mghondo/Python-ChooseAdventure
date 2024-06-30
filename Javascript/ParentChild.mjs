class Parent {
  constructor(name) {
    this.name = name;
  }

  getName() {
    return this.name;
  }
}

class Child extends Parent {
  constructor(name) {
    super(name);
  }

  getMessage() {
    return "Hello " + super.getName();
  }
}

export { Parent, Child };
