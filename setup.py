from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    hyphen_e_dot = '-e .'
    requirements = []
    with open(file_path) as f:
        requirements = [st.strip() for st in f.readlines()]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Bharat',
    author_email='bharatpendyala3@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
