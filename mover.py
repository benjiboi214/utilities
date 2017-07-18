import os, datetime, shutil
from sys import argv

script, arg_from, arg_to = argv

def mover(orig, dest):
    #get OS specific path sep
    sep = os.path.sep

    #get file list
    file_buffer = get_file_list(orig)

    #remove ignored files from list
    file_buffer = remove_dirs(orig, file_buffer)

    #convert datetime to string
    fdate = {}
    for i in file_buffer:
        fdate[i] = datetime_to_str(mod_date(orig + i))

    #create folders with datetime string
    for i in fdate.values():
        create_folder(dest, i)

    #move files overwriting any existing files
    for i in fdate.keys():
        shutil.move(orig + i, dest + fdate[i] + sep + i)
        print "Moving '%s' \nto '%s'" % (orig + i, dest + fdate[i])

def mod_date(file):
    '''Gets the modified date, returns datetime object.'''
    t = os.path.getmtime(file)
    return datetime.datetime.fromtimestamp(t)

def datetime_to_str(datetime):
    '''Takes datetime object and turns it into a string for use as folder name.'''
    #print datetime.date()
    return "%s-%s-%s" % (datetime.year, datetime.month, datetime.day)

def get_file_list(origin_path):
    '''Gets the list of files from in the origin path.
    Removes .DS_Store before returning list'''
    files = os.listdir(origin_path)
    for e in ['.DS_Store', '.localized']:
        try:
            files.remove(e)
        except ValueError:
            pass
    return files

def remove_dirs(path, file_buffer):
    '''Removes any directories from the list of files, so we don't go moving folders.'''
    files = []
    for i in file_buffer:
        if not os.path.isdir(path + i):
            files.append(i)
    return files

def create_folder(dest_path, folder_name):
    folder_path = dest_path + folder_name
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print "Folder '%s' created at '%s'" % (folder_name, dest_path)

#TODO - import list of files and folders to remove.

#TODO - Can add additional condition to the remove dirs
#method to remove these files/directories from the buffer.

#TODO - log everything

if __name__ == '__main__':
    mover(arg_from, arg_to)
