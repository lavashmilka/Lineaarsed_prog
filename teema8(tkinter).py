from tkinter import *
from tkinter import messagebox


k=0
def vajatatud(event):
    global k 
    k+=1
    nupp.config(text=f"Kliki mind {k} korda")




def tuhista(event):
    sisestus.delete(0, END) #sisestus-строка ввода текста

def text_to_label(event):
    if sisestus.get()!="":
        pealkiri.config(text=sisestus.get())
    else:
        messagebox.showwarning("Viga","Sisesta midagi!")
        
  



aken=Tk() #alati T
aken.title("Tere tulemast!")
aken.geometry("900x400")
aken.configure(bg="pink")  #bg-background(фон)
aken.resizable(width=False, height=False) #akna suuruse muutmine
aken.iconbitmap("token_crypto.ico") #akna ikoon
#aken.attributes("-alpha", 0.9) #прозрачность окна
pealkiri=Label(aken, text="Tere tulemast!\n Teema nr.8 Tkinter", font=("Arial", 20))
pealkiri.pack(pady=20) #pady-отступ по вертикали (сверху и снизу))
nupp=Button(aken,text="Valik",bg="orange",fg="white",font=("Arial",15),command=lambda: messagebox.showinfo("Teema8","Tere tulemast!"))
nupp.bind("<Button-3>", vajatatud) #при наведении мыши") 
sisestus=Entry(aken,bg="white",font=("Arial",15),fg="black")
sisestus.insert(0,"Kirjuta siia tekst")

sisestus.bind("<FocusIn>", tuhista)#"<FocusOut">-при потере фокуса
sisestus.bind("<Return>",text_to_label)



pilt=PhotoImage(file="ananas.png").subsample(2,2) #subsample-уменьшение изображения в 2 раза)
pilt_label=Label(aken,image=pilt)






pealkiri.pack(pady=20)
nupp.pack(pady=20) #pady-отступ по вертикали (сверху и снизу))
sisestus.pack(pady=20) #pady-отступ по вертикали (сверху и снизу))
pilt_label.pack(pady=20)
aken.mainloop()