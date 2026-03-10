# NASDAQ分散投資 インデックス分析

NASDAQとの相関が低く、リターンが高いインデックスを特定するデータ分析プロジェクト。

## Quick Start

```bash
pip install -r requirements.txt
python src/fetch_data.py   # Yahoo Financeからデータ取得
python src/analyze.py      # 相関・リターン分析
python src/report.py       # レポート生成
```

結果: `REPORT.md` と `data/results.json`

## 分析対象

15銘柄（米国・欧州・アジア・コモディティ・債券）の5年間デイリーデータ

## スコアリング

`diversification_score = 0.5 × (1 - 相関の正規化) + 0.5 × リターンの正規化`
