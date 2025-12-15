---
description: Generate a summary of work done over a period
arguments:
  - name: period
    description: Time period (day, week, sprint, month)
    required: false
    default: week
---

# Summary Command

Generate a comprehensive summary of work completed over a time period.

## Summary Types

### Daily Summary
Focus on:
- Tasks completed
- Commits made
- Hours worked (if tracked)
- Key achievements

### Weekly Summary
Focus on:
- Tasks completed this week
- Progress on major features
- Blockers encountered and resolved
- Key decisions made
- Next week's priorities

### Sprint Summary
Focus on:
- Sprint goals vs achievements
- Velocity metrics
- Carry-over items
- Retrospective points
- Next sprint planning

### Monthly Summary
Focus on:
- Major features delivered
- Project health trends
- Team productivity metrics
- Strategic accomplishments

## Output Format

```
📊 [PERIOD] SUMMARY
═══════════════════════════════════════════════════════════════

Period: [Start Date] - [End Date]

🎯 HIGHLIGHTS

• [Major achievement 1]
• [Major achievement 2]
• [Major achievement 3]

───────────────────────────────────────────────────────────────

✅ COMPLETED ([count] tasks)

Phase: [Phase Name]
├── [Task 1] - [Status: Done]
├── [Task 2] - [Status: Done]
└── [Task 3] - [Status: Done]

Phase: [Phase Name]
└── [Task 4] - [Status: Done]

───────────────────────────────────────────────────────────────

🚧 IN PROGRESS ([count] tasks)

├── [Task 5] - [X]% complete
└── [Task 6] - [X]% complete

───────────────────────────────────────────────────────────────

📈 METRICS

| Metric | This Period | Previous | Change |
|--------|-------------|----------|--------|
| Tasks Completed | 12 | 10 | +20% |
| Commits | 45 | 38 | +18% |
| PRs Merged | 8 | 6 | +33% |
| Bugs Fixed | 5 | 3 | +67% |

───────────────────────────────────────────────────────────────

🔮 NEXT PERIOD PRIORITIES

1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

───────────────────────────────────────────────────────────────

💡 NOTES & OBSERVATIONS

• [Observation 1]
• [Observation 2]
```

## Data Sources

1. Git history (commits, PRs, branches)
2. Xala PM (tasks, activities, phases)
3. Time tracking (if available)
4. Team activity (if available)

## Guidelines

- Highlight achievements, not just activity
- Include metrics where possible
- Note trends (improving/declining)
- Provide actionable next steps
- Keep it scannable

