"""Render only the saved demo CSV files; no experiment is rerun."""
import argparse
import importlib.util
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.ticker import NullFormatter
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-path", type=Path,
                        default=ROOT / "skills" / "paper-figures")
    parser.add_argument("--output", type=Path, default=ROOT / "examples" / "output")
    args = parser.parse_args()
    helper_path = args.skill_path / "scripts" / "figure_io.py"
    spec = importlib.util.spec_from_file_location("figure_io", helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    data = np.genfromtxt(ROOT/"examples"/"data"/"fields.csv",
                         delimiter=",", names=True)
    conv = np.genfromtxt(ROOT/"examples"/"data"/"convergence.csv",
                         delimiter=",", names=True)
    x, t = np.unique(data["x"]), np.unique(data["t"])
    expected_x, expected_t = np.meshgrid(x, t)
    if not (np.allclose(data["x"], expected_x.ravel())
            and np.allclose(data["t"], expected_t.ravel())):
        raise ValueError("Field rows must preserve their declared space-time grid")
    shape = (len(t), len(x))
    ref = data["reference"].reshape(shape)
    approx = data["interpolation"].reshape(shape)
    error = data["absolute_error"].reshape(shape)
    if not np.allclose(error, np.abs(approx-ref), rtol=1e-10, atol=1e-14):
        raise ValueError("Stored error does not match the reference and interpolation")
    if not all(np.isfinite(data[name]).all() for name in data.dtype.names):
        raise ValueError("Nonfinite field data")
    if np.any(conv["h"] <= 0) or np.any(conv["rms_error"] <= 0):
        raise ValueError("Convergence log axes require positive values")
    norm = Normalize(vmin=min(ref.min(), approx.min()),
                     vmax=max(ref.max(), approx.max()))
    with helper.paper_style(font_size=8):
        fig, axes = plt.subplots(2, 2, figsize=helper.size_inches(17.8, 12.6),
                                 layout="constrained")
        mesh_args = dict(shading="auto", rasterized=True)
        m0 = axes[0,0].pcolormesh(x, t, ref, norm=norm, cmap="viridis", **mesh_args)
        axes[0,1].pcolormesh(x, t, approx, norm=norm, cmap="viridis", **mesh_args)
        fig.colorbar(m0, ax=list(axes[0,:]), label="Solution u(x,t)",
                     fraction=0.045, pad=0.035)
        me = axes[1,0].pcolormesh(x, t, error, cmap="magma",
                                 vmin=0, **mesh_args)
        fig.colorbar(me, ax=axes[1,0], label="Absolute error", pad=0.035)
        titles = ["Analytic reference", "Linear interpolation (12 cells)",
                  "Where the interpolation differs", "Spatial refinement"]
        for label, ax, title in zip("abcd", axes.flat, titles):
            ax.set_title(title, loc="left", pad=7)
            ax.text(-0.14, 1.08, label, transform=ax.transAxes,
                    fontsize=10, fontweight="bold", va="bottom")
        for ax in [axes[0,0], axes[0,1], axes[1,0]]:
            ax.set(xlabel="Position x", ylabel="Time t")
        ax = axes[1,1]
        ax.loglog(conv["h"], conv["rms_error"], "o-", color="#16718B",
                   markersize=4, label="Measured RMS error")
        guide = 0.5 * conv["rms_error"][-1] * (conv["h"]/conv["h"][-1])**2
        ax.loglog(conv["h"], guide, "--", color="#858585",
                   linewidth=1.0, label=r"$O(h^2)$ guide")
        ax.set(xlabel="Spatial interval h", ylabel="RMS error")
        ax.set_xticks(conv["h"], labels=[f"1/{int(n)}" for n in conv["cells"]])
        ax.xaxis.set_minor_formatter(NullFormatter())
        ax.spines[["top","right"]].set_visible(False)
        ax.grid(which="major", color="#e7e7e7", linewidth=0.6)
        ax.legend(loc="upper left", frameon=False)
        fig.suptitle("Analytic heat solution · interpolation demonstration",
                     fontsize=10, fontweight="semibold")
        report = helper.save_figure(fig, args.output/"interpolation",
                                     dpi=300, overwrite=True)
        plt.close(fig)
    args.output.mkdir(parents=True, exist_ok=True)
    public_report = dict(report, files=[Path(p).name for p in report["files"]])
    public_report["data_origin"] = "Analytic solution; piecewise linear interpolation"
    public_report["scientific_scope"] = "Demonstration, not a research benchmark"
    (args.output/"export.json").write_text(json.dumps(public_report, indent=2)+"\n")
    print(json.dumps(public_report, indent=2))


if __name__ == "__main__":
    main()

