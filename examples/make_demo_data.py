"""Create openly shareable numerical demonstration data; no user research data.

The reference is an analytic 1D heat-equation solution. The approximation is
piecewise linear interpolation in space, NOT a new PDE solver or AI method.
"""
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"


def reference(x, t):
    return (np.exp(-np.pi**2 * t) * np.sin(np.pi * x)
            + 0.3 * np.exp(-9 * np.pi**2 * t) * np.sin(3 * np.pi * x))


def interpolate(x, t, cells):
    nodes = np.linspace(0, 1, cells + 1)
    return np.vstack([np.interp(x, nodes, reference(nodes, ti)) for ti in t])


def main():
    DATA.mkdir(parents=True, exist_ok=True)
    x = np.linspace(0, 1, 101)
    t = np.linspace(0, 0.08, 51)
    xx, tt = np.meshgrid(x, t)
    exact = reference(xx, tt)
    approx = interpolate(x, t, 12)
    values = np.column_stack([xx.ravel(), tt.ravel(), exact.ravel(),
                              approx.ravel(), np.abs(approx-exact).ravel()])
    np.savetxt(DATA / "fields.csv", values, delimiter=",", fmt="%.16g",
               header="x,t,reference,interpolation,absolute_error", comments="")
    fine_x = np.linspace(0, 1, 2049)
    fine_t = np.linspace(0, 0.08, 65)
    fine_ref = reference(fine_x[None, :], fine_t[:, None])
    rows = []
    for cells in [12, 24, 48, 96]:
        err = interpolate(fine_x, fine_t, cells) - fine_ref
        rows.append([cells, 1/cells, np.sqrt(np.mean(err**2)), np.max(np.abs(err))])
    np.savetxt(DATA / "convergence.csv", rows, delimiter=",", fmt="%.16g",
               header="cells,h,rms_error,max_error", comments="")
    print("Created analytic interpolation demonstration data in examples/data")


if __name__ == "__main__":
    main()

