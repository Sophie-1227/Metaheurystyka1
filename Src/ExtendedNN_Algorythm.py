#mTak samo jak NNA tylko dodatkowa pętla pozwalająca rozpocząć od każdego z punktów, ale idk czy to legalne
"""
Opisowo:
1. Bierzemy po kolei każdy z punktów na mapie i dodajemy go na początek listy pi (listy kolejnych odwiedzanych punktów).
2. Dla tego punktu szukamy w matrixie najmniejszej odleglości do dowolnego innego punktu (NALEŻY SPRAWDZIĆ CZY WYBRANY PUNKT NIE JEST POCZĄTKOWYM LUB SAMYM SOBĄ)
3. Dodajemy długość tej trasy do sumarycznej odległości, a numer punkty do listy pi
4. I Powtarzamy punkty 2 i 3
5. Wykreślamy poprzedni punkt z dostępnych do losowania
6. Kiedy zostaną nam ostatnie 2 punkty To ta trasa musi być do punktu początkowego, dodajemy odległość, ale punkty do pi juz nie musimy
7. Wyświetlamy i się cieszymy jak działa
"""

"""
Pseudokod:
s = random od 1 do 29 # punkt startowy
list.push(s)
odleglosc = 0
for i<-0 to 29 do
    best = 8364273 #duża odległość, żeby nie było problemu
    for j<-0 to 29 do
        temp = matrix[i][j]
        if temp<best && j nie należy do list
            best = temp
            point = j #punkt, uznany za najlepszy
        list.push(point)
        odleglosc += best
    odleglosc += matrix[j][s]
print(odleglosc)
print(list)     
"""