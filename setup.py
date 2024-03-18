from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str):
    """
    Retrieve a list of required libraries specified in a requirements.txt file.

    Args:
        file_path (str): The file path to the requirements.txt file.

    Returns:
        List[str]: A list of required libraries.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
    """

    try:
        requirements = []

        with open(file_path) as f:
            requirements = f.readlines()

            requirements = [req.replace("\n"," ") for req in requirements]

        return requirements

    except:
        raise "FileNotFoundError"

setup(
    name = 'Book Price Predictor',
    version='0.0.1',
    author='Gaurav',
    author_email='gauravy1905@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
