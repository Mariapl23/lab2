from pathlib import Path
import os
import pandas as pd

# MARIA = '/Users/mariapuig/PycharmProjects/Laboratory1/data' #CAMBIAR!
# MIREIA = '/Users/mireiabragulat/Desktop/DM/lab2'

# Direcció del database
root = Path('/Users/mireiabragulat/Desktop/DM/lab2/Data')

path = os.path.join(root, 'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct')
doc = pd.read_csv(path, skiprows=[0, 1], delimiter='\t')

header = doc.columns

H = []
for variable in header:
    H.append(variable.lower())