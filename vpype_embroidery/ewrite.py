import click
import vpype as vp
import vpype_cli
from pyembroidery import COLOR_BREAK, SEQUENCE_BREAK, STITCH, EmbPattern


_EMB_IN_MM = 0.1
_PX_IN_MM = 0.2645833333333333  # 1/96 inch
_PX_PER_EMB = _PX_IN_MM / _EMB_IN_MM


@click.command()
@click.argument("filename", type=vpype_cli.PathType(exists=False))
@click.option(
    "-v",
    "--version",
    nargs=1,
    default=None,
    type=vpype_cli.TextType(),
    help="version of embroidery file to write",
)
@vpype_cli.global_processor
def ewrite(document: vp.Document, filename: str, version: str):
    pattern = EmbPattern()
    for layer in document.layers.values():
        for p in layer:
            m = p * _PX_PER_EMB
            for v in m:
                pattern.add_stitch_absolute(STITCH, int(v.real), int(v.imag))
            pattern.add_command(SEQUENCE_BREAK)
        pattern.add_command(COLOR_BREAK)
    if version is not None:
        pattern.write(filename, version=version)
    else:
        pattern.write(filename)
    return document


ewrite.help_group = "Embroidery"
