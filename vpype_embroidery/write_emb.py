import click
import vpype as vp
from pyembroidery import EmbPattern, STITCH, COLOR_BREAK

@click.command()
@click.option(
    "-w",
    "--filename",
    nargs=1,
    default=None,
    type=str,
    help="read_emb",
)
@vp.global_processor
def write_emb(document: vp.Document, filename: str):
    pattern = EmbPattern()
    for layer in document:
        for p in layer:
            pattern.add_stitch_absolute(STITCH, p.real, p.imag)
        pattern.add_block(COLOR_BREAK)
    pattern.write(filename)
    return document


