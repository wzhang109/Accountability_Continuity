# Plain-language guide

## The study in one sentence

A falling human override rate does not tell us, by itself, whether an AI system
has improved or whether people have stopped checking it carefully.

## A simple example

Imagine that reviewers initially override 30 out of every 100 AI decisions.
A year later, they override only 12.

That might be good news. The AI may now make fewer mistakes, so there is less to
correct.

It might also be bad news. Reviewers may have learned to trust the system too
much and may no longer examine the underlying evidence.

The observed number is the same in both stories. What happened underneath is
not.

This is the measurement problem the study examines.

## What the study actually does

The study does not use data from a real company or hospital. It creates
synthetic review processes whose underlying conditions are known. That makes it
possible to test what an observer could and could not infer from the recorded
metrics.

The design has four parts.

### 1. Describe how an override can happen

The model separates four things:

* how often the AI is correct;
* whether the reviewer genuinely examines the case;
* whether an engaged reviewer notices and acts on an AI error;
* whether someone overrides for another reason even without substantive review.

This separation matters. A reviewer can be engaged but fail to detect an
error. Detection ability and engagement are not the same thing.

### 2. Ask what override rate alone can reveal

For any observed override rate, there can be many combinations of AI accuracy
and reviewer engagement that produce it. The study maps this full set instead
of presenting only one hand-picked example.

The first finding is therefore mathematical: override rate alone cannot
identify both quantities.

### 3. Add independent evidence

The simulation then adds two possible sources of information:

* an independently adjudicated sample that estimates AI accuracy;
* a process measure, such as whether the reviewer opened the primary evidence.

The process measure is deliberately treated as imperfect. Opening a record is
not proof of thoughtful review. It is only a proxy whose sensitivity and
false-positive rate would need to be validated.

### 4. Test what happens when those assumptions drift

Two stress tests are included:

* reviewers remain engaged, but their ability to detect and act on errors
  declines;
* true engagement remains stable, but the process proxy becomes less reliable.

When the independent data channels no longer agree, the study reports that the
measurement model is incompatible with the observations. It does not claim to
know which omitted real-world mechanism caused the conflict.

## Initial findings

Under the illustrative assumptions:

* thousands of different accuracy and engagement paths can closely reproduce
  the same override trend;
* independent measurements reduce the ambiguity when their calibration is
  valid;
* more data reduce random error but cannot repair a wrong measurement model;
* with detection drift, a model that assumes detection is constant produces a
  precise but false engagement decline;
* an independent predictive check can flag this incompatibility;
* small samples can still push constrained estimates to probability boundaries,
  so boundary diagnostics must be reported alongside interval coverage.

These are findings about the behavior of a stated model. They are not estimates
of what is happening in any real organization.

## A 60-second spoken explanation

> My research asks what organizations can really learn from human oversight
> metrics after adopting AI. I focus on override rate, meaning how often a
> reviewer changes the AI's recommendation. A decline in that rate looks
> reassuring, but it can come from two very different processes: the AI may be
> getting more accurate, or reviewers may be checking less carefully. I first
> show mathematically that override rate alone cannot distinguish those
> explanations. I then use repeated synthetic data to test what additional
> evidence helps, such as an independent accuracy audit and a calibrated
> process measure. Finally, I introduce calibration drift to see whether the
> method can recognize when its assumptions no longer fit. The main lesson is
> not that override rate is useless. It is that a single clean metric can create
> false confidence unless it is interpreted alongside independent evidence and
> explicit assumption checks.

## Questions you should be ready to answer

### Did the study prove that reviewers disengage in practice?

No. It proves that an observed override trend is compatible with more than one
underlying process under the stated model.

### Why use simulation rather than real data?

The first question is whether the quantities are identifiable at all. In
synthetic data, the true process is known, so we can test whether a method
recovers it and how it fails. A real pilot is the next stage, not a substitute
for this identification check.

### Does opening primary evidence measure engagement?

Not directly. It is an example of an imperfect behavioral proxy. It would need
manual validation, and the study explicitly shows that proxy drift can produce
false conclusions.

### What if detection ability or intervention incentives change?

Then an override decline should not automatically be interpreted as falling
engagement. The independent-channel check may reveal that the model is
incompatible with the observations, but additional evidence is needed to
diagnose the cause.

### What would make this an empirical study?

A real study would need a stable held-out accuracy set, validated process
measures, sentinel cases with known errors, information about reviewer and case
clustering, and a plan for changes in case mix and organizational incentives.

# 中文讲解

## 一句话版本

人工推翻 AI 建议的比例下降，并不能单独告诉我们，是 AI 变准确了，还是人越来越不认真检查了。

## 这项研究到底研究什么

假设一个机构原来每 100 个 AI 建议会修改 30 个，一年后只修改 12 个。这个变化有两种完全不同的解释：

* AI 的错误变少了，所以人不需要修改那么多；
* AI 没有变好，但人逐渐形成依赖，不再认真查看原始证据。

机构表面上看到的数字相同，但背后的 oversight quality 完全不同。研究的问题就是：只看 override rate，我们到底能知道什么，又不能知道什么？

## 研究怎么设计

第一步，把模型准确率、reviewer 是否认真参与、认真参与后能否发现错误，以及没有认真参与时偶尔修改建议的概率分开。

第二步，在数学上计算：同一个 override rate 可以由哪些不同的模型准确率和 engagement 组合产生。结论是它对应的是一整组可能性，不是一个唯一答案。

第三步，反复生成我们知道真实答案的模拟数据，再加入两类额外证据：独立的模型准确率 audit，以及 reviewer 是否打开原始材料之类的 process proxy。

第四步，故意让 detection ability 或 proxy 的可靠性发生变化。如果不同数据通道互相矛盾，研究应该报告“当前测量模型不成立”，而不是强行得出“人 disengage 了”。

## 初步发现

在这组说明性的参数下，许多不同路径都可以产生近似相同的 override trend。独立 audit 和经过校准的 proxy 在假设正确时能够减少歧义；但如果 detection 或 proxy calibration 发生变化，更多数据只会让错误结论显得更精确。独立预测检查的价值，是提醒我们现有解释框架与数据不相容，而不是自动诊断真正原因。

## 不能说什么

不能说这项研究证明现实中的 reviewer 正在 disengage，也不能说打开原始材料就证明进行了有意义的审查。它目前证明的是一个 measurement problem，并展示未来的真实研究还需要收集哪些额外证据。
