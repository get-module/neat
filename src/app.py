# entrypoint file
import sys
from utils import colors as colors
from cmd.GenerateLicense.GenerateLicense import GenerateLicense

# --- instantiating all global classes --- #
color = colors.colorize()
# ---                                  --- #


if __name__ ==  "__main__":
    if len(sys.argv) > 1:  # ensures it's not just a dud call
        if sys.argv[1] == "GenerateLicense":
            GenerateLicense(sys.argv[2:])