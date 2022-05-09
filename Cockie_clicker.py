import tkinter
from PIL import ImageTk, Image
import time
import random
def fall(e):
    img = canvas.create_image(random.randint(0,2800), 50, image=image)
    a.append(img)
    for i in a:
       canvas.move(i,0,1)
    window.after(25,fall2)
def fall2():
    for i in a:
        canvas.move(i, 0, 1)
    window.after(25, fall2)
window= tkinter.Tk()
window.title("ajdb")
window.geometry("3000x800")
image = ImageTk.PhotoImage(Image.open(("Cookie-Download-PNG.png")).resize((100,100)))
#image.zoom(0.5)
canvas = tkinter.Canvas(window,width=3000,height=800)
canvas.pack(pady=20)
a=[]
img = canvas.create_image(100, 50, image=image)
a.append(img)
window.bind("<P>",fall)
window.mainloop()
