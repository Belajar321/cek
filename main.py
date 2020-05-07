# cek
import os,sys,time,datetime,random

def ketik(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)


print '========================='
print 'Menu Kami'
print '========================='
print '1. Nasi Goreng'
print '2. Sayur Asem'
print '3. Keluar'
print '========================='
def pilih():
    fad = raw_input('==>')
    if fad == '':
        print 'Masukan Inputnya '
        pilih()
    else:
        if fad == '1':
            pesan1()
        else:
            if fad == '2':
                Pesan2()
            else:
                if fad == '3':
                    Exit()
def pesan1()
ketik('Pesanan Nasi Goreng anda akan kami antarkan')
ketik('Mohon Di tunggu :)')
time.sleep(5)
ketik ('Terimakasih Telah Berkunjung')
time.sleep(1)
ketik ('apakah anda Ingin memesannya yang lain? Y/N')
fad raw_input ('==>')
    If fad == 'Y':
       menu()
    else:
       if fad== 'N':
          Bayar()
def pesan2()
ketik('Pesanan Nasi Sayur Asem anda akan kami antarkan')
ketik('Mohon Di tunggu :)')
time.sleep(5)
ketik ('apakah anda Ingin memesannya yang lain? Y/N')
fad raw_input ('==>')
    If fad == 'Y':
       menu()
    else:
       if fad== 'N':
          Bayar()

def Bayar()
ketik('Total :Gratis')
time.sleep(5)
ketik ('Terimakasih Telah Berkunjung')
time.sleep(1)
ketik ('apakah anda Ingin memesannya yang lain? Y/N')
fad raw_input ('==>')
    If fad == 'Y':
       menu()
    else:
       if fad== 'N':
          Exit()

if __name__ == '__main__':
	menu()

