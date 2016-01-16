class RecoilDamage(RuntimeError):
    """
    Classe d'exception XXX
    """
    def __init__(self, combattant, damage):
        """
        Classe d'exception qui est soulevée lorsqu'un combattant s'attaque lui-même
        """
        self.combattant = combattant
        self.damage = damage
        