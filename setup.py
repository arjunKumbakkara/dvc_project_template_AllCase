from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "DVC NLP"
AUTHOR_USER_NAME = "arjunkumbakkara"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=Arjun Kumbakkara,
    description="A small package for DVC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/arjunKumbakkara/DVC-NLP-Simple-usecase",
    author_email="arjunkumbakkara@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)
