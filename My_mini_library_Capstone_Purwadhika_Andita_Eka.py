from tabulate import tabulate

#book collection
bookColl = [["SN", "Title", "Author", "Language", "Quantity", "Status",],
            ["A1F2019","King's cage (red queen #3)","Victoria aveyard","English",1,"ON SHELF"],
            ["A2F2019","War storm (red queen #4)","Victoria aveyard","English",1,"ON SHELF"],
            ["A3F2019","Padang bulan","Andrea hirata","Indonesia",1,"ON SHELF"],
            ["B1N2020","Fihi ma fihi","Jalaluddin rumi","Indonesia",1,"ON SHELF"],
            ["B2N2017","Rantau 1 muara","Ahmad fuadi","Indonesia",1,"ON SHELF"],
            ["A4N2020","Nadira","Leila s. chudori","Indonesia",1,"ON SHELF"]]

def koleksibuku():
    collTab = tabulate(bookColl,headers='firstrow',tablefmt='grid')
    print(collTab)

def find():
    val = bookColl[1:]
    Dict = []
    for i in range(len(val)+1):
        tmp = {
            "SN": bookColl[i][0], 
            "Title":bookColl[i][1], 
            "Author":bookColl[i][2], 
            "Language":bookColl[i][3], 
            "Quantity":bookColl[i][4],
            "Status":bookColl[i][5],
            }
        Dict.append(tmp)
    bookDict = Dict[1:]
    
    def searchSN():
        srcSN = []
        src = input("Masukkan SN: ").upper()
        for i in range(len(bookDict)):
            if src == bookDict[i]["SN"]:
                srcSN.append(bookDict[i])
            else:
                continue
        if srcSN == []:
            print(f"SN {src} tidak tersedia dalam koleksi")
        else:
            print(tabulate(srcSN, headers='keys',tablefmt='grid'))
    
    def searchTit():
        srcTit = []
        tit = input("Masukkan Title lengkap: ").capitalize()
        for i in range(len(bookDict)):
            if tit == bookDict[i]["Title"]:
                srcTit.append(bookDict[i])
            else:
                continue
        if srcTit == []:
            print(f"Title {tit} tidak tersedia dalam koleksi, pastikan title telah lengkap diinput")
        else:
            print(tabulate(srcTit, headers='keys',tablefmt='grid'))

    def searchAut():
        srcAut = []
        aut = input("Masukkan Author lengkap: ").capitalize()
        for i in range(len(bookDict)):
            if aut == bookDict[i]["Author"]:
                srcAut.append(bookDict[i])
            else:
                continue
        if srcAut == []:
            print(f"Author {aut} tidak tersedia dalam koleksi, pastikan author telah lengkap diinput")
        else:
            print(tabulate(srcAut, headers='keys',tablefmt='grid'))

    def searchLang():
        srcLang = []
        lang = input("Masukkan Language lengkap: ").capitalize()
        for i in range(len(bookDict)):
            if lang == bookDict[i]["Language"]:
                srcLang.append(bookDict[i])
            else:
                continue
        if srcLang == []:
            print(f"Bahasa {lang} tidak tersedia dalam koleksi")
        else:
            print(tabulate(srcLang, headers='keys',tablefmt='grid'))

    def searchStat():
        srcStt = []
        stt = input("Masukkan status buku (on rent/on shelf): ").upper()
        for i in range(len(bookDict)):
            if stt == bookDict[i]["Status"]:
                srcStt.append(bookDict[i])
            else:
                continue
        if srcStt == []:
            print(f"Status {stt} tidak ada dalam klasifikasi")
        else:
            print(tabulate(srcStt, headers='keys',tablefmt='grid'))

    fndKey = input('''
                   1. Berdasarkan SN
                   2. Berdasarkan Title
                   3. Berdasarkan Author
                   4. Berdasarkan Bahasa
                   5. Berdasarkan Status
                   Masukkan menu:
                   ''')
    if (fndKey == '1'):
        searchSN()
    elif (fndKey == '2'):
        searchTit()
    elif (fndKey == '3'):
        searchAut()
    elif (fndKey == '4'):
        searchLang()
    elif (fndKey == '5'):
        searchStat()

def menambahkoleksi():
    def inputSN():
        global SN
        SN = input("Masukkan nomor SN: ").upper()
        aa = []
        for i in range(len(bookColl)):
            if SN == bookColl[i][0]:
                aa.append(bookColl[i])
            else:
                continue
        if aa == []:
            return SN
        else:
            print("SN sudah ada dalam database, masukkan SN baru")
            inputSN()       
    def inputTit():
        global Title
        Title = input("Masukkan judul buku: ").capitalize()
        bb = []
        for i in range(len(bookColl)):
            if Title == bookColl[i][1]:
                bb.append(bookColl[i])
            else:
                continue
        if bb == []:
            return Title
        else:
            print("Title sudah ada dalam database, masukkan title baru")
            inputTit()
    inputSN()
    inputTit()           
    Author = input("Masukkan nama penulis: ").capitalize()
    Language = input("Masukkan bahasa buku: ").capitalize()
    Qty = input("Masukkan jumlah stock buku: ")
    Status = input("Masukkan status buku, 'on shelf' atau 'on rent'?").upper()
    bookColl.append([SN, Title, Author, Language, Qty, Status])
    koleksibuku()
    
def updatekoleksi():
    def converter():
        val = bookColl[1:]
        Dict = []
        for i in range(len(val)+1):
            tmp = {
                "SN": bookColl[i][0], 
                "Title":bookColl[i][1], 
                "Author":bookColl[i][2], 
                "Language":bookColl[i][3], 
                "Quantity":bookColl[i][4],
                "Status":bookColl[i][5],
                }
            Dict.append(tmp)
        bookDict = Dict[1:]
        print(tabulate(bookDict, headers='keys',tablefmt='grid'))
    def chgTit():
        titUpd = input("Masukkan Title update: ").capitalize()
        for i in range(len(bookColl)):
            if snInp == bookColl[i][0]:
                bookColl[i][1] = titUpd
            else:
                continue
        converter()
    def chgAut():
        autUpd = input("Masukkan Author update: ").capitalize()
        for i in range(len(bookColl)):
            if snInp == bookColl[i][0]:
                bookColl[i][2] = autUpd
            else:
                continue
        converter()
    def chgLang():
        langUpd = input("Masukkan Language update: ").capitalize()
        for i in range(len(bookColl)):
            if snInp == bookColl[i][0]:
                bookColl[i][3] = langUpd
            else:
                continue
        converter()
    def chgQty():
        qtyUpd = input("Masukkan Qty update: ")
        for i in range(len(bookColl)):
            if snInp == bookColl[i][0]:
                bookColl[i][4] = qtyUpd
            else:
                continue
        converter()
    def chgSts():
        stsUpd = input("Masukkan Status update: ").upper()
        for i in range(len(bookColl)):
            if snInp == bookColl[i][0]:
                bookColl[i][5] = stsUpd
            else:
                continue
        converter()
    def menUpd():
        keyupdt = input('''
                        1. Update title
                        2. Update author
                        3. Update language
                        4. Update quantity
                        5. Update status
                        Masukkan nomor yang mau diupdate:
                        ''')
        if keyupdt == "1":
            chgTit()
        elif keyupdt == "2":
            chgAut()
        elif keyupdt == "3":
            chgLang()
        elif keyupdt == "4":
            chgQty()
        elif keyupdt == "5":
            chgSts()
    def checker():
        xx = []
        for i in range(len(bookColl)):
            if snInp == bookColl[i][0]:
                xx.append(bookColl[i])
            else:
                continue
        if xx == []:
            print(f"SN {snInp} tidak tersedia dalam koleksi")
        else:
            menUpd()
    snInp = input("Masukkan SN: ").upper()
    checker()

def deleteColl():
    def converter():
        val = bookColl[1:]
        Dict = []
        for i in range(len(val)+1):
            tmp = {
                "SN": bookColl[i][0], 
                "Title":bookColl[i][1], 
                "Author":bookColl[i][2], 
                "Language":bookColl[i][3], 
                "Quantity":bookColl[i][4],
                "Status":bookColl[i][5],
                }
            Dict.append(tmp)
        bookDict = Dict[1:]
        print(tabulate(bookDict, headers='keys',tablefmt='grid'))
    def delcoll():
        for i in range(len(bookColl)):
            if snInp == bookColl[i][0]:
                del bookColl[i]
                break
            else:
                continue
        converter()
    def checker():
        xx = []
        for i in range(len(bookColl)):
            if snInp == bookColl[i][0]:
                xx.append(bookColl[i])
            else:
                continue
        if xx == []:
            print(f"SN {snInp} tidak tersedia dalam koleksi")
        else:
            delcoll()
    snInp = input("Masukkan SN: ").upper()
    checker()

def homeAng():
    hm = input("Menu utama ketik 0, menu anggota ketik 1: ")
    if hm == "0":
        menuUtama()
    elif hm == "1":
        menuAnggota()

def homeAdm():
    hm = input("Menu utama ketik 0, menu admin ketik 1: ")
    if hm == "0":
        menuUtama()
    elif hm == "1":
        menuAdmin()

def menuAnggota():
    IDA = input("Masukkan ID Anggota: ")
    keymodA = input(f'''
                    Selamat datang {IDA},
                    1. Menampilkan seluruh koleksi buku
                    2. Mencari buku
                    3. Kembali ke menu anggota
                    4. Kembali ke menu utama
                    5. Keluar
                    silahkan pilih menu: ''')
    if (keymodA == '1'):
        koleksibuku()
        homeAng()
    elif (keymodA == '2'):
        find()
        homeAng()
    elif (keymodA == '3'):
        menuAnggota()
    elif (keymodA == '4'):
        menuUtama()
    elif (keymodA == '5'):
        print("Program telah selesai")

def menuAdmin():
        IDB = input("Masukkan ID Admin: ")
        keymodB = input(f'''
                        Selamat datang {IDB},
                        1. Menampilkan seluruh koleksi buku
                        2. Mencari buku
                        3. Menambah koleksi buku
                        4. Mengupdate koleksi buku
                        5. Menghapus koleksi buku
                        6. Kembali ke menu admin
                        7. Kembali ke menu utama
                        8. Exit program
                        silahkan pilih menu: ''')
        if (keymodB == '1'):
            koleksibuku()
            homeAdm()
        elif (keymodB == '2'):
            find()
            homeAdm()
        elif (keymodB == '3'):
            menambahkoleksi()
            homeAdm()         
        elif (keymodB == '4'):
            updatekoleksi()
            homeAdm()           
        elif (keymodB == '5'):
            deleteColl()
            homeAdm()          
        elif (keymodB == '6'):
            menuAdmin()
        elif (keymodB == '7'):
            menuUtama()
        elif (keymodB == '8'):
            print("Program telah selesai")

def menuUtama():
    keymod = input('''
        ==========Selamat Datang di Sistem Perpustakaan Mini-ku==========
        Pilih mode:
        1. Anggota
        2. Administrator
        3. Keluar
        Masukkan mode yang ingin dijalankan: ''')
    if(keymod == "1"):
        menuAnggota()
    elif(keymod == "2"):
        menuAdmin()
    else:
        print("Program telah selesai")

menuUtama()