import sys  # command line arguments
import re  # regular expression tools
import os  # checking if file exists

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCountTest.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]

# first check to make sure program exists
if not os.path.exists("WordCount.py"):
    print("wordCount.py doesn't exist! Exiting")
    exit()

# make sure text files exist
if not os.path.exists(textFname):
    print("text file input %s doesn't exist! Exiting" % textFname)
    exit()

# master dictionary
master = set()
list = []
# attempt to open input file
with open(textFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip()
        # split line on whitespace and punctuation
        word = re.split("[ \t.,;:'-]", line)

        for key in word:
            master.add(key.lower())
            list.append(key.lower())

master = sorted(master)
master.remove('')
master = dict.fromkeys(master, 0)

for key in master:
    for word in list:
        if key == word:
            master[key] += 1

f = open("output.txt", "w+")
for key in master:
    f.write("%s %d\n" %(key, master.get(key)))

f.close()

