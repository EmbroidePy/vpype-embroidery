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
    url="https://github.com/abey79/vpype-explorations/",
    license=license,
    packages=["vpype_pyembroidery"],
    install_requires=[
        "click",
        "vpype",
        "numpy",
        "pyembroidery",
    ],
    entry_points="""
            [vpype.plugins]
            read_emb=vpype_embroidery.read_emb:read_emb
            write_emb=vpype_embroidery.write_emb:write_emb
            efill=vpype_embroidery.efill:efill
        """,
)
