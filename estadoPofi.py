import tkinter as tk 

class ClsPersonaje():

    def fntPersonaje(self,ventana):

        self.pofiFrente="shimeji.gif"

        self.frames = 18  # gives total number of frames that gif contains

        # creating list of PhotoImage objects for each frames
        self.mostrarImagenes = [tk.PhotoImage(file=self.pofiFrente,format=f"gif -index {i}") for i in range(self.frames)]

        self.contador = 0

        self.pofiEnLabel = tk.Label(ventana,image="")
        self.pofiEnLabel.pack()

        self.fntAnimacion(self.contador,self.mostrarImagenes,self.frames,ventana,self.pofiEnLabel)

    def fntAnimacion(self,contador,mostrarImagenes,frames,ventana,pofiEnlabel):

        self.iteradorImagen = mostrarImagenes[contador]

        pofiEnlabel.configure(image=self.iteradorImagen)
        contador += 1
        if contador == frames:
            contador = 0
        self.animacion = ventana.after(200,lambda : self.fntAnimacion(contador,mostrarImagenes,frames,ventana,pofiEnlabel))






