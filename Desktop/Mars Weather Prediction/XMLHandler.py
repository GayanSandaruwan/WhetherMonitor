import xml.etree.ElementTree

Class XMLHandler:
	def __init__(self):
		pass
	
	def getURL(dataType):
		xml = xml.etree.ElementTree.parse('URLS.xml').getroot();
		urltype	= xml.find(dataType);
		url = urltype.get('url');
		return url;
