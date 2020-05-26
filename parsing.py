import xml.etree.ElementTree as ET


# Load XML file
doc = ET.parse('target/mutations.xml')
mutants = doc.getroot() # Recovers main tag 

# Parsing XML elements

for mutant in mutants:
    if mutant.attrib['status'] == 'SURVIVED':
        #print mutant.tag, mutant.attrib['detected'],  mutant.attrib['status'], mutant.attrib['numberOfTestsRun']
        numberOfTestsRun = mutant.attrib['numberOfTestsRun']
        sourceFile = mutant.findtext('sourceFile')
        mutatedClass = mutant.findtext('mutatedClass') 
        mutatedMethod = mutant.findtext('mutatedMethod')
        methodDescription = mutant.findtext('methodDescription')
        lineNumber = mutant.findtext('lineNumber')
        mutator = mutant.findtext('mutator') 
        index = mutant.findtext('index')
        block = mutant.findtext('block')
        killingTests = mutant.findtext('killingTests')
        succeedingTests = mutant.findtext('succeedingTests')
        description = mutant.findtext('description')
        
        #print succeedingTests
        print numberOfTestsRun, sourceFile
        testList = succeedingTests.split("|")
        for test in testList:
            print test



        
    

    