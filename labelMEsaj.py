import tkinter as tk
from tkinter import messagebox
import datetime
window = tk.Tk()
window.geometry("500x400")
#Ad Soyad Etiketi olusuturduk
adLabel=tk.Label(window,
                 text="Adınız ve Soyadınız",
                 font=("Verdana",25),
                 fg="red",bg="yellow")
adLabel.pack()
#Ad erigiriş kutusunu oluşturduk
adVerigirisi=tk.Entry(font=("Verdana",25))
adVerigirisi.pack()
# Giriş Butonu
def tiklamaFunc():
    gosterilecekMesaj="Merhaba Sayın "+adVerigirisi.get()
    if adVerigirisi.get()=="":
        tk.messagebox.showerror("Hata","Lütfen Adınızı Giriniz..")
    else:
        tk.messagebox.showinfo("Mesaj",gosterilecekMesaj)
        yazilacakMEsaj = str(datetime.datetime.now()) + ':' + gosterilecekMesaj+'\n'
        with open('bilgi.txt','a') as dosya:
            dosya.write(yazilacakMEsaj)
girisButton=tk.Button(text="Giriş İçin Tıklayınız",
                      font=("Verdana", 25),
                      fg="blue", bg="yellow",
                      command=tiklamaFunc)
girisButton.pack()
window.mainloop()
