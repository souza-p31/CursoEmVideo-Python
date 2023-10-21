# DESAFIO 80
class NumerosOrdenadosSemSort:
    def Adicionar_Ordenar():
        num = []
        for numero in range(0,5):
            add_num = int(input('Digite um valor: '))
            if numero == 0 or add_num > num[-1]:
                num.append(add_num)
            else:
                pos = 0
                while pos < len(num):
                    if add_num <= num[pos]:
                        num.insert(pos,add_num)
                        break
                    pos += 1
        print(f'Lista -> {num}')
    Adicionar_Ordenar()



