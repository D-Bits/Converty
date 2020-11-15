from setuptools import setup
import pathlib


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="converty",
    version="1.0.0",
    description="A library for unit conversions.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Dana Lockwood",
    author_email="lockwood.da88@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9.0",
    ],
    packages=["reader"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)
