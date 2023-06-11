#!/usr/bin/env python3
 
def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)
 
def file_extensions(filename):
    no_extension=[]
    d = {}
    with open(filename) as f:
        for line in f:
            line=line.strip()
            v = line.split('.')
            if len(v) == 1:
                no_extension.append(line)
            else:
                extension = v[-1]
                if extension in d:
                    d[extension].append(line)
                else:
                    d[extension] = [line]
                    
    return (no_extension, d)
 
def main():
    no_extension, d = file_extensions(get_path("filenames.txt"))
    print("%i files with no extension" % len(no_extension))
    for extension in sorted(d):
        print("%s %i" % (extension, len(d[extension])))
 
if __name__ == "__main__":
    main()
 