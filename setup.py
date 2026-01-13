from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="TV-Shows-AI-Recommender",
    version="0.1.0",
    author="DaniReagan",
    packages=find_packages(),
    install_requires=requirements,
)
