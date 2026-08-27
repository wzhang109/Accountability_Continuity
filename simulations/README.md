# Override-rate identification

## Current study

The current version is
[`override_identification_v2/`](override_identification_v2/).

It asks whether a falling override rate can distinguish improving model
accuracy from weakening human review. Its primary result is analytic: under the
stated binary engagement model, override rate alone does not jointly identify
model accuracy and reviewer engagement.

V2 includes:

* analytic equivalence curves and an expected-data likelihood ridge;
* constrained binomial likelihood estimators;
* independent accuracy-audit and imperfect process-proxy channels;
* 1,000 Monte Carlo replications per design cell;
* stable, detection-drift, and proxy-drift checks;
* bias, RMSE, interval coverage, convergence, boundary, and predictive-check
  diagnostics;
* a [plain-language guide](override_identification_v2/PLAIN_LANGUAGE_GUIDE.md)
  in English and Chinese.

Start with the
[plain-language guide](override_identification_v2/PLAIN_LANGUAGE_GUIDE.md),
then read the [results note](override_identification_v2/RESULTS.md) and full
[design documentation](override_identification_v2/README.md).

## Initial demonstration

`sim_identification.py` is retained as the historical first version. It
constructs two processes with an identical expected override-rate path:

* the model improves while reviewer engagement stays constant;
* model accuracy stays constant while reviewer engagement declines.

The second engagement path is solved algebraically from the first, so their
equality is true by construction. This is a valid counterexample, not a
simulation discovery and not evidence about a real deployment.

![Initial demonstration](identification_problem.png)

## Interpretation boundary

Supported:

> A single override trend is compatible with different underlying processes
> under the stated model, and additional measurements only help under explicit
> calibration assumptions.

Not supported:

* real reviewers are disengaging;
* the illustrative parameters describe a real organization;
* opening primary evidence proves substantive review;
* the simulation establishes a causal effect.
