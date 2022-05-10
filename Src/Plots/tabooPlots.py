import tsplib95
import numpy as np
from matplotlib import pyplot as plt

from Src.Algorythms.NN_Algorythm import NNA
from Src.tabuSearch import TabooSearch, two_opt, tabuInvert
#plots for taboo search

def listLengthPlot():
    xpoints = []
    ypoints = []
    for i in range(1,11,2):
        ypoints.append(taboo.basicSearch(neighbourFunction = tabuInvert, starting = startSolution, endCost=endCost, problem = problem, k=i, maxTime=10)[1])
        xpoints.append(i)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Taboo list len (times dimension)')
    plt.ylabel('Tour length')
    plt.title('Result vs taboo list length')
    plt.show()

def timeVsResult(maxTimeIteration):
    xpoints = []
    ypoints = []

    ypoints.append(taboo.basicSearch(neighbourFunction = tabuInvert, starting = startSolution,endCost=endCost, problem = problem, k=3, maxTime=maxTimeIteration)[1])
    temp = taboo.basicSearch(neighbourFunction = tabuInvert, starting = startSolution,endCost=endCost, problem = problem, k=3, maxTime=maxTimeIteration)[0]
    sum = maxTimeIteration
    xpoints.append(sum)

    for i in range(10):
        ypoints.append(taboo.basicSearch(neighbourFunction=tabuInvert,starting=temp, endCost=ypoints[-1], problem=problem, k=3, maxTime=maxTimeIteration)[1])
        temp = taboo.basicSearch(neighbourFunction = tabuInvert, starting = temp, endCost=ypoints[-2], problem = problem, k=3, maxTime=maxTimeIteration)[0]
        sum += maxTimeIteration
        xpoints.append(sum)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Time')
    plt.ylabel('Tour length')
    plt.title('Results in time')
    plt.show()

def averageListLength():
    sucess = 0
    sucessIterations = 0
    defeat = 0
    defeatIteration = 0
    iRange = 10
    jRange = 30
    #totalIterations = jRange*iRange
    for i in range(1, iRange):
        for j in range(1, jRange):
            startSolution, endCost = two_opt(problem, NNAPath)
            #startSolution = list(problem.get_nodes())
            #np.random.shuffle(startSolution)
            #endCost = problem.trace_tours([startSolution])[0]
            temp = taboo.basicSearch(neighbourFunction=tabuInvert, starting=startSolution, endCost=endCost, problem=problem, k=i, maxTime=10)[1]
            if temp<endCost:
                sucess += i
                sucessIterations +=1
            elif endCost == problem.trace_tours(solution.tours)[0]:
                continue
            elif temp>=endCost:
                defeat += i
                defeatIteration +=1

    avarageLength = sucess/sucessIterations
    print("Średnia długość listy ze zmianą wyniku:")
    print(avarageLength)

    avarageLength = defeat/defeatIteration
    print("Średnia długość lisy bez zmiany wyniku:")
    print(avarageLength)

if __name__ == '__main__':
    taboo = TabooSearch()
    problem = tsplib95.load('/Users/grelewski/PycharmProjects/Metaheurystyka1/Data/bays29/bays29.tsp')
    solution = tsplib95.load('/Users/grelewski/PycharmProjects/Metaheurystyka1/Data/bays29/bays29.opt.tour')
    NNAPath, NNACost = NNA(problem, 0)
    startSolution, endCost = two_opt(problem, NNAPath)
    #listLengthPlot()
    #timeVsResult(maxTimeIteration=15)
    averageListLength()