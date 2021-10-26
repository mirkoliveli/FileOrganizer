import os
import sys
import shutil

#HOW TO LAUNCH PROGRAM
    #sys.argv[0] = programname.py
    #sys.argv[1] = directory_to_organize
    #sys.argv[2] = file_extention

#EXAMPLE:
    #python3 organizer.py /home/username/download/ fileextention


def __SelectiveCopy__(folder, extension):
    avoid = '/' + extension
    folder = os.path.abspath(sys.argv[1])
    dest = os.path.join(folder, extension)
    if not os.path.exists(dest):
        os.mkdir(dest, mode=0o777)
    for foldername, subfolder, filename in os.walk(folder):
        if foldername.endswith(avoid):
            print("Not looking in %s" % foldername)
        else:
            print('Looking into %s' % foldername)
            for file in filename:
                if file.endswith('.' + extension):
                    print('\nMoving %s to destination folder...' % file)
                    print("FROM: " + os.path.join(folder, foldername))
                    print("TO: " + dest + '\n')
                    shutil.move(os.path.join(folder, foldername, file), dest)
    print('DONE!')


if os.path.exists(os.path.abspath(sys.argv[1])):
    __SelectiveCopy__(sys.argv[1], sys.argv[2])