class Ruha:
    def __init__(self, nev, meret, ar):
        self.nev = nev
        self.meret = meret
        self.ar = ar

    def __str__(self):
        return f"{self.nev} ({self.meret}) - {self.ar} Ft"


def beolvas_fajlbol(fajlnev):
    ruhak = []
    with open("megadottak.txt", "r", encoding="utf-8") as fajl:
        for sor in fajl:
            reszek = sor.strip().split()
            ruhak.append(Ruha(reszek[0], reszek[1], int(reszek[2])))
    return ruhak


def beker_ruhak():
    ruhak = []
    for _ in range(3):
        nev = input("Add meg a ruhadarab nevét: ")
        meret = input("Add meg a ruhadarab méretét: ")
        ar = int(input("Add meg a ruhadarab árát: "))
        ruhak.append(Ruha(nev, meret, ar))
    return ruhak


def legdragabb_ruha(ruhak):
    legdragabb = ruhak[0]
    for ruha in ruhak:
        if ruha.ar > legdragabb.ar:
            legdragabb = ruha
    return legdragabb


def kiir_legdragabb(fajlnev, ruha):
    with open("megadottak.txt", "w", encoding="utf-8") as fajl:
        fajl.write(ruha.nev + "\n")


def rendezett_kiiras(ruhak):
    for i in range(len(ruhak) - 1):
        for j in range(i + 1, len(ruhak)):
            if ruhak[i].ar < ruhak[j].ar:
                ruhak[i], ruhak[j] = ruhak[j], ruhak[i]

    print("\nRuhák ár szerint csökkenő sorrendben:")
    for ruha in ruhak:
        print(ruha)


ruhak = beolvas_fajlbol("ruhak.txt")
ruhak.extend(beker_ruhak())

legdragabb = legdragabb_ruha(ruhak)
kiir_legdragabb("legdragabb.txt", legdragabb)

rendezett_kiiras(ruhak)
