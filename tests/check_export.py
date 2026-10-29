"""Check physical-size export, input preservation and overwrite protection."""
import argparse
import importlib.util
from pathlib import Path
import tempfile
import xml.etree.ElementTree as ET

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from pypdf import PdfReader


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-path", type=Path,
                        default=Path(__file__).resolve().parents[1]/"skills"/"paper-figures")
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location(
        "figure_io", args.skill_path/"scripts"/"figure_io.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    original_font_size = matplotlib.rcParams["font.size"]
    with tempfile.TemporaryDirectory(prefix="researchflowskills-export-") as tmp:
        with matplotlib.rc_context({"savefig.bbox": "tight"}):
            with module.paper_style(font_size=9):
                fig, ax = plt.subplots(figsize=module.size_inches(8.9, 5.5),
                                       layout="constrained")
                source_x = np.array([0., 1., 3.])
                source_y = np.array([0., 2., 1.])
                line, = ax.plot(source_x, source_y)
                ax.set(xlabel="Time", ylabel="Observed value")
                stem = Path(tmp)/"figure"
                report = module.save_figure(fig, stem, dpi=150)
                assert matplotlib.rcParams["savefig.bbox"] == "tight"
                assert np.array_equal(line.get_xdata(), source_x)
                assert np.array_equal(line.get_ydata(), source_y)
                pdf = PdfReader(stem.with_suffix(".pdf"))
                box = pdf.pages[0].mediabox
                assert abs(float(box.width)/72*2.54-8.9) < 1e-4
                assert abs(float(box.height)/72*2.54-5.5) < 1e-4
                with Image.open(stem.with_suffix(".png")) as im:
                    assert abs(im.width - 8.9/2.54*150) <= 1
                    assert abs(im.height - 5.5/2.54*150) <= 1
                svg = ET.parse(stem.with_suffix(".svg")).getroot()
                assert abs(float(svg.attrib["width"].removesuffix("pt"))/72*2.54-8.9) < 1e-4
                before = stem.with_suffix(".pdf").read_bytes()
                try:
                    module.save_figure(fig, stem)
                except FileExistsError:
                    pass
                else:
                    raise AssertionError("Existing output was not protected")
                assert stem.with_suffix(".pdf").read_bytes() == before
                try:
                    module.save_figure(fig, Path(tmp)/"bad", formats=("jpeg",))
                except ValueError:
                    pass
                else:
                    raise AssertionError("Unsupported format accepted")
                assert not list(Path(tmp).glob("bad.*"))
                plt.close(fig)
            assert matplotlib.rcParams["font.size"] == original_font_size
    for dims in [(0, 1), (-1, 2), (float("nan"), 2)]:
        try:
            module.size_inches(*dims)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid figure size accepted")
    print("PASS: exact PDF/SVG/PNG size, data unchanged, scoped style, overwrite protection, invalid-input checks")


if __name__ == "__main__":
    main()
