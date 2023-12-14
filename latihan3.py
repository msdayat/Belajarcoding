def memenuhi_syarat_donor(usia, berat_badan, tekanan_darah_sistolik):
  if 17 <= usia <= 60:
      if berat_badan >= 45:
          if 100 <= tekanan_darah_sistolik <= 160:
              return True
          else:
              return False
      else:
          return False
  else:
      return False

usia_input = int(input("Masukkan usia: "))
berat_badan_input = float(input("Masukkan berat badan (kg): "))
tekanan_darah_sistolik_input = int(input("Masukkan tekanan darah sistolik: "))

if memenuhi_syarat_donor(usia_input, berat_badan_input, tekanan_darah_sistolik_input):
  print("Calon pendonor memenuhi syarat.")
else:
  print("Calon pendonor tidak memenuhi syarat.")
