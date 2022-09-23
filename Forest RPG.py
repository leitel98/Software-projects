import random
import time


def fightmon(p1, p2):
    act = input("What do you want to do?\n"
                "a-> attack\n"
                "s-> use skill\n"
                "")
    if act == "a":
        p1.hit(p2)
        if p2.life < 0:
            p2.life = 0

    elif act == "s":
        c = 1
        print("What skill do you want to use?")
        for i in p1.skills:
            print(str(c) + "->", i.name)
            c += 1
        s = input()
        p1.spellcast(s, p1, p2)

    if p2.life < 0:
        p2.life = 0
    time.sleep(0.2)
    print(p2.name + ":", str(p2.life) + "/" + str(p2.mxlife), "HP")
    print("")


class Hero:

    def __init__(self, n):
        self.name = n
        self.mxlife = 100
        self.mxatk = 30
        self.mxdfn = 5
        self.mxsp = 4
        self.mxmana = 20
        self.mxint = 30

        self.life = 100
        self.atk = 30
        self.dfn = 5
        self.sp = 4
        self.mana = 20
        self.int = 30

        self.maxp = 25
        self.xp = 0
        self.lvl = 1

        self.items = []
        self.eq = Equipment()
        self.skills = []
        self.role = ""

    def rch(self, r):
        if r == "Knight":
            self.mxlife += 50
            self.mxatk += 15
            self.mxdfn += 10
            self.mxmana += 5
            self.mxint += 5
            self.role = r
        else:
            self.mxlife += 25
            self.mxatk += 7
            self.mxdfn += 6
            self.mxmana += 10
            self.mxint += 20
            self.role = r
        self.life = self.mxlife
        self.atk = self.mxatk
        self.dfn = self.mxdfn
        self.sp = self.mxsp
        self.mana = self.mxmana
        self.int = self.mxint

    def tkitem(self, item):
        for i in self.items:
            if i.name == item.name:
                i.amm += item.amm
            else:
                self.items.append(item)

    def lvlup(self):
        if self.role == "knight":
            self.mxlife += 50
            self.mxatk += 15
            self.mxdfn += 10
            self.mxmana += 5
            self.mxint += 5
        else:
            self.mxlife += 25
            self.mxatk += 7
            self.mxdfn += 6
            self.mxmana += 10
            self.mxint += 20
        self.life = self.mxlife
        self.atk = self.mxatk
        self.dfn = self.mxdfn
        self.sp = self.mxsp
        self.mana = self.mxmana
        self.int = self.mxint
        self.lvl += 1
        self.xp = 0
        self.maxp += 10

    def learnskill(self, s):
        self.skills.append(s)

    def hit(self, mons):
        dmg = self.atk - mons.dfn
        mons.life -= dmg
        time.sleep(0.2)
        print("You atacked", mons.name, "you hurted him by", str(dmg) + "!")

    def spellcast(self, s, p1, p2):
        time.sleep(0.2)

        if self.mana - self.skills[(int(s) - 1)].mcost < 0:
            time.sleep(0.2)
            print("you don´t have enough mana.")
            fightmon(self, p2)
        elif s == "x":
            fightmon(self, p2)
        else:
            print("What is your target?:")
            print("1-> " + p1.name)
            print("2-> " + p2.name)
            tg = input("")
            if tg == "1":
                if self.skills[(int(s) - 1)].type == "dmg":
                    print("target invalid")
                    time.sleep(0.2)
                    print("")
                    p1.fightmon(p1, p2)
                else:
                    self.skills[(int(s) - 1)].cast(p1, p1)
            else:
                if self.skills[(int(s) - 1)].type == "heal":
                    print("target invalid")
                    time.sleep(0.2)
                    print("")
                    p1.fightmon(p1, p2)
                else:
                    self.skills[(int(s) - 1)].cast(p1, p2)

    def __str__(self):
        print(self.name)
        time.sleep(0.2)
        print(self.role, ", level:", str(self.lvl))
        time.sleep(0.2)
        print("life:", str(self.life) + "/" + str(self.mxlife), "HP")
        time.sleep(0.2)
        print("attack:", str(self.atk))
        time.sleep(0.2)
        print("defense:", str(self.dfn))
        time.sleep(0.2)
        print("intelligence:", str(self.int))
        time.sleep(0.2)
        print("mana:", str(self.mana) + "/" + str(self.mxmana))
        time.sleep(0.2)
        print("exp: " + str(self.xp) + "/" + str(self.maxp))
        return ""


class Item:

    def __init__(self, n, t, am, ef, dsc):
        self.name = n
        self.type = t
        self.amm = am
        self.effect = ef
        self.descr = dsc


# Items:
potion = Item("Potion", "cons", 1, 20, "heals 20 HP")


class Equipment:
    def __init__(self, ):
        self.wp = ""
        self.arm = ""


class Goblin:
    def __init__(self):
        self.name = "Goblin"
        self.mxlife = 100
        self.life = 100
        self.atk = 30
        self.dfn = 7
        self.spd = 7
        self.xp = 5

    def hit(self, hero):
        dmg = self.atk - hero.dfn
        hero.life -= dmg
        time.sleep(0.2)
        print("Goblin has attacked you! he has dealt you", str(dmg), "damage!")

    def __str__(self):
        print(self.name + ":", str(self.life) + "/" + str(self.mxlife), "HP")
        return ""


class Skill:
    def __init__(self, n, sd, mc, ty):
        self.name = n
        self.dmg = sd
        self.mcost = mc
        self.type = ty

    def cast(self, p1, p2):
        if self.type == "dmg":
            dmg = (self.dmg * p1.int) - p2.dfn
            p2.life -= dmg
            p1.mana -= self.mcost
            if p1.mana <= 0:
                p1.mana = 0
            time.sleep(0.2)
            print(self.name, "has dealt", dmg, "to", p2.name + "!")
            time.sleep(0.2)
        if self.type == "heal":
            if p1.life + self.dmg > p1.mxlife:
                p1.life = p1.mxlife
            else:
                p1.life += self.dmg
            p1.mana -= self.mcost
            if p1.mana <= 0:
                p1.mana = 0
            time.sleep(0.2)
            print(self.name, "has healed", p1.name, self.dmg, "HP!")
            time.sleep(0.2)
            print(p1.name + ":", str(p1.life) + "/", "HP")


# Skills:
fb = Skill("Fireball", 1, 7, "dmg")
cure = Skill("Cure", 20, 3, "heal")


def fight(p1, p2, k):
    turn = 1
    con = True
    while con:
        if p2.spd > p1.sp:
            if p1.life == 0 or p2.life == 0:
                if p1.life <= 0:
                    time.sleep(0.2)
                    print("You have been killed")
                    con = False
                    k = False
                else:
                    time.sleep(0.2)
                    print("You killed the", p2.name + "!")
                    time.sleep(0.2)
                    print("you are back in the forest")
                    time.sleep(0.2)
                    print("")
                    p1.xp += p2.xp
                    con = False
            elif turn % 2 == 1:
                p2.hit(p1)
                turn += 1
                if p1.life < 0:
                    p1.life = 0
                time.sleep(0.2)
                print(p1.name + ":", str(p1.life) + "/" + str(p1.mxlife), "HP")
                print("")
            else:
                fightmon(p1, p2)
                turn += 1

        else:
            if p1.life == 0 or p2.life == 0:
                if p1.life <= 0:
                    time.sleep(0.2)
                    print("You have been killed")
                    con = False
                    k = False
                else:
                    time.sleep(0.2)
                    print("You killed the", p2.name + "!")
                    time.sleep(0.2)
                    print("you are back in the forest")
                    time.sleep(0.2)
                    print("")
                    p1.xp += p2.xp
                    con = False
            elif turn % 2 == 0:
                p2.hit(p1)
                turn += 1
                if p1.life < 0:
                    p1.life = 0
                time.sleep(0.2)
                print(p1.name + ":", str(p1.life) + "/" + str(p1.mxlife), "HP")
                print("")
            else:
                fightmon(p1, p2)
                turn += 1
        if p1.xp >= p1.maxp:
            nwxp = p1.xp - p1.maxp
            p1.lvlup()
            p1.xp += nwxp
            print("Congrats!, you have reached level " + p1.lvl)
            time.sleep(0.2)
            print(p1)


def move(k):
    action = input("c-> Show state\n"
                   "")
    if action == "c":
        print(hr)

    elif action == "w":
        luck = random.randint(0, 100)
        if 0 <= luck <= 85:
            time.sleep(0.2)
            print("You are walking through the forest")
        else:
            gob = Goblin()
            time.sleep(0.2)
            print("Oh no!, there is a goblin in your way!")
            fight(hr, gob, k)


print("")
time.sleep(0.2)
print("You woke up in a forest, surrounded by trees")
time.sleep(0.2)
print("there is a path in front of you")
time.sleep(0.2)
print("you don´t remember anything...")
time.sleep(0.2)
print("but then, something came flying tou you")
time.sleep(0.2)
print("???: You are lost, right? do you remember your name?")
time.sleep(0.2)
print("")

my_name = input("-> write your name: \n")
hr = Hero(my_name)

hr.learnskill(cure)
time.sleep(0.2)
print("")
time.sleep(0.2)
print(hr.name + ": y-yes... i do...")
time.sleep(0.2)
print("???: good, my name is Frann, and I´m a fairy")
time.sleep(0.2)
print("Frann: so, how do you feel?, strong or inteligent?")
time.sleep(0.2)
print("")

d = input("-> press 's' for strong, press 'i' for inteligent: \n"
          "")

if d == "s":
    dc = "Knight"
    hr.rch(dc)
else:
    dc = "Mage"
    hr.rch(dc)

print("")
time.sleep(0.2)
print("Frann: It looks like you are a", hr.role + "!")
time.sleep(0.2)
print("look, these are your stats")
time.sleep(0.2)
print("")
time.sleep(0.2)
print(hr)
if hr.role == "Mage":
    print("Frann: it looks like you have something in your pocket")
    time.sleep(0.2)
    print("you search in your pocket and founded a book")
    time.sleep(0.2)
    print("")
    time.sleep(0.2)
    print("you have learned fireball!")
    time.sleep(0.2)
    print("")
    time.sleep(0.2)
    print("Frann: Wow, a new spell!, congratulations!")
    time.sleep(0.2)

hr.learnskill(fb)

print("")
time.sleep(0.2)
print("Frann: I think you should go to the nearest town, take this, use it wisely")
time.sleep(0.2)
print("")
time.sleep(0.2)
print("-Frann gave you a potion!-")
time.sleep(0.2)
print("")
time.sleep(0.2)
print("Frann: Farewell!, i'll see you around!")
time.sleep(0.2)
print("Frann flies away")
time.sleep(0.2)
print("")

hr.tkitem(potion)

print("move with W A S D")

keep = True
while keep:
    move(keep)
