from dataclasses import dataclass

@dataclass
class Interazione:
    id_gene1: str
    id_gene2: str
    peso : int

    def __str__(self):
        return self.id_gene1, self.id_gene2, self.peso