from Src.Algorythms.NN_Algorythm import NNA
from Src.Algorythms.krandom import krandom
from Src.Algorythms.two_opt import two_opt

# test, ze jesli odpale two opta na zachlannym np. do two_opt dam krandom to two_opt rozplacze sciezki
# wniosek: sciezka bedzie taka sama/albo szybsza

def two_opt_GRD(problem):
    krandomPath,krandomCost = krandom(problem,100)
    NNA_Path,NNA_Cost = NNA(problem,0)

    # krandom jest rozplatany przez two_opt
    print(krandomCost)
    print(two_opt(problem, krandomPath)[1])

    # analogicznie
    print(NNA_Cost)
    print(two_opt(problem, NNA_Path)[1])
