class Colors:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    RESET = '\033[0m'


class colorize:
    # creates a colored piece of text
    def __init__(self):
        self.colors = {
            # converting the all uppercase values of the Colors items to lowercase
            # excluding any sort of metadata (e.g. __doc__ or __module__)
            name.lower(): value for name, value in Colors.__dict__.items() if not name.startswith('_')
        }

    def __getattr__(self, name: str) -> str or None:
        # dynamic way of accessing colors :)
        color_code = self.colors.get(name.lower())

        if color_code:  # set color and reset at the end of the string
            return lambda text: f"{color_code}{text}{Colors.RESET}"

        # if no valid color raise err
        raise AttributeError(f"No valid color '{name}'")

    def colorize(self, text: str, color: str) -> str:
        # colorize the string using the argument instead of the attribute
        # intended for easier variable color creation
        return self.__getattr__(color)(text)