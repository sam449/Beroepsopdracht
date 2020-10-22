#!/usr/bin/env python
# coding: utf-8

# In[17]:


def storyG():
    print('Toen ze aankwamen in Nederland ging Ibrahim een verblijfsvergunning aanvragen met zijn gezin. Hij wou niet in een vluchtelingenkamp slapen en ging slapen in dure hotels. Het geld ging sneller op dan dat er binnenkwam na 1 jaar kreeg het hele gezin een verblijfsvergunning. Hij had geen geld meer over door de dure hotels en moest het gezin gaan slapen op straat omdat ze nog geen uitkering hadden gekregen terwijl de Ibrahim daar wel op gerekend had. Na 1 jaar leven op straat bij daklozenopvangen overnachten kreeg hij eindelijk zijn uitkering. En woont nu gelukkig met zijn gezin in de Kraaiennest flat in de Bijlmer Amsterdam zuid-oost. Ze hebben het overleefd en leven nu een stress loos leven.')


# In[18]:


def storyF():
    print('Eenmaal in Nederland aangekomen moesten ze een verblijfsvergunning aanvragen voor het hele gezin. Gelukkig had de vader wel nog geld en kon hij na zijn verblijfsvergunning een appartement huren. Door zijn goede studie kon hij snel een nieuwe baan vinden hier in Nederland. Zijn vrouw die geen opleiding gedaan heeft ging in Nederland rechten studeren na een traject van school. Nu na twintig jaar wonen in Nederland woont het gezin weer in een groot huis in Amstelveen. De oudste zoon is inmiddels uit huis en woont op zichzelf hij is een artiest en geeft les op scholen. Yazen (de jongste van het gezin) gaat nu naar de universiteit')
    


# In[19]:


def storyE():
    print('De lange tocht had hun volstrekt uitgeput! Met een draaiend hoofd ging Ibrahim opzoek naar de volgende vrachtwagen die hun nog dieper Europa in zou brengen. Na 1 plaspauze in 14 uur en met nog 15 uur reistijd te gaan kwamen ze eindelijk aan in waar zij dachten Europa te zijn... Maar nee ze kwamen aan in een Russische ghetto waar hun organen gestolen werden en verkocht werden hun lichaam werd in de fik gestoken en zo komen we ook aan het einde van het verhaal..... Erg jammer dat ze het niet overleeft hebben..... (Maar jij wou het verhaal weten, hier alsjeblieft misgunner)')


# In[20]:


def storyD():
    print('De smokkelaar vroegen zoveel geld dat hij bijna niks meer overhad. Het enige wat hij nog kon betalen was eten voor een week en een hotel voor een week. Daarna zou al het geld op zijn. Zijn vrouw ging nadenken hoe ze aan geld konden komen en vonden een uitzendbureau in Roemenië die banen aanbood in Nederland. Maar omdat hij geen Europees paspoort had werd dat erg lastig. Bij de dorps supermarkt kon hij aan een zwart betaald baantje komen. En zijn gezin mocht slapen in het magazijn. Waar genoeg eten en drinken was. Maar ze hebben de tocht wel overleeft en door de goede relatie tussen Ibrahim en zijn vrouw ging hij akkoord met een minimum levensstijl die hij eerder niet gewend was. Maar ze leefden nog lang en gelukkig.')


# In[21]:


def storyC():
    print('Ibrahim en zijn gezin gingen vluchten voor de Saudi Arabische regering. Ze gingen met de vrachtwagen van een smokkelaar naar Irak en daarna via Turkije naar Europa.  De smokkelaar vroegen veel geld om naar Europa te gaan en ze hadden bijna geen geld meer over. Door een lange reis met weinig zuurstof waren ze helemaal kapot aangekomen in Roemenië.')
    print('A) Overleven \nB) overleiden')
    A = ["a","A"]
    B = ["b","B"]
    antwoord_C = input()
    if antwoord_C in A :
        #story D
        storyD()
    elif antwoord_C in B:
        #stroy E
        storyE()
    else:
        print('watkanjewel.nl')
    


# In[22]:


def storyB():
    print('Ibrahim en zijn gezin gingen op de vlucht voor de Saudi Arabische regering. Daar hebben ze verplicht een vliegtuig moeten pakken om naar een ander land te gaan. Ze gingen vluchten naar Turkije. Toen het gezin aankwam in Turkije zijn ze met een transport container naar Europa gegaan en kwamen aan in Italië. Vanuit Italië is het gezin met een taxie naar Nederland gekomen. Toen zij in Nederland aankwamen was alles anders. Een nieuwe wereld zonder baan of kennis van het land.')
    print('A) tijdje dakloos \nB) Veel geld')
    A = ["a","A"]
    B = ["b","B"]
    antwoord_B = input()
    if antwoord_B in A :
        #story G
        storyG()
    elif antwoord_B in B:
        #stroy F
        storyF()
    else:
        print('watkanjewel.nl')
    


# In[23]:


def begin():                        #functie
    print('Mijn verhaal gaat over Ibrahim de vader van een vriend van mij. Voor zijn vertrek naar Nederland zat hij in de politiek. Ze woonden in een mooi groot huis in Riyadh. Ibrahim had een hoge functie in de politiek in Saudi Arabia. Hij woonde samen met zijn vrouw en twee kinderen. Hij was erg gehoorzaam naar de politiek in Saudi Arabia totdat hij het ergens niet mee eens was. Hij gaf tegen gas en had een weerwoord dit tolereerde Saudi Arabia vervolgens niet en hebben hem uit het land gezet (verbannen) en als hij niet zou vertrekken naar een ander land dan zou hij gevangen worden genomen en vervolgens vermoord worden. Waar Ibrahim het niet mee eens was is niet duidelijk volgens Yazen (één van de twee zonen) volgens hem heeft hij dat nog nooit aan niemand vertelt, wel is hem vertelt dat als hij terug zou gaan naar Saudi Arabia dat hij vermoordt zou worden. Terwijl een groot deel van zijn familie gewoon nog leeft in Saudi Arabia.')            #functie 
    print('A) vrachtwagen \nB) vliegtuig')
    A = ["a", "A"]
    B = ["b", "B"]
    antwoord_A = input()
    if antwoord_A in A:          #if zoekt elif else zoekt 
        #story B
        storyB()
    elif antwoord_A in B:
        #stroy C
        storyC()
    else:
        print('LET OP/ antwoord alleen met a of b!')
        


# In[25]:


begin()


# In[ ]:




