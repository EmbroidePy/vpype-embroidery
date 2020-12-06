import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vpype-embroidery",
    version="0.0.2",
    author="Tatarize",
    author_email="tatarize@gmail.com",
    description="vpype embroidery plugin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/embroidepy/vpype-embroidery/",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
    install_requires=[
        "click",
        "vpype",
        "numpy",
        "pyembroidery",
    ],
    entry_points="""
        [vpype.plugins]
        eread=vpype_embroidery.eread:eread
        ewrite=vpype_embroidery.ewrite:ewrite
        efill=vpype_embroidery.efill:efill
    """,
)
