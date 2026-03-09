# INTENT-FORGE ROUTER

## Routing Rules

On user input, execute the 8-step pipeline below. Load each agent via `agents/{name}.md` on demand. Persist all state to `state/session.json` after each step. On error, append to `state/session.json` `errors[]` and continue.

## Pipeline

1. **PARSE** → Load `agents/orchestrator.md` → Extract intent fields: `domain`, `complexity`, `output_type`, `key_verbs`
2. **DESIGN** → Load `agents/orchestrator.md` → Select agent team (max 4) from archetypes, assign roles
3. **DEFINE** → Load `agents/orchestrator.md` → Generate task definitions per agent (I/O, max_turns:3, error handling)
4. **SKILLS** → Load `agents/orchestrator.md` → Select skills per agent from `skills/registry.json`
5. **STRUCTURE** → Load `agents/generator.md` → Design output file tree (max 12 files, each ≤200 lines)
6. **WRITE** → Load `agents/generator.md` → Write files sequentially, log `✅ wrote [filename]` per file
7. **VALIDATE** → Load `agents/reviewer.md` → Check: no docs in CLAUDE.md, max_turns defined, file count ≤12, lines ≤200
8. **SUMMARY** → Load `agents/reviewer.md` → Output summary in required format

## Agent Loading

Load agent instructions from `agents/*.md` only when the pipeline step requires it. Do not preload all agents.

## State Management

After each step, update `state/session.json`:
```json
{
  "current_step": <1-8>,
  "intent": "<original input>",
  "parsed": {},
  "team": [],
  "tasks": [],
  "skills": [],
  "files_written": [],
  "validation": {},
  "errors": []
}
```

## Constraints

- Max agents: 4
- Max turns per agent: 3
- Max pipeline steps: 8
- Max files in output: 12
- Max lines per file: 200
- This file: routing logic only, no documentation or explanations
