import os
import gtts

def list_rooms():
	for r in [os.path.splitext(filename)[0] for filename in os.listdir()]:
    		if r not in "main" and r not in "py":
        		print(r)


print("Salut !")
ready = "o" in input("Vous souhaitez remettre en ordre une pièce ? ?O/N").lower()

if ready:	
	list_rooms()
	room = input("Quelle pièce souhaitez-vous remettre en ordre ?")
	print(open(room + '.txt', mode='r',encoding="utf-8").read())

# Sélectionner l'action parmi la liste proposée de la salle 
# instruction = "En avant ta da da da da !"
# tts = gtts.gTTS(instruction, lang="fr")
# tts.save("sound.mp3")
# os.system("sound.mp3")

