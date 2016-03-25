#!/bin/bash
#
# aligns XP12_lambda.fa reference with XP12_unMC_lambda_reads.fasta generated
# from poretools using marginAlign

# run marginAlign
bash ../marginAlign/marginAlign /Users/farrell/mnt/basecalled_lambda_reads_20150715/downloads/lambda_20150714_reads.fastq XP12_unMC_lambda.fa lambda_20150714_marginAlign.sam --jobTree ./jobTree 2> lambda_20150714_marginAlign_err.txt

# convert sam to bam
samtools view -bt XP12_unMC_lambda.fa.fai lambda_20150714_marginAlign.sam > lambda_20150714_marginAlign.bam

# sort
samtools sort lambda_20150714_marginAlign.bam lambda_20150714_marginAlign.sorted

# index
samtools index lambda_20150714_marginAlign.sorted.bam

# print samtools stats
samtools flagstat lambda_20150714_marginAlign.sorted.bam

# create sam with proper header
samtools view -bt XP12_unMC_lambda.fa.fai lambda_20150714_marginAlign.sam > lambda_20150714_marginAlign_hdr.sam'

# get alignment stats
bash ../tools/marginAlign/marginStats lambda_20150714_marginAlign_hdr.sam /Users/farrell/mnt/basecalled_lambda_reads_20150715/downloads/lambda_20150714_reads.fastq XP12_unMC_lambda.fa --printAlignmentData --includeUnaligned > marginAlign_stats.txt
