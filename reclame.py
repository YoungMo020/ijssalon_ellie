from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_aanbieding = prijs - (prijs * korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_aanbieding} euro."
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    inkomsten_week = sum(inkomsten)
    btw_bedrag = inkomsten_week * btw
    uitvoer = f"Het totaal van alle inkomsten deze week is {inkomsten_week} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return uitvoer

def laag_en_hoog(mijn_lijst):
    inkomen_hoog = max(mijn_lijst)
    inkomen_laag = min(mijn_lijst)
    uitvoer = f"Hoogste waarde: {inkomen_hoog}. Laagste waarde: {inkomen_laag}."
    return uitvoer

def gemiddelde(mijn_lijst):
    inkomen_gemiddelde = int(sum(inkomsten_per_dag) / 7)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {inkomen_gemiddelde} euro."
    return uitvoer

def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
lijst_integers = [10,5,3,2,1,2,9]

print(aanbieding_1("aardbei", 4, 0.1))
print(inkomsten_totaal(inkomsten_per_dag, 0.09))
print(laag_en_hoog(inkomsten_per_dag))
print(gemiddelde(inkomsten_per_dag))
print(meervoudig(lijst_integers))
