from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="greek-normalisation",
    version="0.4",
    description="Python 3 utilities for validating and normalising Ancient Greek text",
    url="http://github.com/jtauber/greek-normalisation",
    author="James Tauber",
    author_email="jtauber@jtauber.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["greek_normalisation"],
    entry_points={
        "console_scripts": [
            "to2019 = greek_normalisation.convert_files:to_2019",
            "toNFC = greek_normalisation.convert_files:to_nfc",
            "toNFD = greek_normalisation.convert_files:to_nfd",
        ],
    },
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Text Processing :: Linguistic",
    ],
)
