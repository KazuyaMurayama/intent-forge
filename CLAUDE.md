# INTENT-FORGE ROUTER

On user input, execute steps 1-8. Load agent from `agents/{name}.md` per step. Update `state/session.json` after each step.

## Prohibitions

- **実分析・実行の禁止**: データ取得、スクリプト実行、API呼び出し等の実作業を行わない。生成するのはプロジェクト構成のみ。
- **生成物の役割**: `output/` はユーザーが別セッションで開いて作業を開始するためのプロジェクトテンプレート。intent-forgeが実行するのではない。

## Pipeline

1. **PARSE** → `orchestrator` → Extract `parsed`
2. **DESIGN** → `orchestrator` → Select team
3. **PLAN** → `orchestrator` → Task definitions per `tasks/task_schema.json` + skills per `config/registry.json`
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

### 開発者の作業環境
- **OS:** Windows 11（Macではない）。シェルは PowerShell 5.1 / Bash（WSL/Git Bash）。`brew` / `Cmd+` / Mac専用コマンドは使用不可。パッケージ管理は `winget` / `scoop`。
- **スマートフォン:** iPhone（iOS）。Android固有の手順・adb・Play Store等は不要。
- コマンド例はPowerShell構文（`;` 連結、`$env:VAR`）で提示。macOS専用ツールを回答に含めない。

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

## ドキュメント日付ルール

レポート・分析・調査系 .md ファイルを新規作成する際は、H1直下に必ず記載:

```
作成日: YYYY-MM-DD
最終更新日: YYYY-MM-DD
```

- 更新時は **最終更新日のみ** を当日付に書き換える（作成日は固定）
- 除外: README / CLAUDE.md / FILE_INDEX / tasks.md / CHANGELOG / LICENSE

## 作業品質ルール

### Git・ブランチ管理
- 作業前: `git branch --show-current` でブランチ確認 → main以外なら `git checkout main && git pull` してから開始。

### ファイル特定（編集前）
- ユーザー発話のキーワード全てをファイル名と照合してから編集。キーワード不完全一致・候補不確かなら必ず確認。

### 成果物報告
- ファイル作成・更新・push後は必ず3列表で報告: `| 成果物 | 説明 | リンク |`
- リンクは `/blob/<実ブランチ>/<パス>` 形式。報告前に `gh api repos/OWNER/REPO/contents/PATH?ref=BRANCH` で存在確認。push前はURL生成しない。

### ドキュメント品質
- UIパス・コマンド・設定名は公式ドキュメントで確認後に記載。確認不可なら「[要確認]」と明記。
- OS/環境制約（例: Windows専用）をタスク開始時に確認。完成後に `brew`/`Cmd`/`macOS` 等をgrepして除去。

## ファイル保存ルール
- 成果物・スクリプトは本リポジトリ内のみに保存。`C:\\Users\\user\\Desktop` への出力禁止（ユーザー明示指定時を除く）。

<!-- SKILLS_RULES_START -->
## Skill 起動ルール（v2.1 / 2026-05-29）
以下のスキルは **必須・スキップ禁止**。該当シーンでは SKILL.md を読んでから作業を開始すること。

- **調査トピックを受け取ったら最初に必ず** `.claude/skills/research-deep/SKILL.md` を読み、手順に従って並列 Web リサーチを実行する
- **複雑な多段タスクに着手する前に必ず** `.claude/skills/sp-writing-plans/SKILL.md` で計画を作成し、`.claude/skills/sp-executing-plans/SKILL.md` の手順で実行する
- **レポート・ドキュメントに図表が必要な時は必ず** `.claude/skills/mermaid-agents365/SKILL.md` を読んでからダイアグラムを作成する
- **アイデア出し・選択肢の洗い出しが必要な時は** `.claude/skills/sp-brainstorming/SKILL.md` を読んでから実施する
- **成果物の納品・コミット前、または品質チェック（QC）・レビューフェーズに入る時は必ず** `.claude/skills/sp-verification-before-completion/SKILL.md` のチェックリストを実行する
- **分析・レポートの品質チェック（QC）・レビュー・共有前は必ず** `.claude/skills/analysis-qa-checklist/SKILL.md` を読んでチェックリストを実施する
- **データ品質・整合性の確認が必要な時は必ず** `.claude/skills/data-quality-audit/SKILL.md` を読んで監査を実行する
<!-- SKILLS_RULES_END -->
