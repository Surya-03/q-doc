import os
import sys
import subprocess

def install_requirements(requirements_file):
    with open(requirements_file, 'r') as f:
        packages = f.read().splitlines()

    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}, skipping...")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <requirements_file>")
        sys.exit(1)

    requirements_file = sys.argv[1]
    if not os.path.isfile(requirements_file):
        print(f"File '{requirements_file}' does not exist.")
        sys.exit(1)

    install_requirements(requirements_file)