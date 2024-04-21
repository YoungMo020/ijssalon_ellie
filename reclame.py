def aanbieding_1(smaak, prijs, korting):
    prijs_aanbieding = prijs - (prijs * korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_aanbieding} euro."
    return uitvoer

def inkomsten_totaal(inkomsten):
    return sum(inkomsten)

print(aanbieding_1("aardbei", 4, 0.1))

inkomsten_dag = [220, 430, 125, 160, 205, 90, 345]
print("Inkomsten deze week:", inkomsten_totaal(inkomsten_dag))

