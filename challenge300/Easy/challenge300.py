import math
import pyaudio
import numpy as np

SAMPLE_RATE = 44100

#note frequencies starting from middle c
scale_freqs = [261.626,293.665,329.628,349.228,391.995,440.0,493.883]

solfege ={"DO": scale_freqs[0],
        "RE": scale_freqs[1],
        "MI": scale_freqs[2],
        "FA": scale_freqs[3],
        "SO": scale_freqs[4],
        "LA": scale_freqs[5],
        "SI": scale_freqs[6]} 

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)    

def play_sine(frequency, length):
    samples = (np.sin(2*np.pi*np.arange(SAMPLE_RATE*length)*frequency/SAMPLE_RATE)).astype(np.float32)
    stream.write(samples)

def play_chord(frequencies, length):

    samples = (np.sin(2*np.pi*np.arange(SAMPLE_RATE*length)*frequencies[0]/SAMPLE_RATE)).astype(np.float32)
    
    for frequency in frequencies[0:]:
        samples += (np.sin(2*np.pi*np.arange(SAMPLE_RATE*length)*frequency/SAMPLE_RATE)).astype(np.float32)
    stream.write(samples)

def play_note(scale_note,length):
    play_sine(solfege[scale_note],length)

def main():

    play_note("MI",2)
    play_note("MI",2)
    play_note("FA",2)
    play_note("SO",2)
    play_note("SO",2)
    play_note("FA",2)
    play_note("MI",2)
    play_note("RE",2)
    play_note("DO",2)
    play_note("DO",2)
    play_note("RE",2)
    play_note("MI",2)
    play_note("MI",4)

    stream.close()
    p.terminate()

if __name__ == '__main__':
    main()
