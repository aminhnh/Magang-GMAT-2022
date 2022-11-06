# Menerima input
data = input().split(",")
error = ["Terjadi kegagalan pada sensor Container", "Terjadi kegagalan pada sensor Science Payload","Terjadi kegagalan pada data posisi Container","Terjadi kegagalan pada data posisi Science Payload", "Release/Separation gagal","Terjadi kegagalan pada video monitoring Science Payload"]

# Melihat apakah terdapat error berdasarkan data[4] & mengeluarkan peringatan
for i in range(len(data[4])):
    if int(data[4][i]):
        print(error[i])
        data[i] = "error"

# Mengeluarkan string berikut jika tidak terdapat error
if int(data[4]) < 1 : print("Tidak terjadi error")

# Mengeluarkan data
for i in range(len(data)):
    print("Data[{}] = {}".format(i, data[i]))


