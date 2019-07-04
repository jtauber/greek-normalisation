from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="greek-normalisation",
    version="0.1",
    description="Python 3 utilities for validating and normalising Ancient Greek text",
    url="http://github.com/jtauber/greek-normalisation",
    author="James Tauber",
    author_email="jtauber@jtauber.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["greek_normalisation"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing :: Linguistic",
    ],
)
