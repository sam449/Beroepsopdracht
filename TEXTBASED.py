#!/usr/bin/env python
# coding: utf-8

# In[12]:


def storyT():
    print('Dat is het einde van mijn Text- Based applicatie, ik wens u nog een fijne dag!') #storyT


# In[13]:


def storyU():
    print('Helaas, dit is het einde van mijn Text- Based applicatie') #storyU


# In[14]:


def storyS():            # s naar U of U
    print('Toen ze aankwamen in Nederland ging Ibrahim een verblijfsvergunning aanvragen met zijn gezin. Hij wou niet in een vluchtelingenkamp slapen en ging slapen in dure hotels. Het geld ging sneller op dan dat er binnenkwam na 1 jaar kreeg het hele gezin een verblijfsvergunning. Hij had geen geld meer over door de dure hotels en moest het gezin gaan slapen op straat omdat ze nog geen uitkering hadden gekregen terwijl de Ibrahim daar wel op gerekend had. Na 1 jaar leven op straat bij daklozenopvangen overnachten kreeg hij eindelijk zijn uitkering. En woont nu gelukkig met zijn gezin in de Kraaiennest flat in de Bijlmer Amsterdam zuid-oost. Ze hebben het overleefd en leven nu een stress loos leven. ') #verhaal S 
    print('A) Pipo \nB) Rico')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_S = input()
    if antwoord_S in A:
        #story u
        storyU()
    elif antwoord_S in B:
        #stroy u
        storyU()
    else:
        print('schrijf alleen A of B')


# In[15]:


def storyR():            # r naar U of U
    print('Eenmaal in Nederland aangekomen moesten ze een verblijfsvergunning aanvragen voor het hele gezin. Gelukkig had de vader wel nog geld en kon hij na zijn verblijfsvergunning een appartement huren. Door zijn goede studie kon hij snel een nieuwe baan vinden hier in Nederland. Zijn vrouw die geen opleiding gedaan heeft ging in Nederland rechten studeren na een traject van school. Nu na twintig jaar wonen in Nederland woont het gezin weer in een groot huis in Amstelveen. De oudste zoon is inmiddels uit huis en woont op zichzelf hij is een artiest en geeft les op scholen. Yazen (de jongste van het gezin) gaat nu naar de universiteit. ') #verhaal r 
    print('A) Einde \nB) Ja?')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_R = input()
    if antwoord_R in A:
        #story u
        storyU()
    elif antwoord_R in B:
        #stroy u
        storyU()
    else:
        print('schrijf alleen A of B')


# In[16]:


def storyM():            # M naar Q of Q
    print(' (Dat is helaas fout!)          Ga verder met het verhaal kies a of b') #verhaal k 
    print('A) ....... \nB) ........')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_Q = input()
    if antwoord_Q in A:
        #story q
        storyQ()
    elif antwoord_Q in B:
        #stroy q
        storyQ()
    else:
        print('schrijf alleen A of B')


# In[17]:


def storyL():            # L naar r of r
    print(' (Dat is het juiste antwoord!)     Ga verder met het verhaal kies a of b') #verhaal L
    print('A) ....... \nB) ........')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_P = input()
    if antwoord_P in A:
        #story r
        storyR()
    elif antwoord_P in B:
        #stroy r
        storyR()
    else:
        print('schrijf alleen A of B')


# In[18]:


def storyO():            # O naar s of s
    print('  Neeej, hij is gevlucht met zijn hele gezin ') #verhaal o 
    print('A) dat \nB) dit')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_O = input()
    if antwoord_O in A:
        #story s
        storyS()
    elif antwoord_O in B:
        #stroy s
        storyS()
    else:
        print('schrijf alleen A of B')


# In[19]:


def storyN():            # N naar s of s
    print(' Dat klopt hij is met zijn hele gezin gevlucht') #verhaal n 
    print('A) OH \nB) AGH')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_N = input()
    if antwoord_N in A:
        #story s
        storyS()
    elif antwoord_N in B:
        #stroy s
        storyS()
    else:
        print('schrijf alleen A of B')


# In[20]:


def storyG():            # g naar n of o
    print('Is hij gevlucht met zijn hele gezin? ') #verhaal G 
    print('A) Ja \nB) Nee')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_M = input()
    if antwoord_M in A:
        #story n
        storyN()
    elif antwoord_M in B:
        #stroy o
        storyO()
    else:
        print('schrijf alleen A of B')


# In[21]:


def storyF():            # f naar l of m
    print('Hoeveel koste de reis denk je? ') #verhaal F 
    print('A) €1000,-  \nB) €2250,-')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_L = input()
    if antwoord_L in A:
        #story l
        storyL()
    elif antwoord_L in B:
        #stroy m
        storyM()
    else:
        print('schrijf alleen A of B')


# In[22]:


def storyC():            # C naar F of G
    print(' Ibrahim en zijn gezin gingen op de vlucht voor de Saudi Arabische regering. Daar hebben ze verplicht een vliegtuig moeten pakken om naar een ander land te gaan. Ze gingen vluchten naar Turkije. Toen het gezin aankwam in Turkije zijn ze met een transport container naar Europa gegaan en kwamen aan in Italië. Vanuit Italië is het gezin met een taxie naar Nederland gekomen. Toen zij in Nederland aankwamen was alles anders. Een nieuwe wereld zonder baan of kennis van het land. (Voor dat we verder gaan, wat wil je van Ibrahim weten?) ( Verder in het verhaal, (A) krijgt Ibrahim later een welvarend leven)(B)Krijgt Ibrahim een normaal leven) ') #verhaal C 
    print('A) Koste reis \nB) Hele gezin mee?')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_K = input()
    if antwoord_K in A:
        #story F
        storyF()
    elif antwoord_K in B:
        #stroy G
        storyG()
    else:
        print('schrijf alleen A of B')


# In[23]:


def storyQ():            # q naar t of t
    print('De lange tocht had hun volstrekt uitgeput! Met een draaiend hoofd ging Ibrahim opzoek naar de volgende vrachtwagen die hun nog dieper Europa in zou brengen. Na 1 plaspauze in 14 uur en met nog 15 uur reistijd te gaan kwamen ze eindelijk aan in waar zij dachten Europa te zijn... Maar nee ze kwamen aan in een Russische ghetto waar hun organen gestolen werden en verkocht werden hun lichaam werd in de fik gestoken en zo komen we ook aan het einde van het verhaal..... Erg jammer dat ze het niet overleeft hebben..... (Maar jij wou het verhaal weten, hier alsjeblieft misgunner) ') #verhaal q 
    print('A) Doei \nB) Doeg')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_J = input()
    if antwoord_J in A:
        #story t
        storyT()
    elif antwoord_J in B:
        #stroy t
        storyT()
    else:
        print('schrijf alleen A of B')


# In[24]:


def storyP():            # p naar t of t
    print(' De smokkelaar vroegen zoveel geld dat hij bijna niks meer overhad. Het enige wat hij nog kon betalen was eten voor een week en een hotel voor een week. Daarna zou al het geld op zijn. Zijn vrouw ging nadenken hoe ze aan geld konden komen en vonden een uitzendbureau in Roemenië die banen aanbood in Nederland. Maar omdat hij geen Europees paspoort had werd dat erg lastig. Bij de dorps supermarkt kon hij aan een zwart betaald baantje komen. En zijn gezin mocht slapen in het magazijn. Waar genoeg eten en drinken was. Maar ze hebben de tocht wel overleeft en door de goede relatie tussen Ibrahim en zijn vrouw ging hij akkoord met een minimum levensstijl die hij eerder niet gewend was. Maar ze leefden nog lang en gelukkig.') #verhaal P
    print('A) Doorgaan \nB) Einde ')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_I = input()
    if antwoord_I in A:
        #story t
        storyT()
    elif antwoord_I in B:
        #stroy t
        storyT()
    else:
        print('schrijf alleen A of B')


# In[25]:


def storyK():            # k naar Q of Q
    print(' Dat is juist! Kiez A of B om verder te gaan ') #verhaal k 
    print('A) willekeurig \nB) willekeurig')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_H = input()
    if antwoord_H in A:
        #story q
        storyQ()
    elif antwoord_H in B:
        #stroy q
        storyQ()
    else:
        print('schrijf alleen A of B')


# In[26]:


def storyJ():            # j naar Q of Q
    print('(Dat is onjuist, Ibrahim is 40 jaar oud')    # verhaal J 
    print('A) willekeurig \nB) willekeurig')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_G = input()
    if antwoord_G in A:
        #story q
        storyQ()
    elif antwoord_G in B:
        #stroy q
        storyQ()
    else:
        print('schrijf alleen A of B')


# In[27]:


def storyE():            # e naar j of k
    print(' Leeftijd van Ibrahim?') #verhaal e
    print('A) 60 jaar oud \nB) 40 jaar oud')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_F = input()
    if antwoord_F in A:
        #story j
        storyJ()
    elif antwoord_F in B:
        #stroy k
        storyK()
    else:
        print('schrijf alleen A of B')


# In[28]:


def storyI():            # H naar p of p
    print('(Dat is helaas fout!)          Ga verder met het verhaal kies a of b ') #verhaal I 
    print('A) Maak zelf een keuze \nB) Het is aan jou!')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_E = input()
    if antwoord_E in A:
        #story p
        storyP()
    elif antwoord_E in B:
        #stroy p
        storyP()
    else:
        print('schrijf alleen A of B')


# In[29]:


def storyH():            # H naar p of p
    print('(Dat is het juiste antwoord!)     Ga verder met het verhaal kies a of b ') #verhaal H 
    print('A) maak zelf een keuze \nB) Het is aan jou!')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_D = input()
    if antwoord_D in A:
        #story p
        storyP()
    elif antwoord_D in B:
        #stroy p
        storyP()
    else:
        print('schrijf alleen A of B')


# In[30]:


def storyD():            # D naar H of I
    print(' ') #verhaal D 
    print('A) 185cm \nB) 175cm')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_C = input()
    if antwoord_C in A:
        #story h
        storyH()
    elif antwoord_C in B:
        #stroy i
        storyI()
    else:
        print('schrijf alleen A of B')


# In[31]:


def storyB():            # B naar D of E
    print('Ibrahim en zijn gezin gingen vluchten voor de Saudi Arabische regering. Ze gingen met de vrachtwagen van een smokkelaar naar Irak en daarna via Turkije naar Europa.  De smokkelaar vroegen veel geld om naar Europa te gaan en ze hadden bijna geen geld meer over. Door een lange reis met weinig zuurstof waren ze helemaal kapot aangekomen in Roemenië. (Voor dat we verder gaan wat wil je van Ibrahim weten?) ( Verder in het verhaal, (A) Ibrahim overleeft de reis)(B)Overleefd de reis niet)') #verhaal B 
    print('A) Lengte \nB) Leeftijd')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_B = input()
    if antwoord_B in A:
        #story d
        storyD()
    elif antwoord_B in B:
        #stroy e
        storyE()
    else:
        print('schrijf alleen A of B')


# In[38]:


def begin():            #new Begin naar B of C
    print('Begin Mijn verhaal gaat over Ibrahim de vader van een vriend van mij. Voor zijn vertrek naar Nederland zat hij in de politiek. Ze woonden in een mooi groot huis in Riyadh. Ibrahim had een hoge functie in de politiek in Saudi Arabia. Hij woonde samen met zijn vrouw en twee kinderen. Hij was erg gehoorzaam naar de politiek in Saudi Arabia totdat hij het ergens niet mee eens was. Hij gaf tegen gas en had een weerwoord dit tolereerde Saudi Arabia vervolgens niet en hebben hem uit het land gezet (verbannen) en als hij niet zou vertrekken naar een ander land dan zou hij gevangen worden genomen en vervolgens vermoord worden. Waar Ibrahim het niet mee eens was is niet duidelijk volgens Yazen (één van de twee zonen) volgens hem heeft hij dat nog nooit aan niemand vertelt, wel is hem vertelt dat als hij terug zou gaan naar Saudi Arabia dat hij vermoordt zou worden. Terwijl een groot deel van zijn familie gewoon nog leeft in Saudi Arabia.')
    print('A) Vrachtwagen \nB) Vliegtuig')      # A en B moet nog een keuze maken
    A = ["a","A"]
    B = ["b","B"]
    antwoord_A = input()
    if antwoord_A in A:
        #story B
        storyB()
    elif antwoord_A in B:
        #stroy C
        storyC()
    else:
        print('schrijf alleen A of B')


# In[ ]:


begin()


# In[ ]:




