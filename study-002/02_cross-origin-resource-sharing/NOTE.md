## === Study Progress ===
- [ ] Cross-origin resource sharing (CORS)
    - [ ] What is CORS (cross-origin resource sharing)?
    - [ ] Same-origin policy
    - [ ] Relaxation of the same-origin policy
    - [ ] Vulnerabilities arising from CORS configuration issues
        - [ ] Server-generated ACAO header from client-specified Origin header
        - [ ] Errors parsing Origin headers
        - [ ] Whitelisted null origin value
        - [ ] Exploiting XSS via CORS trust relationships
        - [ ] Breaking TLS with poorly configured CORS
        - [ ] Intranets and CORS without credentials
    - [ ] How to prevent CORS-based attacks
        - [ ] Proper configuration of cross-origin requests
        - [ ] Only allow trusted sites
        - [ ] Avoid whitelisting null
        - [ ] Avoid wildcards in internal networks
        - [ ] CORS is not a substitute for server-side security policies
    - [ ] Same-origin policy (SOP)
        - [ ] What is the same-origin policy?
        - [ ] Why is the same-origin policy necessary?
        - [ ] How is the same-origin policy implemented?
    - [ ] CORS and the Access-Control-Allow-Origin response header
        - [ ] What is the Access-Control-Allow-Origin response header?
        - [ ] Implementing simple cross-origin resource sharing
        - [ ] Handling cross-origin resource requests with credentials
        - [ ] Relaxation of CORS specifications with wildcards
        - [ ] Pre-flight checks
        - [ ] Does CORS protect against CSRF?

## What is CORS
CORS is a way to relax SOP (Same Origin Policy) on browsers. For example, `mail.google.com` can make request to `slack.com`; however, `slack.com` cannot read data from `mail.google.com` because of the SOP. In this case, one can include CORS to trust `mail.google.com` by `slack.com` with:
```
Access-Control-Allow-Origin: https://mail.google.com
```
But this will only allow accessing "Public" data. In order to allow access to "Private" data, one can add the following header to include a user auth token:
```
Access-Control-Allow-Credentials: true
```

## CORS Attacks
### Simple Origin Reflection
Add `Origin: https://bigb0ss.com` header in your request to see if the server reflects this in its response. e.g., 
```
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https:/bigb0ss.com
Access-Control-Allow-Credentials: true
``` 

### Startswith / Endswith / Insecure Regex Implemenation
Server is only looking for a specific character or URL in CORS requests. This can be bypassed by prefixing or sufixing the specific characters. e.g, 
Startswith
```
GET /api HTTP/1.1
Origin: https://legit.com.evil.net
```
Endswith
```
GET /api HTTP/1.1
Origin: https://NOTzomato.com

HTTP/1.1 200 OK
Content-Security-Policy: frame-ancestors...
Strict-Transport-Security: max-age=3150000
X-Content-Type-Options: nosniff
X-XSS-Protection 1; mode=block;
Access-Control-Allow-Origin: https://NOTzomato.com
Access-Control-Allow-Credentials: true
```

### Null Origin
```
GET /api HTTP/1.1
Origin: null

HTTP/1.1 200 OK
Access-Control-Allow-Origin: null
Access-Control-Allow-Credentials: true
```

Example payload...
```
<iframe sandbox='allow-scripts allow-forms' src='
data:text/html, <!DOCTYPE html>
    <script>
        var req = new XMLHttpRequest();
    </script>
'></iframe>
```

## Pentest Suggestions / Steps
### Detect
1. Try `example.net`, null, anything else
2. Use a request rewrite rule
3. Seek out APIs

### Map
1. Does it only validate the start/end?
2. Does it restrict the protocol?
3. Does it require a valid domain?
4. Are credentials supported?

### Exploit
1. Are there potential exploit chains?
2. Is Vary: Origin specified?
3. Is cache poisoning practical?

