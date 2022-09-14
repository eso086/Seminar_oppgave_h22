#Importerer tkinter
from tkinter import *
#Tkinter er selve hoved-bibloket som brukes for å kjøre kalkulatoren i et eget vindu
# Å importere * betyr å importere alt fra tkinter


import numpy as np
#Numpy også kalt numerisk Python brukes i sammarbeid med Matplotlib for å få fram graf

import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from matplotlib.patches import Ellipse
from IPython.display import display, clear_output






# Vi lager kalkulatoren som en egen klasse kalt LoanCalculator


# __init__ representerer selve konstruksjonen hvor alt som skal lages i klassen
# Blir definert i selve "In it" i selve Lånekalkulatoren

#self - variabelen representerer forekomsten av selve objektet og metodene som definerer objektet. 

class LoanCalculator:
    def __init__(self):
        
        window = Tk()  # Her lager vi et vindu til programmet
        # Spesifiserer vinduet
        window.title("Annuitetskalkulator")
        window.geometry("600x300")
        
        #Vi lager elementene i vinduet og spesiffiserer lokalisering. På Pythonspråket starter indexene på null.
        #Lokaliseringen er gitt med rad, kolone og om den skal ligge West, East, North eller South.
        
        Label(window, text="Størrelse på lån").grid(row=0,
                                               column=1, sticky=W)
        Label(window, text="Antall år").grid(row=1,
                                         column=1, sticky=W)
        
        Label(window, text="Årlig rente").grid(row=2,   column=1, sticky=W)
        
        
    
        Label(window, text="Månedlig betaling").grid(row=3,
        
                                                column=1, sticky=W)
        
        Label(window, text="Total kostnad").grid(row=4,
                                             column=1, sticky=W)
        
        #For å ta inputs
        #Stringvar er en klasse for tkinter som observerer og moderer
        # Inputene er bokser som kan bli fylt med informasjon.
        #Vi bruker Stringvar slik at vi kan definere funksjonene i boksene
           
        self.StørrelsepålånVar = StringVar()
        Entry(window, textvariable=self.StørrelsepålånVar, 
          justify=LEFT).grid(row=0, column=2)
        
        
        self.AntallårVar = StringVar()
        Entry(window, textvariable=self.AntallårVar,
          justify=LEFT).grid(row=1, column=2)
        
          
        
        
        self.ÅrligrenteVar = StringVar()
        Entry(window, textvariable=self.ÅrligrenteVar,
          justify=LEFT).grid(row=2, column=2)

        
        
        
        #Så lager vi outputs - Det som blir resultat av inputtene.
        
        
        
        self.MånedligbetalingVar = StringVar()
        lblMånedligbetaling = Label(window, textvariable=self.MånedligbetalingVar).grid(row=3, column=2, sticky=E)
        
        self.TotalkostnadVar = StringVar()
        lblTotalkostnad = Label(window, textvariable=self.TotalkostnadVar).grid(row=4, column=2, sticky=E)
        
        
        #For å kunne gjøre beregningene trenger vi å lage knapper.
        
        btBeregn = Button(window, text="Beregn",
                                  command=self.Beregn).grid(
            row=5, column=3, sticky=E)
          # Create an event loop - To run the program
        
        
        
        btGraf = Button(window, text="Graf",
                                  command=self.Graf).grid(
            row=6, column=3, sticky=E)
        
        window.mainloop()
        
        #window.mainloop() Er en loop-funksjon i tkinter som gjør at vinduet holdes oppe til vinduet lukkes.





    # Vi definerer kalkuleringsknappen og hva knappen tar utgangspunkt i.
    # Beregn tar utgangspunkt i de tre inputknappene dermed blir inputene
    #Vi bruker .get() slik at vi hente output-knappen og spesifisere va den skal gjøre
    #Spesifisert som variabel med Var på slutten ex: Årligrente.var
    
    
    def Beregn(self):
        Månedligbetaling = self.getMånedligbetaling(
            float(self.StørrelsepålånVar.get()),
            float(self.ÅrligrenteVar.get()) / 1200,
            int(self.AntallårVar.get()))

        self.MånedligbetalingVar.set(format(Månedligbetaling, '10.2f')) # Vi setter format på output "10.2f" det vil si at det er 10 siffer totalt der 2 av dem kommer bak komma.
        Totalkostnad = float(self.MånedligbetalingVar.get()) * 12 \
            * int(self.AntallårVar.get())
            
            
        self.TotalkostnadVar.set(format(Totalkostnad, '10.2f'))
         
    #Vi regner ut månedlig betaling
    
           
    def getMånedligbetaling(self, Størrelsepålån, månedligrente, Antallår):
        Månedligbetaling = Størrelsepålån * månedligrente / \
            (1 - 1 / (1 + månedligrente) ** (Antallår * 12))
        return Månedligbetaling   
    
    
    def Graf(self):
        totalrest = []
        months = []
        rest = float(self.StørrelsepålånVar.get())
        for month in range(int(self.AntallårVar.get()) * 12):
            rest = rest - float(self.MånedligbetalingVar.get())
            print(rest)
            totalrest.append(rest)
            months.append(month)
        plt.plot(months, totalrest)
        plt.xlabel("Måneder")
        plt.ylabel("Restgjeld")
        plt.show()
        
   

 
LoanCalculator()