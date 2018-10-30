"""Parse XML files"""

import xml.etree.ElementTree as et

tree = et.parse('hosts.xml')
print (tree)

print (tree.getroot())
print (tree.getroot().tag)
print (tree.getroot().attrib)

for host_tag in tree.getiterator('host'):

    print (host_tag.get('hostname'), int(host_tag.get('port')))

    for child_tag in host_tag:
        print(child_tag.tag, child_tag.text)


# Print first and last child of root tag
for host_tag in tree.getroot()[0], tree.getroot()[-1]:
    host_config = list()
    host_config.extend([host_tag.get('hostname'), int(host_tag.get('port'))])
    for child_tag in host_tag:
        host_config.append(child_tag.text)

    print (host_config)