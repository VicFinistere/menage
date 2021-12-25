import os
import gtts

print("Salut !")
print("Vous avez un peu de temps ?") 
for r in [os.path.splitext(filename)[0] for filename in os.listdir()]:
    if r not in 'main':
        print(r)
room = input("Quelle pièce souhaitez-vous remettre en ordre ?")
print(open(room + '.txt', mode='r',encoding="utf-8").read())

# Sélectionner l'action parmi la liste proposée de la salle 
tts = gtts.gTTS("Bon appétit Céline ! Billy va au panier s'il te plaît!", lang="fr")
tts.save("sound.wav")
os.system("sound.mp3")

