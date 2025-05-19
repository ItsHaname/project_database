from setuptools import setup, find_packages

setup(
    name="project_database",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Liste de dépendances principales, par exemple :
        # "flask", "requests", etc.
    ],
    extras_require={
        "dev": [
            "unittest",
            "pytest",
            "flake8",
            "black",
        ],
    },
)

