# port availability check

This program gets an IP and a list of ports and checks whether these ports on the input IP are available or not.
I used "scapy" library for this purpose.
The source port sends a TCP message using "sr1" to the destination port with "S" flag which means a request for connection.
* Available: if the destination respones, the source will send another message with "R" flag to terminate the connection. 
* Unavailable: the destination IP does not response; therefore, the port is unavailable.
