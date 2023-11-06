from setuptools import setup


with open("README.md") as f:
    readme = f.read()

setup(
    name="vpype-embroidery",
    version="0.3.2",
    description="vpype embroidery plugin",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tatarize",
    author_email="tatarize@gmail.com",
    url="https://github.com/embroidepy/vpype-embroidery/",
    packages=["vpype_embroidery"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "click",
        "vpype>=1.9,<2.0",
        "numpy",
        "pyembroidery>=1.5.0",
    ],
    entry_points="""
            [vpype.plugins]
            eread=vpype_embroidery.eread:eread
            ewrite=vpype_embroidery.ewrite:ewrite
            efill=vpype_embroidery.efill:efill
        """,
)