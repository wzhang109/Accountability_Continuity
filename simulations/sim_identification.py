"""
Override rate is not identifying: a demonstration
=================================================

Claim being demonstrated
------------------------
In a human-in-the-loop review process, the reviewer's override rate is often
treated as evidence about oversight quality. It cannot carry that weight on its
own. Two very different processes produce the same falling override rate:

    World A  -- the model gets better; the reviewer keeps checking.
    World B  -- the model does not change; the reviewer stops checking.

This script constructs the two worlds so that their override-rate paths are
identical by construction, then shows which additional observables separate them.

What this is and is not
-----------------------
This is a demonstration that a naive measure is non-identifying under a stated
generative model. It is NOT evidence that disengagement occurs in real review
processes, and it is not calibrated to any real deployment. The parameters are
illustrative.

Author: Wenwen (Celine) Zhang
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RNG = np.random.default_rng(20260818)

# ----------------------------------------------------------------------------
# Generative model (one case)
#
#   1. The model proposes an answer. It is correct with probability p.
#   2. The reviewer is "engaged" with probability e -- meaning they actually
#      consult the primary evidence rather than the model's summary.
#   3. If engaged:
#         - they override a wrong answer with probability d   (detection)
#         - they override a correct answer with probability f (false alarm)
#   4. If not engaged, they override with probability q, independent of whether
#      the answer was right. This is the "cargo-cult override": a reviewer who
#      pushes back on the basis of surface cues (e.g. the model flagged low
#      confidence) without checking the evidence.
#
# Observed override rate:
#      R = e * [ d*(1-p) + f*p ] + (1-e) * q
# ----------------------------------------------------------------------------

D = 0.75   # detection rate when engaged
F = 0.05   # false-alarm rate when engaged
Q = 0.04   # override rate when disengaged
T = 24     # periods (e.g. months)
N = 4000   # cases per period

t = np.arange(T)


def override_rate(p, e):
    """Expected override rate given model accuracy p and engagement e."""
    return e * (D * (1 - p) + F * p) + (1 - e) * Q


def override_precision(p, e):
    """P(the model was actually wrong | the reviewer overrode).

    An override is 'right' when it corrects a genuine error.
    """
    joint_wrong_and_override = e * D * (1 - p) + (1 - e) * Q * (1 - p)
    return joint_wrong_and_override / override_rate(p, e)


# ----------------------------------------------------------------------------
# World A: the model improves, engagement is constant
# ----------------------------------------------------------------------------
E_A = 0.90
p_A = np.linspace(0.60, 0.88, T)
e_A = np.full(T, E_A)
R_A = override_rate(p_A, e_A)

# ----------------------------------------------------------------------------
# World B: the model is frozen, engagement decays.
# Engagement is solved so that the override rate path matches World A exactly.
#
#   R = e*[d(1-p0) + f*p0] + (1-e)*q
#   =>  e = (R - q) / ( d(1-p0) + f*p0 - q )
# ----------------------------------------------------------------------------
P0 = 0.60
p_B = np.full(T, P0)
e_B = (R_A - Q) / (D * (1 - P0) + F * P0 - Q)
R_B = override_rate(p_B, e_B)

assert np.allclose(R_A, R_B), "the two worlds must share an override-rate path"
assert e_B.min() > 0 and e_B.max() <= 1, "engagement left the unit interval"


# ----------------------------------------------------------------------------
# Monte Carlo: confirm the analytic paths are what a finite sample would show
# ----------------------------------------------------------------------------
def simulate(p_path, e_path, n=N):
    """Return (override rate, override precision) measured from simulated cases."""
    rates, precisions = [], []
    for p, e in zip(p_path, e_path):
        correct = RNG.random(n) < p
        engaged = RNG.random(n) < e
        u = RNG.random(n)
        overrode = np.where(
            engaged,
            np.where(correct, u < F, u < D),
            u < Q,
        )
        rates.append(overrode.mean())
        precisions.append((overrode & ~correct).sum() / max(overrode.sum(), 1))
    return np.array(rates), np.array(precisions)


sim_R_A, sim_prec_A = simulate(p_A, e_A)
sim_R_B, sim_prec_B = simulate(p_B, e_B)

prec_A = override_precision(p_A, e_A)
prec_B = override_precision(p_B, e_B)

# ----------------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------------
CA, CB = "#1f4e79", "#c1462c"
fig, ax = plt.subplots(2, 2, figsize=(11.5, 8))
fig.suptitle(
    "A falling override rate does not tell you which process produced it",
    fontsize=14, fontweight="bold", y=0.98,
)

# (1) the thing you usually measure
a = ax[0, 0]
a.plot(t, sim_R_A, "o", ms=4, color=CA, alpha=0.55)
a.plot(t, sim_R_B, "s", ms=4, color=CB, alpha=0.55)
a.plot(t, R_A, color=CA, lw=2.5, label="World A — model improves")
a.plot(t, R_B, color=CB, lw=2.5, ls="--", label="World B — reviewer disengages")
a.set_title("1. Override rate — what is usually measured", fontsize=11, fontweight="bold")
a.set_ylabel("share of cases overridden")
a.text(0.5, 0.9, "identical by construction", transform=a.transAxes,
       ha="center", fontsize=10, style="italic", color="#555")
a.legend(fontsize=9, loc="lower left")

# (2) model accuracy on a held-out gold standard
a = ax[0, 1]
a.plot(t, p_A, color=CA, lw=2.5)
a.plot(t, p_B, color=CB, lw=2.5, ls="--")
a.set_title("2. Model accuracy on a held-out gold set", fontsize=11, fontweight="bold")
a.set_ylabel("accuracy")
a.set_ylim(0.5, 1.0)

# (3) engagement — proxied by whether the reviewer opens the primary record
a = ax[1, 0]
a.plot(t, e_A, color=CA, lw=2.5)
a.plot(t, e_B, color=CB, lw=2.5, ls="--")
a.set_title("3. Reviewer engagement (opens primary evidence)", fontsize=11, fontweight="bold")
a.set_ylabel("share of cases")
a.set_xlabel("period")
a.set_ylim(0, 1)

# (4) precision of the overrides that still happen
a = ax[1, 1]
a.plot(t, sim_prec_A, "o", ms=4, color=CA, alpha=0.55)
a.plot(t, sim_prec_B, "s", ms=4, color=CB, alpha=0.55)
a.plot(t, prec_A, color=CA, lw=2.5)
a.plot(t, prec_B, color=CB, lw=2.5, ls="--")
a.set_title("4. Override precision — were the overrides right?", fontsize=11, fontweight="bold")
a.set_ylabel("P(model was wrong | overridden)")
a.set_xlabel("period")

for row in ax:
    for a in row:
        a.grid(alpha=0.25)
        a.spines[["top", "right"]].set_visible(False)

fig.tight_layout(rect=[0, 0.03, 1, 0.95])
fig.text(0.5, 0.005,
         "Dots are simulated (n=4,000 cases/period); lines are analytic. "
         "Illustrative parameters, not calibrated to any deployment.",
         ha="center", fontsize=8.5, color="#666")
fig.savefig("identification_problem.png", dpi=160)
print("wrote identification_problem.png")

# ----------------------------------------------------------------------------
# Console summary
# ----------------------------------------------------------------------------
print("\n" + "=" * 66)
print("Panel 1 — override rate")
print(f"  World A: {R_A[0]:.3f} -> {R_A[-1]:.3f}")
print(f"  World B: {R_B[0]:.3f} -> {R_B[-1]:.3f}   (identical)")
print("\nPanel 3 — engagement")
print(f"  World A: {e_A[0]:.2f} -> {e_A[-1]:.2f}")
print(f"  World B: {e_B[0]:.2f} -> {e_B[-1]:.2f}")
print("\nPanel 4 — override precision")
print(f"  World A: {prec_A[0]:.3f} -> {prec_A[-1]:.3f}")
print(f"  World B: {prec_B[0]:.3f} -> {prec_B[-1]:.3f}")
print("=" * 66)
print("""
Reading of panel 4 (note the direction -- it is not the obvious one):

  Override precision falls FURTHER in World A, the world where oversight is
  working. As the model improves, a growing share of the remaining overrides are
  the reviewer being wrong rather than the model. In World B the model is still
  bad, so the overrides that survive keep catching real errors.

  So low override precision is not by itself a warning sign. It has to be read
  against model accuracy. This is a second reason not to read any single review
  statistic on its own.

Sensitivity worth running before this is claimed as a result:
  the direction in panel 4 depends on the false-alarm rate F. Sweep F and
  report where the ordering flips.
""")
