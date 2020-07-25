
import xml.etree.ElementTree as etxml


class pinMonitor:

   def __init__(self):
      self.pin_map_xml_file = None
      self.xmltree = None

   def load_pin_map(self, fn="pin_map.xml"):
      self.xmltree = etxml.parse(fn)
