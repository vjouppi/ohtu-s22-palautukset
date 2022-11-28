from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.sisalto = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        lkm = 0
        for ostos in self.sisalto.keys():
            lkm += self.sisalto[ostos].lukumaara()
        return lkm
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for ostos in self.sisalto.keys():
            summa += self.sisalto[ostos].hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        nimi = lisattava.nimi()
        if nimi in self.sisalto:
            self.sisalto[nimi].muuta_lukumaaraa(1)
        else:
            self.sisalto[nimi] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        nimi = poistettava.nimi()
        if nimi in self.sisalto:
            self.sisalto[nimi].muuta_lukumaaraa(-1)
            if self.sisalto[nimi].lukumaara() == 0:
                del self.sisalto[nimi]

    def tyhjenna(self):
        self.sisalto = {}
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self.sisalto.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
