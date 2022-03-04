import pathlib

import click
import numpy as np
import vpype as vp
import vpype_cli
from pyembroidery import EmbPattern

_EMB_SCALE_FACTOR = 2.645833333333333


@click.command()
@click.argument("filename", type=vpype_cli.PathType(exists=True))
@vpype_cli.global_processor
def eread(document: vp.Document, filename: str):
    # populate the vp_source[s] properties
    document.set_property(vp.METADATA_FIELD_SOURCE, pathlib.Path(filename).absolute())
    document.add_to_sources(filename)

    pattern = EmbPattern(filename)
    for stitches, color in pattern.get_as_stitchblock():
        if len(stitches) == 0:
            continue
        lc = vp.LineCollection()
        lc.scale(1.0 / _EMB_SCALE_FACTOR)
        stitch_block = np.asarray(stitches, dtype="float")
        stitch_block = stitch_block[..., 0] + 1j * stitch_block[..., 1]
        lc.append(stitch_block)
        lc.set_property(vp.METADATA_FIELD_COLOR, vp.Color(color.hex_color()))
        document.add(lc, with_metadata=True)
    return document


eread.help_group = "Embroidery"
