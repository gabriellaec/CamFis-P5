import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
import suaBibSignal
import time


signal = suaBibSignal.signalMeu()

fs = 44100  # pontos por segundo (frequência de amostragem)
A   = 1.5   # Amplitude
F   = 1     # Hz
T   = 2     # Tempo em que o seno será gerado
t   = np.linspace(-T/2,T/2,T*fs)


frequencias = {  # Tabela --> número : (coluna,linha)
    1 : (1209,697),
    2 : (1336, 697),
    3 : (1447, 697),
    4 : (1209,770),
    5 : (1336, 770),
    6 : (1447, 770),
    7 : (1209,852),
    8 : (1336, 852),
    9 : (1447, 852),
    0 : (1336, 941)
}

def main():

    print("entrou na apicação")
    numero = int(input("Digite um número de 0 a 9: "))
    while numero not in frequencias.keys():
        numero = int(input("Digite um número de 0 a 9: "))

    print(f"Número escolhido: {numero}")
    f1 = frequencias[numero][0]
    f2 = frequencias[numero][1]

    print(f"Identificou as frequências: {f1} e {f2}")

    x1, s1 = signal.generateSin(f1, A, T, fs)
    y2, s2 = signal.generateSin(f2, A, T, fs)

    print("gerou os sinais")

    #som = s1 + s2
    som = []
    for i in range(len(s1)):
        som.append(s1[i] + s2[i])

    print("vai tocar o som!")

    time.sleep(3)

    sd.play(som, fs)
    sd.wait()

    print("gerando os gráficos")
    #plt.stem(y2,som)
    #plt.stem(t, som)
    #plt.xlim(-15, 15)
    
    X, Y = signal.calcFFT(som,fs)

    plt.figure("Fourier Audio")
    plt.plot(X, np.abs(Y))
    plt.xlim([0,2000])

    plt.grid()
    plt.title('Fourier Frequencia')
    plt.show()

    yAudio = som
    plt.plot(t,yAudio)
    plt.grid()
    plt.xlim([0.01,0.02])
    plt.title('Audio no tempo')

    plt.show()

    

if __name__ == "__main__":
    main()

