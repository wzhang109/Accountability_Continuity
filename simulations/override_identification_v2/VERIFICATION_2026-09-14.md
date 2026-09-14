# Methods verification — September 14, 2026

This is an AI-assisted implementation and reproducibility review of the
synthetic override-rate study. It is not independent statistical review or
evidence from a real organization.

## Correction

The previous estimators used a Moore–Penrose pseudoinverse of the information
matrix directly as a covariance estimate. For an information matrix with an
unresolved parameter direction, a pseudoinverse can assign that direction zero
variance. That is a numerical failure if interpreted as ordinary Wald certainty.

Two explicit reproductions before the correction returned an engagement change
of 0 and standard error 0 while reporting optimizer convergence:

| Input condition | Why engagement cannot be learned |
|---|---|
| Proxy sensitivity = proxy false-positive rate = .5 | The proxy rate is .5 at every engagement value |
| d=f=q=.25 | Override rate is .25 at every accuracy and engagement value |

The revised estimators check the eigenvalues of their fitted information matrix.
If the smallest is at or below 1e-10 times the largest, or the matrix is invalid,
they refuse to return finite Wald standard errors and raise an explicit error.
This uses the same numerical cutoff as the existing inverse. It is a guard
against unresolved directions, not a general cure for weak identification.

The default probability model, parameters, scenarios, optimization, and output
definitions were not changed. The auxiliary predictive covariance calculation
still uses a pseudoinverse for its numerical calculation; it is not being used
there to assert that a latent parameter is identified.

## Checks performed

**Tests:** the existing 12 tests passed before the correction. The expanded
17-test suite passed afterward. Five additions cover uninformative proxy data,
uninformative overrides, a single period that cannot identify two endpoints,
increasing uncertainty as proxy separation weakens, and compatibility of
population-level independent channels under the specified stable model.

**Full rerun:** the default configuration was executed from beginning to end,
including all six scenarios, 24 periods, three operational sample sizes, two
audit shares, and 1,000 replications per cell.

| Check | Result |
|---|---:|
| Design cells | 36 |
| Replication records | 36,000 |
| Model fits | 72,000 |
| Fits reporting convergence | 72,000 |
| Candidate paths checked | 60,000 |
| Paths within specified RMSE tolerance | 4,345 |
| Saved CSVs compared | 9 |
| Figures regenerated with identical file hashes | 6 |
| Largest absolute numeric difference across CSVs | 1.67 × 10⁻¹⁶ |

The fresh output was compared with the files present at repository commit
`11f80d772966ad1f4f58ddc88af5ec1211fbf963`. The comparison allowed relative
tolerance 1e-8 and absolute tolerance 1e-10. It also checked the manifest,
replication counts per cell, absence of duplicate replication keys, finite
estimates, and positive finite reported standard errors in all default fits.

The numerical correction does not change the saved default-setting results.
The original CSVs and figures are retained. The report records hashes of the
reviewed simulation code, comparison script, reference CSVs, fresh CSVs, and
fresh replication file. The large replication file remains generated output,
rather than an added repository artifact.

## Reproduce this check

From this simulation directory, using the dependencies in
`requirements.txt`:

```bash
MPLCONFIGDIR=/tmp/ac-mpl python -m unittest discover -s tests -v

MPLCONFIGDIR=/tmp/ac-mpl python simulation_v2.py \
  --config config.json --output-dir /tmp/ac-full-rerun

python verify_reproduction.py --rerun-dir /tmp/ac-full-rerun \
  --report /tmp/ac-verification.json
```

Use a separate output directory so the reference files remain available for
comparison. The checked-in [machine-readable report](verification/2026-09-14.json)
records the environment: Python 3.12.7, NumPy 1.26.4, pandas 2.2.2,
Matplotlib 3.9.2, and SciPy 1.13.1.

## What remains unresolved

- The model is illustrative. No parameters or proxy properties were estimated
  from a real organization.
- In the default simulation, the highest boundary-hit rate in any
  audit-plus-override cell is still **40.2%**; for audit plus proxy it is
  **0.1%**. The rank guard does not solve small-sample boundary inference.
- Known calibration, independent measurement channels, and linear paths are
  strong assumptions. Overlapping samples, reviewer clustering, selective
  review, nonlinear changes, and correlated human/AI errors require further work.
- Convergence reports do not prove a global optimum in every problem. The
  default joint estimator uses multiple starts, and recovery was checked at
  selected population paths.
- The predictive discrepancy is an approximate diagnostic. Rejection does not
  identify a mechanism, and non-rejection does not validate the measurement model.
- Numerical replication can reproduce a model's assumptions and mistakes.
  The review does not prove novelty, a causal effect, or the validity of the
  proposed human-learning task.

For a step-by-step account of the equation and its interpretation, read the
[English and Chinese walkthrough](PLAIN_LANGUAGE_GUIDE.md).
