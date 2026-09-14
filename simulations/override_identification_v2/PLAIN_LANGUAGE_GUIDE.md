# Understanding the override-rate model

**Illustrative model, not data from an organization.**

## The question in plain language

If people change fewer AI recommendations, has the AI improved, or are people
checking less? This project constructs two different processes with exactly
the same expected override rate. It then tests estimation methods on synthetic
data whose underlying process is known.

## What the symbols mean

| Symbol | Meaning in this model | What it does not establish |
|---|---|---|
| p | Probability the AI answer is correct | The quality of the eventual human decision |
| e | Probability of substantive human review | An observed or validated measure of independent thought |
| d | Probability an engaged person overrides an incorrect AI answer | Detection alone; acting on an error is also required |
| f | Probability an engaged person overrides a correct AI answer | The reason for the intervention |
| q | Probability of override without substantive review | Whether the resulting answer is correct |
| R | Overall probability of override | The quality of oversight or final accuracy |
| s, g | Sensitivity and false-positive rate of a review proxy | Known properties of a real process log |

The code retains the name `detection` for d. Its operational meaning combines
noticing an error and acting on it. The simulation does not model whether the
replacement answer after an override is correct.

## Build the equation one part at a time

Under the model, an engaged reviewer encounters an incorrect AI answer with
probability (1-p), and a correct answer with probability p. This uses the same
accuracy distribution for engaged cases as for all cases; selective review of
hard cases would require a different specification.

Among engaged cases, the override probability is:

```text
A(p) = d × (1-p) + f × p
```

Weight this by the proportion reviewed, then add overrides without substantive
review:

```text
R = e × A(p) + (1-e) × q
  = q + e × [A(p)-q]
```

The expression separates possible sources of the recorded action. It does not
tell us why any particular person acted.

## A worked example using the actual reference values

Set d=.75, f=.05, and q=.04. These are illustrative choices.

At the start, p=.60 and e=.90. Out of 1,000 cases **in expectation**:

- 900 receive substantive review;
- of those, 360 contain incorrect AI answers, and 270 are overridden;
- the remaining 540 contain correct AI answers, and 27 are overridden;
- among 100 cases without substantive review, 4 are overridden.

The total is 301 overrides: **30.10%**. Actual sampled counts fluctuate.

Now compare two endpoints:

| Quantity | Starting point | AI improves | Review declines |
|---|---:|---:|---:|
| AI accuracy p | .60 | .88 | .60 |
| Review probability e | .90 | .90 | .291724… |
| Expected override rate R | .3010 | .1246 | .1246 |

For the improving-AI endpoint:

```text
R = .90 × [.75 × .12 + .05 × .88] + .10 × .04
  = .1246
```

If accuracy stays at .60, the same rate is obtained by solving:

```text
e = (.1246-.04) / [.75 × .40 + .05 × .60-.04]
  = .291724…
```

The corresponding paths match at every modeled period, not just at these
endpoints. This equality is constructed by algebra. It is not a discovered
behavior of real people, and the paths are not the only possible explanations.

## Why extra data help only under assumptions

If p is measured independently and d, f, q are known, then:

```text
e = (R-q) / [d(1-p)+fp-q]
```

This inverse only applies when the denominator is nonzero and the implied e
lies between 0 and 1.

If the denominator is zero, engaged and unengaged cases have the same override
probability. When R=q, every e is compatible. When R differs from q, none is
compatible under those exact population assumptions. Very small denominators
make estimates sensitive to small errors.

A second channel is a proxy, such as a record-opening event:

```text
P(proxy=1) = g + (s-g)e
```

Recovering e requires externally justified s and g. If s=g, the proxy contains
no information about e. Opening a record is not proof that someone read it.

The revised estimator refuses to return finite Wald uncertainty when its
information matrix has an unresolved direction. A numerical optimizer can
converge even when a parameter cannot be learned from the measurements.

## Assumptions a real study would have to revisit

| Current choice | Why it matters outside the simulation |
|---|---|
| A binary state of substantive review | Actual review varies in depth, skill, and opportunity |
| Engaged cases have the same AI accuracy p | People may selectively review difficult or suspicious cases |
| Known d, f, q for one estimator | Incentives, reviewer skill, and permission to intervene can change |
| Known, stable s and g for the proxy estimator | Interface changes can alter logging without altering thought |
| Independent binomial measurement channels | Auditing the same cases creates dependence; reviewers and teams also cluster |
| Linear paths across 24 periods | Abrupt or nonlinear change is outside the fitted trend model |
| Model-based approximate Wald intervals | Small samples, weak information, and boundaries can distort uncertainty |

An audit of a fixed test set and an audit of current operational cases answer
different questions. A real design must define its target population and track
case mix rather than assuming that either sample represents the other.

## What the simulation contributes

Repeated synthetic draws test recovery, sampling error, approximate coverage,
and failure under selected calibration changes. An independent-channel check
compares predicted overrides with observed overrides. A rejection indicates
incompatibility with the specified measurement model. It does not diagnose
the cause; non-rejection does not prove the model is correct.

The full setup is in [methods](README.md), historical summaries in
[results](RESULTS.md), and the latest checks in
[verification](VERIFICATION_2026-09-14.md). This is a methods exercise with
substantial AI assistance, not independent external validation.

## Relation to the learning study

The simulation contains no learning process or participants. The proposed
experiment assigns a workflow and measures later performance. A pre-advice
answer is part of an intervention, not a measurement of the simulation's e.
Results from one cannot be used as evidence that the other mechanism occurs.

# 中文讲解

## 先把结论说准

这项研究说明：在指定模型下，同样的人工推翻率下降，可以由“AI 更准确”
或“人工检查减少”产生。它没有发现现实中的人正在失去判断力，也没有验证
一种完整的责任理论。

## 式子究竟在算什么

p 是 AI 答对的概率；e 是进行实质检查的概率。
d 是认真检查的人遇到错误 AI 答案后，发现问题并实际推翻的概率。
它同时包含“发现”和“行动”，不能直接当成认知能力。
f 是认真检查时推翻正确建议的概率；q 是没有实质检查时仍然推翻的概率。

```text
总体推翻率 = e × [d × (1-p) + f × p] + (1-e) × q
```

这里还假定，认真检查的案例和所有案例有相同的 AI 准确率。
如果人专门检查更难的案例，这个写法就需要调整。

## 用仓库里的数字算一次

设 d=.75、f=.05、q=.04。开始时 AI 准确率是 .60，检查概率是 .90。
每 1,000 个案例，期望有 301 个被推翻，即 30.10%。

之后，AI 准确率升到 .88、检查概率仍是 .90，推翻率变为 12.46%。
另一种情况是，AI 准确率仍为 .60，检查概率降到约 .2917，
推翻率同样是 12.46%。

第二条路径是用公式构造出来的。它说明“仅凭这个数字不能唯一判断”，
不是证明第二种情况在现实中确实发生了。模拟也没有记录推翻后的最终答案
是否正确，因此不能用它声称最终决策质量提高或下降。

## 最重要的限制

- 有了独立的 AI 准确率审计，仍然需要对 d、f、q 作出假设，才能估计 e。
- 打开原始材料只是可能有用的行为记录。它和实质检查的对应关系需要另外验证。
- 如果认真检查和没有检查时产生相同的观测概率，数据就无法区分两者。
  此时“标准误为零”不是非常确定，而是错误的数值表达。代码已加入检查。
- 更大的样本可以减少随机误差，但不能自动修复错误假设。
- 数据通道不一致，提示当前模型解释不了观测；它不会自动告诉我们到底哪里变了。
- 目前没有真实受试者、组织数据或学习效果。三组 AI 学习研究仍是下一项设计。

## 一段可用于研究交流的说明

我想了解，组织采用 AI 以后，记录下来的人工审查指标究竟能告诉我们什么。
目前我做的是一个有大量 AI 协助的模拟研究：在指定假设下，AI 更准确和人工
检查减少，可以产生相同的人工推翻率下降。我再用合成数据检查，增加独立
准确率审计和行为记录后，估计会怎样变化，以及假设出错时会发生什么。
它是帮助澄清测量问题的研究工具，还不是现实组织中的实证发现。
