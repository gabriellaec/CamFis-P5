import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
import suaBibSignal
import peakutils
import itertools
import pickle
import math


signal = suaBibSignal.signalMeu()

fs = 44100  # pontos por segundo (frequência de amostragem)
sd.default.samplerate = fs
sd.default.channels = 1
A   = 1.5   # Amplitude
F   = 1     # Hz
T   = 1     # Tempo em que o seno será gerado
t   = np.linspace(-T/2,T/2,T*fs)


frequencias = {  # T1abela --> número : (coluna,linha)
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

            
def compare_picos(lista_picos):
    
    for v in frequencias.keys():
            l=0
            c=0
            t=frequencias[v]
            coluna = t[0]
            linha=t[1]
            for x in lista_picos:
                if abs(coluna-x)<=10:
                    c = coluna
                if abs(linha-x)<=10:
                    l=linha
            if c!=0 and l!=0:
                print("coluna: "+ str(c))
                print("linha: "+str(l))
                return v
                
        
                
                

def main():

    myrecording = sd.rec(int(T * fs))
    sd.wait()

    print(myrecording.shape)
    
    yAudio=myrecording[:,0]

    samplesAudio = len(yAudio)

    plt.plot(t,yAudio)
    plt.grid()
    plt.xlim([0.01,0.02])
    plt.title('Sinal no tempo')

    X, Y = signal.calcFFT(yAudio,fs)

    plt.figure("Fourier Audio")
    plt.plot(X, np.abs(Y))
    plt.grid()
    plt.xlim([0,2000])
    plt.title('Fourier Frequencia')
    
    p=0.9
    n=0
    picos=[]
    while n<3:
        index = peakutils.indexes(np.abs(Y), thres=p, min_dist=100)
        n=0
        for freq in X[index]:
            n+=1
            if freq not in picos:
                picos.append(freq)
            p-=.06
    print("freq de pico sao {}" .format(str([x for x in picos]).strip('[]')))
            
    print("Número escolhido: "+ str(compare_picos(picos)))
            
            
            
    
        



    

if __name__ == "__main__":
    main()

 