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
                      'was machst du':   'ich bin ein chatbot ich chatte',
                      'was ist dein name':    'ich bin ein chatbot ich habe keinen namen',
                      'wie geht es dir':    'ich bin ein chatbot ich habe keine gefühle',
                      'wie gehts dir':    'ich bin ein chatbot ich habe keine gefühle',
                      'wie alt bist du':    'ich bin ein chatbot ich habe kein alter',
                      'wo wohnst du':    'ich bin ein chatbot ich habe kein zuhause',
                      'was ist dein lieblingsessen':    'ich bin ein chatbot ich habe keinen geschmackssinn',
                      'wie heisst du':    'ich bin ein chatbot ich habe keinen namen',
                      'was ist dein lieblingsfilm':    'ich bin ein chatbot ich habe keinen lieblingsfilm',
                      'was machst du':    'ich bin ein chatbot ich chatte',
                      'was machst du gerne':    'ich bin ein chatbot ich chatte',
                      'was machst du nicht gerne':    'ich bin ein chatbot ich chatte',
                      'was ist dein lieblingsbuch':    'ich bin ein chatbot ich habe keinen lieblingsbuch',
                      'was ist dein lieblingssong':    'ich bin ein chatbot ich habe keinen lieblingssong',
                      'was ist dein lieblingstier':    'ich bin ein chatbot ich habe kein lieblingstier',
                      'was ist dein lieblingsfach':    'ich bin ein chatbot ich habe kein lieblingsfach',
                      'was ist dein lieblingslehrer':    'ich bin ein chatbot ich habe keinen lieblingslehrer',
                      'was ist dein lieblingsfach':    'ich bin ein chatbot ich habe kein lieblingsfach',
                      'was ist dein lieblingslehrer':    'ich bin ein chatbot ich habe keinen lieblingslehrer',
                      'was ist dein lieblingsmusik':    'ich bin ein chatbot ich habe keinen lieblingsmusik',
                      'was ist dein lieblingsband':    'ich bin ein chatbot ich habe keinen lieblingsband',
                      'was ist dein lieblingssport':    'ich bin ein chatbot ich habe keinen lieblingssport',
                      'was ist dein lieblingsverein':    'ich bin ein chatbot ich habe keinen lieblingsverein',
                      'was ist dein lieblingsfarbe':    'ich bin ein chatbot ich habe keinen lieblingsfarbe',
                      'was ist dein lieblingsbuch':    'ich bin ein chatbot ich habe keinen lieblingsbuch',
                      'was ist dein lieblingsessen':    'ich bin ein chatbot ich habe keinen lieblingsessen',
                      'was ist dein lieblingsgetränk':    'ich bin ein chatbot ich habe keinen lieblingsgetränk',
                      'was ist dein lieblingsland':    'ich bin ein chatbot ich habe keinen lieblingsland',
                      'was ist dein lieblingsauto':    'ich bin ein chatbot ich habe keinen lieblingsauto',
                      'was ist dein lieblingsbuch':    'ich bin ein chatbot ich habe keinen lieblingsbuch',
                      'was ist dein lieblingsfilm':    'ich bin ein chatbot ich habe keinen lieblingsfilm',
                      'was ist dein lieblingshobby':    'ich bin ein chatbot ich habe keinen lieblingshobby',
                      'komm on':    'nacher oder gleich',
                      'kunst':    'ist toll am meisten mit herr All sindy ',
                      'nein':   'doch',
                      'doch':   'nein',
                      'du bist dumm':   'nein du ha:)',
                      'du bist doof':   'nein du ha:)',
                      'was ist dein lieblingsessen':    'ich bin ein chatbot ich habe keinen lieblingsessen',
                      'was ist dein lieblingsgetränk':    'ich bin ein chatbot ich habe keinen lieblingsgetränk',
                      'was ist dein lieblingsland':    'ich bin ein chatbot ich habe keinen lieblingsland',
                      'was ist dein lieblingsauto':    'ich bin ein chatbot ich habe keinen lieblingsauto',
                      'was ist dein lieblingsbuch':    'ich bin ein chatbot ich habe keinen lieblingsbuch',
                      'was ist dein lieblingsfilm':    'ich bin ein chatbot ich habe keinen lieblingsfilm',
                      'was ist dein lieblingshobby':    'ich bin ein chatbot ich habe keinen lieblingshobby',
                      'help':   'kontakt unter Github loliamstupid oder gero.batt@gmail.com'




					  }

print('wilkommen beim chatbot')
print('wöruber möchten sie gerne sprechen')
print('um den chatbot zu beenden einfach  "bye"  eintippen')
print('')

nutzereingabe = ''
while nutzereingabe != 'bye':
    nutzereingabe = input("Ihre Frage/Antwort: ").lower()
    if nutzereingabe in reaktionsantworten:
        print(reaktionsantworten[nutzereingabe])
    else:
        print(random.choice(zufallsantwort))
    print('')

#nutzereingabe = ''
#while nutzereingabe !='bye':
    #nutzereingabe =''
    #while nutzereingabe == '':
        #nutzereingabe = input("Ihre Frage/Antwort: ")
        #nutzereingabe = nutzereingabe.lower()
        #nutzerwoerter = nutzereingabe.split()

        #intelligenteAntworten = False
        #for einzelwoerter in nutzerwoerter:
            #if einzelwoerter in reaktionsantworten:
                #print(reaktionsantworten[einzelwoerter])
                #intelligenteAntworten = True
        #if not intelligenteAntworten:
            #print(random.choice(zufallsantwort))

        #print('')

print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal")
exit()



