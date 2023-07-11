import random 
import re
from pwinput import pwinput
class Mobil ():
    def __init__(Self,no_mobil,brand_mobil,model_mobil,warna_mobil,jenis_mobil,tahun_keluar,plat_nomor,sewa_mobil,harga_mobil,transmisi_mobil) :
        Self.no_mobil = no_mobil
        Self.brand_mobil = brand_mobil 
        Self.model_mobil = model_mobil
        Self.warna_mobil = warna_mobil
        Self.jenis_mobil = jenis_mobil
        Self.tahun_keluar = tahun_keluar
        Self.plat_nomor = plat_nomor
        Self.sewa_mobil = sewa_mobil
        Self.harga_mobil = harga_mobil
        Self.transmisi_mobil = transmisi_mobil

class Booking ():
    booking_count = 0
    def __init__(Self,booking_nama,booking_no_hp,booking_waktu,booking_harga,booking_bayar,booking_mobil_brand,booking_model_mobil,booking_mobil_index) :
        
        Self.booking_nama = booking_nama
        Self.booking_no_hp = booking_no_hp
        Self.booking_waktu = booking_waktu
        Self.booking_harga = booking_harga
        Self.booking_bayar = booking_bayar 
        Self.booking_mobil_brand = booking_mobil_brand
        Self.booking_model_mobil = booking_model_mobil
        Self.booking_mobil_index = booking_mobil_index
        


class User ():
    def __init__(Self,user_nama,user_no_hp) :
        Self.user_nama = user_nama
        Self.user_no_hp = user_no_hp
        
        

class User2:
    def __init__(Self, username, password):
        Self.username = username
        Self.password = password
        
        
        
        
    @classmethod
    def create_user(cls):
        username = input("Buat username: ")
        password = pwinput("Buat password: ")
        return cls(username, password)
        
        
class Login:
    def add_new_car(Self, mobil):
        Self.List_Mobil.append(mobil)
        
    def add_booking_user(Self, booking):
        
        Self.booking_user.append(booking)
        mobil_index = booking.booking_mobil_index
        mobil = Self.List_Mobil[mobil_index-1]
        
    
    def __init__(Self):
        Self.users = []
        Self.logged_in_user = None
        Self.booking_user = []
        Self.List_Mobil = [
        Mobil(1, "Toyota", "Voxy 2.0", "Putih", "Minivan", 2018, "B805HAR", True, 1000000, "AT"),
        Mobil(2, "Mercedes", "S500 W221", "Putih", "Sedan", 2012, "B2377FW", True, 950000, "AT"),
        Mobil(3, "Toyota", "Alphard 2.4", "Hitam", "Minivan", 2013, "B853ND", True, 800000, "AT"),
        Mobil(4, "Mazda", "5", "Putih", "Minivan", 2017, "B2568SYG", True, 700000, "AT"),
        Mobil(5, "Toyota", "Land Cruiser", "Hitam", "SUV", 1995, "B2441PBK", True, 850000, "MT"),
        Mobil(6, "Daihatsu", "Rocky 1.2 ", "Abu-abu", "SUV", 2022, "B2547PZB", True, 700000, "MT"),
        Mobil(7, "Suzuki", "Jimny Sierra", "Kuning", "SUV", 2020, "B131EEN", True, 900000, "MT"),
        Mobil(8, "Toyota", "Yaris 1.5 ", "Hitam", "Hatchback", 2007, "B2455SBK", True, 500000, "AT"),
        Mobil(9, "Toyota", "Land Cruiser", "Hitam", "SUV", 2012, "B2448SXS", True, 1250000, "AT"),
        Mobil(10, "Honda", "Accord SV4 ", "Hitam", "Sedan", 1994, "B2743BBK", True, 800000, "AT"),
        Mobil(11, "Toyota", "Land Cruiser", "Hitam", "SUV", 2002, "B312CAB", True, 1000000, "AT"),
        Mobil(12, "Toyota", "Crown Royal ", "Putih", "Sedan", 2000, "B8825PM", True, 850000, "AT"),
        Mobil(13, "Mercedes", "E240 W210", "Hitam", "Sedan", 2000, "B8317II", True, 900000, "AT"),
        Mobil(14, "Toyota", "Corolla 1.6 ", "Hitam", "Sedan", 1993, "B275FSK", True, 750000, "AT"),
        Mobil(15, "Suzuki", "Hustler", "Biru", "Hatchback", 2022, "B211NR", True, 1000000, "AT"),
        
       
        ]
        

    def add_user(Self, user):
        Self.users.append(user)

    def login(Self):
        
        
        username = input("Masukkan username: ")
        password = pwinput("Masukkan password: ")

        for user in Self.users:
            if user.username == username and user.password == password:
                Self.logged_in_user = user
                return True

        return False

    def run(Self):
        admin = User2("admin999", "admin212")
        Self.add_user(admin)

        user1 = User2.create_user()
        Self.add_user(user1)

        while True:
            print("\n===== Sistem Booking Mobil=====")
            print("1. Masuk/Login")
            print("2. Keluar/Exit")

            pilihan = input("Masukkan Pilihan: ")

            if pilihan == "1" or pilihan.lower() == "masuk" or pilihan.lower() == "login":
                if Self.login():
                    print(f"Selamat Datang, {Self.logged_in_user.username}!")
                    if Self.logged_in_user.username == "admin999":
                        Self.admin_menu()
                    else:
                        Self.user_menu()
                        
                        
                    
                else:
                    print("username atau password tidak valid. Coba Lagi.")
            elif pilihan == "2" or pilihan.lower() == "keluar" or pilihan.lower() == "exit":
                print("Terima Kasih Telah Menggunakan Sistem Booking Mobil")
                break
            else:
                print("Pilihan Tidak Valid. Coba Lagi.")
                
    def admin_menu(Self):
        List_Mobil = Self.List_Mobil
        
        while True:
            banyak = len(List_Mobil)
            menu = 0
            while menu == 0 :
                print ("=============================================================")
                print ("Selamat Datang Di Aplikasi Penyewaan Mobil") 
                print ("Silahkan Piih Menu Yang Tersedia")
                print ("1. Menu List Detail Mobil")
                print ("2. Menu List Mobil Sederhana")
                print ("3. Menu Pencarian Mobil")
                print ("4. Menu Pembatalan Booking")
                print ("5. Menu Mobil Yang Sedang Di Booking ")
                print ("6. Tambah List Mobil")
                print ("7. Logout")
                menu = input("Silahkan Pilih Menu : ") 
                menu_check = re.sub("\D+", "", menu)
                if len(menu_check) == 0 :
                    print("Mohon Masukan Angka Saja")
                    print(menu_check)
                    menu = 0
                else :
                    menu = re.sub("\D+","",menu)
                    menu = int(menu)
                    x = 0
                
                print ("============================================")
                if menu == 1 :
                    for list_mobil in List_Mobil :
                        if list_mobil.sewa_mobil == True : 
                            print ("=============================================================")
                            print ("Nomor Mobil     : ",list_mobil.no_mobil)
                            print ("Brand Mobil     : ",list_mobil.brand_mobil)
                            print ("Model Mobil     : ",list_mobil.model_mobil)
                            print ("Warna Mobil     : ",list_mobil.warna_mobil)
                            print ("Jenis Mobil     : ",list_mobil.jenis_mobil)
                            print ("Tahun Keluar    : ",list_mobil.warna_mobil)
                            print ("Plat Nomor      : ",list_mobil.plat_nomor)
                            print ("Harga Sewa      :  Rp.",list_mobil.harga_mobil)
                            print ("Mobil Saat ini  :  Tersedia ")
                        elif list_mobil.sewa_mobil == False:
                            print ("=============================================================")
                            print ("Nomor Mobil     : ",list_mobil.no_mobil)
                            print ("Brand Mobil     : ",list_mobil.brand_mobil)
                            print ("Model MObil     : ",list_mobil.model_mobil)
                            print ("Warna Mobil     : ",list_mobil.warna_mobil)
                            print ("Jenis Mobil     : ",list_mobil.jenis_mobil)
                            print ("Tahun Keluar    : ",list_mobil.tahun_keluar)
                            print ("Plat Nomor      : ",list_mobil.plat_nomor)
                            print ("Harga Sewa      :  Rp.",list_mobil.harga_mobil)
                            print ("Mobil Saat ini  :  Tidak Tersedia")
                        else:
                            print("")
                    menu = 0
                elif menu == 2 :
                    print ("Mobil Yang Tersedia : ")
                    x = 0
                    print ("===========================================================================================================================")
                    for mobil in List_Mobil :
                            if mobil.sewa_mobil == True  :
                                print("||{:<8} {:<12} {:<9}".format(mobil.brand_mobil, mobil.model_mobil, mobil.jenis_mobil), end="||   ")
                            else :
                                a = 0
                            x += 1    
                            if x == 3 :
                                print ("")
                                x = 0
                    print ("\n===========================================================================================================================")
                    menu = 0
                elif menu == 3 :
                    print  ("Pilih pencarian berdasarkan : ") 
                    print  ("1. Merek/Brand Mobil") 
                    print  ("2. Jenis Mobil") 
                    print  ("3. Warna Mobil") 
                    print  ("4. Transmisi Mobil") 
                    menu_2 = 0
                    while menu_2 == 0 :
                        menu_2 = input("Masukan Menu Pencarian : ")
                        if  str(menu_2.lower()) == "merek" or str(menu_2.lower()) == "brand" or int(menu_2) == 1 :
                            brand_search = str(input("Masukan Brand/Merek Mobil : "))
                            filter_mobil = list(filter(lambda mobil: mobil.brand_mobil.lower() == brand_search.lower(),List_Mobil))
                            if filter_mobil and len(filter_mobil) > 0 :
                                x = 0
                                print ("===========================================================================================================================")
                                for mobil in filter_mobil :
                                    print("||{:<4} {:<12} {:<10}".format(mobil.brand_mobil, mobil.model_mobil, mobil.plat_nomor), end="||   ")
                                    x += 1
                                    if x == 3 :
                                        print ("")
                                        x = 0
                                print ("\n===========================================================================================================================")
                                menu = 0
                            else :
                                print ("Mobil Dengan Merek '",brand_search,"' TIdak Di Temukan")
                            menu = 0
                        elif menu_2 == 2 or str(menu_2.lower()) == "jenis"  or int(menu_2) == 2:
                            print ("=============================================================")
                            jenis_search = str(input("Masukan Jenis Mobil : "))
                            filter_mobil = list(filter(lambda mobil_2: mobil_2.jenis_mobil.lower() == jenis_search.lower(),List_Mobil))
                            if filter_mobil and len(filter_mobil) > 0 :
                                x = 0
                                print ("===========================================================================================================================\n")
                                for mobil in filter_mobil :
                                    print("||{:<9} {:<13} {:<5} {:<10}".format(mobil.brand_mobil, mobil.model_mobil, mobil.jenis_mobil, mobil.plat_nomor), end="||   ")
                                    x += 1
                                    if x == 3 :
                                        print ("")
                                        x = 0
                                print ("\n===========================================================================================================================")
                                menu = 0
                            else :
                                print ("Mobil Dengan Jenis'",jenis_search,"'Tidak Di Temukan")
                            menu = 0
                                        
                        elif menu_2 == 3 or str(menu_2.lower()) == "warna" or int(menu_2) == 3 :
                            print ("===========================")
                            warna_search = str(input("Masukan Warna Mobil : "))
                            filter_mobil = list(filter(lambda mobil_2: mobil_2.warna_mobil.lower() == warna_search.lower(),List_Mobil))
                            if filter_mobil and len(filter_mobil) > 0 :
                                if filter_mobil and len(filter_mobil) > 0 :
                                    x = 0
                                print ("===========================================================================================================================\n")
                                for mobil in filter_mobil :
                                    print("|| {:<8} {:<11} {:<8} {:<5} ".format(mobil.brand_mobil, mobil.model_mobil, mobil.jenis_mobil, mobil.warna_mobil), end="||   ")
                                    x += 1
                                    if x == 3 :
                                        print ("")
                                        x = 0
                                print ("\n===========================================================================================================================")
                                menu = 0
                            else :
                                print ("Mobil Dengan Warna'",warna_search,"' Tidak Di temukan")
                            menu = 0
                        elif menu_2 == 4 or str(menu_2.lower()) == "transmisi" or int(menu_2) == 4 :
                            print ("=============================================================")
                            transmisi_search = str(input("Masukan Transmisi Mobil (MT/AT) : "))
                            filter_mobil = list(filter(lambda mobil_2: mobil_2.transmisi_mobil.lower() == transmisi_search.lower(),List_Mobil))
                            if filter_mobil and len(filter_mobil) > 0 :
                                x = 0
                                print ("===========================================================================================================================\n")
                                for mobil in filter_mobil :
                                    print("||{:<8} {:<12} {:<9} {:<3} ".format(mobil.brand_mobil, mobil.model_mobil, mobil.jenis_mobil, mobil.transmisi_mobil), end="||   ")
                                    x += 1
                                    if x == 3 :
                                        print ("")
                                        x = 0
                                print ("\n===========================================================================================================================")
                                menu = 0
                            menu = 0
                        else :
                            print ("Menu Tidak Di temukan")
                            menu = 0                   
                elif menu == 4 :
                    if len(Self.booking_user) == 0:
                        print ("Tidak Ada Bookingan Yang Bisa Di Batalkan Saat Ini ")
                        menu = 0
                        
                    else:
                        x=1
                        for booking in Self.booking_user:
                            print ("=============================================================")
                            print("Booking No: ", x)
                            x = x+1
                            print(f"Bookingan Atas Nama  : {Self.users[1].username}")
                            print("Mobil Yang Di Booking : ", booking.booking_mobil_brand,booking.booking_model_mobil)
                            print("Dengan No Hp: ", booking.booking_no_hp)
                            print("Dengan Lama Peminjaman: ", booking.booking_waktu)
                            print("Dengan Tagihan Sebesar: ", booking.booking_bayar)
                            print ("=============================================================")
                            menu = 0
                        booking_id = input("Booking Mana Yang Ingin Di Batalkan : ")
                        booking_id_check = re.sub("\D+", "", booking_id)
                        if len(booking_id_check) == 0:
                            print("Mohon Masukkan Nomor Booking dengan Angka")
                            
                        else:
                            print ("================================")
                            pesan = input("Apakah Anda Yakin Ingin Menghapus Bookingan ini? (y/n) :")
                            booking_id_check = int(booking_id_check)
                            
                            if pesan.lower() == "y" :
                                print (f"Bookingan Atas Nama: {Self.users[1].username}")
                                print ("Dengan No Hp: ",Self.booking_user[booking_id_check-1].booking_no_hp)
                                print ("Dengan Lama Peminjaman: ",Self.booking_user[booking_id_check-1].booking_waktu)
                                
                                print ("Dengan Tagihan Sebesar: ",Self.booking_user[booking_id_check-1].booking_bayar)
                                print ("Brand Mobil Yang Di Booking : ",Self.booking_user[booking_id_check-1].booking_mobil_brand)
                                print ("Model Mobil Yang Di Booking : ",Self.booking_user[booking_id_check-1].booking_model_mobil)
                                print ("Dengan Plat Nomor Mobil: ",List_Mobil[Self.booking_user[booking_id_check-2].booking_mobil_index].plat_nomor) 
                                List_Mobil[Self.booking_user[booking_id_check-1].booking_mobil_index-1].sewa_mobil = True
                               
                                Self.booking_user.pop(booking_id_check-1)
                                print("Booking dengan Nomor Booking", booking_id, "TELAH DIBATALKAN.")
                                
                                menu = 0
                            else:
                                print("Batal Menghapus Bookingan")
                                
                    
                elif menu == 5 :
                    if Self.booking_user:
                        print ("=============================================================")
                        print ("Booking Yang Saat Ini Sedang Berjalan")
                        x = 1
                        for booking in Self.booking_user:
                            print("=============================================================")
                            print("Bookingan No : ", x)
                            x = x+1
                            print(f"Bookingan Atas Nama: {Self.users[1].username}")
                            print("Mobil Yang Di Booking: ", booking.booking_mobil_brand,booking.booking_model_mobil)
                            print("Dengan No Hp: ", booking.booking_no_hp)
                            print("Dengan Lama Peminjaman: ", booking.booking_waktu)
                            print("Dengan Tagihan Sebesar: ", booking.booking_bayar)
                            print("=============================================================")
                    else:
                        print ("=============================================================")
                        print ("Saat Ini Tidak Ada Mobil Yang Sedang Di Booking")
                        menu = 0 
                
                
                elif menu == 6:
                    if Self.logged_in_user.username == "admin999":
                        print("=== Menu Tambah Mobil Baru ===")
                        brand_mobil = input("Brand Mobil: ")
                        model_mobil = input("Model Mobil: ")
                        warna_mobil = input("Warna Mobil: ")
                        jenis_mobil = input("Jenis Mobil: ")
                        tahun_keluar = input("Tahun Keluar: ")
                        plat_nomor = input("Plat Nomor: ")
                        sewa_mobil = input("Status Sewa Mobil (True/False): ")
                        if sewa_mobil.lower() == "true":
                            sewa_mobil = True
                        elif sewa_mobil.lower() == "false":
                            sewa_mobil = False
                            
                        if sewa_mobil == True or sewa_mobil == False:
                        
                            
                            harga_mobil = int(input("Harga Mobil: "))
                            transmisi_mobil = input("Transmisi Mobil (AT/MT): ")
                            if transmisi_mobil.lower() == "at":
                                transmisi_mobil = "AT"
                            elif transmisi_mobil.lower() == "mt":
                                transmisi_mobil = "MT"
                                
                            if transmisi_mobil == "AT" or transmisi_mobil == "MT":
                                mobil_baru = Mobil(
                                    len(List_Mobil) + 1, brand_mobil, model_mobil, warna_mobil, jenis_mobil, tahun_keluar, plat_nomor,
                                    sewa_mobil, harga_mobil, transmisi_mobil
                                )
                
                                Self.add_new_car(mobil_baru)
                                print("Mobil baru berhasil ditambahkan ke List Mobil.")
                                
                            else:
                                print("Inputan Tidak Tepat")
                            
                        else:
                            print("Inputan Tidak Tepat")
            
                        
                    
            
                    menu = 0
                    
                elif menu == 7:
                    Self.logged_in_user = None
                    print("Logged out berhasil!")
                    return
                
                else  :
                    print ("=============================================================")
                    print  ("Menu Tidak Ada")
                    menu = 0
            
                
        
    def user_menu(Self):
        
        List_Mobil = Self.List_Mobil

        while True:
            banyak = len(List_Mobil)
            menu = 0
            while menu == 0 :
                print ("=============================================================")
                print ("Selamat Datang Di Aplikasi Penyewaan Mobil") 
                print ("Silahkan Piih Menu Yang Tersedia")
                print ("1. Menu List Detail Mobil")
                print ("2. Menu List Mobil Sederhana")
                print ("3. Menu Pencarian Mobil")
                print ("4. Menu Booking Mobil")
                print ("5. Menu Pembatalan Booking")
                print ("6. Menu Mobil Yang Sedang Di Booking ")
                print ("7. Logout")
                
                menu = input("Silahkan Pilih Menu : ") 
                menu_check = re.sub("\D+", "", menu)
                if len(menu_check) == 0 :
                    print("Mohon Masukan Angka Saja")
                    print(menu_check)
                    menu = 0
                else :
                    menu = re.sub("\D+","",menu)
                    menu = int(menu)
                    x = 0
                
                print ("============================================")
                if menu == 1 :
                    for list_mobil in List_Mobil :
                        if list_mobil.sewa_mobil == True : 
                            print ("=============================================================")
                            print ("Nomor Mobil     : ",list_mobil.no_mobil)
                            print ("Brand Mobil     : ",list_mobil.brand_mobil)
                            print ("Model Mobil     : ",list_mobil.model_mobil)
                            print ("Warna Mobil     : ",list_mobil.warna_mobil)
                            print ("Jenis Mobil     : ",list_mobil.jenis_mobil)
                            print ("Tahun Keluar    : ",list_mobil.warna_mobil)
                            print ("Plat Nomor      : ",list_mobil.plat_nomor)
                            print ("Harga Sewa      :  Rp.",list_mobil.harga_mobil)
                            print ("Mobil Saat ini  :  Tersedia ")
                        elif list_mobil.sewa_mobil == False:
                            print ("=============================================================")
                            print ("Nomor Mobil     : ",list_mobil.no_mobil)
                            print ("Brand Mobil     : ",list_mobil.brand_mobil)
                            print ("Model MObil     : ",list_mobil.model_mobil)
                            print ("Warna Mobil     : ",list_mobil.warna_mobil)
                            print ("Jenis Mobil     : ",list_mobil.jenis_mobil)
                            print ("Tahun Keluar    : ",list_mobil.tahun_keluar)
                            print ("Plat Nomor      : ",list_mobil.plat_nomor)
                            print ("Harga Sewa      :  Rp.",list_mobil.harga_mobil)
                            print ("Mobil Saat ini  :  Tidak Tersedia")
                        else:
                            print("")
                    menu = 0
                elif menu == 2 :
                    print ("Mobil Yang Tersedia : ")
                    x = 0
                    print ("===========================================================================================================================")
                    for mobil in List_Mobil :
                            if mobil.sewa_mobil == True  :
                                print("||{:<8} {:<12} {:<9}".format(mobil.brand_mobil, mobil.model_mobil, mobil.jenis_mobil), end="||   ")
                            else :
                                a = 0
                            x += 1    
                            if x == 3 :
                                print ("")
                                x = 0
                    print ("===========================================================================================================================")
                    menu = 0
                elif menu == 3 :
                    print  ("Pilih pencarian berdasarkan : ") 
                    print  ("1. Merek/Brand Mobil") 
                    print  ("2. Jenis Mobil") 
                    print  ("3. Warna Mobil") 
                    print  ("4. Transmisi Mobil") 
                    menu_2 = 0
                    while menu_2 == 0 :
                        menu_2 = input("Masukan Menu Pencarian : ")
                        if  str(menu_2.lower()) == "merek" or str(menu_2.lower()) == "brand" or int(menu_2) == 1 :
                            brand_search = str(input("Masukan Brand/Merek Mobil : "))
                            filter_mobil = list(filter(lambda mobil: mobil.brand_mobil.lower() == brand_search.lower(),List_Mobil))
                            if filter_mobil and len(filter_mobil) > 0 :
                                x = 0
                                print ("===========================================================================================================================")
                                for mobil in filter_mobil :
                                    print("||{:<4} {:<12} {:<10}".format(mobil.brand_mobil, mobil.model_mobil, mobil.plat_nomor), end="||   ")
                                    x += 1
                                    if x == 3 :
                                        print ("")
                                        x = 0
                                print ("\n===========================================================================================================================")
                                menu = 0
                            else :
                                print ("Mobil Dengan Merek '",brand_search,"' TIdak Di Temukan")
                            menu = 0
                        elif menu_2 == 2 or str(menu_2.lower()) == "jenis"  or int(menu_2) == 2:
                            print ("=============================================================")
                            jenis_search = str(input("Masukan Jenis Mobil : "))
                            filter_mobil = list(filter(lambda mobil_2: mobil_2.jenis_mobil.lower() == jenis_search.lower(),List_Mobil))
                            if filter_mobil and len(filter_mobil) > 0 :
                                x = 0
                                print ("===========================================================================================================================\n")
                                for mobil in filter_mobil :
                                    print("||{:<9} {:<13} {:<5} {:<10}".format(mobil.brand_mobil, mobil.model_mobil, mobil.jenis_mobil, mobil.plat_nomor), end="||   ")
                                    x += 1
                                    if x == 3 :
                                        print ("")
                                        x = 0
                                print ("\n===========================================================================================================================")
                                menu = 0
                            else :
                                print ("Mobil Dengan Jenis'",jenis_search,"'Tidak Di Temukan")
                            menu = 0
                                        
                        elif menu_2 == 3 or str(menu_2.lower()) == "warna" or int(menu_2) == 3 :
                            print ("===========================")
                            warna_search = str(input("Masukan Warna Mobil : "))
                            filter_mobil = list(filter(lambda mobil_2: mobil_2.warna_mobil.lower() == warna_search.lower(),List_Mobil))
                            if filter_mobil and len(filter_mobil) > 0 :
                                if filter_mobil and len(filter_mobil) > 0 :
                                    x = 0
                                print ("===========================================================================================================================\n")
                                for mobil in filter_mobil :
                                    print("|| {:<8} {:<11} {:<8} {:<5} ".format(mobil.brand_mobil, mobil.model_mobil, mobil.jenis_mobil, mobil.warna_mobil), end="||   ")
                                    x += 1
                                    if x == 3 :
                                        print ("")
                                        x = 0
                                print ("\n===========================================================================================================================")
                                menu = 0
                            else :
                                print ("Mobil Dengan Warna'",warna_search,"' Tidak Di temukan")
                            menu = 0
                        elif menu_2 == 4 or str(menu_2.lower()) == "transmisi" or int(menu_2) == 4 :
                            print ("=============================================================")
                            transmisi_search = str(input("Masukan Transmisi Mobil (MT/AT) : "))
                            filter_mobil = list(filter(lambda mobil_2: mobil_2.transmisi_mobil.lower() == transmisi_search.lower(),List_Mobil))
                            if filter_mobil and len(filter_mobil) > 0 :
                                x = 0
                                print ("===========================================================================================================================\n")
                                for mobil in filter_mobil :
                                    print("||{:<8} {:<12} {:<9} {:<3} ".format(mobil.brand_mobil, mobil.model_mobil, mobil.jenis_mobil, mobil.transmisi_mobil), end="||   ")
                                    x += 1
                                    if x == 3 :
                                        print ("")
                                        x = 0
                                print ("\n===========================================================================================================================")
                                menu = 0
                            menu = 0
                        else :
                            print ("Menu Tidak Di temukan")
                            menu = 0 
                elif menu == 4  :
                    print ("===========================================")
                    booking_index = input("Masukkan Nomor Mobil yang Ingin Di Booking: ")
                    booking_index_check = re.sub("\D+", "", booking_index)
                    if len(booking_index_check) == 0:
                        print("Mohon Input Yang Dengan Angka Yang Benar")
                        menu = 0
                    else:
                        booking_index = booking_index_check
                        booking_index = int(booking_index)
                        if len(List_Mobil) >= booking_index:
                            if List_Mobil[booking_index - 1].sewa_mobil == False:
                                print ("Mobil Yang Di Pesan : ", List_Mobil[booking_index-1].brand_mobil)
                                print ("Dengan Model        :",List_Mobil[booking_index-1].model_mobil)
                                print ("Dengan Jenis        :",List_Mobil[booking_index-1].jenis_mobil)
                                print ("Dengan Warna        :",List_Mobil[booking_index-1].warna_mobil)
                                print ("Dengan Plat no      :",List_Mobil[booking_index-1].plat_nomor)
                                print ("===========================================")
                                print ("Mobil",List_Mobil[booking_index-1].brand_mobil,List_Mobil[booking_index-1].model_mobil,"saat ini tidak tersedia untuk di sewa")
                                menu = 0 
                                
                                
                            else:
                                print ("=============================================================")
                                print ("Mobil Yang Di Pesan : ", List_Mobil[booking_index-1].brand_mobil)
                                print ("Dengan Model        : ",List_Mobil[booking_index-1].model_mobil)
                                print ("Dengan Jenis        : ",List_Mobil[booking_index-1].jenis_mobil)
                                print ("Dengan Warna        : ",List_Mobil[booking_index-1].warna_mobil)
                                print ("Dengan Plat no      : ",List_Mobil[booking_index-1].plat_nomor)
                                print ("=============================================================")
                                booking_nama = print (f"Nama Pemesan                       : {Self.logged_in_user.username}")
                                booking_no_hp = str(input("Masukan No Hp                      : "))
                                booking_waktu = int(input("Masukan Waktu Pinjam (Berapa Hari) : "))
                                booking_harga = List_Mobil[booking_index - 1].harga_mobil
                                total_harga = booking_waktu*booking_harga
                                booking_bayar = booking_waktu*booking_harga
                                booking_mobil_brand = List_Mobil[booking_index - 1].brand_mobil
                                booking_model_mobil = List_Mobil[booking_index - 1].model_mobil
                                booking_mobil_index = booking_index
                                print ("Mobil",List_Mobil[booking_index-1].brand_mobil, List_Mobil[booking_index-1].brand_mobil,"Dengan Waktu",booking_waktu,"Hari", "Berharga : Rp,",total_harga)
                                pesan = str(input("Apakah Anda Yakin Ingin Membooking? (Y/N) : "))
                                print ("=============================================================")
                                if pesan.lower() == "y" :
                                    print("Bookingan Berhasil Di Tambahkan")
                
                                    new_booking = Booking(
                                        booking_nama,
                                        booking_no_hp,
                                        booking_waktu,
                                        booking_harga,
                                        booking_bayar,
                                        booking_mobil_brand,
                                        booking_model_mobil,
                                        booking_mobil_index,
                                    )
                                    Self.add_booking_user(new_booking) 
                
                                    List_Mobil[booking_index - 1].sewa_mobil = False
                                     
                                    print(List_Mobil[booking_index - 1].sewa_mobil)
                                    
                                    menu = 0 
                                else:
                                    print ("Bookingan Di Batalkan")
                                    menu = 0
                        else:
                            print ("=============================================================")
                            print ("Mobil Dengan Nomor ", booking_index,"Tidak ada")
                            print ("=============================================================")
                            menu = 0
                    
                elif menu == 5 :
                    if len(Self.booking_user) == 0:
                        print ("Tidak Ada Bookingan Yang Bisa Di Batalkan Saat Ini ")
                        menu = 0
                        
                    else:
                        x=1
                        for booking in Self.booking_user:
                            print ("=============================================================")
                            print("Booking No: ", x)
                            x = x+1
                            print(f"Bookingan Atas Nama  : {Self.logged_in_user.username}")
                            print("Mobil Yang Di Booking : ", booking.booking_mobil_brand,booking.booking_model_mobil)
                            print("Dengan No Hp: ", booking.booking_no_hp)
                            print("Dengan Lama Peminjaman: ", booking.booking_waktu)
                            print("Dengan Tagihan Sebesar: ", booking.booking_bayar)
                            print ("=============================================================")
                            menu = 0
                        booking_id = input("Booking Mana Yang Ingin Di Batalkan : ")
                        booking_id_check = re.sub("\D+", "", booking_id)
                        if len(booking_id_check) == 0:
                            print("Mohon Masukkan Nomor Booking dengan Angka")
                            
                        else:
                            print ("================================")
                            pesan = input("Apakah Anda Yakin Ingin Menghapus Bookingan ini? (y/n) :")
                            booking_id_check = int(booking_id_check)
                            
                            if pesan.lower() == "y" :
                                print (f"Bookingan Atas Nama: {Self.logged_in_user.username}")
                                print ("Dengan No Hp: ",Self.booking_user[booking_id_check-1].booking_no_hp)
                                print ("Dengan Lama Peminjaman: ",Self.booking_user[booking_id_check-1].booking_waktu)
                                
                                print ("Dengan Tagihan Sebesar: ",Self.booking_user[booking_id_check-1].booking_bayar)
                                print ("Brand Mobil Yang Di Booking : ",Self.booking_user[booking_id_check-1].booking_mobil_brand)
                                print ("Model Mobil Yang Di Booking : ",Self.booking_user[booking_id_check-1].booking_model_mobil)
                                print ("Dengan Plat Nomor Mobil: ",List_Mobil[Self.booking_user[booking_id_check-2].booking_mobil_index].plat_nomor) 
                                List_Mobil[Self.booking_user[booking_id_check-1].booking_mobil_index-1].sewa_mobil = True
                                
                                Self.booking_user.pop(booking_id_check-1)
                                print("Booking dengan Nomor Booking", booking_id, "TELAH DIBATALKAN.")
                                
                                menu = 0
                            else:
                                print("Batal Menghapus Bookingan")
                                
                    
                elif menu == 6 :
                    if Self.booking_user:
                        print ("=============================================================")
                        print ("Booking Yang Saat Ini Sedang Berjalan")
                        x = 1
                        for booking in Self.booking_user:
                            print("=============================================================")
                            print("Bookingan No : ", x)
                            x = x+1
                            print(f"Bookingan Atas Nama: {Self.logged_in_user.username}")
                            print("Mobil Yang Di Booking: ", booking.booking_mobil_brand,booking.booking_model_mobil)
                            print("Dengan No Hp: ", booking.booking_no_hp)
                            print("Dengan Lama Peminjaman: ", booking.booking_waktu)
                            print("Dengan Tagihan Sebesar: ", booking.booking_bayar)
                            print("=============================================================")
                    else:
                        print ("=============================================================")
                        print ("Saat Ini Tidak Ada Mobil Yang Sedang Di Booking")
                        menu = 0 
                elif menu == 7:
                    Self.logged_in_user = None
                    print("Logged out berhasil!")
                    return
                
                
                
                else  :
                    print ("=============================================================")
                    print  ("Menu Tidak Ada")
                    menu = 0
            

            
    

    

log_in=Login()
log_in.run()
