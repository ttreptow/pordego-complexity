from setuptools import setup, find_packages

ANALYSIS_PLUGINS = [
    "complexity = pordego_complexity.complexity_analysis:analyze_complexity"
]

with open('LICENSE') as f:
    LICENSE = f.read()

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7"
]

VERSION = "1.0.3"

setup(name="pordego-complexity",
      version=VERSION,
      license=LICENSE,
      author="Tim Treptow",
      author_email="tim.treptow@gmail.com",
      description="Pordego plugin for code complexity analysis using the Radon library",
      packages=find_packages(exclude=('tests', 'docs', "tests.*")),
      url="https://github.com/ttreptow/pordego-complexity",
      download_url="https://github.com/ttreptow/pordego-complexity/tarball/{}".format(VERSION),
      entry_points={"pordego.analysis": ANALYSIS_PLUGINS},
      classifiers=CLASSIFIERS,
      install_requires=["radon==2.0.0"]
      )
