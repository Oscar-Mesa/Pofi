import tkinter as tk
from estadoPofi import ClsPersonaje


class ClsVentana():

    def __init__(self):

        self.ventana = tk.Tk()

        self.altoVentana = 150
        self.anchoVentana = 150

    def fntParametrosVentana(self,altoVentana,anchoVentana,coordenadaX,coordenadaY):

      

        #ancho #largo #coordenada x  #coordenada y
        self.ventana.geometry(f"{altoVentana}x{anchoVentana}+{coordenadaX}+{coordenadaY}")
        #color de la ventana
        self.ventana.tk_setPalette("beige")
        #Quitamos barra de título
        self.ventana.wm_overrideredirect(True)
        #superpongo ventana 
        self.ventana.wm_attributes("-topmost",True)
        #la hago transaparente, pero le digo que color quiero que sea transaparente
        self.ventana.wm_attributes("-transparentcolor","beige")

        objClsPersonaje = ClsPersonaje()
        objClsPersonaje.fntPersonaje(self.ventana)


        while True:
            self.ventana.update()



    def fntPosicionInicial(self):

        anchoPantalla = self.ventana.winfo_screenwidth()
        altoPantalla = self.ventana.winfo_screenheight()

        coordernadaX = anchoPantalla - self.anchoVentana
        coordernadaY = altoPantalla - self.altoVentana
        self.fntParametrosVentana(self.anchoVentana,self.altoVentana,coordernadaX,coordernadaY)



#------------------------
    #esto sirve para ver si el código está siendo ejecutado directamente desde este archivo
    #cuando importo una clase de otro archivo la clase se va a ejecutar si no trae este parametro


    #es decir, tengo un archivo llamado "llamado.py" y ese archivo tiene una clase
    #que para ejecutarse la llamo al final del archivo "Prueba()"",si lo importo aquí
    #"import llamado", entonces como ese archivo que no tiene este condicional se va a ejecutar
    #sin que yo se lo haya pedido
#------------------------
if __name__ == '__main__':

    objVentana = ClsVentana()
    objVentana.fntPosicionInicial()


    
