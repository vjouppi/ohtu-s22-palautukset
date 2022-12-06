KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin täytyy olla postiivinen kokonaisluku")  # heitin vaan jotain :D

        self.kapasiteetti = kapasiteetti
        
        self.kasvatuskoko = kasvatuskoko

        self.lukujoukko = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.lukujoukko:
            return True
        else:
            return False

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.lukujoukko[0] = n
            self.alkioiden_lkm = 1
            return True

        if not self.kuuluu(n):
            self.lukujoukko[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.lukujoukko) == 0:
                taulukko_old = self.lukujoukko
                self.kopioi_taulukko(self.lukujoukko, taulukko_old)
                self.lukujoukko = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.lukujoukko)

            return True

        return False

    def poista(self, n):
        kohta = -1
        temp = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujoukko[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujoukko[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                temp = self.lukujoukko[j]
                self.lukujoukko[j] = self.lukujoukko[j + 1]
                self.lukujoukko[j + 1] = temp

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujoukko[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujoukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujoukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujoukko[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
