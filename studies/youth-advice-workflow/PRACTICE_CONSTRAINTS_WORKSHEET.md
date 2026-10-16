# Constraint practice worksheet

**October 16, 2026 · fictional development materials, not a ready study instrument**

Use only the supplied record. Choose Supported, Contradicted, or Not enough information and explain briefly. Unknown is not zero. The rules are fictional objectives, not school-policy recommendations.

## Y01 School exhibition plans

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

**Answer:** Supported / Contradicted / Not enough information

**Reason:** _______________________________________________

**Confidence that your answer is correct:** ____ / 100

## Y11 School science display plans

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
      "cost": 94,
      "seats": 26
    },
    {
      "name": "B",
      "cost": 128,
      "seats": null
    },
    {
      "name": "C",
      "cost": 82,
      "seats": 22
    }
  ],
  "note": "B's seat count was not recorded. All costs and seat counts are non-negative whole numbers; an unknown value is not zero."
}
```

**Claim:** Plan A is the plan to choose under the stated rule.

**Answer:** Supported / Contradicted / Not enough information

**Reason:** _______________________________________________

**Confidence that your answer is correct:** ____ / 100

## Y12 School history display plans

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
      "cost": 94,
      "seats": 26
    },
    {
      "name": "B",
      "cost": null,
      "seats": 30
    },
    {
      "name": "C",
      "cost": 82,
      "seats": 22
    }
  ],
  "note": "B's cost was not recorded. All costs and seat counts are non-negative whole numbers; an unknown value is not zero."
}
```

**Claim:** Plan B is the plan to choose under the stated rule.

**Answer:** Supported / Contradicted / Not enough information

**Reason:** _______________________________________________

**Confidence that your answer is correct:** ____ / 100

## Y13 School language display plans

```json
{
  "requirements": {
    "budget_max": 100,
    "seats_min": 20,
    "priority": "Largest seat count among plans meeting both constraints",
    "tie_break": "Lower cost when seat counts tie"
  },
  "plans": [
    {
      "name": "A",
      "cost": 96,
      "seats": 24
    },
    {
      "name": "B",
      "cost": 82,
      "seats": 22
    },
    {
      "name": "C",
      "cost": 90,
      "seats": null
    }
  ],
  "note": "C's seat count was not recorded. All costs and seat counts are non-negative whole numbers; an unknown value is not zero. If eligible plans have the same seat count, choose the lower-cost plan."
}
```

**Claim:** Plan C is the plan to choose under the stated rule.

**Answer:** Supported / Contradicted / Not enough information

**Reason:** _______________________________________________

**Confidence that your answer is correct:** ____ / 100

## Y14 School music display plans

```json
{
  "requirements": {
    "budget_max": 100,
    "seats_min": 20,
    "priority": "Largest seat count among plans meeting both constraints",
    "tie_break": "Lower cost when seat counts tie"
  },
  "plans": [
    {
      "name": "A",
      "cost": 96,
      "seats": 24
    },
    {
      "name": "B",
      "cost": 82,
      "seats": 22
    },
    {
      "name": "C",
      "cost": null,
      "seats": 18
    }
  ],
  "note": "C's cost was not recorded. All costs and seat counts are non-negative whole numbers; an unknown value is not zero. If eligible plans have the same seat count, choose the lower-cost plan."
}
```

**Claim:** Plan A is the plan to choose under the stated rule.

**Answer:** Supported / Contradicted / Not enough information

**Reason:** _______________________________________________

**Confidence that your answer is correct:** ____ / 100

