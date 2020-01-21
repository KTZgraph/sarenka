from setuptools import setup, find_packages

"""
Solving problem with imports from parent directory
https://stackoverflow.com/questions/6323860/sibling-package-imports
cd sarenka/backend
pip install -e .
"""

setup(name='sarenka', version='0.0', packages=find_packages())
