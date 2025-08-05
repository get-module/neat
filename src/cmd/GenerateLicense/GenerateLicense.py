import utils.colors as colors
import requests
import os

color = colors.colorize()

def get_licenses() -> object:
    try:
        response = requests.get("https://api.github.com/licenses")  # public API, rate limited at 60 / min
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print(color.red("Connection error. Make sure you have internet connection."))
    except requests.exceptions.Timeout:
        print(color.red("Timeout error. Make sure you have internet connection."))
    except requests.exceptions.HTTPError as e:
        print(color.red("HTTP error. Most likely an internal error, please report the following trace and commands you entered:\n" + color.yellow(str(e))))
    except Exception as e:
        print("Unexpected internal error occurred, please report the following trace and commands you entered:\n" + color.yellow(str(e)))

def create_license(selected_license, authors, year) -> str:
    try:
        response = requests.get(f"https://api.github.com/licenses/{selected_license}")  # public API, rate limited at 60 / min
        response.raise_for_status()
        data = str(response.json()["body"])  # {body: the license itself}
        return data.replace("<year>", str(year)).replace("<name of author>", authors).replace('[year]', year).replace('[fullname]', authors)
    except requests.exceptions.ConnectionError:
        print(color.red("Connection error. Make sure you have internet connection."))
    except requests.exceptions.Timeout:
        print(color.red("Timeout error. Make sure you have internet connection."))
    except requests.exceptions.HTTPError as e:
        print(color.red("HTTP error. Most likely an internal error, please report the following trace and commands you entered:\n" + color.yellow(str(e))))
    except Exception as e:
        print("Unexpected internal error occurred, please report the following trace and commands you entered:\n" + color.yellow(str(e)))

def write_license(license: str, path="./") -> str:
    try:
        with open(os.path.join(path, "LICENSE.txt"), "w") as f:
            f.write(license)
    except Exception as e:
        print(color.red("An error occurred while trying to write LICENSE.txt to disk: " + str(e)))

def GenerateLicense(*args):
    args = list(args) # escape tuple
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = list(args[0])  # Support tuple/list unpacking

    licenses = get_licenses()
    if not licenses:
        return

    authors, year, selected_license, output_path = "", "", "", None
    licenses = get_licenses()
    if type(licenses) != list: return -1

    if not args:  # if there's no flags
        selected_license = input(color.yellow("Select license (rerun cmd with -help for a full list of available licenses): "))
        authors = input(color.yellow("Authors: "))
        year = input(color.yellow("Year: "))
    if len(args) == 1:
        if args[0] == "-help":
            print(
                color.purple("Neat CLI command GenerateLicense help: \n") +
                color.blue("arg[0]: license name\n") +
                color.blue("arg[1]: Authors\n") +
                color.blue("arg[2]: Year\n\n") +
                color.yellow("Available Licenses: \n") +
                color.red("IMPORTANT: use the key that's in the parentheses when calling\n") +
                color.cyan("- ".join(f"{d['name']} ({d['key']})\n" for d in licenses))
        )
            return
    if len(args) == 3 or len(args) == 4:
        selected_license = args[0]
        authors = args[1]
        year = args[2]

        if len(args) == 4: output_path = args[3]

    # quick validation
    if not selected_license or not authors or not year:  # if blanks
        raise ValueError("Insufficient arguments provided. Expected <license> <authors> <year> <optional: output_path>")
    if not any(selected_license in d.values() for d in licenses):  # makes sure the license exists
        raise ValueError("Invalid license type -help for a full list of available licenses")

    data = create_license(selected_license, authors, year)
    if output_path: write_license(data, output_path)
    else: write_license(data)