# Fictional school-project task examples

**October 7, 2026 · eight development examples · no participants or observed results**

Use only the supplied fictional record. Choose Supported, Contradicted, or Not enough information. Advice is shown only at the assigned stage. Keys and feedback below are reviewer materials and must not appear beside a task before the response is recorded. All examples require independent review.

The four delayed examples are new related records, not psychometrically matched forms. Their stored advice variants are for development review; the delayed participant view never exposes them.

## Y01  School exhibition plans

**Illustrative phase:** practice · **Skill family:** constraints

**Fictional record**

```json
{
  "requirements": {
    "budget_max": 100,
    "seats_min": 20,
    "priority": "Largest seat count among plans meeting both constraints"
  },
  "plans": [
    {
      "name": "A",
      "cost": 96,
      "seats": 24
    },
    {
      "name": "B",
      "cost": 88,
      "seats": 18
    },
    {
      "name": "C",
      "cost": 108,
      "seats": 30
    }
  ]
}
```

**Claim:** Plan C is the plan to choose under the stated rule.

**Key:** Contradicted

**Correct prepared advice:** Contradicted. Plan C has the largest seat count, but its cost exceeds the stated budget. The rule permits comparison only among plans meeting both requirements. Plan A meets those requirements and is the eligible choice.

**Misleading prepared advice:** Supported. Plan C has the largest seat count, so it provides the most exhibition places. The stated priority is to maximize seats. Since C reaches the minimum number of seats, it is the plan to choose.

**Common verified feedback:** Contradicted. C costs 108, above the budget of 100. B has only 18 seats, below the minimum of 20. A meets both constraints. The priority applies only after checking eligibility.

**Review issue:** Budget and seating are invented task rules, not a definition of what a school ought to value.

## Y02  School newsletter workshops

**Illustrative phase:** practice · **Skill family:** rates

**Fictional record**

```json
{
  "groups": [
    {
      "name": "A",
      "invited": 60,
      "completed": 24
    },
    {
      "name": "B",
      "invited": 100,
      "completed": 35
    }
  ]
}
```

**Claim:** A larger proportion of invited students completed the workshop in Group A.

**Key:** Supported

**Correct prepared advice:** Supported. Group A has 24 completions among 60 invited students, while Group B has 35 among 100. The question asks about completion proportions. Dividing each count by its own invitation total gives A the higher proportion.

**Misleading prepared advice:** Contradicted. Group A has 24 completions while Group B has 35 completions. The question compares workshop completion, and B has the larger completion total. That larger total shows B has the higher completion proportion among invited students.

**Common verified feedback:** Supported. A has 24/60 = 40%; B has 35/100 = 35%. B has more completers, but A has the higher proportion among invited students.

**Review issue:** May test prior arithmetic knowledge; pretest whether feedback supports learning rather than ceiling performance.

## Y03  Two school club activity days

**Illustrative phase:** practice · **Skill family:** pooling

**Fictional record**

```json
{
  "groups": [
    {
      "name": "Small day",
      "total": 30,
      "completed": 15
    },
    {
      "name": "Large day",
      "total": 90,
      "completed": 18
    }
  ]
}
```

**Claim:** Across both days together, 35% of students completed all stations.

**Key:** Contradicted

**Correct prepared advice:** Contradicted. The two days have unequal numbers of students. The combined completion proportion uses total completions divided by total students. There are 33 completers out of 120 students, so the pooled percentage is 27.5 rather than 35.

**Misleading prepared advice:** Supported. The small day has a 50% completion proportion and the large day has a 20% completion proportion. Averaging these two percentages gives 35%. This average is the completion proportion across the two school activity days together.

**Common verified feedback:** Contradicted. Combine counts: (15 + 18)/(30 + 90) = 33/120 = 27.5%. The mean of day percentages weights the smaller day equally and answers a different question.

**Review issue:** Decimal calculation may add burden; adjust numbers after educator review without silently altering the scoring key.

## Y04  Classroom recycling project

**Illustrative phase:** practice · **Skill family:** causal_evidence

**Fictional record**

```json
{
  "before_week": {
    "paper_waste_sheets": 100
  },
  "after_week": {
    "paper_waste_sheets": 70
  },
  "same_class": true,
  "comparison_group": false,
  "other_changes_recorded": false
}
```

**Claim:** The new recycling project caused the entire decrease in paper waste.

**Key:** Not enough information

**Correct prepared advice:** Not enough information. Paper waste was lower in the later week, but the record has no comparison group or account of other changes. It establishes a decrease. It does not isolate how much of that decrease the recycling project caused.

**Misleading prepared advice:** Supported. Paper waste fell after the recycling project began in the same class. The record shows a decrease of 30 sheets, so this difference measures the effect of the project. The project caused the entire recorded decrease in waste.

**Common verified feedback:** Not enough information. Waste decreased by 30 sheets. Without evidence ruling out other influences, this record cannot establish that the project caused the entire decrease. It also does not establish zero effect.

**Review issue:** A plausible alternative explanation and a clearly bounded claim need human review; do not reward reflexive skepticism.

## Y05  School reading room plans

**Illustrative phase:** delayed_unaided · **Skill family:** constraints

**Fictional record**

```json
{
  "requirements": {
    "budget_max": 90,
    "seats_min": 16,
    "priority": "Largest seat count among plans meeting both constraints"
  },
  "plans": [
    {
      "name": "A",
      "cost": 92,
      "seats": 26
    },
    {
      "name": "B",
      "cost": 86,
      "seats": 22
    },
    {
      "name": "C",
      "cost": 75,
      "seats": 15
    }
  ]
}
```

**Claim:** Plan B is the plan to choose under the stated rule.

**Key:** Supported

**Correct prepared advice:** Supported. Plan B stays within the budget and provides at least the required number of seats. Plan A costs too much, and Plan C has too few seats. B is the only eligible plan under the stated decision rule.

**Misleading prepared advice:** Contradicted. Plan A offers more seats than Plan B and therefore best meets the priority of maximizing seating. Both A and B exceed the required minimum number of seats. The plan with the larger seating total is the one to choose.

**Common verified feedback:** Supported. B costs 86, within the budget of 90, and has 22 seats, at least 16. A fails the budget requirement and C fails the seating requirement.

**Review issue:** The example deliberately changes the correct label and winning plan; this does not establish equal difficulty across forms.

## Y06  School planting sessions

**Illustrative phase:** delayed_unaided · **Skill family:** rates

**Fictional record**

```json
{
  "groups": [
    {
      "name": "X",
      "invited": 80,
      "completed": 32
    },
    {
      "name": "Y",
      "invited": 50,
      "completed": 25
    }
  ]
}
```

**Claim:** A larger proportion of invited students completed the session in Group X.

**Key:** Contradicted

**Correct prepared advice:** Contradicted. Group X has more completers, but it also invited more students. The relevant proportions are 32 out of 80 and 25 out of 50. Comparing those proportions gives Y, rather than X, the higher completion proportion.

**Misleading prepared advice:** Supported. Group X has 32 completers, compared with 25 in Group Y. The question asks which session achieved more completion, and X has the larger recorded total. That larger completion total shows X had the higher proportion among invited students.

**Common verified feedback:** Contradicted. X has 32/80 = 40%, while Y has 25/50 = 50%. More completers does not establish a higher completion proportion.

**Review issue:** A related new task measures near transfer, not broad independent judgment or real-world decision quality.

## Y07  Two school library activity days

**Illustrative phase:** delayed_unaided · **Skill family:** pooling

**Fictional record**

```json
{
  "groups": [
    {
      "name": "Small day",
      "total": 40,
      "completed": 12
    },
    {
      "name": "Large day",
      "total": 80,
      "completed": 48
    }
  ]
}
```

**Claim:** Across both days together, 50% of students completed all activities.

**Key:** Supported

**Correct prepared advice:** Supported. The combined proportion uses total completions divided by total students. There are 12 plus 48 completions among 40 plus 80 students. The resulting 60 out of 120 is 50%, matching the claim about both days together.

**Misleading prepared advice:** Contradicted. The small day has a 30% completion proportion and the large day has a 60% completion proportion. Averaging these percentages gives 45%. That is the combined completion proportion, so the claim that half of students completed is false.

**Common verified feedback:** Supported. (12 + 48)/(40 + 80) = 60/120 = 50%. The 45% mean weights days equally, rather than weighting each student equally.

**Review issue:** The phrase across both days must be understood consistently; no real school events are represented.

## Y08  School art project display

**Illustrative phase:** delayed_unaided · **Skill family:** causal_evidence

**Fictional record**

```json
{
  "before_week": {
    "average_visitors": 40
  },
  "after_week": {
    "average_visitors": 55
  },
  "same_room": true,
  "comparison_group": false,
  "other_changes_recorded": false
}
```

**Claim:** Changing the display caused the entire increase in average visitors.

**Key:** Not enough information

**Correct prepared advice:** Not enough information. Average visitors increased after the display changed, but the record gives no comparison group or information about other changes. The increase is observed. The share of the increase caused by the display change is not established.

**Misleading prepared advice:** Supported. Average visitors increased from 40 to 55 after the display changed in the same room. This before-and-after difference is 15 visitors, so it measures the effect of changing the display. The changed display caused the entire recorded increase.

**Common verified feedback:** Not enough information. An increase of 15 visitors was observed. The record does not separate the display change from other possible influences and does not establish that it had no effect.

**Review issue:** Same answer category as its practice counterpart could cue memorization; expand and balance the full bank.

## What is still missing

These examples contain three Supported, three Contradicted and two Not enough information keys. A complete study requires 30 distinct items: six baseline, twelve practice, eight delayed and four challenge. Twenty-two items and the actual counterbalanced lists remain to be developed. Keys, challenge difficulty, wording and advice plausibility need educator review and pretesting. Passing structural checks is not validation with adolescents.
