from libs.flatten.flatten import Flatten
import sys
import xmltodict

PATH_TO_XML = sys.argv[-1]

with open(PATH_TO_XML, 'r') as f:
    xml_str = f.read()
    res = xmltodict.parse(xml_str)

inst = Flatten()
inst.flatten_recursive(res)
sys.stdout.write(f"{str(inst.get_depth_without_atr())}\n")
