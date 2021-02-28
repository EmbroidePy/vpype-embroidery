from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

setup(
    name="vpype-embroidery",
    version="0.1.0",
    description="vpype embroidery plugin",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tatarize",
    author_email="tatarize@gmail.com",
    url="https://github.com/embroidepy/vpype-embroidery/",
    packages=["vpype_embroidery"],
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