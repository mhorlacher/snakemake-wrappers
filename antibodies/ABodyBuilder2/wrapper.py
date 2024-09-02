__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"


# ---
from pathlib import Path

import tqdm
from ImmuneBuilder import ABodyBuilder2

predictor = ABodyBuilder2()

with open(snakemake.input[0]) as f:
    for i, line in tqdm.tqdm(enumerate(f), desc="Predicting", unit="seq"):
        vh, vl = line.strip().split(",")
        predictor.predict(vh, vl).save(Path(snakemake.output[0]) / f"i.pdb")
