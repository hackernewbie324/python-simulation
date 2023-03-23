user_id = 0
loop = "n"
users = [
    {
        "id": "bot",
        "no_rekening": "bot",
        "username": "bot",
        "pin": "bot",
        "$": 0
    },
    {
        "id": "bot",
        "no_rekening": "bot",
        "username": "bot",
        "pin": "bot",
        "$": 0
    },
    {
        "id": "bot",
        "no_rekening": "bot",
        "username": "bot",
        "pin": "bot",
        "$": 0
    },
    {
        "id": "bot",
        "no_rekening": "bot",
        "username": "bot",
        "pin": "bot",
        "$": 1000
    },
    {
        "id": "v-miai4612[vip]",
        "no_rekening": "4612",
        "username": "v-miai4612[vip]",
        "pin": "4612",
        "$": 1000
     },
    {
        "id": "x-adim324[vvip]",
        "no_rekening": "324",
        "username": "x-adim324[vvip]",
        "pin": "324",
        "$": 100000000000000000000
    }
]
status_login = False
pakai_atm = "y"
 
 
def cek_login(p):
    for user in users:
        if user['pin'] == p:
            return user
    return False
 
 
def cek_user(id):
    for i in range(len(users)):
        if users[i]['id'] == str(id):
            return int(i)
    return -1
 
 
def cek_rekening(no):
    for i in range(len(users)):
        if str(users[i]['no_rekening']) == str(no):
            return int(i)
    return -1
 
 
def tranfer_uang(uang, no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >= 0:
        if users[index1]['$'] >= int(uang):
            users[index1]['$'] = users[index1]['$'] - int(uang)
            users[index2]['$'] = users[index2]['$'] + int(uang)
            print("Anda berhasil mentransfer uang Rp." + str(uang) + " ke Rekening " + no_rekening)
            print("sisa saldo anda adalah $", users[index1]['$'])
        else:
            print("Ops saldo anda tidak cukup")
 
 
def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if users[index1]['$'] >= int(uang):
            users[index1]['$'] = users[index1]['$'] - int(uang)
            print("Anda berhasil menarik uang $" + str(uang))
            print("sisa saldo anda adalah $", users[index1]['$'])
        else:
            print("Ops saldo anda tidak cukup")
 
 
while pakai_atm == "y":
    while not status_login:
        print("SELAMAT DATANG DI PAYPAL")
        print("Silahkan masukan pin anda")
        pin = input("Masukan PIN : ")
 
        cl = cek_login(pin)
        if cl:
            print("selamat datang " + cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Ops PIN anda salah")
            print("")
            print("")
 
    while loop == "y" and status_login:
        u = users[cek_user(user_id)]
        print("SELAMAT DATANG DI PAYPAL")
        print("1.Cek Saldo")
        print("2.Transfer Uang")
        print("3.Ambil Uang")
        print("4.Logout")
        print("5.Keluar ATM")
        a = int(input("Silahkan pilih menu : "))
        if a == 1:
            print("")
            print("Sisa Saldo anda adalah $", u['$'])
            print("")
            print("")
            loop = "n"
        elif a == 2:
            print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
            no_rek = input("Masukan No Rekening Tujuan : ")
            cnk = cek_rekening(no_rek)
 
            if cnk >= 0:
                print("Nomor rekening ditemukan,silahkan masukan nominal yang yang akan di transfer")
                nominal = input("Nominal Yang Akan Di Transfer : ")
                tranfer_uang(nominal, no_rek)
                print("")
                loop = "n"
            else:
                print("")
                print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
                print("")
                loop = "n"
 
        elif a == 3:
            nominal = input("Nominal Yang Akan Di Tarik : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            status_login = False
 
        elif a == 5:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("pilihan tidak tersedia")
        if status_login == True:
            input("kembali Ke menu (Enter) ")
            print("")
            loop = "y"

