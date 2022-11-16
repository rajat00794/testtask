from setuptools import setup
import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cobraframework",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)
# setup(
#     name="test",
#     version="1.0",
#     description="Candidate Module",
#     author="Rajat Mishra",
#     author_email="rajatm@capitalnumbers.com",
#     url="https://www.python.org/sigs/distutils-sig/",
#     install_requires=["pinject", "odmantic", "bson", "pymongo[srv]"],
# )
