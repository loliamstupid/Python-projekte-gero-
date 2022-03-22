#von Gero
#Github:loliamstupid
#Konktakt:gero.batt@gmail.com
import random
zufallsantwort =['oh wirklich', 'interessant...', 'kann man so sehen ','aah ich verstehe ']
reaktionsantworten = {"hallo":   "aber Hallo",
					  "geht":    "Was verstehst du darunter?",
					  "essen":   "Ich habe leider keinen Geschmackssinn :(",
                      'hey':    'bin beschäfigt sorry:(',
                      'wmd':    'das müssen sie meinen autor fragen wenn er wider da ist sie werden eine nachricht bekommen wenn er da ist',
                      'komm on':    'nacher oder gleich',
                      'kunst':    'ist toll am meisten mit herr All sindy ',
                      'nein':   'doch',
                      'doch':   'nein',
                      'du bist dumm':   'nein du ha:)',
                      'help':   'kontakt unter Github loliamstupid oder gero.batt@gmail.com'

					  }

print('wilkommen beim chatbot')
print('wöruber möchten sie gerne sprechen')
print('um den chatbot zu beenden einfach  "bye"  eintippen')
print('')

nutzereingabe = ''
while nutzereingabe !='bye':
    nutzereingabe =''
    while nutzereingabe == '':
        nutzereingabe = input("Ihre Frage/Antwort: ")
        nutzereingabe = nutzereingabe.lower()
        nutzerwoerter = nutzereingabe.split()

        intelligenteAntworten = False
        for einzelwoerter in nutzerwoerter:
            if einzelwoerter in reaktionsantworten:
                print(reaktionsantworten[einzelwoerter])
                intelligenteAntworten = True
        if intelligenteAntworten == False:
            print(random.choice(zufallsantwort))

        print('')

print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal")
exit()



