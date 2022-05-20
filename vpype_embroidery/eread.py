import pathlib

import click
import numpy as np
import vpype as vp
import vpype_cli
from pyembroidery import EmbPattern

_EMB_IN_MM = 0.1
_PX_IN_MM = 0.2645833333333333  # 1/96 inch
_EMB_PER_PX = _EMB_IN_MM / _PX_IN_MM


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
        stitch_block = np.asarray(stitches, dtype="float")
        stitch_block = stitch_block[..., 0] + 1j * stitch_block[..., 1]
        lc.append(stitch_block)
        lc.set_property(vp.METADATA_FIELD_COLOR, vp.Color(color.hex_color()))
        lc.scale(_EMB_PER_PX)
        document.add(lc, with_metadata=True)
    return document


eread.help_group = "Embroidery"
