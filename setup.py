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
    url="https://github.com/abey79/vpype-explorations/",
    license=license,
    packages=["vpype_embroidery"],
    install_requires=[
        "click",
        "vpype",
        "pyembroidery",
        "svgelements",
        "numpy",
    ],
    entry_points="""
            [vpype.plugins]
            read_emb=vpype_embroidery.read_emb:read_emb
            efill=vpype_embroidery.efill:efill
        """,
)
