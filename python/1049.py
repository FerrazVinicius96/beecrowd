lista = [["vertebrado", "mamifero", "onivoro"],
        ["vertebrado", "mamifero", "herbivoro"], 
        ["vertebrado", "ave", "carnivoro"], 
        ["vertebrado", "ave", "onivoro"],
        ["invertebrado", "inseto", "hematofago"],
        ["invertebrado", "inseto", "herbivoro"],
        ["invertebrado", "anelideo", "hematofago"],
        ["invertebrado", "anelideo", "onivoro"]] 

resposta = [input() for _ in range(3)]

for verificacao in range(len(lista)):
    if resposta == lista[0]:
        print('homem')
        break
    elif resposta == lista[1]:
        print('vaca')
        break
    elif resposta == lista[2]:
        print('aguia')
        break
    elif resposta == lista[3]:
        print('pomba')
        break
    elif resposta == lista[4]:
        print('pulga')
        break
    elif resposta == lista[5]:
        print('lagarta')
        break
    elif resposta == lista[6]:
        print('sanguessuga')
        break
    elif resposta == lista[7]:
        print('minhoca')
        break