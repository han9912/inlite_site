var value = 1;

var foo = {
    value: 2,
    bar: function() {
        return this.value;
    }
}

console.log(foo.bar());

// example of instance
class Car {
    setName(name) {
        this.name = name
    }
    getName(){
        return this.name
    }
}
const myCar = new Car()
myCar.setName('hello')
console.log(myCar.getName())

const obj = {
    value: 1,
    hello: function() {
        console.log(this.value)
    }
}

obj.hello()
const