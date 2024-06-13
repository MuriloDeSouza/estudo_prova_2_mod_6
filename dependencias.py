import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Lista de pacotes para instalar
packages = [
    "wandb",
    "matplotlib",
    "tensorflow",
    "scikit-learn"
]

for package in packages:
    install(package)
