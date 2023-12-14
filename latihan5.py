import random

def pilih_angka():
    return random.randint(1, 101)

def tebak_angka(angka, maksimum_tebakan):
    nomor_tebakan = 0
    tebakan_benar = False

    print('Komputer telah memilih angka secara acak dari 1 s.d 100')
    print('Tebaklah angka tersebut dengan jumlah tebakan seminimum mungkin')
    print('Anda harus dapat menebak dalam {} percobaan'.format(maksimum_tebakan))

    teks_petunjuk = 'Ini adalah tebakan ke-{} anda. Masukkan angka kemudian tekan ENTER '

    while not tebakan_benar and not nomor_tebakan >= maksimum_tebakan:
        nomor_tebakan += 1
        tebakan = input(teks_petunjuk.format(nomor_tebakan))
        tebakan = int(tebakan)

        if tebakan == angka:
            tebakan_benar = True
        elif tebakan > angka:
            print('Angka yang anda masukkan terlalu besar')
        else:
            print('Angka yang anda masukkan terlalu kecil')

    return tebakan_benar, nomor_tebakan

def main():
    angka = pilih_angka()
    maksimum_tebakan = 7

    tebakan_benar, nomor_tebakan = tebak_angka(angka, maksimum_tebakan)

    if tebakan_benar:
        print('Selamat! Anda berhasil menebak angka pada kesempatan ke-{}'.format(nomor_tebakan))
    else:
        print('Kesempatan menebak anda habis, anda kalah.')

main()
