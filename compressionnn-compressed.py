20
"<(~","#"*5,"/","*","\\"*14,"______4.DECOMPRESS__","\\"*14,"*","\\","#"*5,"~)>" ~9
"<(~","#"*6,"/","*","/"*13,"______3.COMPRESS____","/"*13,"*","\\","#"*6,"~)>" ~10
stores ~18
"<(~","#"*4,"/","*","/"*15,"______5.EXIT________","/"*15,"*","\\","#"*4,"~)>" ~11
"<(~","#"*8,"|","*","/"*11,"______1.BROWSE______","/"*11,"*","|","#"*8,"~)>" ~12
",os.path.getsize(filename2[:-1*(len(ext)+1)]+"-compressed."+ext),"bytes" ~13
compress(filename2[:-1*(len(ext)+1)]+"-compressed."+ext,n-ctr-6) ~16
self.lines ~17
"<(~","#"*5,"\\","*","\\"*12,"+","--------------------","+","\\"*12,"*","/","#"*5,"~)>" ~4
"<(~","#"*7,"/","*","\\"*12,"______2.SIZE________","\\"*12,"*","\\","#"*7,"~)>" ~8
dictionary ~19
print ~1
"<(~","#"*7,"\\","*","\\"*12,"******FUNCTIONS*****","\\"*12,"*","/","#"*7,"~)>" ~7
"<(~","#"*2,"\\","*","/"*15,"+","--------------------","+","/"*15,"*","/","#"*2,"~)>" ~5
file ~6
x=os.path.getsize(filename2[:-1*(len(ext)+1)]+"-compressed."+ext) ~15
tkFileDialog.askopenfilename(parent=root,title='Browse ~0
root.attributes("-topmost", ~2
root.destroy() ~14
compressed ~3
import os
from os.path import join, getsize
import Tkinter
import tkFileDialog

#Function to browse the ~6 to be ~3
#It uses the tkinter gui to open the ~6 dialog box which allows the user
#to browse through files on the computer
def browsefl():
root = Tkinter.Tk()
~2 True)#it prevents the dialog box to open behind other windows
filename = ~0 for the file')
if len(filename) > 0:
~1 "You chose ",filename
~14

#Function to browse the directory in which the ~6 is stored
def browsedr():
root = Tkinter.Tk()
~2 True)
dirct = tkFileDialog.askdirectory(parent=root, title='Open folder where the ~6 to be ~3 is stored')
~1 "Directory is :",dirct
s=""
for t in str(dirct):
if t=="/":
s+='\\'+'\\'
else:
s+=t

~1 "Path is :",s+"\\"+"\\"
~14



class compress:
'''
# syntax : c = compress(fileName, dictionarySize)
# so if we have c = compress('text.txt',100), then
# we are compressing the ~6 named text.txt and we replace 100 words
# The ~3 ~6 can be accesed as c.compressedFile
'''

def __init__(self, readFileName,num):
self.readFileName = readFileName

# self.num is the number of element in the key
self.num = num

# ~17 ~18 the ~6 as a list of lines of the ~6
~17 = []

# self.d ~18 the frequency of occurence of each word.
self.d = {}

# self.l ~18 the list of tuples as explained later.
self.l = []

# self.key ~18 the best words to replace. it maps words to their coded text
self.key = {}

#self.compressedFile ~18 the coded ~6 as a list of strings.
self.compressedFile = []

#Method that calls all other methods of the class to compress the ~6
def compressFile(self):
self.readFile()
self.buildDict()
self.optimise()
self.buildList()
self.sortedList()
self.buildKey()
self.searchAndReplace()

#Method that ~18 each line in the text ~6 as an element in the list ~17
def readFile(self):
f = open(self.readFileName,'r')
~17 = f.readlines()
f.close()

# this method builds the ~19 self.d calculating frequency of each word.
# since the replacements are from ~0 to ~99, we replace only those elements
# with length > 3 and that are not whitespace
def buildDict(self):
for line in self.lines:

# we split each line on whitespace characters using .split() method.
for word in line.split():
# add each element with length>3 to self.d and update frequency
if len(word)>3:
if word in self.d.keys():
self.d[word]+=1
else:
self.d[word] = 1


# this calculates freq * length for every word in passage.
# so if '^' occurs 15 times and 'hello' occurs 4 times
# self.d['^'] = 1*15 and self.d['hello'] = 4*5
# so 'hello' gets a higher rank than '^' even though '^' occurs more frequently
def optimise(self):
for k in self.d.keys():
self.d[k] = self.d[k] * len(k)

# by now we have freq * len of all words in our file. We need to find the best words
# to replace. Since sorting is not supported in dictionary, we need to build a list
# and sort on the basis of freq * length

# this method builds a list of tuples self.l where
# each element in the list is a (word , freq * length) tuple
def buildList(self):
for word in self.d.keys():
# t is a tuple with first element as the word
# and the second element as its freq * len.
t = (word,self.d[word])
self.l.append(t)

# this method sorts the list of tuples according to freq * length
# i.e. the second element of the tuple.
# with reverse selection sort
def sortedList(self):
L=self.l
for i in range(len(L)):
for j in range(i+1,len(L)):
if L[i][1]<L[j][1]:
temp=L[j]
L[j]=L[i]
L[i]=temp
self.l=L
# this method builds a ~19 'self.num', of the best words with their replacements
# so the best word maps to ~0, second best to ~1 and so on..
# for example self.key['advertaisment'] = '~10'. if 'advertaisment' has rank 10 in the sorted list.
def buildKey(self):
for i in range(self.num):
self.key[self.l[i][0]] = ('~'+str(i), self.l[i][1])

# this method looks up each word in the ~19
# if found, it replaces with ~rank
# so if "hello" gets the highest weight, it gets switched by ~0 in the ~3 ~6
def searchAndReplace(self):
for line in self.lines:
# list 'line' converts to list 'newLine' after replacing with the code text.
newLine = []
# here I split each line into a list of strings according to whitespace, using
# the regular expression (\s+) with the re.split() method.
# using re.plit() instead of .split() here is important since we need to preserve the delimiters
# such as spaces, tabs, etc to retain formatting.
# so for example re.split(r'(\s+)','It is a beautiful day ') would return
# ['It', ' ', 'is', ' ', 'a', ' ', 'beautiful', ' ', 'day', ' \t', '']
# original text can be reassembled from the above list by using the "[separation]".join() method
q=[]
for x in line.split():
q.append(x)

for word in q:
# if word is found in key, replace it
if word in self.key.keys():
newLine.append(self.key[word][0])
# if not found in key, use original word
else:
newLine.append(word)


self.compressedFile.append(" ".join(newLine))


# this method prints in the following in order
# ~19 size
# ~19
# ~3 text
def printFile(self, writefileName):
f = open(writefileName,'w')
f.write(str(self.num)+'\n')
for word in self.key.keys():
f.write(word + ' ' + self.key[word][0] + '\n')
f.write("\n".join(self.compressedFile))
f.close()


class decompress:
'''
# syntax : decompress(fileName)
# so if we have d = decompress('text.txt'), then
# we are decompressing the ~6 named text.txt
# The decompressed ~6 can be accesed as c.originalFile
'''

def __init__(self, readFileName):
self.readFileName = readFileName
# self.num ~18 the number of elements in the key. ie number of coded words
self.num = 0
# self,lines ~18 the text ~6 as a list of strings of each line.
~17 = []
# self.revkey maps the coded text to the original word.
self.revKey = {}
#self.originalFile ~18 the decoded ~6 as a list of strings of each line.
self.originalFile = []

def decompressFile(self):
self.readFile()
self.buildReverseKey()
self.searchAndReplace()

# this function reads the ~3 file.
# the first line of the ~3 ~6 should contain
# the ~19 size
def readFile(self):
f = open(self.readFileName,'r')
~17 = f.readlines()
# self.num is the number of elements in the key.
# first line of the coded text ~18 this value
self.num = int(self.lines[0].split()[0])
f.close()

#this method builds the key using the lines 1 to self.num, of the ~3 ~6
# so if 'hello' switched with ~5 in the original key while encoding, now
# ~5 replaced by 'hello' while decoding.
def buildReverseKey(self):
for line in self.lines[1:self.num+1]:
l = line.split()
self.revKey[l[1]] = l[0]

# this method replaces the code words with their original word
# again using concepts of list is important here to preserve the formatting
def searchAndReplace(self):
for line in self.lines[self.num+1:]:
newLine = []
q=[]
for x in line.split():
q.append(x)
q.append(' ')

for word in q:
if word in self.revKey.keys():
newLine.append(self.revKey[word])
else:
newLine.append(word)
self.originalFile.append("".join(newLine))
def printFile(self, writeFileName):
f = open(writeFileName,'w')
f.write("\n".join(self.originalFile))
f.close()

#Function to compress the ~6
def runprocompress():
y=1
while y==1:
try:
root = Tkinter.Tk()
~2 True)#it prevents the dialog box to open behind other windows
filename2 = ~0 for the file')
if len(filename2) > 0:
~1 "You chose ",filename2
~14
b=filename2.split("/")
Fn=b[len(b)-1]
if os.path.isfile(filename2):
~1 "YEAH!! file's there"
~1 "File size is ",os.path.getsize(filename2),"bytes"
break
except:
y=1
pass


n=input('no. keys >>>')
# start compression
c = compress(filename2,n)
c.compressFile()
extarr = filename2.split(".")
ext = extarr[len(extarr)-1]
c.printFile(filename2[:-1*(len(ext)+1)]+"-compressed."+ext)
~15
ctr=1
#print "File size after compression number",ctr," is ",x,"bytes"
#c = ~16
#c.compressFile()
#ctr+=1
#c.printFile(filename2[:-1*(len(ext)+1)]+"-compressed."+ext)
~1 "File size after compression number ",ctr," is ~13
~1 "Successfully compressed!!"

#Function to decompress an already ~3 ~6
def runprodecompress():
y=1
while y==1:
try:
root = Tkinter.Tk()
~2 True)#it prevents the dialog box to open behind other windows
filename3 = ~0 for the file')
if len(filename3) > 0:
~1 "You chose ",filename3
~14
b=filename3.split("/")
Fn=b[len(b)-1]
if os.path.isfile(filename3):
~1 "Yeah file's there"
~1 "File size of ~3 file-",os.path.getsize(filename3),"bytes"
break
except:
y=1
pass
d = decompress(filename3)
d.decompressFile()
extarr = filename3.split(".")
ext = extarr[len(extarr)-1]
d.printFile(filename3[:-1*(12 + len(ext))]+"-new."+ext)
#d = decompress(filename3[:-1*(12 + len(ext))]+"-new."+ext)
#d.decompressFile()
#d.printFile(filename3[:-1*(12 + len(ext))]+"-new"+ext)
~1 "File decompressed, Decompressed filename:",filename3.split("/")[len(b)-1][:-1*(12 + len(ext))]+"-new."+ext
~1 "DONE!!"


# WELCOME SCREEN / UI

~1 " O ","/+\\"*23," O "
~1 " X ","|"*70," X "
~1 "<(~","#"*70,"~)>"
~1 ~5
~1 "<(~","#"*3,"\\","*","\\"*14,"|","DATA FILE COMPRESSER","|","\\"*14,"*","/","#"*3,"~)>"
~1 "<(~","#"*4,"\\","*","/"*13,"|"," DECOMPRESSER ","|","/"*13,"*","/","#"*4,"~)>"
~1 ~4
~1 "<(~","#"*6,"\\","*","/"*48,"*","/","#"*6,"~)>"
~1 ~7
~1 ~12
~1 ~8
~1 ~10
~1 ~9
~1 ~11
~1 "<(~","#"*3,"/","*","\\"*54,"*","\\","#"*3,"~)>"
~1 "<(~","#"*2,"/","*","/"*56,"*","\\","#"*2,"~)>"
~1 "<(~","#"*70,"~)>"
~1 " X ","|"*70," X "
~1 " O ","\V/"*23," O "

while True:
try:
#Option for user to choose the desired action to be performed
FC=input("Enter Action Choice >>>")
if FC==1:
v=raw_input("Browse File('f') or Directory('d')? ")
if v=='f':
browsefl()
if v=='d':
browsedr()
if FC==2:
root = Tkinter.Tk()
~2 True)#it prevents the dialog box to open behind other windows
filename1 = ~0 for the file')
if len(filename1) > 0:
~1 "You chose ",filename1
~14
b=filename1.split("/")
Fn=b[len(b)-1]
if not os.path.isfile(filename1):
~1 "File not found"
else:
~1 "Size of ",Fn," is ",os.path.getsize(filename1),"bytes"
if FC==3:
runprocompress()
if FC==4:
runprodecompress()
if FC==5:
~1 "exit"
exit(0)
except EOFError:
~1 "NOPE!! Re input Please :)"
pass