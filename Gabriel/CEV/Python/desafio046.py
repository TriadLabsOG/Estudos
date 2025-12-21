from time import sleep
from playsound import playsound
from emoji import emojize

for segundos in range (10, 0, -1):
    print(emojize(f'Faltam {segundos} segundos pra 2025! :hourglass_not_done:'))
    sleep(0.1)
print(emojize('FELIZ ANO NOVO!!!! :confetti_ball:'))
playsound(r"CEV\Desafios\foguetes.wav")