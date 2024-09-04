__author__ = "Marc Horlacher"
__copyright__ = "Copyright 2024, Marc Horlacher"
__email__ = "marc.horlacher@gmail.com"
__license__ = "MIT"


import argparse

if 'snakemake' not in globals():
    # Run from CLI for local testing
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str)
    parser.add_argument("-o", "--output", type=str)
    args = parser.parse_args()

    IN_FASTA = args.input
    OUT_FASTA = args.output

else:
    # If we are running as a snakemake rule, skip the CLI parsing
    IN_FASTA = snakemake.input.fasta
    OUT_FASTA = snakemake.output.fasta

# ---
import tqdm
from Bio import SeqIO

with open(OUT_FASTA, 'w') as out_fa:
    for record in tqdm.tqdm(SeqIO.parse(IN_FASTA, 'fasta')):
        print(f'>{record.id}', file=out_fa)
        print(record.seq.translate(), file=out_fa)