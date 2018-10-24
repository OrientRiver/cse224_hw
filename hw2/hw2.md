# HW2

Chenlin Liu	PID:A53284481

## Paper 

#### Motivations

In packet switching networks, computers and terminals shares a common protocol. However, existing protocols have addressed only the problem of communication on the same network. This paper presents a protocol design and philosophy that supports the sharing of resources that exist in different packet switching networks.

#### Contributions

This paper describe the function of a GATEWAY as an interface between networks and discuss its role in the protocol. The authors then consider the various details of the protocol, including addressing, formatting, buffering, sequencing, flow control, error control, and so forth. They close with a description of an inter-process communication mechanism and show how it can be supported by the internetwork protocol.

#### Definitions

##### Gateway:

The gateway is an interface between networks that resolves differences between them.  The functions of gateways include data routing, data sequencing, packets splitting (fragmentation) and accounting. 

##### Retransmission window:

The retransmission window is a strategy used to solve  duplicates detection in data retransmission. The retransmission window defines the length of previously received/sent packets that the receiver and sender need to remember in order to detect duplicates.

##### The "thin waist" idea:

The architecture of TCP is a "thin waits" between the visible upper and lower layers. There is still a vast diversity of applications and hardware that sit above and below the thin waist. 

#### Ensure reliability

- The internetwork header contains  several bits of sequence number to ensure sequencing among arriving packets.
- The internetwork header contains a flag field which is used for end of a segment (ES) bits and the end of a message (EM) bits to ensure the ordering after message splitting and packet splitting.
- They propose a timeout and positive acknowledgement mechanism which will allow TCP's to recover from packet losses. This paper also used a retransmission window strategy to solve  duplicates detection in data retransmission.

## Problem set

#### 3.4

Forwarding tables:

Switch S1:

| Destination | Port |
| ----------- | ---- |
| A           | 1    |
| B           | 2    |
| Default     | 3    |

Switch S2:

| Destination | Port |
| ----------- | ---- |
| A           | 1    |
| B           | 1    |
| C           | 3    |
| D           | 3    |
| Default     | 2    |

Switch S3

| Destination | Port |
| ----------- | ---- |
| C           | 2    |
| D           | 3    |
| Default     | 1    |

Switch S4

| Destination | Port |
| ----------- | ---- |
| D           | 2    |
| Default     | 1    |

#### 3.13

1. Add B1
2. Add B3, select E
3. Add B2, select D
4. Add B4, select G
5. Add B5, select F
6. Add B6, select H
7. Add B7, select C

Ports not selected:  I, J, B, A

#### 3.15

| B1   |      |
| ---- | ---- |
| A    | A    |
| B2   | C    |

| B2   |      |
| ---- | ---- |
| B1   | A    |
| B3   | C    |
| B4   | D    |

| B3   |      |
| ---- | ---- |
| C    | C    |
| B2   | A    |

| B4   |      |
| ---- | ---- |
| D    | D    |
| B2   | A    |

#### 3.46

(a). Each node knows only the distances to its immediate neighbors.     

|      | A    | B    | C    | D    | E    | F    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| A    | 0    | inf  | 3    | 8    | inf  | inf  |
| B    | inf  | 0    | inf  | inf  | 2    | inf  |
| C    | 3    | inf  | 0    | inf  | 1    | 6    |
| D    | 8    | inf  | inf  | 0    | 2    | inf  |
| E    | inf  | 2    | 1    | 2    | 0    | inf  |
| F    | inf  | inf  | 6    | inf  | inf  | 0    |

(b). Each node has reported the information it had in the preceding step to its immediate neighbors.

|      | A    | B    | C    | D    | E    | F    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| A    | 0    | inf  | 3    | 8    | 4    | 9    |
| B    | inf  | 0    | 3    | 4    | 2    | inf  |
| C    | 3    | 3    | 0    | 3    | 1    | 6    |
| D    | 8    | 4    | 3    | 0    | 2    | inf  |
| E    | 4    | 2    | 1    | 2    | 0    | 7    |
| F    | 9    | inf  | 6    | inf  | 7    | 0    |

(c). Step (b) happens a second time.

|      | A    | B    | C    | D    | E    | F    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| A    | 0    | 6    | 3    | 6    | 4    | 9    |
| B    | 6    | 0    | 3    | 4    | 2    | 9    |
| C    | 3    | 3    | 0    | 3    | 1    | 6    |
| D    | 6    | 4    | 3    | 0    | 2    | 9    |
| E    | 4    | 2    | 1    | 2    | 0    | 7    |
| F    | 9    | 9    | 6    | 9    | 7    | 0    |

#### 3.54

(a). The tables of A, B, D, and F after C and E have reported the news.

| Table A |      |
| ------- | ---- |
| B       |      |
| C       | C    |
| D       |      |
| E       |      |
| F       | C    |

| Table B |      |
| ------- | ---- |
| A       |      |
| C       |      |
| D       | E    |
| E       | E    |
| F       |      |

| Table D |      |
| ------- | ---- |
| A       |      |
| B       | E    |
| C       |      |
| E       | E    |
| F       |      |

| Table F |      |
| ------- | ---- |
| A       | C    |
| B       |      |
| C       | C    |
| D       |      |
| E       |      |

(b). The tables of A and D after their next mutual exchange.

| Table A |      |
| ------- | ---- |
| B       | D    |
| C       | C    |
| D       | D    |
| E       | D    |
| F       | C    |

| Table D |      |
| ------- | ---- |
| A       | A    |
| B       | E    |
| C       | A    |
| E       | E    |
| F       | A    |

(c). The table of C after A exchanges with it.

| Table C |      |
| ------- | ---- |
| A       | A    |
| B       | A    |
| D       | A    |
| E       | A    |
| F       | F    |

#### 3.73

| Problem | Next hop |
| ------- | -------- |
| (a)     | F        |
| (b)     | B        |
| (c)     | C        |
| (d)     | A        |
| (e)     | D        |
| (f)     | C        |

## Computing routes

| Step | Confirmed                                                    | Tentative                               |
| ---- | ------------------------------------------------------------ | --------------------------------------- |
| 1    | (a, 0, --)                                                   |                                         |
| 2    | (a, 0, --)                                                   | (b, 4, b)<br />(g, 6, g)<br />(f, 1, f) |
| 3    | (a, 0, --)<br />(f, 1, f)                                    | (b, 4, b)<br />(g, 6, g)<br />          |
| 4    | (a, 0, --)<br />(f, 1, f)                                    | (b, 4, b)<br />(g, 3, f)<br />(e, 7, f) |
| 5    | (a, 0, --)<br />(f, 1, f)<br />(g, 3, f)                     | (b, 4, b)<br />(e, 7, f)                |
| 6    | (a, 0, --)<br />(f, 1, f)<br />(g, 3, f)                     | (b, 4, b)<br />(e, 6, f)<br />(d, 4, g) |
| 7    | (a, 0, --)<br />(f, 1, f)<br />(g, 3, f)<br />(b, 4, b)      | (e, 6, f)<br />(d, 4, g)                |
| 8    | (a, 0, --)<br />(f, 1, f)<br />(g, 3, f)<br />(b, 4, b)      | (c, 7, b)<br />(d, 4, g)<br />(e, 7, f) |
| 9    | (a, 0, --)<br />(f, 1, f)<br />(g, 3, f)<br />(b, 4, b)<br />(d, 4, g) | (c, 7, b)<br />(e, 7, f)                |
| 10   | (a, 0, --)<br />(f, 1, f)<br />(g, 3, f)<br />(b, 4, b)<br />(d, 4, g) | (c, 6, d)<br />(e, 7, f)                |
| 11   | (a, 0, --)<br />(f, 1, f)<br />(g, 3, f)<br />(b, 4, b)<br />(d, 4, g)<br />(c, 6, d) | (e, 7, f)                               |
| 12   | (a, 0, --)<br />(f, 1, f)<br />(g, 3, f)<br />(b, 4, b)<br />(d, 4, g)<br />(c, 6, d)<br />(e, 7, f) |                                         |

## Sockets programming

```python
import socket
HOST = 'cse224.sysnet.ucsd.edu'
PORT = 5555
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))
	s.sendall(b'A53284481\r\n')
	temp = s.recv(1024)
	data = temp
	while True:
		temp = s.recv(1024)
		if temp == b'':
			break
		data = data + temp  

print('received', repr(data))
```

The title of received literature and my keyword is listed below:

```
title: KING HENRY IV, THE FIRST PART
my keyword: 3960
```

