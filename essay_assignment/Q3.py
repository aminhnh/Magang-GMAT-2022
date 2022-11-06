# Menerima data
# data = input()
data = "1024,6,7,1,2,51024,9,8,7,6,5;"

valid_packets = []
while "1024" in data and ";" in data:
    batas = data.find("1024")
    packet = data[batas : data.find(";",batas)+1]
    if packet.count(",") == 5:
        valid_packets.append(packet)
        print(packet)
        data = data[batas+5:]
    else:
        data = data[batas+5:]
# print(valid_packets)
