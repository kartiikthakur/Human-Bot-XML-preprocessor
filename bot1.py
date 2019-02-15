# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import xml.etree.ElementTree as ET
import unicodedata

path = 'pan19-author-profiling-training-2019-01-28\en'
filepath = 'truthEN.txt'

for filename in os.listdir(path):
	authorid = filename.split(".")[0]
	with open(filepath) as fp:
		for line in fp:
			lines = line.replace(":::", " @@@ ")
			output1 = lines.replace("\n", "")
			result = line.split(":::")
			if(authorid == result[0]):
				newpath = path + "\\" + authorid + ".xml"
				with open(newpath) as np:
					tree = ET.parse(newpath)
					root = tree.getroot()
					f = open("bot1.txt", "a")
					for child in root.iter('document'):
						texts = child.text
						if ("\n") in texts:
							texts = texts.replace("\n","").strip("\n")
							output = str(output1) + " @@@ " + texts
							if isinstance(texts,unicode):
								output2 = unicodedata.normalize('NFKD', texts).encode('ascii', 'ignore')
								output = output1 + " @@@ " + output2 + "\n"
								f.write(output)
								
							else:
								output = output1 + " @@@ " + texts + "\n"
								f.write(output)
						else:
							output = str(output1) + " @@@ " + texts
							if isinstance(texts,unicode):
								output2 = unicodedata.normalize('NFKD', texts).encode('ascii', 'ignore')
								output = output1 + " @@@ " + output2 + "\n"
								f.write(output)
								
							else:
								output = output1 + " @@@ " + texts + "\n"
								f.write(output)
						