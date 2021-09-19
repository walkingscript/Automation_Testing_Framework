import json
import xml.etree.ElementTree as ElementTree

from logging import getLogger

logger = getLogger(__name__)


class BaseJSONDataProvider:

    def __init__(self, filename):
        logger.info('Initialization of JSON data provider')
        with open(filename, 'r', encoding='utf-8') as f:
            self.data = json.load(f)


class BaseXMLDataProvider:

    def __init__(self, xml_file):
        logger.info('Initialization of XML data provider')
        self.xml_tree = ElementTree.parse(xml_file)
        self.root = self.xml_tree.getroot()


__all__ = ['BaseJSONDataProvider', 'BaseXMLDataProvider']
