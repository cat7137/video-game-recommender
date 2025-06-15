from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR = 'Cody Thompson'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR,
    author_email = 'cat7137@rit.edu',
    description = 'A small package for a video game recommender',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = [SRC_REPO],
    python_requires = '>= 3.13',
    install_requires = LIST_OF_REQUIREMENTS,
)