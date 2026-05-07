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

## 🚀 自動実行ポリシー

### 確認不要で即実行する操作
- 全ファイル操作（作成・編集・削除）
- 全シェルコマンド（PowerShell, Bash, git, gh, npm, node, python）
- Git操作: add / commit / push（featureブランチ）/ pull / fetch / merge / branch -D / reset --hard
- GitHub操作: gh pr create / gh api 全般 / ブランチ削除
- パッケージ操作: npm install / pip install
- Web検索・フェッチ
- バックグラウンドプロセス起動

### 事前確認が必要な操作（例外のみ）
- `git push --force` を main / master ブランチに対して実行する場合
- `gh repo delete` 実行時

### 動作原則
- 計画提示（簡潔）→ 即実行 → 結果報告 のフロー厳守
- 事前確認文（「Should I run...?」等）を出力しない
- エラー時は即再試行 or 別アプローチで対応、判断が必要な場合のみ報告
