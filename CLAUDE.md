# INTENT-FORGE ROUTER

## Routing Rules

On user input, execute the 8-step pipeline below. Load each agent via `agents/{name}.md` on demand. Persist all state to `state/session.json` after each step.

## Pipeline

1. **PARSE** → `agents/orchestrator.md` → Extract `parsed`: domain, complexity, output_type, key_verbs
2. **DESIGN** → `agents/orchestrator.md` → Select team (max 4) from archetypes
3. **PLAN** → `agents/orchestrator.md` → Task definitions + skill assignments per agent
4. **RESEARCH** → `agents/researcher.md` → If researcher in team: structured findings → `research_output`. Else: skip, set null
5. **STRUCTURE** → `agents/generator.md` → Design file tree (max 12 files, ≤200 lines each)
6. **WRITE** → `agents/generator.md` → Write files to `output/`, log `✅ wrote [filename]`
7. **VALIDATE** → `agents/reviewer.md` → Run 10 checks (see reviewer.md)
8. **SUMMARY** → `agents/reviewer.md` → Output summary + actionable next steps

## State

Use `state/session.json` as schema template. Update after each step.

## Error Convention

On error at any step: append `{ "step": N, "agent": "<name>", "message": "<error>" }` to `state/session.json` `errors[]` and continue. Halt only if intent cannot be determined.

## Output Convention

All generated files → `output/` directory. Self-contained project ready for `gh repo create` + `git push`. STEP 8 includes copy-pasteable commands.

## Constraints

- Max agents: 4 | Max turns/agent: 3 | Max steps: 8
- Max files: 12 | Max lines/file: 200
- Output → `output/` | This file: routing logic only
