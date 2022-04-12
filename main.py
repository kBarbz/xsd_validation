from lxml import etree


if __name__ == "__main__":
    xml_path = input("XML Path:")
    xsd_path = input("XSD Path:")

    xml_doc = etree.parse(xml_path)
    xmlschema_doc = etree.parse(xsd_path)

    xmlschema = etree.XMLSchema(xmlschema_doc)

    if not xmlschema.validate(xml_doc):
        print(xmlschema.assertValid(xml_doc))
    else:
        print("Valid!")
