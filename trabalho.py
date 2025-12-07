import random

def generator(total, vetor_x, vetor_y):

    for i in range(total):
        
        # populando os vetores com "total" pontos dentro do quadrado de lado 2
        vetor_x.append(random.uniform(-1, 1))
        vetor_y.append(random.uniform(-1, 1))

    
def inside_circle(vetor_x, vetor_y):

    inside = 0
    
    # contando os pontos dentro do circulo
    for i in range(len(vetor_x)):
        if vetor_x[i] ** 2 + vetor_y[i] ** 2 <= 1:
            inside += 1
    return inside

def countQuadrants(vetor_x, vetor_y, quadrant):

    inside = 0

    for x, y in zip(vetor_x, vetor_y): # isso aqui é épico, é literalmente matemática

        # setor lógico para detectar o quadrante

        if quadrant == 1 and not (x >= 0 and y >= 0):
            continue
        if quadrant == 2 and not (x <= 0 and y >= 0):
            continue
        if quadrant == 3 and not (x <= 0 and y <= 0):
            continue
        if quadrant == 4 and not (x >= 0 and y <= 0):
            continue

        if x ** 2 + y ** 2 <= 1:
            inside += 1

    return inside

def pointsQuadrant(vetor_x, vetor_y, quadrant):

    count = 0

    # esse loop usa a mesma lógica da contagem de quadrantes, porém, é uma função específica que conta quantos pontos tem em cada quadrante
    # basicamente itera um valor sempre q cair um ponto no quadrante
    for x, y in zip(vetor_x, vetor_y):
        if quadrant == 1 and (x >= 0 and y >= 0):
            count += 1
        elif quadrant == 2 and (x <= 0 and y >= 0):
            count += 1
        elif quadrant == 3 and (x <= 0 and y <= 0):
            count += 1
        elif quadrant == 4 and (x >= 0 and y <= 0):
            count += 1
            
    return count

def pi_estimative(total, inside):
    
    # estima o valor de pi com a fórmula
    return 4 * inside/float(total)

def adjust(totalPi):
    
    # ajusta pra 6 casas decimais
    return round (totalPi, 6)


def main():
    print("Bem-vindo a calculadora estimativa de pi!")
    total = int(input("Insira o número de pontos a serem gerados para a estimativa: "))
    print(" ")
    
    while total < 1:
        print("Insira um valor válido! Tente novamente: ")
        total = int(input("Insira um número positivo maior que 1: "))
        print(" ")

    
    vetor_x = []
    vetor_y = []

    # vai jogar pra função que gera os pontos aleatórios
    generator(total, vetor_x, vetor_y)

    # vai verificar quantos caíram no círculo todo usando a funçao inside_circle
    totalCircle = inside_circle(vetor_x, vetor_y)

    # vai estimar o valor de pi usando a funçao pi_estimative e o circulo todo
    totalPi = pi_estimative(total, totalCircle)

    # funçao de ajuste
    totalPi = adjust(totalPi)

    for quadrant in range(1, 5):

        # total de pontos do quadrante
        totalQuadrant = pointsQuadrant(vetor_x, vetor_y, quadrant)

        # total de pontos dentro do círculo do quadrante
        insideQuadrant = countQuadrants(vetor_x, vetor_y, quadrant)

        # calcula o pi do quadrante
        quadrantPi = pi_estimative(totalQuadrant, insideQuadrant)

        # ajusta
        quadrantPi = adjust(quadrantPi)

        print("Quadrante: %d " %quadrant)
        print("Número de pontos dentro do quadrante: %d" %totalQuadrant)
        print("Número de pontos dentro do círculo do quadrante: %d" %insideQuadrant)
        print("Estimativa de pi para o quadrante: %f" %quadrantPi)
        print(" ")


    print("Número total de pontos dentro do círculo: %d" %totalCircle)
    print("Estimativa total de pi: %f" %totalPi)

if __name__ == "__main__":
    main() 

# link pro github:
# https://github.com/MasterT0ad/Monte-carlo-para-pi