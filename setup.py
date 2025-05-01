from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    """
    Reads requirements.txt file
    returns list of packages
    """
    with open(file_path,'r') as requirements_file:
        packages = requirements_file.readlines()

    packages = [ package.strip() for package in packages if '-e' not in package]

    return packages

setup(
    name="mlproject",
    version='0.0.1',
    author='hillul',
    author_email='hillulchutia@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)