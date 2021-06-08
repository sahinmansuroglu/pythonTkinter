import tkinter as tk
from tkinter import messagebox
import datetime
window = tk.Tk()
window.geometry("500x400")
#Kullanıcı Adı Etiketi olusuturduk
kulAdLabel=tk.Label(window,
                 text="Kullanıcı Adı",
                 font=("Verdana",20),
                 fg="blue",bg="gray")
kulAdLabel.pack()
#Kul Ad giriş kutusunu oluşturduk
kulAdGiris=tk.Entry(font=("Verdana",20))
kulAdGiris.pack()

#Şifre Etiketi olusuturduk
kulSifreLabel=tk.Label(window,
                 text="Kullanıcı Şifresi",
                 font=("Verdana",20),
                 fg="blue",bg="gray")
kulSifreLabel.pack()
#Ad erigiriş kutusunu oluşturduk
kulSifreGiris=tk.Entry(font=("Verdana",20),show="*")
kulSifreGiris.pack()

# Giriş Butonu
def tiklamaFunc():
    girilenAd=kulAdGiris.get()
    girilenSifre=kulSifreGiris.get()
    if (girilenAd=="" or girilenSifre==""):
        tk.messagebox.showerror("Hata", "Lütfen Tüm kutucukları Doldurun")
    else:
        if (girilenAd=="sahin" and girilenSifre=="1234"):
            gosterilecekMesaj=f"Sayın  {girilenAd} başarılı şekilde giriş yaptınız.."
            tk.messagebox.showinfo("Mesaj",gosterilecekMesaj)
        else:
            tk.messagebox.showerror("Hata", "Kullanıcı Adı ve şifre yanlış")
            yazilacakMesajBolum=f"{girilenAd} kullanıcı adlı kişi {girilenSifre} şifresi ile sisteme girmeye çalıştı"
            yazilacakMEsaj = str(datetime.datetime.now()) + ':' + yazilacakMesajBolum + '\n'
            with open('hata.txt', 'a') as dosya:
                dosya.write(yazilacakMEsaj)


girisButton=tk.Button(text="Giriş İçin Tıklayınız",
                      font=("Verdana", 25),
                      fg="blue", bg="yellow",
                      command=tiklamaFunc)
girisButton.pack()
window.mainloop()
