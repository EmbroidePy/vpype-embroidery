import click
import vpype as vp
from pyembroidery import EmbPattern

@click.command()
@click.option(
    "-r",
    "--filename",
    nargs=1,
    default=None,
    type=str,
    help="read_emb",
)
@vp.generator
def read_emb(filename: str):
    pattern = EmbPattern(filename)
    lc = [(s[0], s[1]) for s in pattern.stitches]
    return vp.LineCollection(lc)


read_emb.help_group = "Plugins"
