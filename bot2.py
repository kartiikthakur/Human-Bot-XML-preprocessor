# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import xml.etree.ElementTree as ET
import unicodedata


path = 'pan19-author-profiling-training-2019-01-28\en'
filepath = 'truthEN.txt'
with open(filepath) as fp:
	for line in fp:
		lines = line.replace(":::", " @@@ ")
		output1 = lines.replace("\n","")
		result = line.split(":::")
		for filename in os.listdir(path):
			authorid = filename.split(".")[0]
			if(authorid == result[0]):
				newpath = path + "\\" + authorid + ".xml"
				with open(newpath) as np:
					tree = ET.parse(newpath)
					root = tree.getroot()
					f = open("bot2.txt", "a")
				for child in root.iter('document'):
					texts = child.text
					if not ("\n") in texts:
						output = str(output1) + " @@@ " + texts
						if isinstance(texts,unicode):
							output2 = unicodedata.normalize('NFKD', texts).encode('ascii', 'ignore')
							output = output1 + " @@@ " + output2 + "\n"
							f.write(output)



						else:
							output = output1 + " @@@ " + texts + "\n"
							f.write(output)
