from setuptools import setup, find_packages

setup(
    name="aka_json",
    version="1.0.0",
    author="FluffyFolfie",
    author_email="e-stepanov-ig@yandex.ru",
    description="JSON/JSON5 file handling with dataclass support",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/FluffyFolfie/aka_json",
    packages=find_packages(),
    install_requires=[
        "dacite>=1.6.0",
        "json5>=0.9.5"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
