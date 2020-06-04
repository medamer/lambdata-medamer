# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdatamedamer", # the name that you will install via pip
    version="1.2",
    author="mohamed edamer",
    author_email="edamer.mo@gmail.com",
    description="not now, just testing",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/medamer/lambdata-medamer",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)