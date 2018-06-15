# this is to read the quasar catalog
from astroquery.sdss import SDSS
import numpy as np
from astropy.table import Table
def readquasarcatalog():

	quasars = Table.read('/data/DR14Q_v4_4.fits')
	return quasars

def getspectrum(plate, fiber, mjd):
	hdulist=SDSS.get_spectra(plate=plate, fiberID=fiber, mjd=mjd)[0]
	spectrum=hdulist[1].data
	return spectrum



quasars = readquasarcatalog()
print(quasars)
#spec = getspectrum(7666, 121, 57339)
#print(Table(spec))