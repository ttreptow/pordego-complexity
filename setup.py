from setuptools import setup, find_packages

ANALYSIS_PLUGINS = [
    "complexity = pordego_complexity.complexity_analysis:analyze_complexity"
]

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7"
]


setup(name="pordego-complexity",
      version="1.0.0",
      author="Tim Treptow",
      author_email="tim.treptow@gmail.com",
      description="Pordego plugin for code complexity analysis using the Radon library",
      packages=find_packages(),
      url="https://github.com/ttreptow/pordego-complexity",
      download_url="https://github.com/ttreptow/pordego-complexity/tarball/1.0.0",
      entry_points={"pordego.analysis": ANALYSIS_PLUGINS},
      classifiers=CLASSIFIERS,
      install_requires=["radon"]
      )
