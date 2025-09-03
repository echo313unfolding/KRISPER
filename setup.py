#!/usr/bin/env python3
"""
Setup configuration for KRISPER + Bio_Poetica
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="krisper-biopoetica",
    version="0.2.0",
    author="Echo Labs",
    author_email="echo313unfolding@gmail.com",
    description="Natural language programming through plain English and executable poetry",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/echo313unfolding/krisper",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Compilers", 
        "Topic :: Software Development :: Interpreters",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "krisper=krisper:main",
            "bio-poetica=bio_poetica:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/echo313unfolding/krisper/issues",
        "Source": "https://github.com/echo313unfolding/krisper",
    },
    keywords=[
        "natural-language-programming",
        "compiler", 
        "transpiler",
        "poetry",
        "natural-language",
        "bio-computing",
        "nlp",
        "code-generation",
        "dsl",
        "domain-specific-language"
    ],
)