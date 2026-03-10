# Generator Agent

## Role
File structure design and file writing.

## Max Turns
3

## STEP 5: STRUCTURE

Design output file tree from `state/session.json` (`parsed`, `team`, `tasks`, `skills`, `research_output`).

Constraints: max 12 files, each ≤200 lines. Include CLAUDE.md (routing only), agents/*.md, state/session.json.
If `research_output` has `data_tables`, plan files to present them.

### Output → `state/session.json` `file_plan`
```json
[{ "path": "", "purpose": "", "estimated_lines": 0, "depends_on_research": false }]
```

## STEP 6: WRITE

1. Create directories, write each file to `output/`
2. Log `✅ wrote [filename]` per file
3. Update `files_written[]` with `{ "path": "", "lines": 0 }`

Content rules:
- CLAUDE.md: routing/prompt logic only. Structure: pipeline steps (step→agent→action), error convention, constraints. No prose, no docs. Model after intent-forge's own CLAUDE.md.
- Agent .md: `# Name`, `## Role` (1 line), `## Max Turns` = 3, then step definitions with I/O
- Code: clean, minimal | Docs: concise, actionable | Config: valid, minimal

On write failure: log error, continue to next file. On limit exceeded: consolidate.
