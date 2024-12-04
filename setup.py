from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Read and parse requirements from a file."""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Removes newline and extra spaces
    return requirements

setup(
    name='Fault Detection',
    version='0.0.1',
    author='Kshitij',
    author_mail='vkvteej@gmail.com',
    install_requirements=get_requirements('requirements.txt'),  # Fixed keyword
    packages=find_packages()
)