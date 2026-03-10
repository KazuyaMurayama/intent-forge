# Reviewer Agent

## Role
Validation and summary output.

## Max Turns
3

## STEP 7: VALIDATE

Run 10 checks on generated output:

| # | Check | Criterion |
|---|-------|-----------|
| 1 | claude_md_purity | CLAUDE.md has only routing logic, no docs |
| 2 | max_turns_defined | Every agents/*.md has `## Max Turns` = 3 |
| 3 | file_count | Total files ≤ 12 |
| 4 | line_count | Each file ≤ 200 lines |
| 5 | agent_count | ≤ 4 agents in team |
| 6 | state_schema | session.json has all required fields with correct types |
| 7 | no_monolith | No file has >40% of total logic |
| 8 | task_schema | Each task has: agent, task, input, output, max_turns, skills, depends_on |
| 9 | dag_valid | No cycles in task dependency graph |
| 10 | skill_valid | All skill IDs exist in registry.json and match applicable_agents |

### Output → `state/session.json` `validation`
```json
{ "passed": true, "checks": [{ "name": "", "passed": true, "detail": "" }] }
```

Auto-fix: line count (split file), missing max_turns (add it). Report unfixable in summary.

## STEP 8: SUMMARY

```
=== INTENT-FORGE COMPLETE ===
INTENT: [original input]
AGENTS: [names]
TASKS: [descriptions]
FILES: [count]
VALIDATION: [PASSED | FAILED (N issues)]
REPO: intent-forge-[domain]-[YYYYMMDD-HHMM]

--- NEXT ACTIONS ---
1. gh repo create intent-forge-[domain] --public --clone
   cd intent-forge-[domain]
   cp -r ./output/* .
   git add -A && git commit -m "Initial intent-forge generated project"
   git push -u origin main
2. claude
3. INTENT: [original input]
```
