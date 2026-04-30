# INTENT-FORGE ROUTER

On user input, execute steps 1-8. Load agent from `agents/{name}.md` per step. Update `state/session.json` after each step.

## Prohibitions

- **実分析・実行の禁止**: データ取得、スクリプト実行、API呼び出し等の実作業を行わない。生成するのはプロジェクト構成のみ。
- **生成物の役割**: `output/` はユーザーが別セッションで開いて作業を開始するためのプロジェクトテンプレート。intent-forgeが実行するのではない。

## Pipeline

1. **PARSE** → `orchestrator` → Extract `parsed`
2. **DESIGN** → `orchestrator` → Select team
3. **PLAN** → `orchestrator` → Task definitions per `tasks/task_schema.json` + skills per `skills/registry.json`
4. **RESEARCH** → `researcher` → If in team: `research_output`. Else: null, skip
5. **STRUCTURE** → `generator` → File tree → `file_plan`
6. **WRITE** → `generator` → Files → `output/`, log `✅ wrote [filename]`
7. **VALIDATE** → `reviewer` → 10 checks
8. **SUMMARY** → `reviewer` → Summary + next actions

## Error Convention

On error: append `{ "step": N, "agent": "", "message": "" }` to `errors[]` and continue. Halt only if intent is undetermined.

## Constraints

- Agents ≤ 4 | Turns/agent ≤ 3 | Steps ≤ 8 | Files ≤ 12 | Lines/file ≤ 200
- Output → `output/` (self-contained, ready for `gh repo create` + `git push`)
- This file: routing logic only

## 開発者情報・命名ルール

このリポジトリの開発者・所有者は **男座員也（Kazuya Oza / おざ かずや）** です。

- ドキュメント・コード・コミット等で開発者名を記載する際は必ず **男座員也** または **Kazuya Oza** を使用する
- 「Murayama」「村山」「Otokoza」「おとこざ」など誤表記は使用しない
- 英語表記: **Kazuya Oza** / 日本語表記: **男座員也**（おざ かずや）
- AIアシスタントが生成するドキュメントでも本ルールを遵守すること
