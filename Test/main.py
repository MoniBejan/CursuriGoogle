#declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
#afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
#afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
#afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
#afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
#afișarea elementelor multipli ai lui 3.
#a se păstra acuratețea indexilor - aceștia trebuie să fie cât mai specifici.
list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

list.sort()
print(list)

list.reverse()
print(list)
list.reverse()
print(list[1::2])
print(list[::2])
print(list[2::3])




