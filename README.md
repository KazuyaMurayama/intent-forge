# intent-forge

AIエージェントチーム自動生成ツール。1〜3文の目的・テーマを入力すると、最適なエージェントチーム・タスク定義・スキル構成を自動生成します。

## Usage

Claude Codeでこのリポジトリを開き、INTENTを入力:

```
INTENT: NASDAQと相関が低くリターンが高いインデックスを特定して、簡潔なレポートにまとめたい
```

## Architecture

- `CLAUDE.md` - ルーター（8ステップパイプライン制御）
- `agents/` - エージェント定義（最大4体、オンデマンドロード）
  - `orchestrator.md` - タスクルーティング・フロー管理・意図解析
  - `researcher.md` - 情報収集・分析・パターン発見
  - `generator.md` - コンテンツ・コード・構造生成
  - `reviewer.md` - バリデーション・レビュー・最終整形
- `tasks/task_schema.json` - タスク定義スキーマ
- `skills/registry.json` - スキルレジストリ
- `state/session.json` - セッション状態永続化

## Constraints

- エージェント数上限: 4体
- 各エージェント max_turns: 3
- パイプラインステップ: 8以内
- 出力ファイル数: 12以内
- 1ファイル: 200行以内
