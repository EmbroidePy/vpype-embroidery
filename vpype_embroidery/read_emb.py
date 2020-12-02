import click
import vpype as vp
from pyembroidery import EmbPattern
_EMB_SCALE_FACTOR = 2.645833333333333

@click.command()
@click.option(
    "-r",
    "--filename",
    nargs=1,
    default=None,
    type=str,
    help="read_emb",
)
@vp.global_processor
def read_emb(document: vp.Document, filename: str):
    pattern = EmbPattern(filename)

    for stitches, color in pattern.get_as_colorblocks():
        lc = [(s[0] * _EMB_SCALE_FACTOR, s[1] * _EMB_SCALE_FACTOR) for s in stitches]
        c = color.color
        # Color here is simply ignored.
        document.add(vp.LineCollection(lc))
    return document




read_emb.help_group = "Plugins"
