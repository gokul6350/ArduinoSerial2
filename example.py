import arduinoserial2 as as2
as2.checks()
print(as2.dectect()[0])
conection=as2.connect()


as2.send(conection,"Hello")

as2.read(serial=conection)
