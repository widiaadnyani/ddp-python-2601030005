print("*** PROGRAM TRANSLASI SKALA SUHU CELSIUS ***")
print("-" * 48)
derajat_celsius = float(input("Masukkan angka suhu dalam skala Celsius (C): "))
hasil_fahrenheit = (derajat_celsius * 9/5) + 32
hasil_kelvin = derajat_celsius + 273.15
print("=" * 48)
print(f"-> Hasil ke Fahrenheit : {hasil_fahrenheit} F")
print(f"-> Hasil ke Kelvin     : {hasil_kelvin} K")
print("-" * 48)
