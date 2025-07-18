# osi/osi.py
'''
* Author: TanB
* Created: 7/16/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
"""
Physical Layer - This is the media you use to communicate (RS-485/Ethernet ect).
Data Link Layer - This is the subnet communication, or for example, the communication of MS/TP on a field bus.
Network Layer - This is typically were your supervisory devices lie and is where IP messages exist and route outside of the local subnet.
Transport Layer - This is where the data verification exist for communication. Typically, when you are transferring code or you are logging into a system, the verification of the transport is made at the Transport layer.
Session Layer - This is where the conversation is initiated. Often times, two supervisory devices will create a session to discuss. As you learn more about TCP and UDP, you will learn that UDP is a connection-less protocol.Essentially it just sends out data. Our control systems usually do not  require verification of commands.  As such, our systems rely on UDP sessions.
Presentation Layer - This is where the data is taken and formulated into view-able information. Often times, this is when the raw  CoAP or BACnet/IP data shifts into a view-able data format, whether that be ASCII or UNICODE.Additionally, the presentation layer can translate data into XML which is utilized by the majority of the web based building automation systems.
Application Layer - Here programs run to visually present and physically interact with the data from the previous layers. Typically building automation systems will use applications built around the HTTP or SNMP protocols.Additionally, applications can create FTP connections between one another to transfer data this is often seen in high level peer to peer supervisory communication.
"""