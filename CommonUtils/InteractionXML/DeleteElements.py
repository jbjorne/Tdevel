import sys, os, copy
extraPath = os.path.dirname(os.path.abspath(__file__))+"/../.."
#IF LOCAL
extraPath = os.path.dirname(os.path.abspath(__file__))+"/../../JariSandbox/ComplexPPI/Source"
#ENDIF
sys.path.append(extraPath)
import sys, os
thisPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(thisPath,"..")))
sys.path.append(os.path.abspath(os.path.join(thisPath,"../..")))
from Utils.ProgressCounter import ProgressCounter
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import cElementTree as ET
import cElementTreeUtils as ETUtils
from collections import defaultdict
import types

def getEmptyCorpus(xml, deletionRules=None):
    """
    A convenience function for getting an empty corpus, useful for testing for information leaks
    in the event extraction process.
    """
    if type(xml) in types.StringTypes:
        # XML is read from disk, so it's a new copy and can be safely modified
        xml = ETUtils.ETFromObj(xml)
    else:
        # XML is already an object in memory. To prevent problems with other users of it, a copy
        # is created before deleting elements.
        xml = copy.deepcopy(xml)
    if deletionRules == None: # use default rules for BioNLP Shared Task
        # We remove all interactions, and all entities that are not named entities. This leaves only
        # the gold standard protein/gene names
        deletionRules = {"interaction":{},"entity":{"isName":"False"}}
    # Remove elements and return the emptied XML
    return processCorpus(xml, None, deletionRules)
    
def removeElements(parent, elementName, attributes, countsByType):
    toRemove = []
    for element in parent.getchildren():
        attrType = {}
        if element.tag == elementName:
            remove = True
            for attrName,values in attributes.iteritems():
                if element.get(attrName) not in values:
                    remove = False
                    break
                else:
                    if attrName not in attrType:
                        attrType[attrName] = set()
                    attrType[attrName].add(element.get(attrName))
            if remove:
                toRemove.append(element)
                countsByType[elementName + " " + str(attrType)] += 1
        else:
            removeElements(element, elementName, attributes, countsByType)
    for element in toRemove:
        parent.remove(element)
        #countsByType[elementName] += 1
            
# Splits entities/edges with merged types into separate elements
def processSentence(sentence, rules, countsByType):
    for key in sorted(rules.keys()):
        #print key, rules[key]
        removeElements(sentence, key, rules[key], countsByType)

def processCorpus(inputFilename, outputFilename, rules):
    print >> sys.stderr, "Loading corpus file", inputFilename
    corpusTree = ETUtils.ETFromObj(inputFilename)
    corpusRoot = corpusTree.getroot()
    
    for eType in rules.keys():
        for attrRule in rules[eType].keys():
            rules[eType][attrRule] = rules[eType][attrRule].split("|")
    
    documents = corpusRoot.findall("document")
    counter = ProgressCounter(len(documents), "Documents")
    countsByType = defaultdict(int)
    for document in documents:
        counter.update()
        for sentence in document.findall("sentence"):
            processSentence(sentence, rules, countsByType)
    print >> sys.stderr, "Removed"
    for k in sorted(countsByType.keys()):
        print >> sys.stderr, "  " + k + ":", countsByType[k]
    
    if outputFilename != None:
        print >> sys.stderr, "Writing output to", outputFilename
        ETUtils.write(corpusRoot, outputFilename)
    return corpusTree

if __name__=="__main__":
    import sys
    print >> sys.stderr, "##### Split elements with merged types #####"
    
    from optparse import OptionParser
    # Import Psyco if available
    try:
        import psyco
        psyco.full()
        print >> sys.stderr, "Found Psyco, using"
    except ImportError:
        print >> sys.stderr, "Psyco not installed"

    optparser = OptionParser(usage="%prog [options]\nPath generator.")
    optparser.add_option("-i", "--input", default=None, dest="input", help="Corpus in interaction xml format", metavar="FILE")
    optparser.add_option("-o", "--output", default=None, dest="output", help="Output file in interaction xml format.")
    optparser.add_option("-r", "--rules", default=None, dest="rules", help="dictionary of python dictionaries with attribute:value pairs.")    
    (options, args) = optparser.parse_args()
    
    if options.input == None:
        print >> sys.stderr, "Error, input file not defined."
        optparser.print_help()
        sys.exit(1)
    if options.output == None:
        print >> sys.stderr, "Error, output file not defined."
        optparser.print_help()
        sys.exit(1)

    # Rules e.g. "{\"pair\":{},\"interaction\":{},\"entity\":{\"isName\":\"False\"}}"
    rules = eval(options.rules)
    print >> sys.stderr, "Rules:", rules
    processCorpus(options.input, options.output, rules)
