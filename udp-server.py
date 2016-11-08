import socket, traceback

host = '0.0.0.0'                               # Bind to all interfaces
port = 2081

print "Creating socker on port: ", port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#print "Setting REUSEADDR option"
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print "Setting SO_BROADCAST option"
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print "Binding to host: ", host
s.bind((host, port))

print "Entering loop ..."
while 1:
    try:
        print "... waiting for data ..."
        message, address = s.recvfrom(8192)
        print "Got data from", address
        # Acknowledge it.
        s.sendto("I am here", address)

    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()



