import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="PyPanda",
    version="0.0.1",
    author="Om3gaOfficial",
    description="PyPanda is an easy to use Python 3 based library providing simple and easy access to the API of Bitpanda and Bitpanda Pro.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Om3gaOfficial/PyPanda",
    project_urls={
        "Bug Tracker": "https://github.com/Om3gaOfficial/PyPanda/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
