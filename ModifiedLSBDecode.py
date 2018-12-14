# Use wave package (native to Python) for reading the received audio file
import wave
song = wave.open("vaikunth.wav", mode='rb')
# Convert audio to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))
DecodeMsg=''
song.setpos(0)
length=1080
sf = song.getnframes()  // length
for i in range(length):
    temp=bytearray(list(song.readframes(sf)))
    tempextracted=[temp[i] & 1 for i in range(len(temp))]    
    tempstring = "".join(chr(int("".join(map(str,tempextracted[i:i+8])),2)) for i in range(0,len(tempextracted),8))    
    decoded = tempstring.split("&")[0]
    DecodeMsg=DecodeMsg+decoded
print "Secret Message :",DecodeMsg
    


song.close()