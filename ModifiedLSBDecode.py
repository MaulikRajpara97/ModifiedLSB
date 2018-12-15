
import wave
song = wave.open("output.wav", mode='rb')

frame_bytes = bytearray(list(song.readframes(song.getnframes())))
DecodeMsg=''
song.setpos(0)
# enter key value in length that you got in encoding 
length=12
sf = song.getnframes()  // length
for i in range(length):
    temp=bytearray(list(song.readframes(sf)))
    tempextracted=[temp[i] & 1 for i in range(len(temp))]    
    tempstring = "".join(chr(int("".join(map(str,tempextracted[i:i+8])),2)) for i in range(0,len(tempextracted),8))    
    decodechar = tempstring.split("&")[0]
    DecodeMsg=DecodeMsg+decodechar
print "Secret Message :",DecodeMsg
    


song.close()
