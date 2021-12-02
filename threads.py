import time
from threading import Thread


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print(f'Piloto: {piloto} Km {trajeto}\n')
        time.sleep(1)
        trajeto += velocidade


if __name__ == '__main__':
    t_carro1 = Thread(target=carro, args=[1, 'Neto'])
    t_carro2 = Thread(target=carro, args=[2, 'X'])
    t_carro1.start()
    t_carro2.start()
