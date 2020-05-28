#!/usr/bin/python
import xml.etree.ElementTree as ET

# Load XML file
doc = ET.parse('target/mutations.xml')
mutations = doc.getroot() # Recovers main tag

# Prepare output XML
root = ET.Element('mutations')

# Parsing XML elements
for mutation in mutations:

    detected = mutation.attrib['detected']
    status = mutation.attrib['status']
    numberOfTestsRun = mutation.attrib['numberOfTestsRun']
    sourceFile = mutation.findtext('sourceFile')
    mutatedClass = mutation.findtext('mutatedClass') 
    mutatedMethod = mutation.findtext('mutatedMethod')
    methodDescription = mutation.findtext('methodDescription')
    lineNumber = mutation.findtext('lineNumber')
    mutator = mutation.findtext('mutator') 
    index = mutation.findtext('index')
    block = mutation.findtext('block')
    killingTests = mutation.findtext('killingTests')
    succeedingTests = mutation.findtext('succeedingTests')
    description = mutation.findtext('description')
    
    if status == 'SURVIVED':

        # Create an element for each succeeding
        succeeded = succeedingTests.split("|")
        i = 1

        for stest in succeeded:
            # Add elements into new XML root
            _mutation = ET.SubElement(root, 'mutation', detected=detected, status=status, numberOfTestsRun=numberOfTestsRun)
            ET.SubElement(_mutation, "counter").text = str(i)
            ET.SubElement(_mutation, "sourceFile").text = sourceFile
            ET.SubElement(_mutation, "mutatedClass").text = mutatedClass
            ET.SubElement(_mutation, "mutatedMethod").text = mutatedMethod
            ET.SubElement(_mutation, "methodDescription").text = methodDescription
            ET.SubElement(_mutation, "lineNumber").text = lineNumber
            ET.SubElement(_mutation, "mutator").text = mutator
            ET.SubElement(_mutation, "index").text = index
            ET.SubElement(_mutation, "block").text = block
            ET.SubElement(_mutation, "killingTests").text = 'none'
            ET.SubElement(_mutation, "succeedingTests").text = stest
            ET.SubElement(_mutation, "description").text = description
            i += 1

    else: # Status = Killed

        # Create lists of killed and suceeded tests
        killed = killingTests.split("|")
        succeeded = succeedingTests.split("|")
        i = 1

        for ktest in killed:
            
            # Add elements into new XML root
            _mutation = ET.SubElement(root, 'mutation', detected='true', status='KILLED', numberOfTestsRun=numberOfTestsRun)
            ET.SubElement(_mutation, "counter").text = str(i)
            ET.SubElement(_mutation, "sourceFile").text = sourceFile
            ET.SubElement(_mutation, "mutatedClass").text = mutatedClass
            ET.SubElement(_mutation, "mutatedMethod").text = mutatedMethod
            ET.SubElement(_mutation, "methodDescription").text = methodDescription
            ET.SubElement(_mutation, "lineNumber").text = lineNumber
            ET.SubElement(_mutation, "mutator").text = mutator
            ET.SubElement(_mutation, "index").text = index
            ET.SubElement(_mutation, "block").text = block
            ET.SubElement(_mutation, "killingTests").text = ktest
            ET.SubElement(_mutation, "succeedingTests").text = 'none'
            ET.SubElement(_mutation, "description").text = description
            i += 1
        
        i = 1
        for stest in succeeded:
            # Add elements into new XML root
            _mutation = ET.SubElement(root, 'mutation', detected='false', status='SURVIVED', numberOfTestsRun=numberOfTestsRun)
            ET.SubElement(_mutation, "counter").text = str(i)
            ET.SubElement(_mutation, "sourceFile").text = sourceFile
            ET.SubElement(_mutation, "mutatedClass").text = mutatedClass
            ET.SubElement(_mutation, "mutatedMethod").text = mutatedMethod
            ET.SubElement(_mutation, "methodDescription").text = methodDescription
            ET.SubElement(_mutation, "lineNumber").text = lineNumber
            ET.SubElement(_mutation, "mutator").text = mutator
            ET.SubElement(_mutation, "index").text = index
            ET.SubElement(_mutation, "block").text = block
            ET.SubElement(_mutation, "killingTests").text = 'none'
            ET.SubElement(_mutation, "succeedingTests").text = stest
            ET.SubElement(_mutation, "description").text = description
            i += 1

# Write tree as new file
tree = ET.ElementTree(root)
tree.write('target/mutation_parsed.xml') 