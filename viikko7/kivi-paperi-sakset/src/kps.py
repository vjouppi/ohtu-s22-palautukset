from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._siirto_pl1()
        tokan_siirto = self._siirto_pl2(None)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._siirto_pl1()
            tokan_siirto = self._siirto_pl2(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _siirto_pl1(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _siirto_pl2(self, ensimmaisen_siirto):
        return "p"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _siirto_pl2(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _siirto_pl2(self, ensimmaisen_siirto):
        omasiirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {omasiirto}")
        return omasiirto

class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _siirto_pl2(self, ensimmaisen_siirto):
        omasiirto = self.tekoaly.anna_siirto()
        if ensimmaisen_siirto is not None:
            self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        print(f"Tietokone valitsi: {omasiirto}")
        return omasiirto

def luo_peli(tyyppi):
    if tyyppi == 'a':
        return KPSPelaajaVsPelaaja()
    if tyyppi == 'b':
        return KPSTekoaly()
    if tyyppi == 'c':
        return KPSParempiTekoaly()
    return None
