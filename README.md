# intent-forge

AIエージェントチーム自動生成ツール。1〜3文の目的・テーマを入力すると、最適なエージェントチーム・タスク定義・スキル構成を自動生成します。

## Usage

Claude Codeでこのリポジトリを開き、INTENTを入力:

```
INTENT: NASDAQと相関が低くリターンが高いインデックスを特定して、簡潔なレポートにまとめたい
```

生成されたプロジェクトは `output/` ディレクトリに出力されます。

## Quick Start: 生成物からGitHubリポジトリを作成

パイプライン完了後、STEP 8のサマリーに以下のようなコマンドが表示されます:

```bash
# 1. GitHubリポジトリ作成
gh repo create intent-forge-finance --public --clone
cd intent-forge-finance

# 2. 生成ファイルをコピー
cp -r ../intent-forge/output/* .

# 3. コミット＆プッシュ
git add -A && git commit -m "Initial intent-forge generated project"
git push -u origin main

# 4. Claude Codeで開く
claude
```

## Architecture

- `CLAUDE.md` - ルーター（8ステップパイプライン制御のみ）
- `agents/` - エージェント定義（最大4体、オンデマンドロード）
  - `orchestrator.md` - 意図解析・チーム設計・タスク計画 (STEP 1-3)
  - `researcher.md` - 情報収集・分析・パターン発見 (STEP 4)
  - `generator.md` - ファイル構造設計・ファイル書き込み (STEP 5-6)
  - `reviewer.md` - バリデーション・サマリー・次のアクション提示 (STEP 7-8)
- `tasks/task_schema.json` - タスク定義スキーマ
- `skills/registry.json` - スキルレジストリ（適用条件・依存関係付き）
- `state/session.json` - セッション状態永続化
- `output/` - 生成されたプロジェクト（そのままGitHubリポジトリに変換可能）

## Pipeline

| Step | Name | Agent | Description |
|------|------|-------|-------------|
| 1 | PARSE | orchestrator | Intent解析 |
| 2 | DESIGN | orchestrator | チーム設計 |
| 3 | PLAN | orchestrator | タスク定義+スキル割当 |
| 4 | RESEARCH | researcher | データ収集・分析（チームに含まれる場合） |
| 5 | STRUCTURE | generator | ファイル構造設計 |
| 6 | WRITE | generator | ファイル書き込み→`output/` |
| 7 | VALIDATE | reviewer | 制約チェック（10項目） |
| 8 | SUMMARY | reviewer | サマリー+次のアクション |

## Constraints

- エージェント数上限: 4体
- 各エージェント max_turns: 3
- パイプラインステップ: 8以内
- 出力ファイル数: 12以内
- 1ファイル: 200行以内
