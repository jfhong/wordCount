# wordCount
Python script that counts words using hash table. Not perfect yet as I need to figure out how to take out the apostrophe from some words as I haven't figured that out on python yet.

Before we run this script, you need a few things to be in order.
  1. Make sure .TXT file and .PY file are both in the same folder.
  2. Go into the .PY file and on line 1, change file path to find your .TXT file.
  
  2.1 to find path to .TXT file, go into your terminal, 'cd' until you reach the folder of your .TXT file and enter in    terminal 'pwd'. This will give you your file path. Copy and paste that into the .PY file on the first line, after the '('.
  
  2.2 here is an example of FINISHED file path for .PY file.
  
  2.2.1 f = open("/.../.../.../.../TEXTFILE.txt", "r")
  
Making sure the above is completed, we are now going to run the script.
  1. In terminal, travel to the folder that holds both the .PY and .TXT file.
  2. Type the command into terminal: python3 playingwhashtables.py
  
This script is returning the hashtable itself in the format of: 'words' to 'value'. It also returns the number of words in the hashtable, this was a test I was using as I was making sure the counter was correct.
