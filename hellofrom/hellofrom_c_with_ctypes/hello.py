from pathlib import Path
import sysconfig
import ctypes

# We need a bit of gymnastics to retrive the shared 
# library path
thisfolder = Path(__file__).parent.absolute()
suffix = sysconfig.get_config_var('EXT_SUFFIX')

# Load compiled shared library
hc = ctypes.CDLL(thisfolder.joinpath(
    'hellofcctyp' + suffix))
