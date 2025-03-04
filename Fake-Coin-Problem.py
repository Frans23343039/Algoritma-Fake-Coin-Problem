def cariKoinPalsu(koin):
    # Jika hanya ada satu koin, kembalikan koin tersebut sebagai koin palsu
    if len(koin) == 1:
        return koin[0]

    # Membagi koin menjadi tiga kelompok
    kelompok_a = koin[:len(koin)//3]
    kelompok_b = koin[len(koin)//3:2*(len(koin)//3)]
    kelompok_c = koin[2*(len(koin)//3):]

    # Timbang kelompok A dan B
    if sum(kelompok_a) == sum(kelompok_b):
        # Jika A == B, koin palsu ada di kelompok C
        return cariKoinPalsu(kelompok_c)
    else:
        # Jika A != B, koin palsu ada di kelompok A atau B
        # Tentukan kelompok yang lebih ringan atau lebih berat
        if sum(kelompok_a) < sum(kelompok_b):
            return cariKoinPalsu(kelompok_a)
        else:
            return cariKoinPalsu(kelompok_b)

# Daftar koin dengan berat yang berbeda-beda
koin = [1, 1, 1, 1, 0.5, 1, 1, 1, 1]  # Koin palsu ada di posisi 4

# Mencari koin palsu
koin_palsu = cariKoinPalsu(koin)
print("Koin palsu adalah:", koin_palsu)
