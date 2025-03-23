from setuptools import setup, find_packages

setup(
    name="update-reqs",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "update-reqs=update_reqs.cli:main",
        ],
    },
)
