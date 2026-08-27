# Results note

## What the study establishes

The primary result is analytic, not empirical. Under the stated binary model,
the override rate

```text
R = e[d(1 - p) + fp] + (1 - e)q
```

does not jointly identify model accuracy `p` and reviewer engagement `e`.
For a fixed observed `R`, every feasible pair satisfying

```text
e = (R - q) / [d(1 - p) + fp - q]
```

is observationally equivalent.

The exact improvement and disengagement paths therefore serve as a constructive
proof. Their equality is true by construction and should not be described as a
simulation discovery.

## What the simulation adds

The simulation asks whether the ambiguity persists beyond one hand-matched
pair, how independent measurements affect recovery, and how calibration drift
can create precise but wrong conclusions.

The verified run used:

* 24 periods;
* 250, 1,000, or 4,000 operational cases per period;
* 10% or 25% independent accuracy-audit samples;
* a 25% process-proxy sample;
* 1,000 replications per scenario and design cell;
* six scenarios, including stable, detection-drift, and proxy-drift checks;
* fixed master seed `20260827`.

## Main results

### Override-only ambiguity

Of 60,000 smooth candidate endpoint pairs drawn from fixed ranges, 4,345
produced an override path within the fixed RMSE tolerance of .005. This count is
not a prevalence estimate and depends on the sampling ranges and tolerance. Its
role is to show that the result is not confined to one matched pair.

The expected-data likelihood surface forms one connected ridge. The
improvement endpoint has delta log likelihood 0.000 and the exact-equivalent
disengagement endpoint has delta log likelihood 0.077 on the finite grid.

### Recovery when assumptions hold

Across the four correctly specified scenarios, engagement-trend RMSE decreases
with sample size for both constrained estimators. At a 10% audit share:

* audit plus override mean RMSE decreases from .143 at 250 cases per period to
  .040 at 4,000;
* audit plus calibrated proxy mean RMSE decreases from .047 to .012;
* approximate interval coverage remains close to the nominal 95% level;
* the independent override predictive check rejects 5.4% of correctly
  specified replications overall.

The proxy result is a best-case benchmark because its sensitivity and
false-positive rate are treated as known and stable.

### Detection drift

When detection falls from .75 to .30 while true engagement remains .90, the
audit-plus-override estimator interprets the decline as an engagement change.
Its engagement-trend bias remains approximately minus .56 even as the sample
size grows. More observations make the wrong answer more precise rather than
repairing misspecification.

The independent-channel predictive check rejects the stated model in 99.1% of
replications at 250 cases per period and 100% at 1,000 and 4,000.

### Proxy drift

When proxy sensitivity falls from .90 to .65 while true engagement is stable,
the audit-plus-proxy estimator has engagement-trend bias of approximately minus
.28. The predictive check rejects the joint measurement model in 67.1% of
replications at 250 cases per period and 100% at 1,000 and 4,000.

### Numerical diagnostics

All 72,000 constrained fits across 36,000 replication records converged. The audit-plus-override fit hit a
probability boundary in 5.4% of replications overall and in 40.2% of the
smallest-sample improvement-only cell at a 10% audit share. The boundary rate
falls to zero in that cell at 4,000 cases per period. These diagnostics are
retained because constrained estimates can still be unstable even when they
remain physically possible.

## Defensible interpretation

The study supports this conclusion:

> Override rate is an ambiguous surface measure. Under a stated binary model,
> it cannot by itself distinguish improving model accuracy from changing human
> engagement. Independent measurements can reduce that ambiguity, but only
> under calibration assumptions that should themselves be tested.

It does not show that real reviewers are disengaging, that the illustrative
parameters are realistic, or that a process log proves substantive review.

## Remaining limitations

The current data-generating model uses independent aggregate binomial channels
and linear probability paths. It does not yet model reviewer clustering, case
difficulty, correlated human and model errors, serial dependence, or changing
case mix. The 95% intervals use expected-Fisher Wald approximations; profile or
bootstrap intervals are preferable near a weak-identification ridge. These are
future extensions, not hidden assumptions.
