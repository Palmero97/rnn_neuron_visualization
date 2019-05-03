# Used to read and write xml files
import xml.etree.ElementTree as ET
# Used to prettify elementree written files
from xml.dom import minidom

from faker import Faker

import re

fake = Faker()

writeTree = ET.Element('users')

for _ in range(10000): # Remove the first empty list
	userItem = ET.SubElement(writeTree, 'user')

	nameItem = ET.SubElement(userItem, 'name')
	nameItem.text = fake.name()

	emailItem = ET.SubElement(userItem, 'email')
	email = fake.free_email()
	emailItem.text = re.sub(r"\W+", "",nameItem.text.replace(" ","").lower()) + email[email.find("@"):]

	ccItem = ET.SubElement(userItem, 'creditcard')
	ccItem.text = fake.credit_card_number()

	dateItem = ET.SubElement(userItem, 'date')
	dateItem.text = fake.date_this_century().strftime("%Y-%m-%d")


# Create XML file and write the results
with open("xml_dataset.xml", "w") as f:
	writeStr = minidom.parseString(ET.tostring(writeTree)).toprettyxml()
	f.write(writeStr)

"""
<users>
	<user>
		<name> fake.name()
		<email> fake.free_email(*args, **kwargs)
		<creditcard> fake.credit_card_number(card_type=None)
		<date> fake.date_this_century(before_today=True, after_today=False)
	</user>
</user>

"""
