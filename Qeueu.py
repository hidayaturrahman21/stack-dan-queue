from collections import deque

def simulasi_antrian():
    queue = deque()
    
    while True:
        print("\n1. Tambah pelanggan ke antrian")
        print("2. Layani pelanggan")
        print("3. Tampilkan antrian")
        print("4. Keluar")
        
        pilihan = input("Pilih opsi: ")  
        if pilihan == "1":
            nama = input("Masukkan nama pelanggan: ")
            queue.append(nama)  
            print("Pelanggan", nama, "ditambahkan ke dalam antrian.")

        elif pilihan == "2":
            if queue:
                dilayani = queue.popleft() 
                print("Pelanggan", dilayani, "sedang dilayani.")
            else:
                print("Antrian kosong, tidak ada pelanggan yang bisa dilayani.")

        elif pilihan == "3":
            if queue:
                print("Antrian saat ini:", list(queue)) 
            else:
                print("Antrian kosong.")

        elif pilihan == "4":
            print("Keluar dari program.")
            break 
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")  

simulasi_antrian()