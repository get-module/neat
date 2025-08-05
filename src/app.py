# entrypoint file
import sys
from utils import colors as colors
from cmd.GenerateLicense.GenerateLicense import GenerateLicense
import importlib

# --- instantiating all global classes --- #
color = colors.colorize()
# ---                                  --- #

def call_function_by_name(name: str, params):
    # Build module path, e.g., 'cmd.a.a'
    module_path = f"cmd.{name}.{name}"

    try:
        # Import the module
        mod = importlib.import_module(module_path)

        # Get the function from the module
        func = getattr(mod, name)

        # Call the function
        return func(params)
    except (ImportError, AttributeError) as e:
        print(f"Error calling '{name}': {e}")
        return None

if __name__ ==  "__main__":
    if len(sys.argv) > 1:  # ensures it's not just a dud call
        call_function_by_name(sys.argv[1], sys.argv[2:])