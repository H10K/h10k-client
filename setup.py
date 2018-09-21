import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="h10k-client",
    version="0.0.1",
    author="League of Crafty Programmers Ltd",
    author_email="info@locp.co.uk",
    description="H10K Client Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h10k/h10k-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
