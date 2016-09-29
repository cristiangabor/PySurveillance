import os
from xml.etree import ElementTree
file_name="info.xml"
fullname=os.path.abspath(file_name)
BOLD = '\033[1m'
NORMAL = '\033[0m'

def manage_xml(fullname,BOLD,NORMAL):
	#print(fullname)

	dom=ElementTree.parse(fullname)
	root=dom.getroot()
	#print (root)


	childrens=root.getchildren()

	for i in childrens:
		print(BOLD + "\n{}".format(i.tag))
		print(NORMAL + "\n\t{}".format(i.text))
		print("\n")

manage_xml(fullname,BOLD,NORMAL)
