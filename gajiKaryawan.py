Gajipokok  = 5000000
Tunjangan  = 750000

GajiKotor = Gajipokok + Tunjangan

PotonganPajak = 5 / 100
PotonganBPJS = 2 / 100
Persen = PotonganPajak + PotonganBPJS

TotalPotongan = GajiKotor * Persen

GajiBersih = GajiKotor - TotalPotongan
print("total bersih gaji karyawan RP:",GajiBersih)
