from setuptools import setup, find_packages

setup(
    name="gitpatch-agent",
    version="0.1.0",
    packages=find_packages(),
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "gitpatch=main:main",
        ],
    },
)
