import xml.dom.minidom as m
import parse as p

def create_document(title, description=''):
    """Create the overall KML document."""

    # Initialization of an XML doc
    doc = m.Document()

    # Define as a KML-type XML doc
    kml = doc.createElement('kml')

    # Pull in common attributes and set it for our doc
    kml.setAttribute('xmlns', 'http://www.opengis.net/kml/2.2')
    doc.appendChild(kml)
    
    # Create common elements that Google will read/plot
    document = doc.createElement('Document')
    kml.appendChild(document)
    docName = doc.createElement('title')
    document.appendChild(docName)
    docName_text = doc.createTextNode(title)
    docName.appendChild(docName_text)
    docDesc = doc.createElement('description')
    document.appendChild(docDesc)
    docDesc_text = doc.createTextNode(description)
    docDesc.appendChild(docDesc_text)

    return doc

def create_placemark(address):
    """Generate the KML Placemark for a given address.
    This is the function that takes the info from the
    file we parse at the end of this script.
    """

    # Create an initial XML Document
    doc = m.Document()

    # Create elements for Placemark and add to our new doc
    pm = doc.createElement("Placemark")
    doc.appendChild(pm)
    name = doc.createElement("name")
    pm.appendChild(name)
    name_text = doc.createTextNode('{0[name]}'.format(address))
    name.appendChild(name_text)
    desc = doc.createElement("description")
    pm.appendChild(desc)
    desc_text = doc.createTextNode('Date: {0[date]}, {0[description]}'.
                                   format(address))
    desc.appendChild(desc_text)
    pt = doc.createElement("Point")
    pm.appendChild(pt)
    coords = doc.createElement("coordinates")
    pt.appendChild(coords)
    coords_text = doc.createTextNode('{0[longitude]},{0[latitude]}'.format(address))
    coords.appendChild(coords_text)

    return doc

def create_gmap(data_file):
    # Create a new KML doc
    kml_doc = create_document("Crime map", "Plots of Recent SF Crime")

    document = kml_doc.documentElement.getElementsByTagName("Document")[0]

    for line in data_file:
        placemark_info = {'longitude': line['X'],
                          'latitude': line['Y'],
                          'name': line['Category'],
                          'description': line['Descript'],
                          'date': line['Date']
                          }

        if placemark_info['longitude'] == "0":
            continue

        placemark = create_placemark(placemark_info)

        document.appendChild(placemark.documentElement)
    
    # Create the KML file
    with open('file_sf.kml', 'w') as f:
        f.write(kml_doc.toprettyxml(indent="  ", encoding='UTF-8'))

def main():
    data = p.parse(p.MY_FILE, ",")

    return create_gmap(data)

if __name__ == "__main__":
    main()
