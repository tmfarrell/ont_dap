#!/usr/bin/env bash
# 
# runs useful poretools functions on base-called ONT data (i.e. after Metrichor)
# 

if [[ $1 == "-h" ]]; then 
    echo ""
    echo -e "Usage:\t\$ ./run_poretools.sh path/to/metrichor/downloads/ [output_dir]\n" 
    echo "If output_dir not specified, saves results to <path/to/metrichor/downloads>."
    echo ""
    exit
fi

if [[ -d $2 ]]; then 
    output_dir=$2
else 
    output_dir=$1
fi

poretools=poretools/poretools/poretools_main.py

echo "Running poretools stats..."
(python $poretools stats $1) > $output_dir/stats.txt

echo "Getting fastq..."
(python $poretools fastq $1) > $output_dir/sequence.fastq

echo "Generating read yield and histogram plots..."
python $poretools yield_plot --plot-type basepairs --saveas $output_dir/yield.png $1
python $poretools hist --saveas $output_dir/hist.png $1

echo "Done."

#eof