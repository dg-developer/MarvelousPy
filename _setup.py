
import setuptools

with open("ReadMe.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="marvelous_drg.developer.2",
    version="0.0.0.0",
    author="David Gayman",
    description="Functional programming features for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # packages=["marvelous.src"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["marvelous"],
    package_dir={'':'marvelous/src'},
    install_requires=[]
)
