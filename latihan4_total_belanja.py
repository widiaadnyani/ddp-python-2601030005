print("*** NOTA KASIR OTOMATIS & TARIF PPN 11% ***")
print("=" * 45)
belanja_awal = float(input("Masukkan nilai subtotal belanja awal (Rp): "))
hitung_ppn = belanja_awal * 0.11
biaya_akhir = belanja_awal + hitung_ppn
print("-" * 45)
print(f"-> Belanja Awal    : Rp {belanja_awal:,.2f}")
print(f"-> Pajak PPN 11%   : Rp {hitung_ppn:,.2f}")
print(f"-> Total Bayar     : Rp {biaya_akhir:,.2f}")
print("=" * 45)
