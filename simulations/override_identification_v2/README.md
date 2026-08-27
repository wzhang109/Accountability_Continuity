# Accountability Continuity: Override-Rate Identification Study

## Research question

Can a falling override rate distinguish improving model accuracy from weakening
human review?

The answer is no when override is the only observed measure. This repository
establishes that narrow identification result under a stated binary model. It
then asks what can be learned after adding independent measurements and what
happens when their calibration assumptions fail.

This is an illustrative methodological study. It is not an experiment on real
reviewers, it does not estimate the prevalence of disengagement, and it does
not establish a causal effect.

## Why the original demonstration was not enough

The original script constructed one model-improvement path and solved
algebraically for one disengagement path with the same expected override rate.
That is a valid counterexample, but equality is true by construction. It should
not be described as a discovered simulation result.

This version makes the analytic identification result primary and uses
simulation only for sampling, recovery, calibration, and falsification checks.
It adds:

1. full analytic equivalence curves;
2. 60,000 smooth candidate paths drawn from fixed ranges;
3. an expected-data likelihood surface with fixed starts and linear paths;
4. six specified data-generating scenarios;
5. constrained binomial likelihood estimators rather than unbounded
   period-by-period inversion;
6. 1,000 Monte Carlo replications per design cell;
7. approximate interval coverage, convergence, and boundary diagnostics;
8. independent accuracy-audit and process-proxy channels;
9. an override predictive check that can return “assumptions fail” instead of
   forcing every decline into an engagement explanation;
10. detection-drift and proxy-drift misspecification scenarios.

## ADEMP specification

### Aim

Establish when override rate fails to jointly identify model accuracy and
reviewer engagement. Quantify recovery under explicit measurement assumptions,
then test how the conclusions fail when those assumptions drift.

### Data-generating model

For case `i` in period `t`:

* the model is correct with probability `p_t`;
* the reviewer is substantively engaged with probability `e_t`;
* an engaged reviewer overrides a wrong answer with probability `d_t`;
* an engaged reviewer overrides a correct answer with probability `f`;
* a disengaged reviewer overrides with probability `q`.

The expected override rate is:

```text
R_t = e_t [d_t(1 - p_t) + f p_t] + (1 - e_t) q
```

The reference values `d=.75`, `f=.05`, and `q=.04` are illustrative. They are
not claimed to be calibrated to any deployment.

An imperfect process measure `Z`, such as whether primary evidence was opened
before sign-off, is generated with sensitivity `s` and false-positive rate `g`:

```text
P(Z_t = 1) = g_t + (s_t - g_t)e_t
```

Opening evidence is not engagement by definition. It is a noisy behavioral
proxy whose calibration would need independent validation.

### Scenarios

| Scenario | Model accuracy | Engagement | Detection | Proxy calibration | Purpose |
|---|---|---|---|---|---|
| Improvement only | .60 to .88 | .90 constant | .75 constant | stable | reference |
| Exact equivalent disengagement | .60 constant | .90 to .292 | .75 constant | stable | constructive proof |
| Mixed | .60 to .75 | .90 to .55 | .75 constant | stable | both processes move |
| Stable negative control | .75 constant | .75 constant | .75 constant | stable | false-positive check |
| Detection drift | .60 constant | .90 constant | .75 to .30 | stable | override-model misspecification |
| Proxy drift | .60 constant | .90 constant | .75 constant | sensitivity .90 to .65 | proxy misspecification |

All main probability paths are linear so that the estimand below is exactly an
endpoint change. Nonlinear paths require a different estimand or a richer trend
model.

### Estimands

```text
theta_p = p_T - p_1
theta_e = e_T - e_1
```

Engagement is only one necessary component of meaningful oversight. Detection,
intervention thresholds, reviewer skill, and case mix can change independently.

### Methods

**Override only**

Reports equivalence sets and an expected-data likelihood ridge. It does not
report a point estimate of engagement.

**Accuracy audit plus override**

Fits the endpoints of linear `p_t` and `e_t` paths by constrained joint binomial
likelihood. It assumes `d`, `f`, and `q` are known and constant. The
detection-drift scenario intentionally violates this assumption.

**Accuracy audit plus calibrated proxy**

Fits `p_t` from an independently adjudicated accuracy sample and `e_t` from an
independent proxy sample by constrained binomial likelihood. This is a
best-case benchmark because `s` and `g` are treated as known and stable. The
proxy-drift scenario and calibration grid show why that assumption matters.

**Independent override predictive check**

The audit-plus-proxy fit is used to predict the override path under the stated
`d`, `f`, and `q`. A covariance-adjusted chi-square discrepancy checks whether
the independent measurements and override data are mutually compatible. A
rejection means that the stated measurement model is incomplete. It does not,
by itself, identify which omitted mechanism changed.

### Performance measures

The Monte Carlo output reports:

* bias and RMSE;
* empirical standard deviation and mean model-based standard error;
* approximate 95% Wald interval coverage;
* Monte Carlo standard errors for bias and coverage;
* optimizer convergence and boundary-hit rates;
* predictive-check rejection rates;
* secondary labels for statistically detected `p` and `e` trends.

The trend labels are not called mechanism classification. A detection-drift or
case-mix process can share the same `p,e` label while having a different cause.

The Wald intervals are a diagnostic, not the final inferential method for a
deployed study. Near a weak-identification ridge, profile-likelihood or
bootstrap intervals are preferable.

## Identification statement

With override rate alone, every feasible pair satisfying

```text
e = (R - q) / [d(1 - p) + f p - q]
```

is observationally equivalent under the model. Model accuracy and engagement
are not jointly point identified whenever more than one feasible pair exists.

Even after model accuracy is independently measured, engagement is only
identified under assumptions about `d`, `f`, and `q`. When

```text
|d(1 - p) + f p - q|
```

approaches zero, the problem is weakly identified and small sampling or
calibration errors can create large engagement errors.

## Reproduction

The verified run used Python 3.12 in the bundled Anaconda environment. From
this directory:

```bash
MPLCONFIGDIR=/tmp/accountability_mpl \
  python simulation_v2.py --config config.json --output-dir outputs

MPLCONFIGDIR=/tmp/accountability_mpl \
  python -m unittest discover -s tests -v
```

Package requirements are recorded in `requirements.txt`; exact versions for a
run are written to `outputs/run_manifest.json`. The master seed, parameter
ranges, sample sizes, and replication count are all in `config.json`.

## Outputs

Figures:

1. `figure_1_scenarios.png`: specified accuracy, engagement, override, and
   proxy paths
2. `figure_2_equivalence.png`: analytic curves and accepted smooth paths
3. `figure_3_likelihood_ridge.png`: expected-data likelihood ridge
4. `figure_4_recovery.png`: at a 10% audit share, RMSE and coverage averaged
   over four correctly specified scenarios, plus predictive checks for the
   stable and misspecified scenarios; the panel also discloses the maximum
   small-sample boundary-hit rate
5. `figure_5_sensitivity.png`: sensitivity to `d`, `f`, and `q`
6. `figure_6_proxy_calibration.png`: bias under proxy-calibration error

Checked-in machine-readable CSVs contain scenario paths, candidate paths,
likelihood values, recovery summaries, trend-regime summaries, assumption
checks, and sensitivity results. The full replication-level file
`outputs/monte_carlo_replications.csv` is generated by the script but is not
committed because of its size.

## Interpretation boundaries

Supported:

> Under a stated binary engagement model, override rate alone does not jointly
> identify model accuracy and reviewer engagement.

> The study constructs observationally equivalent processes and shows how
> independent measurements change estimation error under explicit assumptions.

> Calibration drift can make a precise estimate wrong, so incompatible data
> channels should trigger an unresolved-assumption finding rather than an
> automatic disengagement conclusion.

Not supported:

* falling override rates show that real reviewers are disengaging;
* a process log proves meaningful review;
* the reference parameters are realistic for a particular organization;
* the simulation establishes causality;
* the current aggregate model is robust to reviewer clustering, changing case
  mix, correlated human and model errors, or serial dependence;
* the model contains evidence about young people or learning.

## Separate future experiment

A Human First versus AI First study is a different project. Human First is an
experimentally assigned interface condition, engagement is a latent mechanism,
and override is an observed transition. They should not be treated as the same
variable.

A credible future experiment would randomize workflow order, require an
initial unaided commitment, insert controlled wrong-AI trials, measure decision
revisions and calibration, and test later AI-absent performance. The current
repository does not claim to have run that experiment.

## Methodological grounding

The structure follows the ADEMP reporting logic for simulation studies in
Morris, White, and Crowther (2019): https://doi.org/10.1002/sim.8086

The distinction between reliance, appropriate reliance, and agreement is
informed by Schemmer et al. (2023): https://doi.org/10.1145/3581641.3584066

For the separate future workflow experiment, Buçinca, Malaya, and Gajos (2021)
motivate commit-before-AI and controlled wrong-AI trials:
https://doi.org/10.1145/3449287

Bastani et al. (2025) motivate measuring both AI-present performance and later
AI-absent performance: https://doi.org/10.1073/pnas.2422633122
