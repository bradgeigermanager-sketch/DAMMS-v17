"""Setup script for DAMMS Unified System"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="damms-unified",
    version="17.0.0",
    author="bradgeigermanager-sketch",
    description="Distributed Agentic Multi-Model System - Unified Architecture",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bradgeigermanager-sketch/DAMMS-v17",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=1.9.0",
        "aiofiles>=0.8.0",
        "aiohttp>=3.8.0",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
    ],
)
