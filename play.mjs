import { doSomething } from "./Javascript/promise.mjs";
import { Parent, Child } from "./Javascript/ParentChild.mjs";

const bob = new Parent("Bob");

console.log(bob.getName());
// bob.getMessage();

const jack = new Child("Jack");
jack.getMessage();
console.log(jack.getMessage());
