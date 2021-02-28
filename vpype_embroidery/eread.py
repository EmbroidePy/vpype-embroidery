import click
import numpy as np
import vpype as vp
from pyembroidery import EmbPattern

_EMB_SCALE_FACTOR = 2.645833333333333


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@vp.global_processor
def eread(document: vp.Document, filename: str):
    pattern = EmbPattern(filename)
    for stitches, color in pattern.get_as_stitchblock():
        if len(stitches) == 0:
            continue
        lc = vp.LineCollection()
        lc.scale(1.0 / _EMB_SCALE_FACTOR)
        stitch_block = np.asarray(stitches, dtype="float")
        stitch_block = stitch_block[..., 0] + 1j * stitch_block[..., 1]
        lc.append(stitch_block)
        lc.emb_thread = color  # No defined color api.
        document.add(lc)
    return document


eread.help_group = "Embroidery"
