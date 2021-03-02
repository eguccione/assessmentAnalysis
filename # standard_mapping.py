# standard_mapping
# stolen from https://miro.com/app/board/o9J_lW8A4QU=/ by @vickytnz
# Digital by default Service Standard to Digital Service Standard

import pandas as pd

DbyDSS_to_DSS = {
    'DbyDSS': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
    'DSS':  [1, 3, 7, 7, 6, 17, 5, 12, 14, 14, 14, 14, 13, 5,
             8, 9, 10, 15, 5, 2, 16, 16, 16, 14, 10, 18]}

DSS_to_SS = {
    'DSS': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    'SS': [1, 1, 6, 7, 8, 11, 9, 12, 13, 14, 14, 5, 4, 3, 10, 10, 10, 'na']}

DSS_to_SS_df = pd.DataFrame(DSS_to_SS)
DSS_to_SS_df.to_csv('DSS_to_SS_df.csv')

DbyDSS_to_DSS = pd.DataFrame(DbyDSS_to_DSS)
DbyDSS_to_DSS.to_csv('DbyDSS_to_DSS.csv')
