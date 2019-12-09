import os

from pywps import Process
from pywps import LiteralInput
from pywps import ComplexOutput
from pywps import FORMATS, Format
from pywps import configuration
from pywps.app.Common import Metadata


from vulture.subsetter import Subsetter
from vulture.plotter import Plotter
from vulture.search import Search
from vulture.ncdump import ncdump
from vulture import util

class CmipSubsetter(Process):
	def __init__(self):
		
