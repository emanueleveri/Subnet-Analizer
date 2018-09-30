from subnet import subnetAnalizer
print("Subnet Analizer")
ip1 = str(input("Inserire il primo indirizzo ip "))
ip2 = str(input("Inserire il secondo indirizzo ip "))
mask = str(input("Inserire la maschera "))
pointer = subnetAnalizer(ip1, ip2, mask)
pointer.split()