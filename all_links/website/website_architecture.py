import json
from xml.etree.ElementTree import Element, tostring, SubElement


class WebsiteArchitecture:
    def __init__(self, website_links):
        self.website_links = website_links

    def to_dict(self):
        descriptor = {}

        for link in self.website_links:
            section = link.split("/")[3]
            if section in descriptor.keys():
                descriptor[section].append(link)

            else:
                descriptor[section] = [link]

        return descriptor

    def to_json(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=4)

    def to_xml(self):
        elem = Element("urls")

        for section, links in self.to_dict().items():
            section = SubElement(elem, section)

            for link in links:
                link_xml = SubElement(section, "link")
                link_xml.text = link

        return tostring(elem).decode("utf-8")
