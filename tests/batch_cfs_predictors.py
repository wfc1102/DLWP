#
# Copyright (c) 2017-18 Jonathan Weyn <jweyn@uw.edu>
#
# See the file LICENSE for your rights.
#

"""
Test conversion of CFS data into preprocessed predictors/targets for the DLWP model.
"""

from DLWP.data import CFSReanalysis
from DLWP.model import Preprocessor
from datetime import datetime
import pandas as pd

start_date = datetime(2000, 1, 1)
end_date = datetime(2009, 12, 31)
dates = list(pd.date_range(start_date, end_date, freq='D').to_pydatetime())
variables = ['HGT']
levels = [500]
data_root = '/home/disk/wave2/jweyn/Data'

cfs = CFSReanalysis(root_directory='%s/CFSR' % data_root, file_id='dlwp_')
cfs.set_dates(dates)
cfs.open(autoclose=True)
cfs.Dataset = cfs.Dataset.isel(lat=(cfs.Dataset.lat >= 0.0))

pp = Preprocessor(cfs, predictor_file='%s/DLWP/cfs_2000-2009_hgt_500_NH.nc' % data_root)
pp.data_to_samples(batch_samples=500, variables=variables, levels=levels, scale_variables=True,
                   overwrite=False, verbose=True)
print(pp.data)
pp.close()