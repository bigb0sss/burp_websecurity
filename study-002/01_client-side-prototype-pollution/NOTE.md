## === Study Progress ===
- [X] Client-side prototype pollution
    - [X] [JavaScript prototypes and inheritance](https://portswigger.net/web-security/prototype-pollution/javascript-prototypes-and-inheritance)
    - [ ] What is prototype pollution?
    - [ ] Finding client-side prototype pollution vulnerabilities
    - [ ] Prototype pollution via browser APIs
    - [ ] Preventing prototype pollution
    - [ ] JavaScript prototypes and inheritance
        - [ ] What is an object in JavaScript?
        - [ ] What is a prototype in JavaScript?
        - [ ] How does object inheritance work in JavaScript?
        - [ ] The prototype chain
        - [ ] Accessing an object's prototype using __proto__
        - [ ] Modifying prototypes
    - [X] [What is prototype pollution?](https://portswigger.net/web-security/prototype-pollution/what-is-prototype-pollution)
        - [X] How do prototype pollution vulnerabilities arise?
        - [X] Prototype pollution sources
            - [X] Prototype pollution via the URL
            - [X] Prototype pollution via JSON input
        - [X] Prototype pollution sinks
        - [X] Prototype pollution gadgets
            - [ ] Example of a prototype pollution gadget
    - [ ] Finding prototype pollution vulnerabilities
        - [ ] Finding prototype pollution sources manually
        - [ ] Finding prototype pollution sources using DOM Invader
        - [ ] Finding prototype pollution gadgets manually
        - [ ] Finding prototype pollution gadgets using DOM Invader
        - [ ] Prototype pollution via the constructor
        - [ ] Prototype pollution in external libraries
    - [ ] Prototype pollution via browser APIs
        - [ ] Prototype pollution via fetch()
        - [ ] Prototype pollution via Object.defineProperty()
    - [ ] How to prevent prototype pollution vulnerabilities
        - [ ] Sanitize property keys
        - [ ] Prevent changes to global prototypes
        - [ ] Prevent an object from inheriting properties
        - [ ] Use safer alternatives where possible

## Prototype Poulltion
Prototype pollution vulnerabilities typically arise when a JavaScript function recursively merges an object containing user-controllable properties into an existing object, without first sanitizing the keys.

Successful exploitation of prototype pollution requires the following key components:
- A prototype pollution source - This is any input that enables you to poison global prototypes with arbitrary properties.
- A DOM XSS sink - In other words, a JavaScript function or DOM element that enables arbitrary code execution.
- An exploitable gadget - This is any property that is passed into a sink without proper filtering or sanitization.

## Recommendations
