import os, shutil

def flattenfiles():
    '''Main function for logic'''
    usb_name = get_usb_name()
    dest_path = get_dest_path()
    
    file_list = get_directories(usb_name)
    
    move_files(file_list, dest_path)

def get_usb_name():
    '''Function for getting the name of the USB off the user.'''
    while True:
        print "Please enter the name of the rekordbox USB"
        usb_path = "/Volumes/%s/Contents" % raw_input(">: ")
        if os.path.exists(usb_path):
            return usb_path
        print "Error: Check USB name and that 'Contents' folder exists on USB."

def get_dest_path():
    '''Function for retreiving the destination path from the user's head'''
    while True:
        print "Please enter the absolute path to the destination directory"
        dest_path = raw_input(">: ")
        if os.path.exists(dest_path):
            return dest_path
        print "Error: Check the path, does not exist."

def get_directories(contents):
    '''Where contents is the contents folder on rekordbox USB'''
    file_list = []
    
    for dirPath, dirNames, fileNames in os.walk(contents):
        for i in fileNames:
            file_list.append(os.path.join(dirPath, i))
    
    return file_list

def move_files(file_list, destination):
    '''Takes the list of files and iterates over them transferring them one by one.'''
    for item in file_list:
            print "Copying %s" % item
            shutil.copy(item, destination)

if __name__ == '__main__':
    flattenfiles()