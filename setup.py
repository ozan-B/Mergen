import subprocess

libraries = [
    "requests",
    "colorama",
    "tqdm",
    "argparse",
    "threading",
    "datetime",
    "os",
    "socket",
    "phonenumbers",
    "builtwith",
    "selenium",
    "bs4",
    "prettytable"
]

def install_libraries():
    installed_libraries = []
    for lib in libraries:
        try:
            __import__(lib)
            print(f"{lib} already installed.")
            installed_libraries.append(lib)
        except ImportError:
            print(f"{lib} not installed. Installing...")
            subprocess.call(['pip', 'install', lib])
            installed_libraries.append(lib)
    return installed_libraries

if __name__ == "__main__":
    installed = install_libraries()
    print("\nInstalled libraries:", installed)
