import sys
import subprocess
from os.path import join

out = subprocess.check_output([join(sys.prefix, 'NSIS', 'makensis.exe'),
                               '/VERSION']).decode('ascii')
assert out.strip() == 'v3.01', out
