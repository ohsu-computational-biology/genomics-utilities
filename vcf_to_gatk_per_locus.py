#!/usr/bin/env python

### Convert a VCF in to the per locus output usually seen in GATK's DepthOfCoverage.
### USAGE: python vcf_to_gatk_per_locus.py <vcf input> <GATK per locus output>
### Requires PyVCF and natsort.
### John Letaw 02/03/16

import sys
import vcf
from natsort import natsorted

# vcf.Reader object returns:
# Record(CHROM=12, POS=112186211, REF=T, ALT=[C])

# GATK per locus output looks like:
# Locus\tTotal_Depth\tAverage_Depth_sample\tDepth_for___at__NS500390:64:H7NFVAFXX:1
# 1:65509\t0\t0.00\t0

def writeFakeDoc(chrom, coord):
    return (str(chrom) + ':' + str(coord) + '\t100\t100.00\t100\n')

def main():

    per_locus_out = open(sys.argv[2], 'w')

    per_locus_out.write("Locus\tTotal_Depth\tAverage_Depth_whatever\tDepth_for_whatever\n")
    for record in natsorted(vcf.Reader(open(sys.argv[1], 'rU')), key=lambda entry: (entry.CHROM, entry.POS)):
        per_locus_out.write(writeFakeDoc(record.CHROM, record.POS))

    ### These should be hard-coded to the file, as SeattleSeq writeGenotypes will not run if you don't add them.
    per_locus_out.write(writeFakeDoc("7", "6026775"))
    per_locus_out.write(writeFakeDoc("13", "32929387"))
    per_locus_out.write(writeFakeDoc("1", "169519049"))
    per_locus_out.write(writeFakeDoc("14", "75513883"))

    per_locus_out.close()

if __name__ == "__main__":
    main()
