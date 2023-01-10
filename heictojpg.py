import os, subprocess

directory = '.'

for filename in os.listdir(directory):
    if filename.lower().endswith(".heic"): 
        print('Converting %s...' % os.path.join(directory, filename))
        command = "magick '%s' '%s'" % (filename, filename[0:-5] + '.jpg')
        subprocess.run(command, shell=True)
        continue
