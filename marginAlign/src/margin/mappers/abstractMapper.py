from jobTree.scriptTree.target import Target
from margin.marginAlignLib import chainSamFile, realignSamFileTargetFn
import os
from sonLib.bioio import system

class AbstractMapper(Target):
    """Base class for mappers. Inherit this class to create a mapper
    """
    def __init__(self, readFastqFile, referenceFastaFile, outputSamFile, options):
        Target.__init__(self)
        self.readFastqFile = readFastqFile
        self.referenceFastaFile = referenceFastaFile
        self.outputSamFile = outputSamFile
        self.options = options #These are the options from cactus_expectationMaximisation
        
    def chainSamFile(self):
        """Converts the sam file so that there is at most one global alignment of each read
        """ 
        tempSamFile = os.path.join(self.getLocalTempDir(), "temp.sam")
        system("cp %s %s" % (self.outputSamFile, tempSamFile))
        chainSamFile(tempSamFile, self.outputSamFile, self.readFastqFile, self.referenceFastaFile)
    
    def realignSamFile(self):
        """Chains and then realigns the resulting global alignments.
        """
        tempSamFile = os.path.join(self.getGlobalTempDir(), "temp.sam")
        system("cp %s %s" % (self.outputSamFile, tempSamFile))
        self.addChildTargetFn(realignSamFileTargetFn, args=(tempSamFile, self.outputSamFile, 
                                                            self.readFastqFile, self.referenceFastaFile, self.options))
