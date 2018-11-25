# Priklad prace se tridami a objekty

class Obdelnik:
    def __init__(self, a, b):
        self.strana_a = a
        self.strana_b = b

    def obsah(self):
        return self.strana_a * self.strana_b

    def obvod(self):
        return 2 * (self.strana_a + self.strana_b)


obd = Obdelnik(2, 3)
print("Obdelnik ma obvod {} a obsah {}.".format(obd.obvod(),
                                            obd.obsah() )
    )

