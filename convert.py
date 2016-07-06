import os
import subprocess 
import shutil

def ffmpeg_conv(input, output, codec):
	print "hola"
	#ffmpeg_path='C:/ffmpeg/ffmpeg.exe'
	print ("Enter the path for ffmpeg")
	input(path)
	cmd = [path]
	
	cmd.append('-i')
	cmd.append('C:/ffmpeg/'+input+'.wav')
	#cmd.append('.wav')
	
	cmd.append('-codec:a')
	cmd.append(codec)
	
	if codec == 'aac':
		#cmd.append('aac')
		cmd.append(output+'.mp4')
		#cmd.append('.m4a')
	elif codec == 'mp3':
		cmd.append('libmp3lame -qscale:a 2')
		cmd.append(output)
		cmd.append('.mp3')
	else:
		print "not available"
	
	return cmd
cadena = ffmpeg_conv("input", "output", "aac")
cadena2 =' '.join(cadena)
subprocess.call(cadena2)
subprocess.call('C:/Users/aanguiax/Documents/dev/SoundRecorder.exe')





#c:\ffmpeg\ffmpeg.exe -i c:\ffmpeg\input.wav -codec:a aac output.m4a
