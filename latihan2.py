def istilah_yunani(bilangan):
    if 1 <= bilangan <= 10:
      istilah = ["momo", "di", "tri", "tetra", "penta", "hexa", "hepta",
       "octa", "nona", "deca"]
      print(istilah[bilangan - 1])
    else:
      print("Masukan bilangan antara 1 sampai 10")  
      
bilangan_input = int(input("Masukan bilangan bulat antara 1 sampai 10"))
istilah_yunani(bilangan_input)
