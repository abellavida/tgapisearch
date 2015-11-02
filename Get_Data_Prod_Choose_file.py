import httplib2
import Tkinter as tk
import tkFileDialog
import xml.etree.ElementTree as ET
from cStringIO import StringIO

http = httplib2.Http()
headers = {'Content-Type':'application/x-www-form-urlencoded'}
url = """http://import.brassring.com/WebRouter/WebRouter.asmx/route"""

#body = open("c:/Pyfiles/Web API Scripts/Canada_Stage_Test_2.txt", 'r')
kxa_out = open("c:/TEST/ResponseXML/Data_out.xml", 'w')

input_xml=''
kxa_output = []

#xml_in = body.read()

def get_data(input_xml):

    input_xml = ("inputXml=%s" %input_xml)
    response, content = http.request(uri=url, method='POST', headers=headers, body=input_xml)
    
    #print response, '\n'
    #print content, '\n'
    kxa_output = str(content)
    tree = ET.ElementTree(ET.fromstring(kxa_output))
    #print 'Tree:', tree
    root = tree.getroot()
    #print root.attrib, '\n', root.text
    out_xml = root.text
    #print out_xml
    out_xml = out_xml.encode('ascii', 'ignore')
    kxa_out.write(out_xml)
    kxa_out.close()
    

def main():

    root = tk.Tk()
    root.withdraw()
    
    xfile = tkFileDialog.askopenfilename(parent=root)
##    input_xml = filename.read()
    #print xfile
    if xfile != None:
        input_xml = open(xfile)
        r = input_xml.read()
        #print "mainloop", '\n', r
        get_data(r)
    else:
        print "had to pass"    

    

if __name__ == '__main__':
    main()

    
#body.close()
#kxa_out.close()

