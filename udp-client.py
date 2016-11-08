import socket, traceback

host = '255.255.255.255'                               # Bind to all interfaces
port = 2081

print "Creating socker on port: ", port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#print "Setting REUSEADDR option"
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print "Setting SO_BROADCAST option"
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print "Connecting to host: ", host
s.connect((host, port))

try:
    print "Going to send data ..."
    s.send("I am here")
    print "... sent"
except (KeyboardInterrupt, SystemExit):
    raise
except:
    traceback.print_exc()


