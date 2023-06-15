# coding: utf-8

import librosa
from librosa.core.spectrum import amplitude_to_db
import numpy as np
from scipy.signal import lfilter, firwin, freqz
import soundfile as sf
import importlib,sys

importlib.reload(sys)

def enhenc(filename): 
    noisy_wav_file = filename
    noisy,fs = librosa.load(noisy_wav_file,sr=None)

    # 计算nosiy信号的频谱
    S_noisy = librosa.stft(noisy,n_fft=256, hop_length=128, win_length=256)
    D,T = np.shape(S_noisy)
    Mag_noisy= np.abs(S_noisy)
    Phase_nosiy= np.angle(S_noisy)
    Power_nosiy = Mag_noisy**2

    # 估计噪声信号的能量 这里假设noisy信号的前30帧为噪声
    Mag_nosie = np.mean(np.abs(S_noisy[:,:31]),axis=1,keepdims=True)
    Power_nosie = Mag_nosie**2
    Power_nosie = np.tile(Power_nosie,[1,T])
    
    # 引入平滑
    Mag_noisy_new = np.copy(Mag_noisy)
    k=1
    for t in range(k,T-k):
        Mag_noisy_new[:,t] = np.mean(Mag_noisy[:,t-k:t+k+1],axis=1)  
    Power_nosiy = Mag_noisy_new**2
    
    # 超减法去噪
    alpha = 4
    gamma = 1
    Power_enhenc = np.power(Power_nosiy,gamma) - alpha*np.power(Power_nosie,gamma)
    Power_enhenc = np.power(Power_enhenc,1/gamma)
    
    # 对过小值用beta* Power_nosie替代
    beta = 0.0001
    mask = (Power_enhenc>=beta*Power_nosie)-0
    Power_enhenc = mask*Power_enhenc + beta*(1-mask)*Power_nosie
    Mag_enhenc = np.sqrt(Power_enhenc)    
    Mag_enhenc_new  = np.copy(Mag_enhenc)

    # 计算最大噪声残差
    maxnr = np.max(np.abs(S_noisy[:,:31])-Mag_nosie,axis =1)
    k = 1
    for t in range(k,T-k):
        index = np.where(Mag_enhenc[:,t]<maxnr)[0]
        temp = np.min(Mag_enhenc[:,t-k:t+k+1],axis=1)
        Mag_enhenc_new[index,t] = temp[index]
            
    # 对信号进行恢复
    S_enhec = Mag_enhenc_new*np.exp(1j*Phase_nosiy)
    enhenc = librosa.istft(S_enhec, hop_length=128, win_length=256)
    sf.write("/home/pi/enhenc.wav",enhenc,fs)
    
if __name__ == "__main__":
    filename = '/home/pi/voice.wav'
    enhenc(filename)
   
   
