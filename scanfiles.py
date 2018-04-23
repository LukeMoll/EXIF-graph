import exifread
import dateutil.parser
from sys import argv
import os
import re

def get_date(path_name):
    """
        Shamelessly ripped from ExifRead PyPi page
    """
    # Open image file for reading (binary mode)
    f = open(path_name, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)
    date = tags.get('Image DateTimeOriginal')
    return None if date is None else dateutil.parser.parse(str(date)


regex = re.compile(r'.+\.nef$', flags=re.IGNORECASE)

def main(basepath):
    # files = glob.glob(os.path.join(basepath, '/**'), recursive=True)

    dates = []
    for root, dirnames, filenames in os.walk(basepath):
        for filename in filenames:
            if regex.match(filename):
                date = get_date(os.path.join(root,filename))
                if(date is None): 
                    print(os.path.join(root,filename))
                else:
                    dates.append(date)

    outfile_name = list(filter(lambda e:len(e) > 0,basepath.split(os.sep)))[-1]+".txt"
    with open(outfile_name, 'w+') as outfile:
        for date in dates:
            outfile.write(date.isoformat(" ") + "\n")    
    print(len(dates),"dates written to", outfile_name)

if __name__ == '__main__':
    if(len(argv) > 1):
        main(argv[1])
    else:
        print("No argument supplied!")
