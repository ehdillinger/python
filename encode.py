#### LIBRARIES ####

### This code assumes you are running under windows environment ###

import subprocess
import glob, os
import shutil
import random
import argparse

#### CLASSES ####

class audioEncode:
	ffmpegpath = 'c:/ffmpeg/ffmpeg.exe'
	input = '-i c:/ffmpeg/input.wav'
	command = [ffmpegpath]
	codec = ['aac', 'libmp3lame', 'hi']

	def __init__(self, output):
		self.output = output

	def setCodec(self, codec):
		if codec == '1':
			self.codec = '-codec:a libmp3lame -qscale:a 1'
		elif codec == '2':
			self.codec = '-codec:a libmp3lame -qscale:a 2'
		elif codec == '3':
			self.codec = '-codec:a libmp3lame -qscale:a 3'
		elif codec == '4':
			self.codec = '-codec:a libmp3lame -qscale:a 4'
		elif codec == '5':
			self.codec = '-codec:a libmp3lame -qscale:a 5'
		elif codec == '6':
			self.codec = '-codec:a libmp3lame -qscale:a 6'
		elif codec == '7':
			self.codec = '-codec:a libmp3lame -qscale:a 7'
		elif codec == '8':
			self.codec = '-codec:a libmp3lame -qscale:a 8'
		elif codec == '9':
			self.codec = '-codec:a libmp3lame -qscale:a 9'
		elif codec == '0':
			self.codec = '-codec:a libmp3lame -qscale:a 0'
		elif codec == 'max':
			self.codec = '-codec:a libmp3lame -b:a 320k'

	def getCodec(self):
		return self.code

	def setOutput(self, output):
		self.output=output

	def getOutput(self):
		return self.Output

#help
parser=argparse.ArgumentParser(
    description='''Convert all *.wav files from a given directory to mp3 lame /n
-b 320	320	320 CBR (non VBR) example	-b:a 320k (NB this is 32KB/s, or its max)/n
-V 0	245	220-260	-q:a 0 (NB this is VBR from 22 to 26 KB/s)/n
-V 1	225	190-250	-q:a 1/n
-V 2	190	170-210	-q:a 2/n
-V 3	175	150-195	-q:a 3/n
-V 4	165	140-185	-q:a 4/n
-V 5	130	120-150	-q:a 5/n
-V 6	115	100-130	-q:a 6/n
-V 7	100	80-120	-q:a 7/n
-V 8	85	70-105	-q:a 8/n
-V 9	65	45-85	-q:a 9/n''',
    epilog="""***Thank you***""")
#parser.add_argument('--foo', type=int, default=42, help='FOO!')
args=parser.parse_args()

#main

print ("Enter encode 0-9 max")
codec = input()
print ("Enter path for lossless files")
path = input()
#test
test = audioEncode('encode')
#test.setCodec('-codec:a aac')
test.setCodec(codec)
test.setOutput('test')
hi = test.getCodec()

#iterate over directories

os.chdir(path)
for file in glob.glob("*.wav"):
	print (file)
	mainCommand = test.ffmpegpath+' '+ '-i c:/ffmpeg/'+file +' '+ test.getCodec() + ''+' '+"output.mp3"
#print test.getCodec()
print (test.ffmpegpath+' '+ test.input +' '+ test.getCodec() + '' )

print (mainCommand)
while True:
	subprocess.call(mainCommand)



#ffmpeg.exe -i input.wav -codec:a aac output.m4a

#c:/WinExec/ffmpeg.exe -i c:/WinExec/input.wav -codec:a aac output.m4a



