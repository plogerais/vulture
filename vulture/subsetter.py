import os
import tempfile

#from cdo import Cdo
#
#from c4cds.util import cordex_country_drs_filename

import xarray as xr

COUNTRY_BBOX = {
    # bbox: min_lon, max_lon, min_lat, max_lat
    # values taken from: https://data.humdata.org/dataset/bounding-boxes-for-countries
    'Egypt': '13,37,5,50.861',
    'UK': '-13.683,3.858,48.5,64.067',
    'France': '-5.225,9.55,41.333,51.2',
    'Germany': '5.867,15.033,45.967,55.133',
}


class Subsetter(object):
    def __init__(self, output_dir=None):
        self.output_dir = output_dir or '/tmp/out'
        if not os.path.isdir(self.output_dir):
            os.makedirs(self.output_dir)

    def subset_by_country(self, dataset, country):
        if country not in COUNTRY_BBOX:
            raise Exception("Unknown country: {}".format(country))
        bbox = COUNTRY_BBOX[country]
	list_lon_lat = [float(i) for i in bbox.split(',')] # min_lon, max_lon, min_lat, max_lat
#        outfile = os.path.join(
#            self.output_dir,
#            cordex_country_drs_filename(dataset, country))
#        cdo = Cdo()
#        cdo.sellonlatbox(bbox, input=dataset, output=outfile)

	# Nous avons un dataset, donc il suffit d’appeler xarray.
	subset_data = dataset[variable] # exemple de valeur de variable : 'tas'
	subset_data = subset_data.sel(lat=slice(list_lon_lat[2], list_lon_lat[3], lon=list_lon_lat[0], list_lon_lat[1]))
	out_filename = country + "_" + model + "_" + experiment + "_" + variable + "_" + year
	outfile = os.path.join(self.output_dir, out_filename)

	subset_data.to_netcdf(outfile)

        return outfile
