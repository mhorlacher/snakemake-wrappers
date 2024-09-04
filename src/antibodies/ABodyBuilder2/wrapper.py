__author__ = "Marc Horlacher"
__copyright__ = "Copyright 2024, Marc Horlacher"
__email__ = "marc.horlacher@gmail.com"
__license__ = "MIT"


import argparse
from pathlib import Path

import tqdm
from ImmuneBuilder import ABodyBuilder2


if 'snakemake' not in globals():
    # Run from CLI for local testing
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=str, help="Input CSV file")
    parser.add_argument("-o", "--output-dir", type=str, help="Output directory")
    args = parser.parse_args()

    INPUT_CSV = args.input_csv
    OUTPUT_DIR = args.output_dir
else:
    # If we are running as a snakemake rule, skip the CLI parsing
    INPUT_CSV = snakemake.input[0]
    OUTPUT_DIR = snakemake.output[0]
Path(OUTPUT_DIR).mkdir(exist_ok=True)



predictor = ABodyBuilder2()
with open(INPUT_CSV) as f:
    for i, line in tqdm.tqdm(enumerate(f), desc="Predicting", unit="seq"):
        vh, vl = line.strip().split(",")
        structure = predictor.predict({'H': vh, 'L': vl})
        structure.save(str(Path(OUTPUT_DIR) / f"{i}.pdb"))
