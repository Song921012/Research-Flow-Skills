"""Original, optional Matplotlib helpers for physical-size figure export.

Export reports describe files and sizes, not scientific or visual correctness.
"""
from contextlib import contextmanager
import math
from pathlib import Path
import matplotlib as mpl


def size_inches(width_cm, height_cm):
    """Convert positive finite centimetres to inches."""
    values = (float(width_cm), float(height_cm))
    if any(not math.isfinite(v) or v <= 0 for v in values):
        raise ValueError("Figure dimensions must be positive finite centimetres")
    return tuple(v / 2.54 for v in values)


@contextmanager
def paper_style(font_size=8, font_family=None):
    """Apply a temporary baseline without a fixed palette or permanent changes."""
    if not math.isfinite(float(font_size)) or float(font_size) <= 0:
        raise ValueError("font_size must be positive and finite")
    settings = {
        "font.size": font_size,
        "axes.labelsize": font_size,
        "axes.titlesize": font_size,
        "legend.fontsize": max(1, font_size - 0.5),
        "xtick.labelsize": max(1, font_size - 0.5),
        "ytick.labelsize": max(1, font_size - 0.5),
        "axes.linewidth": 0.7,
        "lines.linewidth": 1.4,
        "legend.frameon": False,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
    }
    if font_family is not None:
        settings["font.family"] = font_family
    with mpl.rc_context(settings):
        yield


def save_figure(fig, stem, formats=("pdf", "svg", "png"), dpi=300, overwrite=False):
    """Export the figure's exact canvas size, without implicit tight cropping."""
    stem = Path(stem)
    if stem.suffix:
        raise ValueError("Pass a filename stem without an extension")
    if isinstance(formats, str):
        raise ValueError("formats must be a sequence such as ('pdf', 'png')")
    formats = tuple(str(f).lower() for f in formats)
    if not formats or len(set(formats)) != len(formats):
        raise ValueError("Choose at least one distinct output format")
    if any(f not in {"pdf", "svg", "png"} for f in formats):
        raise ValueError("Supported formats: pdf, svg, png")
    if not math.isfinite(float(dpi)) or float(dpi) <= 0:
        raise ValueError("dpi must be positive and finite")
    width, height = (float(v) for v in fig.get_size_inches())
    if any(not math.isfinite(v) or v <= 0 for v in (width, height)):
        raise ValueError("The figure must have positive finite dimensions")
    paths = [stem.with_suffix("." + f) for f in formats]
    if not overwrite and any(p.exists() for p in paths):
        raise FileExistsError("Output exists; choose a new stem or use overwrite=True")
    stem.parent.mkdir(parents=True, exist_ok=True)
    with mpl.rc_context({"savefig.bbox": None, "savefig.pad_inches": 0.0}):
        for fmt, path in zip(formats, paths):
            fig.savefig(path, format=fmt, dpi=dpi, bbox_inches=None)
    return {
        "files": [str(p) for p in paths],
        "width_cm": width * 2.54,
        "height_cm": height * 2.54,
        "dpi": float(dpi),
    }

