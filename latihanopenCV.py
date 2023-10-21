import cv2
import sys
citra = cv2.imread('download.png', cv2.IMREAD_COLOR) # menampilkan gambar berwarna asli gambarnya
cv2.imshow('download.png', citra) # untuk memunculkan tapi tidak lama
cv2.waitKey(0) # tambahan kode untuk memunculkan gambar
# if not citra is None:
#     cv2.imshow('download.png', citra)
#     cv2.waitKey(0)
citra2 = cv2.imread('download.png', cv2.IMREAD_GRAYSCALE) # menampilakn gambar dalambentuk warna abu-abu
cv2.imshow('download.png', citra2) # untuk memunculkan tapi tidak lama
cv2.waitKey(0)

citra3 = cv2.imread('download.png')
citra3[0,1]
# Tujuannya mengecek gambar yang kita miliki berwarna apa enggak
if len (sys.argv) == 1:
    print('Masukkan nama berkas gambar :')
else :
    berkas =sys.argv[1]
    citra3 = cv2.imread(berkas, cv2.IMREAD_UNCHANGED)
    if citra3 is None:
        print('tidak dapat membuka gambar', berkas)
    else :
        info = citra3.shape
        if len(info) == 2:
            print("citra berskala keabu-abuan")
        else :
            print("citra berwarna")
# contoh pemberian bingkai pada gambar
citra = cv2.imread('download.png', 35) # semakin kecil angkanya semakin besar gambar yang dimunculkan
hasil = citra.copy ()
# pengolahan citra
tebal = 20
hitam = 0
jumBaris = hasil.shape[0] # untuk mendapatkan jumlah baris pada gambar
jumKolom = hasil.shape[1] # untuk mendapatkan jumlah kolom pada gambar
# --- Bingkai diatas
for baris in range (tebal):
    for kolom in range (jumKolom):
        hasil[baris, kolom] = hitam
# --- Bingkai di bawah 
for baris in range (jumBaris - tebal - 1, jumBaris) :
    for kolom in range (jumKolom):
        hasil[baris, kolom] = hitam

#--- Bingkai dikiri
for baris in range (tebal, jumBaris - tebal - 1) :
    for kolom in range (tebal):
        hasil[baris, kolom] = hitam

#--- Bingkai di kanan
for baris in range (tebal, jumBaris - tebal - 1) :
    for kolom in range (jumKolom - tebal - 1, jumKolom):
        hasil[baris, kolom] = hitam

cv2.imshow('Gambar asal', citra)
cv2. imshow('Gambar hasil', hasil)
cv2.waitKey (0) # jgn lupa nanti munculnya hanya sebentar
cv2.destroyAllWindows ()
# jika kita ingin mengambil sampel gambar tertentu

citraZoom = cv2.imread ("download.png")
zoom = citraZoom[400:700, 500:800] #200:450
cv2.imshow ("Irisan", zoom)
#cv2.imshow("asli", citraZoom)
cv2.waitKey(0)

# kalau kita mau mmengeblur 
citraZoom = cv2.imread ("download.png")
citraZoom[400:700, 500:800] = [31, 57, 63] # tambahan [31, 57, 63] untuk ngeblur bagian yg dibutuhkan
# permasalahannya gambarnya terlalu besar, cara memperkecil ukurannya ?
cv2.imshow ("Irisan", citraZoom)
cv2.waitKey(0)
