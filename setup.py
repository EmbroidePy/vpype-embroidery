from setuptools import setup, find_packages


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
