class Hero:
    def __init__(self, jmeno:str, lvl:int, lokace= "hrad"):
        self.jmeno = jmeno
        self.lvl = lvl
        self.lokace = lokace 
        pass

    def pokrik(self):
        return "bleeeeee"

    def predstavSe(self):
        return f"Jmenuji se {self.jmeno} a mam level {self.lvl}"

    def kdeJsi(self):
        return f"Jsem v místě zvaném {self.lokace}"

    def presun_se(self, lokace:str):
        self.lokace = lokace
        return f"Přesunul jsem se do {self.lokace}"


hero = Hero("matyas",99)
print(hero.pokrik())
print(hero.predstavSe())
print(hero.presun_se("les"))
print(hero.kdeJsi())
