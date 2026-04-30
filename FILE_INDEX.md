# FILE_INDEX.md — intent-forge

> **新セッション開始時に必ずこのファイルを読む。**
> ファイル追加・削除・移動時は必ずこのファイルを更新すること。
> 最終更新: 2026-04-30

## 概要
AIエージェントが意図(Intent)を解析・生成・レビューするマルチエージェントフレームワーク。

**スタック:** Python, JSON, Markdown

---

## 📋 最初に読むべきファイル

| 優先度 | ファイル | 内容 |
|---|---|---|
| ★★★ | `CLAUDE.md` | 運用ルール |
| ★★★ | `agents/orchestrator.md` | オーケストレーターエージェント定義 |
| ★★ | `README.md` | 概要・使い方 |
| ★★ | `output/src/analyze.py` | 分析スクリプト |
| ★★ | `tasks/task_schema.json` | タスクスキーマ定義 |

---

## 🗂️ ディレクトリ構造

```
intent-forge/
├── CLAUDE.md                    ← 最重要ルール
├── README.md
├── agents/
│   ├── generator.md             ← 生成エージェント
│   ├── orchestrator.md          ← オーケストレーター
│   ├── researcher.md            ← リサーチエージェント
│   └── reviewer.md              ← レビューエージェント
├── skills/registry.json
├── state/session.json
├── tasks/task_schema.json
└── output/
    ├── CLAUDE.md
    ├── README.md
    ├── requirements.txt
    ├── agents/
    │   ├── data_agent.md
    │   └── report_agent.md
    ├── src/
    │   ├── analyze.py
    │   ├── fetch_data.py
    │   └── report.py
    └── state/session.json
```

---

## 📑 全ファイル一覧

| パス | 種別 | 説明 |
|---|---|---|
| `CLAUDE.md` | ドキュメント | 運用ルール |
| `README.md` | ドキュメント | プロジェクト概要 |
| `agents/orchestrator.md` | エージェント | オーケストレーター定義 |
| `agents/generator.md` | エージェント | Intent生成エージェント |
| `agents/researcher.md` | エージェント | リサーチエージェント |
| `agents/reviewer.md` | エージェント | レビューエージェント |
| `skills/registry.json` | データ | スキルレジストリ |
| `tasks/task_schema.json` | データ | タスクスキーマ定義 |
| `state/session.json` | データ | セッション状態 |
| `output/src/analyze.py` | Python | 分析スクリプト |
| `output/src/fetch_data.py` | Python | データ取得スクリプト |
| `output/src/report.py` | Python | レポート生成スクリプト |

---

## 🔖 ファイル更新ルール

1. 新ファイル追加時: 該当セクションに1行追加
2. ファイル削除・移動時: 該当行を削除または更新
3. 更新後: `git add FILE_INDEX.md && git commit -m "docs: FILE_INDEX.md更新"`
