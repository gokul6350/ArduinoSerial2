import arduinoserial2.arduinoserial2 as as2
as2.checks()
print(as2.detect()[0])
conection=as2.connect()


as2.send_data(conection,"Hello")

as2.read(serial=conection)


as2.read_start