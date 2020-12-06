from setuptools import setup


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="vpype-embroidery",
    version="0.0.1",
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tatarize",
    url="https://github.com/embroidepy/vpype-embroidery/",
    license=license,
    packages=["vpype_embroidery"],
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
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
