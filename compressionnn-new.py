import os 
from os.path import join, getsize 
import Tkinter 
import tkFileDialog 

#Function to browse the file to be compressed 
#It uses the tkinter gui to open the file dialog box which allows the user 
#to browse through files on the computer 
def browsefl(): 
root = Tkinter.Tk() 
root.attributes("-topmost", True)#it prevents the dialog box to open behind other windows 
filename = tkFileDialog.askopenfilename(parent=root,title='Browse for the file') 
if len(filename) > 0: 
print "You chose ",filename 
root.destroy() 

#Function to browse the directory in which the file is stored 
def browsedr(): 
root = Tkinter.Tk() 
root.attributes("-topmost", True) 
dirct = tkFileDialog.askdirectory(parent=root, title='Open folder where the file to be compressed is stored') 
print "Directory is :",dirct 
s="" 
for t in str(dirct): 
if t=="/": 
s+='\\'+'\\' 
else: 
s+=t 

print "Path is :",s+"\\"+"\\" 
root.destroy() 



class compress: 
''' 
# syntax : c = compress(fileName, dictionarySize) 
# so if we have c = compress('text.txt',100), then 
# we are compressing the file named text.txt and we replace 100 words 
# The compressed file can be accesed as c.compressedFile 
''' 

def __init__(self, readFileName,num): 
self.readFileName = readFileName 

# self.num is the number of element in the key 
self.num = num 

# self.lines stores the file as a list of lines of the file 
self.lines = [] 

# self.d stores the frequency of occurence of each word. 
self.d = {} 

# self.l stores the list of tuples as explained later. 
self.l = [] 

# self.key stores the best words to replace. it maps words to their coded text 
self.key = {} 

#self.compressedFile stores the coded file as a list of strings. 
self.compressedFile = [] 

#Method that calls all other methods of the class to compress the file 
def compressFile(self): 
self.readFile() 
self.buildDict() 
self.optimise() 
self.buildList() 
self.sortedList() 
self.buildKey() 
self.searchAndReplace() 

#Method that stores each line in the text file as an element in the list self.lines 
def readFile(self): 
f = open(self.readFileName,'r') 
self.lines = f.readlines() 
f.close() 

# this method builds the dictionary self.d calculating frequency of each word. 
# since the replacements are from tkFileDialog.askopenfilename(parent=root,title='Browse to ~99, we replace only those elements 
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
# this method builds a dictionary 'self.num', of the best words with their replacements 
# so the best word maps to ~0, second best to print and so on.. 
# for example self.key['advertaisment'] = '~10'. if 'advertaisment' has rank 10 in the sorted list. 
def buildKey(self): 
for i in range(self.num): 
self.key[self.l[i][0]] = ('~'+str(i), self.l[i][1]) 

# this method looks up each word in the dictionary 
# if found, it replaces with ~rank 
# so if "hello" gets the highest weight, it gets switched by tkFileDialog.askopenfilename(parent=root,title='Browse in the compressed file 
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
# dictionary size 
# dictionary 
# compressed text 
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
# we are decompressing the file named text.txt 
# The decompressed file can be accesed as c.originalFile 
''' 

def __init__(self, readFileName): 
self.readFileName = readFileName 
# self.num stores the number of elements in the key. ie number of coded words 
self.num = 0 
# self,lines stores the text file as a list of strings of each line. 
self.lines = [] 
# self.revkey maps the coded text to the original word. 
self.revKey = {} 
#self.originalFile stores the decoded file as a list of strings of each line. 
self.originalFile = [] 

def decompressFile(self): 
self.readFile() 
self.buildReverseKey() 
self.searchAndReplace() 

# this function reads the compressed file. 
# the first line of the compressed file should contain 
# the dictionary size 
def readFile(self): 
f = open(self.readFileName,'r') 
self.lines = f.readlines() 
# self.num is the number of elements in the key. 
# first line of the coded text stores this value 
self.num = int(self.lines[0].split()[0]) 
f.close() 

#this method builds the key using the lines 1 to self.num, of the compressed file 
# so if 'hello' switched with "<(~","#"*2,"\\","*","/"*15,"+","--------------------","+","/"*15,"*","/","#"*2,"~)>" in the original key while encoding, now 
# "<(~","#"*2,"\\","*","/"*15,"+","--------------------","+","/"*15,"*","/","#"*2,"~)>" replaced by 'hello' while decoding. 
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

#Function to compress the file 
def runprocompress(): 
y=1 
while y==1: 
try: 
root = Tkinter.Tk() 
root.attributes("-topmost", True)#it prevents the dialog box to open behind other windows 
filename2 = tkFileDialog.askopenfilename(parent=root,title='Browse for the file') 
if len(filename2) > 0: 
print "You chose ",filename2 
root.destroy() 
b=filename2.split("/") 
Fn=b[len(b)-1] 
if os.path.isfile(filename2): 
print "YEAH!! file's there" 
print "File size is ",os.path.getsize(filename2),"bytes" 
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
x=os.path.getsize(filename2[:-1*(len(ext)+1)]+"-compressed."+ext) 
ctr=1 
#print "File size after compression number",ctr," is ",x,"bytes" 
#c = compress(filename2[:-1*(len(ext)+1)]+"-compressed."+ext,n-ctr-6) 
#c.compressFile() 
#ctr+=1 
#c.printFile(filename2[:-1*(len(ext)+1)]+"-compressed."+ext) 
print "File size after compression number ",ctr," is ",os.path.getsize(filename2[:-1*(len(ext)+1)]+"-compressed."+ext),"bytes" 
print "Successfully compressed!!" 

#Function to decompress an already compressed file 
def runprodecompress(): 
y=1 
while y==1: 
try: 
root = Tkinter.Tk() 
root.attributes("-topmost", True)#it prevents the dialog box to open behind other windows 
filename3 = tkFileDialog.askopenfilename(parent=root,title='Browse for the file') 
if len(filename3) > 0: 
print "You chose ",filename3 
root.destroy() 
b=filename3.split("/") 
Fn=b[len(b)-1] 
if os.path.isfile(filename3): 
print "Yeah file's there" 
print "File size of compressed file-",os.path.getsize(filename3),"bytes" 
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
print "File decompressed, Decompressed filename:",filename3.split("/")[len(b)-1][:-1*(12 + len(ext))]+"-new."+ext 
print "DONE!!" 


# WELCOME SCREEN / UI 

print " O ","/+\\"*23," O " 
print " X ","|"*70," X " 
print "<(~","#"*70,"~)>" 
print "<(~","#"*2,"\\","*","/"*15,"+","--------------------","+","/"*15,"*","/","#"*2,"~)>" 
print "<(~","#"*3,"\\","*","\\"*14,"|","DATA FILE COMPRESSER","|","\\"*14,"*","/","#"*3,"~)>" 
print "<(~","#"*4,"\\","*","/"*13,"|"," DECOMPRESSER ","|","/"*13,"*","/","#"*4,"~)>" 
print "<(~","#"*5,"\\","*","\\"*12,"+","--------------------","+","\\"*12,"*","/","#"*5,"~)>" 
print "<(~","#"*6,"\\","*","/"*48,"*","/","#"*6,"~)>" 
print "<(~","#"*7,"\\","*","\\"*12,"******FUNCTIONS*****","\\"*12,"*","/","#"*7,"~)>" 
print "<(~","#"*8,"|","*","/"*11,"______1.BROWSE______","/"*11,"*","|","#"*8,"~)>" 
print "<(~","#"*7,"/","*","\\"*12,"______2.SIZE________","\\"*12,"*","\\","#"*7,"~)>" 
print "<(~","#"*6,"/","*","/"*13,"______3.COMPRESS____","/"*13,"*","\\","#"*6,"~)>" 
print "<(~","#"*5,"/","*","\\"*14,"______4.DECOMPRESS__","\\"*14,"*","\\","#"*5,"~)>" 
print "<(~","#"*4,"/","*","/"*15,"______5.EXIT________","/"*15,"*","\\","#"*4,"~)>" 
print "<(~","#"*3,"/","*","\\"*54,"*","\\","#"*3,"~)>" 
print "<(~","#"*2,"/","*","/"*56,"*","\\","#"*2,"~)>" 
print "<(~","#"*70,"~)>" 
print " X ","|"*70," X " 
print " O ","\V/"*23," O " 

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
root.attributes("-topmost", True)#it prevents the dialog box to open behind other windows 
filename1 = tkFileDialog.askopenfilename(parent=root,title='Browse for the file') 
if len(filename1) > 0: 
print "You chose ",filename1 
root.destroy() 
b=filename1.split("/") 
Fn=b[len(b)-1] 
if not os.path.isfile(filename1): 
print "File not found" 
else: 
print "Size of ",Fn," is ",os.path.getsize(filename1),"bytes" 
if FC==3: 
runprocompress() 
if FC==4: 
runprodecompress() 
if FC==5: 
print "exit" 
exit(0) 
except EOFError: 
print "NOPE!! Re input Please :)" 
pass 