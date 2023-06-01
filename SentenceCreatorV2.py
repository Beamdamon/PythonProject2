from textblob import TextBlob
from textblob import Word
import tkinter as tk
import tkinter.font as TkFont
import random


# comments - name, assignment, estimate, actual
#Damon Beam - Library Implementations - Expected time 2 hours - Actual time: 2 hours
#A relatively simple addition to my project, I was just looking to add the two functions. Most of the time taken was figuring out how to get the functions to work, and then trial and
#error with the gui aspect of things. Functions work well to show subjectivity, but unfortunately did not improve the quality of the sentences.


#Classes - WordStructure, Word, Sentence
class WordStructure:
    def __init__(self, partsofspeech):
        self.partsofspeech = partsofspeech

class Word(WordStructure):
    def __init__(self, word):
        self.word = word

class Sentence(Word):
    def __init__(self, subject, predicate):
        self.subject = subject
        self.predicate = predicate

#Definite Article list of the three most common articles. Word list contains the 1000 most used words in English.
defArticleList = TextBlob("A The")
wordList = TextBlob(" of to and in is it you that he was for on are with as I his they be at one have this from or had by not word but what some we can out other were all there when up use your how said an each she which do their time if will way about many then them write would like so these her long make thing see him two has look more day could go come did number sound no most people my over know water than call first who may down side been now find any new work part take get place made live where after back little only round man year came show every good me give our under name very through just form sentence great think say help low line differ turn cause much mean before move right boy old too same tell does set three want air well also play small end put home read hand port large spell add even land here must big high such follow act why ask men change went light kind off need house picture try us again animal point mother world near build self earth father head stand own page should country found answer school grow study still learn plant cover food four between state keep eye never last let thought city tree cross farm hard start might story saw far sea draw left late run don't while press close night real life few north open seem together next white children begin got walk example ease paper group always music those both mark often letter until mile river car feet care second book carry took science eat room friend began idea fish mountain stop once base hear horse cut sure watch color face wood main enough plain girl usual young ready above ever red list though feel talk bird soon body dog family direct pose leave song measure door product black short numeral class wind question happen complete ship area half rock order fire south problem piece told knew pass since top whole king space heard best hour better true during hundred five remember step early hold west ground interest reach fast verb sing listen six table travel less morning ten simple several vowel toward war lay against pattern slow center love person money serve appear road map rain rule govern pull cold notice voice unit power town fine certain fly fall lead cry dark machine note wait plan figure star box noun field rest correct able pound done beauty drive stood contain front teach week final gave green oh quick develop ocean warm free minute strong special mind behind clear tail produce fact street inch multiply nothing course stay wheel full force blue object decide surface deep moon island foot system busy test record boat common gold possible plane stead dry wonder laugh thousand ago ran check game shape equate hot miss brought heat snow tire bring yes distant fill east paint language among grand ball yet wave drop heart am present heavy dance engine position arm wide sail material size vary settle speak weight general ice matter circle pair include divide syllable felt perhaps pick sudden count square reason length represent art subject region energy hunt probable bed brother egg ride cell believe fraction forest sit race window store summer train sleep prove lone leg exercise wall catch mount wish sky board joy winter sat written wild instrument kept glass grass cow job edge sign visit past soft fun bright gas weather month million bear finish happy hope flower clothe strange gone jump baby eight village meet root buy raise solve metal whether push seven paragraph third shall held hair describe cook floor either result burn hill safe cat century consider type law bit coast copy phrase silent tall sand soil roll temperature finger industry value fight lie beat excite natural view sense ear else quite broke case middle kill son lake moment scale loud spring observe child straight consonant nation dictionary milk speed method organ pay age section dress cloud surprise quiet stone tiny climb cool design poor lot experiment bottom key iron single stick flat twenty skin smile crease hole trade melody trip office receive row mouth exact symbol die least trouble shout except wrote seed tone join suggest clean break lady yard rise bad blow oil blood touch grew cent mix team wire cost lost brown wear garden equal sent choose fell fit flow fair bank collect save control decimal gentle woman captain practice separate difficult doctor please protect noon whose locate ring character insect caught period indicate radio spoke atom human history effect electric expect crop modern element hit student corner party supply bone rail imagine provide agree thus capital won't danger fruit rich thick soldier process operate guess necessary sharp wing create neighbor wash bat rather crowd corn compare poem string bell depend meat rub tube famous dollar stream fear sight thin triangle planet hurry chief colony clock mine tie enter major fresh search send yellow gun allow print dead spot desert suit current lift rose continue block chart hat sell success company subtract event particular deal swim term opposite wife shoe shoulder spread arrange camp invent cotton born determine quart nine truck noise level chance gather shop stretch throw shine property column molecule select wrong gray repeat require broad prepare salt nose plural anger claim continent oxygen sugar death pretty skill women season solution magnet silver thank branch match suffix especially fig afraid huge sister steel discuss forward similar guide experience score apple bought led pitch coat mass card band rope slip win dream evening condition feed tool total basic smell valley nor double seat arrive master track parent shore division sheet substance favor connect post spend chord fat glad original share station dad bread charge proper bar offer segment slave duck instant market degree populate chick dear enemy reply drink occur support speech nature range steam motion path liquid log meant quotient teeth shell neck")

#Sentence Parts of Speech:
#DT = Article
#IN = Preposition
#JJ = Adjective
#NN = Noun
#VB = verb
#RB = Adverb
# Some have modifiers attached, example: JJR = adjective, comparative


#Creates a list for each of the different parts of speech. Theses are then used to create the sentences in the functions below.
adjList = list()
for Word.word, WordStructure.partsofspeech in wordList.tags:
    if WordStructure.partsofspeech == 'JJ' or WordStructure.partsofspeech == 'JJR' or WordStructure.partsofspeech == 'JJS':
        adjList.append(Word.word)

verbList = list()
for Word.word, WordStructure.partsofspeech in wordList.tags:
    if WordStructure.partsofspeech == 'VB' or WordStructure.partsofspeech == 'VBD' or WordStructure.partsofspeech == 'VBG' or WordStructure.partsofspeech == 'VBN' or WordStructure.partsofspeech == 'VBP' or WordStructure.partsofspeech == 'VBZ':
        verbList.append(Word.word.pluralize())

advList = list()
for Word.word, WordStructure.partsofspeech in wordList.tags:
    if WordStructure.partsofspeech == 'RB' or WordStructure.partsofspeech == 'RBR' or WordStructure.partsofspeech == 'RBS' :
        advList.append(Word.word)

dArticleList = list()
for Word.word, WordStructure.partsofspeech in defArticleList.tags:
    if WordStructure.partsofspeech == 'DT':
        dArticleList.append(Word.word)

articleList = list()
for Word.word, WordStructure.partsofspeech in wordList.tags:
    if WordStructure.partsofspeech == 'DT':
        articleList.append(Word.word)

prepositionList = list()
for Word.word, WordStructure.partsofspeech in wordList.tags:
    if WordStructure.partsofspeech == 'IN':
        prepositionList.append(Word.word)

nounList = list()
for Word.word, WordStructure.partsofspeech in wordList.tags:
    if WordStructure.partsofspeech == 'NN' or WordStructure.partsofspeech == 'NNS' or WordStructure.partsofspeech == 'NNP' or WordStructure.partsofspeech == 'NNPS' :
        nounList.append(Word.word)

pronounList = list()
for Word.word, WordStructure.partsofspeech in wordList.tags:
    if WordStructure.partsofspeech == 'PRP' or WordStructure.partsofspeech == 'PRP$':
        pronounList.append(Word.word)


#Creates a three word sentence using the strucure: Article Noun Verb. Writes to it's respective file.
def three_word_sentence():
    writeFile = open('3WordSentences.txt', 'a')
    Sentence.subject = random.choice(dArticleList) + " "  + random.choice(nounList) + " "
    Sentence.predicate = random.choice(verbList) + "."
    sentenceLabel.config(text=Sentence.subject + Sentence.predicate)
    writeFile.write(Sentence.subject + Sentence.predicate + '\n')

#Creates a four word sentence using the strucure: Article Adjective Noun Verb. Writes to it's respective file.
def four_word_sentence():
    writeFile = open('4WordSentences.txt', 'a')
    Sentence.subject = random.choice(dArticleList) + " " + random.choice(adjList) + " " + random.choice(nounList) + " "
    Sentence.predicate = random.choice(verbList) + "."
    sentenceLabel.config(text=Sentence.subject + Sentence.predicate)
    writeFile.write(Sentence.subject + Sentence.predicate + '\n')
    writeFile.close()

#Creates a five word sentence using the strucure: Article Adjective Noun Verb adverb. Writes to it's respective file.
def five_word_sentence():
    writeFile = open('5WordSentences.txt', 'a')
    Sentence.subject = random.choice(dArticleList) + " " + random.choice(adjList) + " " + random.choice(nounList) + " "
    Sentence.predicate = random.choice(verbList) + " " + random.choice(advList) + "."
    sentenceLabel.config(text=Sentence.subject + Sentence.predicate)
    writeFile.write(Sentence.subject + Sentence.predicate + '\n')
    writeFile.close()

#Creates a six word sentence using the strucure: Article Noun Verb Preposition Article Noun. Writes to it's respective file.
def six_word_sentence():
    writeFile = open('6WordSentences.txt', 'a')
    Sentence.subject = random.choice(dArticleList) + " " + random.choice(nounList) + " "
    Sentence.predicate = random.choice(verbList) + " " + random.choice(prepositionList) + " " + random.choice(articleList) + " " + random.choice(nounList) + "."
    sentenceLabel.config(text=Sentence.subject + Sentence.predicate)
    writeFile.write(Sentence.subject + Sentence.predicate + '\n')
    writeFile.close()

#Creates a 5 word sentence that then filters for a subjective sentence,  prints to label sentence with subjectivity > 0.75
def subjectiveSentence(): 
    Sentence.subject = random.choice(dArticleList) + " " + random.choice(adjList) + " " + random.choice(nounList) + " "
    Sentence.predicate = random.choice(verbList) + " " + random.choice(advList) + "."
    newSentence = TextBlob(Sentence.subject + Sentence.predicate)

    while newSentence.subjectivity < 0.75:
        Sentence.subject = random.choice(dArticleList) + " " + random.choice(adjList) + " " + random.choice(nounList) + " "
        Sentence.predicate = random.choice(verbList) + " " + random.choice(advList) + "."
        newSentence = TextBlob(Sentence.subject + Sentence.predicate).correct()
    else:
        sentenceLabel.config(text=newSentence + "   Subjectivity:" + str(newSentence.subjectivity))

#Creates a 5 word sentence that then filters for a objective sentence,  prints to label sentence with subjectivity < 0.25
def objectiveSentence(): 
    Sentence.subject = random.choice(dArticleList) + " " + random.choice(adjList) + " " + random.choice(nounList) + " "
    Sentence.predicate = random.choice(verbList) + " " + random.choice(advList) + "."
    newSentence = TextBlob(Sentence.subject + Sentence.predicate)

    while newSentence.subjectivity > 0.25:
        Sentence.subject = random.choice(dArticleList) + " " + random.choice(adjList) + " " + random.choice(nounList) + " "
        Sentence.predicate = random.choice(verbList) + " " + random.choice(advList) + "."
        newSentence = TextBlob(Sentence.subject + Sentence.predicate).correct()
    else:
        sentenceLabel.config(text=newSentence + "   Subjectivity:" + str(newSentence.subjectivity))
   
#Tkinter Window and Values - Main Menu

window = tk.Tk()
greeting = tk.Label(text="Sentence Creator - Main Menu")
greeting.pack()
font = TkFont.Font(size=36)

label = tk.Label(text= """
    1 = Create a 3 word sentence (Article Noun Verb)
    2 = Create a 4 word sentence (Article Adjective Noun Verb)
    3 = Create a 5 word sentence (Article Adjective Noun Verb Adverb)
    4 = Create a 6 word sentence (Article Noun Verb Preposition Article Noun)
    5 = Creates a Subjective 5 word sentence
    6 = Creates a Objective 5 word sentence
    7 = Exit
    """, bg="gray30", fg="white", width=143, height=10)
label.config(font=(24))
label.pack()

sentenceLabel = tk.Label(text= "", width=143, height=5, background="gray30", fg="white")
sentenceLabel.config(font=(24))
sentenceLabel.pack()

button1 = tk.Button(
    text="1", width=25, height=5, bg="DarkSlateGray4", fg="white",)
def handle_click1(event):
    three_word_sentence()
button1.bind("<Button-1>", handle_click1)
button1.pack(side=tk.LEFT)

button2 = tk.Button(
    text="2", width=25, height=5, bg="DarkSlateGray4", fg="white",)
def handle_click2(event):
    four_word_sentence()
button2.bind("<Button-1>", handle_click2)
button2.pack(side=tk.LEFT)

button3 = tk.Button(
    text="3", width=25, height=5, bg="DarkSlateGray4", fg="white",)
def handle_click3(event):
    five_word_sentence()
button3.bind("<Button-1>", handle_click3)
button3.pack(side=tk.LEFT)

button4 = tk.Button(
    text="4", width=25, height=5, bg="DarkSlateGray4", fg="white",)
def handle_click4(event):
    six_word_sentence()
button4.bind("<Button-1>", handle_click4)
button4.pack(side=tk.LEFT)

button5 = tk.Button(
    text="5", width=25, height=5, bg="DarkSlateGray4", fg="white",)
def handle_click5(event):
    subjectiveSentence()
button5.bind("<Button-1>", handle_click5)
button5.pack(side=tk.LEFT)

button6 = tk.Button(
    text="6", width=25, height=5, bg="DarkSlateGray4", fg="white",)
def handle_click6(event):
    objectiveSentence()
button6.bind("<Button-1>", handle_click6)
button6.pack(side=tk.LEFT)

button7 = tk.Button(
    text="7", width=25, height=5, bg="DarkSlateGray4", fg="white",)
def handle_click7(event):
    window.destroy()   
button7.bind("<Button-1>", handle_click7)
button7.pack(side=tk.LEFT)

window.mainloop()