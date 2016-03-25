#!/usr/bin/env bash
#
# aligns fastq generated by poretools; then computes stats on that alignment 
# 

if [[ $1 == "-h" ]]; then 
    echo ""
    echo -e "Usage:\t\$ ./run_alignment.sh sequence.fastq reference.fasta [output_dir]\n" 
    echo "If output_dir not specified, saves results to <path/to/metrichor/downloads/>."
    echo ""
    exit
fi 
    
fastq=$1
reference=$2
if [[ -d $4 ]]; then 
    output_dir=$4
else 
    output_dir=$1 
fi 

# get marginAlign dir
mA="marginAlign"
mA_bin=$(which $mA)
mA_dir=${mA_bin:0: ${#mA_bin}-${#mA}}

# run marginAlign
marginAlign $fastq $reference $output_dir/alignment.sam --jobTree $mA_dir/jobTree 2> $output_dir/align_err.txt

# create index for reference
samtools faidx $reference

# convert sam to bam
samtools view -bt $reference.fai $output_dir/alignment.sam > $output_dir/alignment.bam

# sort
samtools sort $output_dir/alignment.bam $output_dir/alignment.sorted

# index
samtools index $output_dir/alignment.sorted.bam

# print samtools stats
samtools flagstat $output_dir/alignment.sorted.bam

# create sam with proper header
samtools view -bt $reference.fai $output_dir/alignment.sam > $output_dir/alignment_hdr.sam

# get alignment stats
marginStats $output_dir/alignment_hdr.sam $fastq $reference --printAlignmentData --includeUnaligned > $output_dir/alignment_stats.txt
