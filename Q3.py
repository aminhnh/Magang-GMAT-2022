# Menerima data
# data = input()
data = "1024,6,7,1,2,51024,9,8,7,6,5;"

valid_packets = []
while "1024" in data and ";" in data:
    a1 = data.find("1024")
    packet = data[a1 : data.find(";",a1)+1]
    
    # print("Data:",data,"\tPacket:",packet,"batasan:",a1,a2)
    
    if packet.count(",") == 5:
        valid_packets.append(packet)
        print(packet)
        data = data[a1+5:]
    else:
        data = data[a1+5:]
        
# print(valid_packets)
