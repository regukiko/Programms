
from tkinter import ttk
import googletrans
import tkinter
def buttonf():
    f={"Italienisch":"it","Französisch":"fr","Türkisch":"tr","Englisch":"en","Deutsch":"de"}
    s=f[combo.get()]
    d=f[combo2.get()]
    translator = googletrans.Translator()
    g=text1.get(1.0,tkinter.END)
    b = translator.translate(g,dest=d,src=s)
    label3["text"]=s+"-"+d
    text2.delete(1.0,tkinter.END)
    text2.insert(1.0,b.text)
window= tkinter.Tk()
label=tkinter.Label(text="input the text")
label.place(x=100,y=50)
label2=tkinter.Label(text="translated text")
label2.place(x=600,y=50)
label3=tkinter.Label(text="")
label3.place(x=475,y=75)
window.title("ajdb")
window.geometry("1000x600")
button=tkinter.Button(text="Translate",command= buttonf )
button.place(x=450,y=500)
text1=tkinter.Text(height=10,width=30)
text2=tkinter.Text(height=10,width=30)
text1.place(x=100,y=100)
text2.place(x=600,y=100)
combo=ttk.Combobox()
combo.place(x=100,y=75)
combo['values'] = ("Italienisch","Französisch","Türkisch","Englisch","Deutsch")
combo2=ttk.Combobox()
combo2.place(x=600,y=75)
combo2['values'] = ("Italienisch","Französisch","Türkisch","Englisch","Deutsch")
combo.current(3)
combo2.current(4)
window.mainloop()
