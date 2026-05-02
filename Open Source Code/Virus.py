import tkinter as tk
import threading
import time
import random

def pencere_olustur(x, y):
    root = tk.Tk()
    root.title("SYSTEM FAILURE")
    root.geometry(f"300x100+{x}+{y}") # Pencereyi belirlenen konuma açar
    
    # Kapatma butonunu ve çerçeveyi tamamen kaldırır (Daha korkutucu durur)
    # root.overrideredirect(True) # Eğer pencere başlığı olsun istemiyorsan bu satırı açabilirsin
    
    root.attributes('-topmost', True) # Hep en üstte kalır
    root.protocol("WM_DELETE_WINDOW", lambda: None) # X butonu çalışmaz

    label = tk.Label(root, text="YOU HAVE BEEN HACKED!", fg="red", font=("Courier", 12, "bold"))
    label.pack(expand=True)
    
    root.mainloop()

def kaos_dongusu():
    # Ekran çözünürlüğünü almak için geçici bir pencere
    temp_root = tk.Tk()
    ekran_genislik = temp_root.winfo_screenwidth()
    ekran_yukseklik = temp_root.winfo_screenheight()
    temp_root.destroy()

    x_pozisyonu = 0
    y_pozisyonu = 0
    adim_x = 100 
    adim_y = 50  

    while True:
        
        threading.Thread(target=pencere_olustur, args=(x_pozisyonu, y_pozisyonu)).start()
        
        
        x_pozisyonu += adim_x
        
        
        if x_pozisyonu + 300 > ekran_genislik:
            x_pozisyonu = 0
            y_pozisyonu += adim_y
            
        
        if y_pozisyonu + 100 > ekran_yukseklik:
            y_pozisyonu = 0
            x_pozisyonu = 0

        time.sleep(0.0001) 

if __name__ == "__main__":
    kaos_dongusu()