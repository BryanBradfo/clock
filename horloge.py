import tkinter as tk
import time

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Horloge")

# Création de l'horloge
horloge = tk.Label(fenetre, font=('times', 20, 'bold'), bg='white')
horloge.pack(fill=tk.BOTH, expand=1)

# Fonction pour mettre à jour l'horloge toutes les secondes
def tick():
    heure_actuelle = time.strftime("%I:%M:%S %p")
    horloge.config(text=heure_actuelle)
    horloge.after(200, tick)

# Mise à jour de l'horloge pour la première fois
tick()

# Démarrage de la boucle principale de Tkinter
fenetre.mainloop()
