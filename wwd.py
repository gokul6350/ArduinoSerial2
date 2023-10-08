import arduinoserial2 as as2

connection = as2.connect()

as2.read_start(connection)

print ("hello")