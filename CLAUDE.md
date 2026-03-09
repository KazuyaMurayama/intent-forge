# INTENT-FORGE ROUTER

## Routing Rules

On user input, execute the 8-step pipeline below. Load each agent via `agents/{name}.md` on demand. Persist all state to `state/session.json` after each step. On error, append to `state/session.json` `errors[]` and continue.

## Pipeline

1. **PARSE** → Load `agents/orchestrator.md` → Extract intent fields: `domain`, `complexity`, `output_type`, `key_verbs`
2. **DESIGN** → Load `agents/orchestrator.md` → Select agent team (max 4) from archetypes, assign roles
3. **PLAN** → Load `agents/orchestrator.md` → Generate task definitions + assign skills per agent (I/O, max_turns:3, skills from `skills/registry.json`, error handling)
4. **RESEARCH** → Load `agents/researcher.md` → If researcher in team: gather data, analyze, produce structured findings. If not: skip, set `research_output: null`
5. **STRUCTURE** → Load `agents/generator.md` → Design output file tree (max 12 files, each ≤200 lines), consume research_output if available
6. **WRITE** → Load `agents/generator.md` → Write files to `output/` directory sequentially, log `✅ wrote [filename]` per file
7. **VALIDATE** → Load `agents/reviewer.md` → Run all checks: CLAUDE.md purity, max_turns, file count ≤12, lines ≤200, agent count ≤4, schema compliance, DAG validity
8. **SUMMARY** → Load `agents/reviewer.md` → Output summary in required format

## Agent Loading

Load agent instructions from `agents/*.md` only when the pipeline step requires it. Do not preload all agents.

## State Schema

After each step, update `state/session.json`:
```json
{
  "version": "1.0",
  "timestamp": "",
  "current_step": 0,
  "intent": "",
  "parsed": { "domain": "", "complexity": "", "output_type": "", "key_verbs": [] },
  "team": [],
  "tasks": [],
  "skills": {},
  "research_output": null,
  "file_plan": [],
  "files_written": [],
  "validation": { "passed": false, "checks": [] },
  "errors": []
}
```

## Output Convention

All generated files are written to `output/` directory. This directory is a self-contained project ready for `gh repo create` and `git push`. STEP 8 summary includes copy-pasteable commands for GitHub repo creation and Claude Code launch.

## Constraints

- Max agents: 4
- Max turns per agent: 3
- Max pipeline steps: 8
- Max files in output: 12
- Max lines per file: 200
- Generated files go to `output/` directory
- This file: routing logic only, no documentation or explanations
