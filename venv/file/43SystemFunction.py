import os
import time


def createJavaProgram():
    with open('Java.java', 'w') as f:
        f.write('class Java {\n')
        f.write(' public static void main(String[] args) {\n')
        f.write('  System.out.println("Hello world from java");\n')
        f.write(' }\n')
        f.write('}\n')


os.system('pwd')
os.system('dir')
os.system('python3 42StatPrintSome.py')
createJavaProgram()
os.system('cat Java.java')
os.system('javac Java.java')
os.system('java Java')
# os.system('gedit')
time.sleep(5)
os.system('clear')

# via terminal
# :~/Code/venv/file$ python3 43SystemFunction.py
# /Code/venv/file
# 01ListIsTemp.py		       08FilePropertiesa+Mode.py  15ReadDataNCharacters.py  22ReadOneFileWrite.py  29Seek03.py					   36ReadCSV.py		 43SystemFunction.py
# 02ListIsTemp.py		       09FilePropertiesxMode.py   16ReadDataNCharacters.py  23With.py		   30CheckFilePresent.py			   37Zip.py		 Hmm.png
# 03FileProperties.py	       10Write.py		  17ReadDataNCharacters.py  24WithExceptions.py    31CheckFilePresentPrintLinesWordsCharacters.py  38UnZip.py		 Java.class
# 04FilePropertiesWriteMode.py   11WriteAppend.py		  18ReadDataLine.py	    25NormalExceptions.py  32BinaryData.py				   39Directory.py	 Java.java
# 05FilePropertiesAppendMode.py  12WriteLines.py		  19ReadDataLineLoop.py     26Tell.py		   33BinaryDataFix.py				   40ListOfDirectory.py
# 06FilePropertiesr+Mode.py      13ReadDataWrite.py	  20ReadAllLines.py	    27Seek01.py		   34CSV.py					   41Stat.py
# 07FilePropertiesw+Mode.py      14ReadData.py		  21ReadMix.py		    28Seek02.py		   35CSVFixBlankLine.py				   42StatPrintSome.py
# type(stats): <class 'os.stat_result'>
# File Size in Bytes: 475
# File Last Accessed Time: 2020-05-25 10:18:03.651505
# File Last Modified Time: 2020-05-25 10:14:59.514970
# class Java {
#  public static void main(String[] args) {
#   System.out.println("Hello world from java");
#  }
# }
# Hello world from java


# :~/Code/venv/file$
