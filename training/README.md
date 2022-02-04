How browsers work:

https://developer.mozilla.org/en-US/docs/Web/Performance/How_browsers_work

Users want and expect web experiences with content that is fast to load and smooth to interact with.

Two major issues in web performance are
1. latency: Network latency is the time it takes to transmit bytes over the air to computers.
2. browsers are single-threaded: Web performance can be improved by understanding the single-threaded nature of the browser and minimizing the main thread's responsibilities.
Navigation: Navigation is the first step in loading a web page. When navigated to a URL, the HTML page is located on the server with an IP address,

DNS Lookup: If never visited the site, a DNS lookup must happen, which is eventually fielded by a name server, which in turn responds with an IP address. After this initial request, the IP will likely be cached for a time.

TCP Handshake: the browser sets up a connection to the server via a TCP three-way handshake which is often referred to as "SYN-SYN-ACK".
TLS negotiation: For secure connections established over HTTPS, another "handshake" is required, i.e. TLS Negotiation, which determines which cipher will be used to encrypt the communication, verifies the server, and establishes that a secure connection is in place before beginning the actual transfer of data. 

While making the connection secure adds time to the page load, a secure connection is worth the latency expense.

After the 8 round trips, the browser is finally able to make the request.

Response: Once we have an established connection to a web server, the browser sends an initial HTTP GET request on behalf of the user, which for websites is most often an HTML file.

TCP slow start: The first response packet will be 14Kb, then after the server doubles the size of the next packet to around 28Kb. Subsequent packets increase in size until a predetermined threshold is reached, or congestion is experienced.

Congestion control: The connection has a limited capacity depending on hardware and network conditions. If the server sends too many packets too quickly, they will be dropped (no acknowledgment, missing ACKs).

Parsing: Parsing is the step the browser takes to turn the data it receives over the network into the DOM and CSSOM, which is used by the renderer to paint a page to the screen.
The DOM is the internal representation of the markup for the browser. 

We describe five steps in the critical rendering path.
DOM: The first step is processing the HTML markup and building the DOM tree. 

 

The optimizations the preload scanner provides reduce blockages.
CSSOM: The second step in the critical rendering path is processing CSS and building the CSSOM tree.

The DOM and CSSOM are both trees. 

Some browser engines take the Abstract Syntax Tree and pass it into an interpreter, outputting bytecode which is executed on the main thread. This is known as JavaScript compilation.

Render: Rendering steps include style, layout, paint, and, in some cases, compositing. 

The CSSOM and DOM trees created in the parsing step are combined into a render tree which is then used to compute the layout of every visible element, which is then painted to the screen.

Style: The third step in the critical rendering path is combining the DOM and CSSOM into a render tree.

Layout: The fourth step in the critical rendering path is running layout on the render tree to compute the geometry of each node. 
The first time the size and position of nodes are determined is called layout. 
Subsequent recalculations of node size and locations are called reflows.

Paint: The last step in the critical rendering path is painting the individual nodes to the screen
