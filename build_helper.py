import platform
import sys

WINDOWS = sys.platform == 'win32'

if WINDOWS:
    BUILD_PREFIX = f'build_{platform.machine()}_{platform.python_version()}'
else:
    BUILD_PREFIX = 'build'

