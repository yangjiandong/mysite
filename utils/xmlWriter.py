
from xml.dom.minidom import Document
from xml.sax.saxutils import unescape

class XmlWriter:

  def __init__(self):
    self.doc = Document()

  def createNode(self, nodeName, parentNode = '', withAttribs = {}):
    node = self.doc.createElement(nodeName)
    if parentNode == '':   # create a parent node
      createdNode = self.doc.appendChild(node)
    else:                  # create a child node
      createdNode = parentNode.appendChild(node)

    if withAttribs != {}:
      for key, value in withAttribs.items():
        self.setAttribute(createdNode, key, value)

    return createdNode

  def setAttribute(self, node, key, value):
    node.setAttribute(key, value)

  def printXML(self):
    print self.doc.toprettyxml(indent="  ")
