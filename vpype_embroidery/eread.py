import click
import vpype as vp
from pyembroidery import EmbPattern
_EMB_SCALE_FACTOR = 2.645833333333333

@click.command()
@click.argument('filename', type=click.Path(exists=True))
@vp.global_processor
def eread(document: vp.Document, filename: str):
    pattern = EmbPattern(filename)
    for stitches, color in pattern.get_as_stitchblock():
        if len(stitches) == 0:
            continue
        lc = vp.LineCollection([(stitches[i-1][0] + stitches[i-1][1] * 1j,
                                 stitches[i][0] + stitches[i][1] * 1j)
                                for i in range(1,len(stitches))])
        lc.scale(1.0/_EMB_SCALE_FACTOR)
        c = color.color
        # Color here is simply ignored.
        document.add(lc)
    return document

eread.help_group = "Embroidery"
