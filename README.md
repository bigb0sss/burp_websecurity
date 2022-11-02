# Web Security Academy
## Material Checklist

- [ ] JWT attacks
    - [ ] What are JWTs?
    	- [ ] JWT format
    	- [ ] JWT signature
    	- [ ] JWT vs JWS vs JWE
    	What are JWT attacks?
    	What is the impact of JWT attacks?
    	How do vulnerabilities to JWT attacks arise?
    	How to work with JWTs in Burp Suite
    	Exploiting flawed JWT signature verification
    	    	Accepting arbitrary signatures
    	    	Accepting tokens with no signature
    	Brute-forcing secret keys
    	    	Brute-forcing secret keys using hashcat
    	JWT header parameter injections
    	    	Injecting self-signed JWTs via the jwk parameter
    	    	Injecting self-signed JWTs via the jku parameter
    	    	Injecting self-signed JWTs via the kid parameter
    	    	Other interesting JWT header parameters
    	JWT algorithm confusion
    	How to prevent JWT attacks
    	    	Additional best practice for JWT handling
    	Working with JWTs in Burp Suite
    	    	Viewing the contents of JWTs
    	    	Editing the contents of JWTs
    	    	Adding new signing keys
    	    	Signing JWTs
    	Algorithm confusion attacks
    	    	Symmetric vs asymmetric algorithms
    	    	How do algorithm confusion vulnerabilities arise?
    	    	Performing an algorithm confusion attack
    	    	    	Step 1 - Obtain the server's public key
    	    	    	Step 2 - Convert the public key to a suitable format
    	    	    	Step 3 - Modify your JWT
    	    	    	Step 4 - Sign the JWT using the public key
    	    	Deriving public keys from existing tokens
File upload vulnerabilities
    	What are file upload vulnerabilities?
    	What is the impact of file upload vulnerabilities?
    	How do file upload vulnerabilities arise?
    	How do web servers handle requests for static files?
    	Exploiting unrestricted file uploads to deploy a web shell
    	Exploiting flawed validation of file uploads
    	    	Flawed file type validation
    	    	Preventing file execution in user-accessible directories
    	    	Insufficient blacklisting of dangerous file types
    	Overriding the server configuration
    	Obfuscating file extensions
    	    	Flawed validation of the file's contents
    	    	Exploiting file upload race conditions
    	Race conditions in URL-based file uploads
    	Exploiting file upload vulnerabilities without remote code execution
    	    	Uploading malicious client-side scripts
    	    	Exploiting vulnerabilities in the parsing of uploaded files
    	Uploading files using PUT
    	How to prevent file upload vulnerabilities
OAuth 2.0 authentication vulnerabilities
    	What is OAuth?
    	How does OAuth 2.0 work?
    	    	OAuth authentication
    	How do OAuth authentication vulnerabilities arise?
    	Identifying OAuth authentication
    	Recon
    	Exploiting OAuth authentication vulnerabilities
    	    	Vulnerabilities in the OAuth client application
    	Improper implementation of the implicit grant type
    	Flawed CSRF protection
    	    	Leaking authorization codes and access tokens
    	    	Flawed scope validation
    	    	Unverified user registration
    	Extending OAuth with OpenID Connect
    	Preventing OAuth authentication vulnerabilities
    	How to prevent OAuth authentication vulnerabilities
    	    	For OAuth service providers
    	    	For OAuth client applications
    	OAuth grant types
    	    	What is an OAuth grant type?
    	    	OAuth scopes
    	    	Authorization code grant type
    	    	Implicit grant type
    	OpenID Connect
    	    	What is OpenID Connect?
    	    	How does OpenID Connect work?
    	    	    	OpenID Connect roles
    	    	    	OpenID Connect claims and scopes
    	    	    	ID token
    	    	Identifying OpenID Connect
    	    	OpenID Connect vulnerabilities
    	    	    	Unprotected dynamic client registration
    	    	    	Allowing authorization requests by reference
Put your recon skills to the test
Getting started with the Web Security Academy
    	How the Web Security Academy works
    	Get started with your first topic
    	Find your way around Burp Suite with our video tutorials
    	Keep up with the latest from the Web Security Academy
HTTP Host header attacks
    	What is the HTTP Host header?
    	What is the purpose of the HTTP Host header?
    	    	Virtual hosting
    	    	Routing traffic via an intermediary
    	    	How does the HTTP Host header solve this problem?
    	What is an HTTP Host header attack?
    	How do HTTP Host header vulnerabilities arise?
    	Exploiting HTTP Host header vulnerabilities
    	How to prevent HTTP Host header attacks
    	How to identify and exploit HTTP Host header vulnerabilities
    	    	How to test for vulnerabilities using the HTTP Host header
    	    	    	Supply an arbitrary Host header
    	    	    	Check for flawed validation
    	    	    	Send ambiguous requests
    	    	    	Inject host override headers
    	    	How to exploit the HTTP Host header
    	    	    	Password reset poisoning
    	    	    	Web cache poisoning via the Host header
    	    	    	Exploiting classic server-side vulnerabilities
    	    	    	Accessing restricted functionality
    	    	    	Accessing internal websites with virtual host brute-forcing
    	    	    	Routing-based SSRF
    	    	    	Connection state attacks
    	    	    	SSRF via a malformed request line
    	    	Password reset poisoning
    	    	    	How does a password reset work?
    	    	    	How to construct a password reset poisoning attack
SQL injection
    	What is SQL injection (SQLi)?
    	What is the impact of a successful SQL injection attack?
    	SQL injection examples
    	Retrieving hidden data
    	Subverting application logic
    	Retrieving data from other database tables
    	Examining the database
    	Blind SQL injection vulnerabilities
    	How to detect SQL injection vulnerabilities
    	SQL injection in different parts of the query
    	SQL injection in different contexts
    	Second-order SQL injection
    	Database-specific factors
    	How to prevent SQL injection
    	SQL injection UNION attacks
    	    	Determining the number of columns required in an SQL injection UNION attack
    	    	Finding columns with a useful data type in an SQL injection UNION attack
    	    	Using an SQL injection UNION attack to retrieve interesting data
    	    	Retrieving multiple values within a single column
    	Examining the database in SQL injection attacks
    	    	Querying the database type and version
    	    	Listing the contents of the database
    	    	    	Equivalent to information schema on Oracle
    	Blind SQL injection
    	    	What is blind SQL injection?
    	    	Exploiting blind SQL injection by triggering conditional responses
    	    	Inducing conditional responses by triggering SQL errors
    	    	Exploiting blind SQL injection by triggering time delays
    	    	Exploiting blind SQL injection using out-of-band (OAST) techniques
    	    	How to prevent blind SQL injection attacks?
    	SQL injection cheat sheet
    	    	String concatenation
    	    	Substring
    	    	Comments
    	    	Database version
    	    	Database contents
    	    	Conditional errors
    	    	Batched (or stacked) queries
    	    	Time delays
    	    	Conditional time delays
    	    	DNS lookup
    	    	DNS lookup with data exfiltration
Cross-site scripting
    	What is cross-site scripting (XSS)?
    	How does XSS work?
    	XSS proof of concept
    	What are the types of XSS attacks?
    	Reflected cross-site scripting
    	Stored cross-site scripting
    	DOM-based cross-site scripting
    	What can XSS be used for?
    	Impact of XSS vulnerabilities
    	How to find and test for XSS vulnerabilities
    	Content security policy
    	Dangling markup injection
    	How to prevent XSS attacks
    	Common questions about cross-site scripting
    	Reflected XSS
    	    	What is reflected cross-site scripting?
    	    	Impact of reflected XSS attacks
    	    	Reflected XSS in different contexts
    	    	How to find and test for reflected XSS vulnerabilities
    	    	Common questions about reflected cross-site scripting
    	Cross-site scripting (XSS) cheat sheet
    	    	Event handlers
    	    	    	Event handlers that do not require user interaction
    	    	    	Event handlers that do require user interaction
    	    	Consuming tags
    	    	File upload attacks
    	    	Restricted characters
    	    	Frameworks
    	    	Protocols
    	    	Other useful attributes
    	    	Special tags
    	    	Encoding
    	    	Obfuscation
    	    	Client-side template injection
    	    	    	VueJS reflected
    	    	    	AngularJS sandbox escapes reflected
    	    	    	DOM based AngularJS sandbox escapes
    	    	    	AngularJS CSP bypasses
    	    	Scriptless attacks
    	    	    	Dangling markup
    	    	Polyglots
    	    	WAF bypass global objects
    	    	Content types
    	    	Response content types
    	    	Impossible labs
    	    	Prototype pollution
    	    	Classic vectors (XSS crypt)
    	Stored XSS
    	    	What is stored cross-site scripting?
    	    	Impact of stored XSS attacks
    	    	Stored XSS in different contexts
    	    	How to find and test for stored XSS vulnerabilities
    	DOM-based XSS
    	    	What is DOM-based cross-site scripting?
    	    	How to test for DOM-based cross-site scripting
    	    	    	Testing HTML sinks
    	    	    	Testing JavaScript execution sinks
    	    	    	Testing for DOM XSS using DOM Invader
    	    	Exploiting DOM XSS with different sources and sinks
    	    	    	Sources and sinks in third-party dependencies
    	    	DOM XSS in jQuery
    	    	DOM XSS in AngularJS
    	    	DOM XSS combined with reflected and stored data
    	    	Which sinks can lead to DOM-XSS vulnerabilities?
    	    	How to prevent DOM-XSS vulnerabilities
    	Exploiting cross-site scripting vulnerabilities
    	    	Exploiting cross-site scripting to steal cookies
    	    	Exploiting cross-site scripting to capture passwords
    	    	Exploiting cross-site scripting to perform CSRF
    	Cross-site scripting contexts
    	    	XSS between HTML tags
    	    	XSS in HTML tag attributes
    	    	XSS into JavaScript
    	    	    	Terminating the existing script
    	    	    	Breaking out of a JavaScript string
    	    	    	Making use of HTML-encoding
    	    	    	XSS in JavaScript template literals
    	    	XSS via client-side template injection
    	    	Client-side template injection
    	    	    	What is client-side template injection?
    	    	    	What is the AngularJS sandbox?
    	    	    	How does the AngularJS sandbox work?
    	    	    	How does an AngularJS sandbox escape work?
    	    	    	How does an AngularJS CSP bypass work?
    	    	    	How to prevent client-side template injection vulnerabilities
    	Content security policy
    	    	What is CSP (content security policy)?
    	    	Mitigating XSS attacks using CSP
    	    	Mitigating dangling markup attacks using CSP
    	    	Bypassing CSP with policy injection
    	    	Protecting against clickjacking using CSP
    	Dangling markup injection
    	    	What is dangling markup injection?
    	    	How to prevent dangling markup attacks
    	How to prevent XSS
    	    	Encode data on output
    	    	Validate input on arrival
    	    	    	Whitelisting vs blacklisting
    	    	Allowing "safe" HTML
    	    	How to prevent XSS using a template engine
    	    	How to prevent XSS in PHP
    	    	How to prevent XSS client-side in JavaScript
    	    	How to prevent XSS in jQuery
    	    	Mitigating XSS using content security policy (CSP)
Cross-site request forgery (CSRF)
    	What is CSRF?
    	What is the impact of a CSRF attack?
    	How does CSRF work?
    	How to construct a CSRF attack
    	How to deliver a CSRF exploit
    	Preventing CSRF attacks
    	Common CSRF vulnerabilities
    	    	Validation of CSRF token depends on request method
    	    	Validation of CSRF token depends on token being present
    	    	CSRF token is not tied to the user session
    	    	CSRF token is tied to a non-session cookie
    	    	CSRF token is simply duplicated in a cookie
    	Referer-based defenses against CSRF
    	    	Validation of Referer depends on header being present
    	    	Validation of Referer can be circumvented
    	Defending against CSRF with SameSite cookies
    	XSS vs CSRF
    	    	What is the difference between XSS and CSRF?
    	    	Can CSRF tokens prevent XSS attacks?
    	CSRF tokens
    	    	What are CSRF tokens?
    	    	How should CSRF tokens be generated?
    	    	How should CSRF tokens be transmitted?
    	    	How should CSRF tokens be validated?
XML external entity (XXE) injection
    	What is XML external entity injection?
    	How do XXE vulnerabilities arise?
    	What are the types of XXE attacks?
    	Exploiting XXE to retrieve files
    	Exploiting XXE to perform SSRF attacks
    	Blind XXE vulnerabilities
    	Finding hidden attack surface for XXE injection
    	    	XInclude attacks
    	    	XXE attacks via file upload
    	    	XXE attacks via modified content type
    	How to find and test for XXE vulnerabilities
    	How to prevent XXE vulnerabilities
    	XML entities
    	    	What is XML?
    	    	What are XML entities?
    	    	What is document type definition?
    	    	What are XML custom entities?
    	    	What are XML external entities?
    	Finding and exploiting blind XXE vulnerabilities
    	    	What is blind XXE?
    	    	Detecting blind XXE using out-of-band (OAST) techniques
    	    	Exploiting blind XXE to exfiltrate data out-of-band
    	    	Exploiting blind XXE to retrieve data via error messages
    	    	Exploiting blind XXE by repurposing a local DTD
    	    	    	Locating an existing DTD file to repurpose
Clickjacking (UI redressing)
    	What is clickjacking?
    	How to construct a basic clickjacking attack
    	    	Clickbandit
    	Clickjacking with prefilled form input
    	Frame busting scripts
    	Combining clickjacking with a DOM XSS attack
    	Multistep clickjacking
    	How to prevent clickjacking attacks
    	    	X-Frame-Options
    	    	Content Security Policy (CSP)
Cross-origin resource sharing (CORS)
    	What is CORS (cross-origin resource sharing)?
    	Same-origin policy
    	Relaxation of the same-origin policy
    	Vulnerabilities arising from CORS configuration issues
    	    	Server-generated ACAO header from client-specified Origin header
    	    	Errors parsing Origin headers
    	    	Whitelisted null origin value
    	    	Exploiting XSS via CORS trust relationships
    	    	Breaking TLS with poorly configured CORS
    	    	Intranets and CORS without credentials
    	How to prevent CORS-based attacks
    	    	Proper configuration of cross-origin requests
    	    	Only allow trusted sites
    	    	Avoid whitelisting null
    	    	Avoid wildcards in internal networks
    	    	CORS is not a substitute for server-side security policies
    	Same-origin policy (SOP)
    	    	What is the same-origin policy?
    	    	Why is the same-origin policy necessary?
    	    	How is the same-origin policy implemented?
    	CORS and the Access-Control-Allow-Origin response header
    	    	What is the Access-Control-Allow-Origin response header?
    	    	Implementing simple cross-origin resource sharing
    	    	Handling cross-origin resource requests with credentials
    	    	Relaxation of CORS specifications with wildcards
    	    	Pre-flight checks
    	    	Does CORS protect against CSRF?
Server-side request forgery (SSRF)
    	What is SSRF?
    	What is the impact of SSRF attacks?
    	Common SSRF attacks
    	    	SSRF attacks against the server itself
    	    	SSRF attacks against other back-end systems
    	Circumventing common SSRF defenses
    	    	SSRF with blacklist-based input filters
    	    	SSRF with whitelist-based input filters
    	    	Bypassing SSRF filters via open redirection
    	Blind SSRF vulnerabilities
    	Finding hidden attack surface for SSRF vulnerabilities
    	    	Partial URLs in requests
    	    	URLs within data formats
    	    	SSRF via the Referer header
    	Blind SSRF vulnerabilities
    	    	What is blind SSRF?
    	    	What is the impact of blind SSRF vulnerabilities?
    	    	How to find and exploit blind SSRF vulnerabilities
HTTP request smuggling
    	What is HTTP request smuggling?
    	What happens in an HTTP request smuggling attack?
    	How do HTTP request smuggling vulnerabilities arise?
    	How to perform an HTTP request smuggling attack
    	    	CL.TE vulnerabilities
    	    	TE.CL vulnerabilities
    	    	TE.TE behavior: obfuscating the TE header
    	How to identify HTTP request smuggling vulnerabilities
    	How to exploit HTTP request smuggling vulnerabilities
    	Advanced HTTP request smuggling
    	Browser-powered request smuggling
    	How to prevent HTTP request smuggling vulnerabilities
    	Finding HTTP request smuggling vulnerabilities
    	    	Finding HTTP request smuggling vulnerabilities using timing techniques
    	    	    	Finding CL.TE vulnerabilities using timing techniques
    	    	    	Finding TE.CL vulnerabilities using timing techniques
    	    	Confirming HTTP request smuggling vulnerabilities using differential responses
    	    	    	Confirming CL.TE vulnerabilities using differential responses
    	    	    	Confirming TE.CL vulnerabilities using differential responses
    	Exploiting HTTP request smuggling vulnerabilities
    	    	Using HTTP request smuggling to bypass front-end security controls
    	    	Revealing front-end request rewriting
    	    	Bypassing client authentication
    	    	Capturing other users' requests
    	    	Using HTTP request smuggling to exploit reflected XSS
    	    	Using HTTP request smuggling to turn an on-site redirect into an open redirect
    	    	    	Turning root-relative redirects into open redirects
    	    	Using HTTP request smuggling to perform web cache poisoning
    	    	Using HTTP request smuggling to perform web cache deception
    	Advanced request smuggling
    	    	HTTP/2 request smuggling
    	    	    	HTTP/2 message length
    	    	    	HTTP/2 downgrading
    	    	    	H2.CL vulnerabilities
    	    	    	H2.TE vulnerabilities
    	    	Response queue poisoning
    	    	Request smuggling via CRLF injection
    	    	HTTP/2 request splitting
    	    	    	Accounting for front-end rewriting
    	    	HTTP request tunnelling
    	    	Response queue poisoning
    	    	    	What is the impact of response queue poisoning?
    	    	    	How to construct a response queue poisoning attack
    	    	    	    	Understanding the aftermath of request smuggling
    	    	    	    	Smuggling a complete request
    	    	    	    	Desynchronizing the response queue
    	    	    	    	Stealing other users' responses
    	    	HTTP request tunnelling
    	    	    	Request tunnelling with HTTP/2
    	    	    	Leaking internal headers via HTTP/2 request tunnelling
    	    	    	Blind request tunnelling
    	    	    	Non-blind request tunnelling using HEAD
    	    	    	Web cache poisoning via HTTP/2 request tunnelling
    	    	HTTP/2 downgrading
    	    	    	What risks are associated with HTTP/2 downgrading?
    	    	HTTP/2-exclusive vectors
    	    	    	Injecting via header names
    	    	    	Injecting via pseudo-headers
    	    	    	    	Supplying an ambiguous host
    	    	    	    	Supplying an ambiguous path
    	    	    	    	Injecting a full request line
    	    	    	    	Injecting a URL prefix
    	    	    	    	Injecting newlines into pseudo-headers
    	Browser-powered request smuggling
    	    	CL.0 request smuggling
    	    	Client-side desync
    	    	Pause-based desync
    	    	CL.0 request smuggling
    	    	    	Testing for CL.0 vulnerabilities
    	    	    	Eliciting CL.0 behavior
    	    	    	Exploiting CL.0 vulnerabilities
    	    	    	H2.0 vulnerabilities
    	    	    	How to prevent CL.0 vulnerabilities
    	    	Client-side desync
    	    	    	What is a client-side desync?
    	    	    	Testing for client-side desync vulnerabilities
    	    	    	    	Probing for client-side desync vectors
    	    	    	    	Confirming the desync vector in Burp
    	    	    	    	Building a proof of concept in a browser
    	    	    	    	Handling redirects
    	    	    	Exploiting client-side desync vulnerabilities
    	    	    	    	Client-side variations of classic attacks
    	    	    	    	Client-side cache poisoning
    	    	    	Poisoning the cache with a redirect
    	    	    	Triggering the resource import
    	    	    	Delivering a payload
    	    	    	    	Pivoting attacks against internal infrastructure
    	    	    	How to prevent client-side desync vulnerabilities
    	    	Pause-based desync
    	    	    	Server-side pause-based desync
    	    	    	    	Testing for pause-based CL.0 vulnerabilities
    	    	    	Client-side pause-based desync
    	    	    	How to prevent pause-based desync vulnerabilities
OS command injection
    	What is OS command injection?
    	Executing arbitrary commands
    	Useful commands
    	Blind OS command injection vulnerabilities
    	    	Detecting blind OS command injection using time delays
    	    	Exploiting blind OS command injection by redirecting output
    	    	Exploiting blind OS command injection using out-of-band (OAST) techniques
    	Ways of injecting OS commands
    	How to prevent OS command injection attacks
Server-side template injection
    	What is server-side template injection?
    	What is the impact of server-side template injection?
    	How do server-side template injection vulnerabilities arise?
    	Constructing a server-side template injection attack
    	    	Detect
    	    	Identify
    	    	Exploit
    	How to prevent server-side template injection vulnerabilities
    	Exploiting server-side template injection vulnerabilities
    	    	Read
    	    	    	Learn the basic template syntax
    	    	    	Read about the security implications
    	    	    	Look for known exploits
    	    	Explore
    	    	    	Developer-supplied objects
    	    	Create a custom attack
    	    	    	Constructing a custom exploit using an object chain
    	    	    	Constructing a custom exploit using developer-supplied objects
Insecure deserialization
    	What is serialization?
    	    	Serialization vs deserialization
    	What is insecure deserialization?
    	How do insecure deserialization vulnerabilities arise?
    	What is the impact of insecure deserialization?
    	How to exploit insecure deserialization vulnerabilities
    	How to prevent insecure deserialization vulnerabilities
    	Exploiting insecure deserialization vulnerabilities
    	    	How to identify insecure deserialization
    	    	    	PHP serialization format
    	    	    	Java serialization format
    	    	Manipulating serialized objects
    	    	    	Modifying object attributes
    	    	    	Modifying data types
    	    	Using application functionality
    	    	Magic methods
    	    	Injecting arbitrary objects
    	    	Gadget chains
    	    	    	Working with pre-built gadget chains
    	    	    	Working with documented gadget chains
    	    	Creating your own exploit
    	    	PHAR deserialization
    	    	Exploiting deserialization using memory corruption
Directory traversal
    	What is directory traversal?
    	Reading arbitrary files via directory traversal
    	Common obstacles to exploiting file path traversal vulnerabilities
    	How to prevent a directory traversal attack
Access control vulnerabilities and privilege escalation
    	What is access control?
    	    	Vertical access controls
    	    	Horizontal access controls
    	    	Context-dependent access controls
    	Examples of broken access controls
    	    	Vertical privilege escalation
    	    	Horizontal privilege escalation
    	    	Horizontal to vertical privilege escalation
    	    	Insecure direct object references
    	    	Access control vulnerabilities in multi-step processes
    	    	Referer-based access control
    	    	Location-based access control
    	How to prevent access control vulnerabilities
    	Access control security models
    	    	What are access control security models?
    	    	Programmatic access control
    	    	Discretionary access control (DAC)
    	    	Mandatory access control (MAC)
    	    	Role-based access control (RBAC)
    	Insecure direct object references (IDOR)
    	    	What are insecure direct object references (IDOR)?
    	    	IDOR examples
    	    	    	IDOR vulnerability with direct reference to database objects
    	    	    	IDOR vulnerability with direct reference to static files
Authentication vulnerabilities
    	What is authentication?
    	    	What is the difference between authentication and authorization?
    	How do authentication vulnerabilities arise?
    	What is the impact of vulnerable authentication?
    	Vulnerabilities in authentication mechanisms
    	    	Vulnerabilities in third-party authentication mechanisms
    	Preventing attacks on your own authentication mechanisms
    	Vulnerabilities in password-based login
    	    	Brute-force attacks
    	    	    	Brute-forcing usernames
    	    	    	Brute-forcing passwords
    	    	    	Username enumeration
    	    	Flawed brute-force protection
    	    	    	Account locking
    	    	    	User rate limiting
    	    	HTTP basic authentication
    	Vulnerabilities in multi-factor authentication
    	    	Two-factor authentication tokens
    	    	Bypassing two-factor authentication
    	    	Flawed two-factor verification logic
    	    	Brute-forcing 2FA verification codes
    	Vulnerabilities in other authentication mechanisms
    	    	Keeping users logged in
    	    	Resetting user passwords
    	    	    	Sending passwords by email
    	    	    	Resetting passwords using a URL
    	    	Changing user passwords
    	Authentication lab usernames
    	Authentication lab passwords
    	How to secure your authentication mechanisms
    	    	Take care with user credentials
    	    	Don't count on users for security
    	    	Prevent username enumeration
    	    	Implement robust brute-force protection
    	    	Triple-check your verification logic
    	    	Don't forget supplementary functionality
    	    	Implement proper multi-factor authentication
Business logic vulnerabilities
    	What are business logic vulnerabilities?
    	How do business logic vulnerabilities arise?
    	What is the impact of business logic vulnerabilities?
    	What are some examples of business logic vulnerabilities?
    	How to prevent business logic vulnerabilities
    	Examples of business logic vulnerabilities
    	    	Excessive trust in client-side controls
    	    	Failing to handle unconventional input
    	    	Making flawed assumptions about user behavior
    	    	    	Trusted users won't always remain trustworthy
    	    	    	Users won't always supply mandatory input
    	    	    	Users won't always follow the intended sequence
    	    	Domain-specific flaws
    	    	Providing an encryption oracle
Testing for WebSockets security vulnerabilities
    	WebSockets
    	Manipulating WebSocket traffic
    	    	Intercepting and modifying WebSocket messages
    	    	Replaying and generating new WebSocket messages
    	    	Manipulating WebSocket connections
    	WebSockets security vulnerabilities
    	    	Manipulating WebSocket messages to exploit vulnerabilities
    	    	Manipulating the WebSocket handshake to exploit vulnerabilities
    	    	Using cross-site WebSockets to exploit vulnerabilities
    	How to secure a WebSocket connection
    	What are WebSockets?
    	    	What is the difference between HTTP and WebSockets?
    	    	How are WebSocket connections established?
    	    	What do WebSocket messages look like?
    	Cross-site WebSocket hijacking
    	    	What is cross-site WebSocket hijacking?
    	    	What is the impact of cross-site WebSocket hijacking?
    	    	Performing a cross-site WebSocket hijacking attack
DOM-based vulnerabilities
    	What is the DOM?
    	Taint-flow vulnerabilities
    	    	What is taint flow?
    	    	Common sources
    	    	Which sinks can lead to DOM-based vulnerabilities?
    	    	How to prevent DOM-based taint-flow vulnerabilities
    	DOM clobbering
    	Controlling the web message source
    	    	What is the impact of DOM-based web message vulnerabilities?
    	    	How to construct an attack using web messages as the source
    	    	Origin verification
    	    	Which sinks can lead to DOM-based web message vulnerabilities?
    	DOM-based open redirection
    	    	What is DOM-based open redirection?
    	    	What is the impact of DOM-based open redirection?
    	    	Which sinks can lead to DOM-based open-redirection vulnerabilities?
    	    	How to prevent DOM-based open-redirection vulnerabilities
    	DOM-based cookie manipulation
    	    	What is DOM-based cookie manipulation?
    	    	What is the impact of a DOM-based cookie-manipulation attack?
    	    	Which sinks can lead to DOM-based cookie-manipulation vulnerabilities?
    	    	How to prevent DOM-based cookie-manipulation vulnerabilities
    	DOM-based JavaScript injection
    	    	What is DOM-based JavaScript injection?
    	    	What is the impact of a DOM-based JavaScript-injection attack?
    	    	Which sinks can lead to DOM-based JavaScript-injection vulnerabilities?
    	    	How to prevent DOM-based JavaScript-injection vulnerabilities
    	DOM-based document-domain manipulation
    	    	What is DOM-based document-domain manipulation?
    	    	Which sinks can lead to DOM-based document-domain manipulation vulnerabilities?
    	    	How to prevent DOM-based document-domain manipulation vulnerabilities
    	DOM-based WebSocket-URL poisoning
    	    	What is DOM-based WebSocket-URL poisoning?
    	    	What is the impact of WebSocket-URL poisoning?
    	    	Which sinks can lead to WebSocket-URL poisoning vulnerabilities?
    	    	How to prevent DOM-based WebSocket-URL poisoning vulnerabilities
    	DOM-based link manipulation
    	    	What is DOM-based link manipulation?
    	    	What is the impact of a DOM-based link-manipulation attack?
    	    	Which sinks can lead to DOM-based link-manipulation vulnerabilities?
    	    	How to prevent DOM-based link-manipulation vulnerabilities
    	Web message manipulation
    	    	What is DOM-based web message manipulation?
    	    	Which sinks can lead to DOM-based web-message manipulation vulnerabilities?
    	    	How to prevent DOM-based web message manipulation
    	DOM-based Ajax request-header manipulation
    	    	What is DOM-based Ajax request-header manipulation?
    	    	What is the impact of DOM-based Ajax request-header manipulation?
    	    	Which sinks can lead to DOM-based Ajax request-header manipulation vulnerabilities?
    	    	How to prevent DOM-based Ajax request-header manipulation
    	DOM-based local file-path manipulation
    	    	What is DOM-based local file-path manipulation?
    	    	What is the impact of DOM-based local file-path manipulation?
    	    	Which sinks can lead to DOM-based local file-path manipulation vulnerabilities?
    	    	How to prevent DOM-based local file-path manipulation vulnerabilities
    	DOM-based client-side SQL injection
    	    	What is DOM-based client-side SQL injection?
    	    	What is the impact of DOM-based client-side SQL injection?
    	    	Which sinks can lead to DOM-based client-side SQL-injection vulnerabilities?
    	    	How to prevent DOM-based client-side SQL-injection vulnerabilities
    	DOM-based HTML5-storage manipulation
    	    	What is DOM-based HTML5-storage manipulation?
    	    	Which sinks can lead to DOM-based HTML5-storage manipulation vulnerabilities?
    	    	How to prevent DOM-based HTML5-storage manipulation vulnerabilities
    	DOM-based client-side XPath injection
    	    	What is DOM-based XPath injection?
    	    	What is the impact of DOM-based XPath injection?
    	    	Which sinks can lead to XPath-injection vulnerabilities?
    	    	How to prevent DOM-based XPath-injection vulnerabilities
    	DOM-based client-side JSON injection
    	    	What is DOM-based JSON injection?
    	    	What is the impact of a DOM-based JSON-injection attack?
    	    	Which sinks can lead to DOM-based JSON-injection vulnerabilities?
    	    	How to prevent client-side JSON-injection vulnerabilities?
    	DOM-data manipulation
    	    	What is DOM-data manipulation?
    	    	What is the impact of DOM-data manipulation?
    	    	Which sinks can lead to DOM-data manipulation vulnerabilities?
    	    	How to prevent DOM-data manipulation vulnerabilities
    	DOM-based denial of service
    	    	What is DOM-based denial of service?
    	    	Which sinks can lead to DOM-based denial-of-service vulnerabilities?
    	    	How to prevent DOM-based denial-of-service vulnerabilities
    	DOM clobbering
    	    	What is DOM clobbering?
    	    	How to exploit DOM-clobbering vulnerabilities
    	    	How to prevent DOM-clobbering attacks
Web cache poisoning
    	What is web cache poisoning?
    	    	Web cache poisoning research
    	    	How does a web cache work?
    	What is the impact of a web cache poisoning attack?
    	Constructing a web cache poisoning attack
    	    	Identify and evaluate unkeyed inputs
    	Param Miner
    	    	Elicit a harmful response from the back-end server
    	    	Get the response cached
    	Exploiting web cache poisoning vulnerabilities
    	How to prevent web cache poisoning vulnerabilities
    	Exploiting cache design flaws
    	    	Using web cache poisoning to deliver an XSS attack
    	    	Using web cache poisoning to exploit unsafe handling of resource imports
    	    	Using web cache poisoning to exploit cookie-handling vulnerabilities
    	    	Using multiple headers to exploit web cache poisoning vulnerabilities
    	    	Exploiting responses that expose too much information
    	    	    	Cache-control directives
    	    	    	Vary header
    	    	Using web cache poisoning to exploit DOM-based vulnerabilities
    	    	Chaining web cache poisoning vulnerabilities
    	Exploiting cache implementation flaws
    	    	Cache key flaws
    	    	Cache probing methodology
    	    	    	Identify a suitable cache oracle
    	    	    	Probe key handling
    	    	    	Identify an exploitable gadget
    	    	Exploiting cache key flaws
    	    	    	Unkeyed port
    	    	    	Unkeyed query string
    	    	    	Unkeyed query parameters
    	    	    	Cache parameter cloaking
    	    	    	Normalized cache keys
    	    	    	Cache key injection
    	    	Poisoning internal caches
    	    	    	How to identify internal caches
    	    	    	Testing internal caches safely
Information disclosure vulnerabilities
    	What is information disclosure?
    	How do information disclosure vulnerabilities arise?
    	What is the impact of information disclosure vulnerabilities?
    	    	How to assess the severity of information disclosure vulnerabilities
    	Exploiting information disclosure
    	How to prevent information disclosure vulnerabilities
    	How to find and exploit information disclosure vulnerabilities
    	    	How to test for information disclosure vulnerabilities
    	    	    	Fuzzing
    	    	    	Using Burp Scanner
    	    	    	Using Burp's engagement tools
    	    	    	Engineering informative responses
    	    	Common sources of information disclosure
    	    	    	Files for web crawlers
    	    	    	Directory listings
    	    	    	Developer comments
    	    	    	Error messages
    	    	    	Debugging data
    	    	    	User account pages
    	    	    	Source code disclosure via backup files
    	    	    	Information disclosure due to insecure configuration
    	    	    	Version control history
Reference
    	Augmenting your manual testing with Burp Scanner
    	    	Scanning a specific request
    	    	Scanning custom insertion points
    	    	Scanning non-standard data structures
    	Obfuscating attacks using encodings
    	    	Context-specific decoding
    	    	Decoding discrepancies
    	    	Obfuscation via URL encoding
    	    	Obfuscation via double URL encoding
    	    	Obfuscation via HTML encoding
    	    	    	Leading zeros
    	    	Obfuscation via XML encoding
    	    	Obfuscation via unicode escaping
    	    	Obfuscation via hex escaping
    	    	Obfuscation via octal escaping
    	    	Obfuscation via multiple encodings
    	    	Obfuscation via the SQL CHAR() function
