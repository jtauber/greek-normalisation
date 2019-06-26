from setuptools import setup

setup(
    name="greek-normalisation",
    version="0.0",
    description="Python 3 utilities for validating and normalising Ancient Greek text",
    url="http://github.com/jtauber/greek-normalisation",
    author="James Tauber",
    author_email="jtauber@jtauber.com",
    license="MIT",
    packages=["greek_normalisation"],
    zip_safe=False,
    classifiers=[
        # "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Text Processing :: Linguistic",
    ],
)
