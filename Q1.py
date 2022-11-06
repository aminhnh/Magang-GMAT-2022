# Menerima input
n = int(input())
data = input().split(",")

# Mengeluarkan data jika jumlah data sama dengan n
if len(data) == n:
    for i in range(len(data)):
        print("Data[{}] = {}".format(i, data[i]))
else: 
    print("Data Salah")

