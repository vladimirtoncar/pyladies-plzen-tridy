# Priklad prace se tridami a objekty

class Obdelnik:
    def __init__(self, a, b):
        self.strana_a = a
        self.strana_b = b

    def obsah(self):
        return self.strana_a * self.strana_b

    def obvod(self):
        return 2 * (self.strana_a + self.strana_b)

    def mensi_nez(self, other):
        return self.obsah() < other.obsah()


class Ctverec(Obdelnik):
    def __init__(self, a):
        super().__init__(a, a)


ctv1 = Ctverec(5)
print("Ctverec 1 ma obvod {} a obsah {}.".format(ctv1.obvod(),
                                            ctv1.obsah() )
    )

ctv2 = Ctverec(3)
print("Ctverec 2 ma obvod {} a obsah {}.".format(ctv2.obvod(),
                                            ctv2.obsah() )
    )

if ctv1.mensi_nez(ctv2):
    print("Ctverec 1 je mensi")
else:
    print("Ctverec 2 je mensi")



