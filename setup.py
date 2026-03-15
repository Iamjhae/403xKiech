from setuptools import setup, find_packages

setup(
    name="403x",
    version="1.0",
    author="Arookiech",
    description="Pro 403 Bypass Scanner for Bug Bounty",
    packages=find_packages(),
    install_requires=[
        "requests",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "403x=403x.cli:main"
        ]
    }
)
