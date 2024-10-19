from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirement(file_path: str) -> List[str]:
    requirements = []
    try:
        with open(file_path) as f:
            requirements = f.readlines()
            requirements = [req.replace("\n", "") for req in requirements]
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"File {file_path} not found. Please check the path.")
    return requirements


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


__version__ = "0.0.4"
REPO_NAME = "mongo-db"
PKG_NAME = "MongoConnect"
AUTHOR_USER_NAME = "Pakistan971"
AUTHOR_EMAIL = "sunny.savita@ineuron.ai"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Corrected here
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirement("requirements_dev.txt")  # Fixed path
)
