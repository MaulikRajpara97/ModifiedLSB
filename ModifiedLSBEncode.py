
import wave
import os

song = wave.open("input.wav", mode='rb')

frame_bytes = bytearray(list(song.readframes(song.getnframes())))
song.setpos(0)
finaltemp=''
hidden_file = open('data.txt', 'r')

file_size = os.path.getsize('data.txt')

string = hidden_file.read(-1)
print "Key=",len(string)


sf = song.getnframes()  // len(string)
for i in range(len(string)):
    temp=bytearray(list(song.readframes(sf)))   
    tempstring = string[i] + int((len(temp)-(len(string[i])*8*8))/8) *'&'    
    tempbits = list(map(int, ''.join([bin(ord(j)).lstrip('0b').rjust(8,'0') for j in tempstring])))
    for k, tempbit in enumerate(tempbits):
        temp[k] = (temp[k] & 254) | tempbit
    finaltemp=finaltemp+bytes(temp)
    
nd = wave.open('output.wav', 'wb')
nd.setparams(song.getparams())
nd.writeframes(finaltemp)
print "Stego Audio Genrated"
nd.close()

song.close()