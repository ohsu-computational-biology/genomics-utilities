#!/bin/env python

### Convert BED formatted file to GATK interval format (chrom:start-stop).
### John Letaw 01/19/15
### USAGE: python bed_to_gatk_intervals.py <bedfile> <output interval file>
### https://www.broadinstitute.org/gatk/guide/article?id=1204

import sys

bedfile = open(sys.argv[1], 'rU')
interval_out = open(sys.argv[2], 'w')

print("WARNING: BED Files are 0-based in the START position, while GATK INTERVAL files are 1-based.")
print("Please be sure your BED file was properly formatted, or else you will be off by one position for each interval!")

with bedfile as bed:
    for coords in bed:
        coords = coords.rstrip('\n').split('\t')
        chrom = coords[0]
        start = int(coords[1]) + 1
        stop = int(coords[2])
        interval_out.write(chrom + ':' + str(start) + '-' + str(stop) + '\n')

interval_out.close()
