# HW3

Chenlin Liu	PID:A53284481

Yihui Qian	PID:A53277815

## The QUIC paper

### What major problem does QUIC intend to solve?

QUIC is a new transport designed from the ground up to improve performance for HTTPS traffic and to enable rapid deployment and continued evolution of transport mechanisms. 

Growth in latency-sensitive web services and  secure traffic both make delay a big problem.  However, due to several reasons such as protocol entrenchment, implementation entrenchment, handshake delay and head-of-line blocking delay,  the deployment of transport modifications for the web is difficult. QUIC intend to solve this problem. 

### Briefly describe the mechanisms that QUIC is based on

- QUIC is a user-space transport with UDP as a substrate.  Building QUIC in user-space facilitated its deployment as part of various applications and enabled iterative changes to occur at application update timescales. The use of UDP allows QUIC packets to traverse middleboxes.
- QUIC is an encrypted transport: packets are authenticated and encrypted, preventing modification and limiting ossification of the protocol by middleboxes.
- QUIC uses a cryptographic handshake that minimizes handshake latency for most connections.
- QUIC eliminates head-of-line blocking delays by using a lightweight data-structuring abstraction called streams.

### Why this paper now?

- A general trend: demands on reducing web latency are unprecedented. Also,  the Internet is rapidly shifting from insecure to secure traffic, which adds delays.
- For the original protocols: the following limitations hampered the  deployment of transport modifications, such as a QUIC-like design.
  - Protocol Entrenchment:  modifying protocols like TCP remains challenging due to its ossification by middleboxes.
  - Implementation Entrenchment:  pushing changes to protocols typically requires OS upgrades, which limits the deployment and iteration velocity of even simple networking changes.
  - Handshake Delay:  costs of layering have become increasingly visible with increasing latency demands on the HTTPS stack.  Short transfers are most impacted by unnecessary handshake round trips.
  - Head-of-line Blocking Delay:  TCP’s bytestream abstraction prevents applications from controlling the framing of their communications and imposes a "latency tax" on application frames whose delivery must wait for retransmissions of previously lost TCP segments.

## TritonHTTP test cases

- 200 error code response
  - request for HTML
  - request for JPEG (subdirectory)
  - request for PNG (subdirectory)
  - GET /
- non-200 error code responses
  - handles 404 for files that aren’t found
  - handles 404 for URLs that escape the doc root
  - malformed HTTP requests 400 error
    - missing GET header
    - wrong format GET header
      - no URL
      - no HTTP version
    - missing HOST
    - wrong format HOST header
      - wrong HOST name
      - empty
    - wrong CR LF and missing CR LF
- pipelined request

## 200 error code response

### Request for HTML

```html
GET /index.html HTTP/1.1<CR><LF>
Host: www.cs.ucsd.edu<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: an HTML file called index.html exists in the doc root.

Expected behavior: the server returns a 200 status code reply followed by the text of the index.html file

### Request for JPEG (subdirectory)

```html
GET /images/myimg.jpg HTTP/1.1<CR><LF>
Host: www.cs.ucsd.edu<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: an jpeg file called myimg.jpg exists in the subdirectory /images.

Expected behavior: the server returns a 200 status code followed by the binary data of the myimg. jpg file. 

### Request for PNG (subdirectory)

```html
GET /images/myimg2.png HTTP/1.1<CR><LF>
Host: www.cs.ucsd.edu<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: an png file called myimg2.png exists in the subdirectory /images.

Expected behavior: the server returns a 200 status code followed by the binary data of the myimg2. png file. 

### GET /

```html
GET / HTTP/1.1<CR><LF>
Host: www.cs.ucsd.edu<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: an HTML file called index.html exists in the doc root.

Expected behavior: the server returns a 200 status code reply followed by the text of the index.html file

## 404 error code responses

### 404 for files that aren’t found

```html
GET /images/myimg3.jpg HTTP/1.1<CR><LF>
Host: www.cs.ucsd.edu<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: no file called myimg3.jpg exists in the subdirectory /images.

Expected behavior: the server returns a 404 status code because file /images/myimg3.jpg are not found.

### 404 for URLs that escape the doc root

```html
GET /myhtml/myhtml.html HTTP/1.1<CR><LF>
Host: www.cs.ucsd.edu<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: no subdirectory called /myhtml exists in the doc root.

Expected behavior: the server returns a 404 status code because subdirectory /myhtml are not found.

## 400 error code responses (malformed)

### Missing GET header

```html
Host: www.cs.ucsd.edu<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: none

Expected behavior: the server returns a 400 status code because the GET header is missing.

### Wrong format GET header - missing URL

```html
GET HTTP/1.1<CR><LF>
Host: www.cs.ucsd.edu<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: none

Expected behavior: the server returns a 400 status code because the URL of GET header is missing.

### Wrong format GET header - missing HTTP version

```html
GET /index.html<CR><LF>
Host: www.cs.ucsd.edu<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: none

Expected behavior: the server returns a 400 status code because the HTTP version of GET header is missing.

### Missing HOST header

```html
GET /index.html HTTP/1.1<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: none

Expected behavior: the server returns a 400 status code because the HOST header is missing.

### Wrong format HOST header - wrong HOST name

```html
GET /index.html HTTP/1.1<CR><LF>
Host: 12345abcde<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: none

Expected behavior: the server returns a 400 status code because the HOST name is wrong.

### Wrong format HOST header - empty

```html
GET /index.html HTTP/1.1<CR><LF>
Host: <CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: none

Expected behavior: the server returns a 400 status code because the HOST header is empty.

### Missing CR LF

```html
GET /index.html HTTP/1.1
Host: www.cs.ucsd.edu
User-Agent: MyClient/1.0
```

Pre-conditions: none

Expected behavior: the server returns a 400 status code because the some CR LF are missing.

## Pipelined request

### Pipelined request of an HTML file and a JPEG file

```html
GET / HTTP/1.1<CR><LF>
Host: www.cs.ucsd.edu<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
GET /image/myimg.jpg HTTP/1.1<CR><LF>
Host: www.cs.ucsd.edu<CR><LF>
User-Agent: MyClient/1.0<CR><LF>
<CR><LF>
```

Pre-conditions: an HTML file called index.html exists in the doc root and a jpeg file called myimg.jpg exists in the subdirectory /images.

Expected behavior: the server returns a 200 status code reply followed by the text of the index.html file and the binary data of the myimg. jpg file. After the timeout occurs, the server should close the connection.



