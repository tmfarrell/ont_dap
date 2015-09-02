import os
import sys
from optparse import OptionParser
from jobTree.src.bioio import logger, setLoggingFromOptions, addLoggingOptions
from margin.utils import ReadAlignmentStats
import numpy

"""Simple script to calculate alignment statistics from a SAM file.
"""

def main():
    #Parse the inputs args/options
    parser = OptionParser(usage="usage: samFile, readFastqFile, referenceFastaFile [options]",
                          version="%prog 0.1")

    #Options
    parser.add_option("--identity", dest="identity",
                      help="Print identity of alignments",
                      default=False, action="store_true")

    parser.add_option("--readCoverage", dest="readCoverage",
                      help="Print read coverage of alignments",
                      default=False, action="store_true")

    parser.add_option("--mismatchesPerAlignedBase", dest="mismatchesPerAlignedBase",
                      help="Print mismatches per aligned base",
                      default=False, action="store_true")

    parser.add_option("--deletionsPerReadBase", dest="deletionsPerReadBase",
                      help="Print deletions per base of alignments",
                      default=False, action="store_true")

    parser.add_option("--insertionsPerReadBase", dest="insertionsPerReadBase",
                      help="Print insertions per base of alignments",
                      default=False, action="store_true")

    parser.add_option("--localAlignment", dest="localAlignment",
                      help="Ignore unaligned prefix and suffix of each read in making calculation",
                      default=False, action="store_true")

    parser.add_option("--printValuePerReadAlignment", dest="printValuePerReadAlignment",
                      help="Prints the value of statistics for each read alignment",
                      default=False, action="store_true")

    parser.add_option("--noStats", dest="noStats",
                      help="Do not print stats (avg, median, min, max, mode) of desired statistic",
                      default=False, action="store_true")

    parser.add_option("--printAlignmentData", dest="printAlignmentData",
                      help="Print all stats for each read alignment in tabular format; include unaligned with --includeUnaligned",
                      default=False, action="store_true")

    parser.add_option("--includeUnaligned", dest="includeUnaligned",
                      help="Includes unaligned reads when printing alignment data",
                      default=False, action="store_true")

    addLoggingOptions(parser)

    #Parse the options/arguments
    options, args = parser.parse_args()

    #Setup logging
    setLoggingFromOptions(options)

    #Print help message if no input
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    #Exit if the arguments are not what we expect
    if len(args) != 3:
        raise RuntimeError("Expected three arguments, got: %s" % " ".join(args))

    #Now do the stats calculation
    samFile, readFastqFile, referenceFastaFile = args

    readAlignmentStats = ReadAlignmentStats.getReadAlignmentStats(samFile, readFastqFile,
                                             referenceFastaFile, globalAlignment=not options.localAlignment,
                                             includeUnaligned=options.includeUnaligned)

    def report(values, statisticName):
        if not options.noStats:
            print "Average" + statisticName, numpy.average(values)
            print "Median" + statisticName, numpy.median(values)
            print "Min" + statisticName, min(values)
            print "Max" + statisticName, max(values)
        if options.printValuePerReadAlignment:
            print "Values" + statisticName, "\t".join(map(str, values))


    def report_alignment_data():
        name = map(lambda rAS: rAS.readName(), readAlignmentStats)
        ref_id = map(lambda rAS: rAS.referenceID(), readAlignmentStats)
        read_type = map(lambda rAS: rAS.readType(), readAlignmentStats)
        length = map(lambda rAS: rAS.readLength(), readAlignmentStats)
        identity = map(lambda rAS: rAS.identity(), readAlignmentStats)
        read_coverage = map(lambda rAS: rAS.readCoverage(), readAlignmentStats)
        ref_coverage = map(lambda rAS: rAS.referenceCoverage(), readAlignmentStats)
        mismatch = map(lambda rAS: rAS.mismatchesPerAlignedBase(), readAlignmentStats)
        insertion = map(lambda rAS: rAS.insertionsPerReadBase(), readAlignmentStats)
        deletion = map(lambda rAS: rAS.deletionsPerReadBase(), readAlignmentStats)
        mean_quality = map(lambda rAS: rAS.readMeanQuality(), readAlignmentStats)
        aligned = map(lambda rAS: rAS.isAligned(), readAlignmentStats)
        aligned_length = map(lambda rAS: rAS.alignedReadLength(), readAlignmentStats)
        ref_c_content = map(lambda rAS: rAS.getRefCContent(), readAlignmentStats)
        ref_gc_content = map(lambda rAS: rAS.getRefGcContent(), readAlignmentStats)

        print "\t".join(["Name", "ReferenceID", "ReadType", "Length", "Aligned", \
                        "AlignedLength", "Identity", "ReadCoverage", \
                        "ReferenceCoverage", "MismatchPerBase", \
                        "InsertionPerBase", "DeletionPerBase", "MeanQuality",
                        "RefCContent", "RefGcContent"])

        for read in zip(name, ref_id, read_type, length, aligned, aligned_length, \
                        identity, read_coverage, ref_coverage, mismatch, insertion,\
                        deletion, mean_quality, ref_c_content, ref_gc_content):
            print "\t".join(map(str, read))


    if options.printAlignmentData:
        report_alignment_data()

    else:
        if options.identity:
            report(map(lambda rAS : rAS.identity(), readAlignmentStats), "Identity")

        if options.readCoverage:
            report(map(lambda rAS : rAS.readCoverage(), readAlignmentStats), "ReadCoverage")

        if options.mismatchesPerAlignedBase:
            report(map(lambda rAS : rAS.mismatchesPerAlignedBase(), readAlignmentStats), "MismatchesPerAlignedBase")

        if options.deletionsPerReadBase:
            report(map(lambda rAS : rAS.deletionsPerReadBase(), readAlignmentStats), "DeletionsPerReadBase")

        if options.insertionsPerReadBase:
            report(map(lambda rAS : rAS.insertionsPerReadBase(), readAlignmentStats), "InsertionsPerReadBase")

if __name__ == '__main__':
    main()
