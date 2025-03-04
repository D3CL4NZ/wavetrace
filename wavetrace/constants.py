import os
from pathlib import Path


PROJECT_ROOT = Path(os.path.abspath(os.path.join(
  os.path.dirname(__file__), '../')))
SECRETS_PATH = PROJECT_ROOT/'secrets.json'

#: SRTM tiles that cover the East Coast Tri-State Area
SRTM_EC_TILE_IDS = [
  'N38W075',
  'N38W076',
  'N38W077',
  'N39W075',
  'N39W076',
  'N39W077',
  'N40W075',
  'N40W076',
  'N40W077',
  ]

#: Transmitter CSV files must have these header columns
REQUIRED_TRANSMITTER_FIELDS = [
  'network_name',    
  'site_name',
  'latitude', # WGS84 float
  'longitude', # WGS84 float 
  'antenna_height', # meters
  'polarization', # 0 (horizontal) or 1 (vertical)
  'frequency', # megaherz
  'power_eirp', # watts
  ]

#: SPLAT! Earth dielectric constant.
#: According to the SPLAT! documentation, typical Earth dielectric constants and conductivities are: 
#: Salt water, 80, 5.000;
#: Good ground, 25, 0.020;
#: Fresh water, 80, 0.010;
#: Marshy land, 12, 0.007;
#: Farmland or forest, 15, 0.005;
#: Average ground, 15, 0.005;
#: Mountain or sand, 13, 0.002;
#: City, 5, 0.001;
#: Poor ground, 4, 0.001;
EARTH_DIELECTRIC_CONSTANT = 15

#: SPLAT! Earth earth_conductivity in Siemens per meter
EARTH_CONDUCTIVITY = 0.005

#: SPLAT! radio climate codes.
#: 1=Equatorial (Congo);
#: 2=Continental Subtropical (Sudan);
#: 3=Maritime Subtropical (West coast of Africa);
#: 4=Desert (Sahara);
#: 5=Continental Temperate;
#: 6=Maritime Temperate, over land (UK and west coasts of US & EU);
#: 7=Maritime Temperate, over sea
RADIO_CLIMATE = 5

#: SPLAT! time variability parameter
FRACTION_OF_TIME = 0.5

#: SPLAT! location variability parameter
FRACTION_OF_SITUATIONS = 0.5

#: SPLAT receiver sensitivity parameter in decibel-milliwatts (dBm). 
#: For example, minimum received signal power of wireless networks (802.11 variants) is -100 dBm.
RECEIVER_SENSITIVITY = -110 
#: WGS84 semimajor axis in meters
WGS84_A = 6378137
#: WGS84 flattening 
WGS84_F = 1/298.257223563
#: WGS84 eccentricity squared (e^2)
WGS84_E2 = 2*WGS84_F - WGS84_F**2
#: Distance in meters of a geostationary satellite from the center of the Earth (and hence the center of the WGS84 ellipsoid);
#: taken from the Wikipedia article `Geostationary orbit <https://en.wikipedia.org/wiki/Geostationary_orbit>`_
R_S = 42164000
#: Distance in meters of a geostationary satellite from the WGS84 ellipsoid
H_S = R_S - WGS84_A
