"""Generate REPORT.md from analysis results."""
import json


def generate_report():
    with open("data/results.json") as f:
        data = json.load(f)

    top = data["top_candidates"]
    all_idx = data["all_indices"]
    nasdaq_ret = data["nasdaq_annual_return_pct"]

    lines = []
    lines.append("# NASDAQ分散投資 インデックス分析レポート\n")
    lines.append(f"分析期間: {data['analysis_period']} | データソース: {data['data_source']}\n")

    # Executive Summary
    lines.append("## エグゼクティブサマリー\n")
    lines.append(f"NASDAQの年率リターン **{nasdaq_ret}%** に対し、")
    lines.append("相関が低くリターンが高いインデックスを15銘柄から特定しました。\n")
    lines.append("### 推奨 TOP 5\n")
    lines.append("| 順位 | 銘柄 | 相関係数 | 年率リターン | シャープ比 | 分散スコア |")
    lines.append("|------|------|---------|------------|-----------|-----------|")
    for i, c in enumerate(top, 1):
        lines.append(
            f"| {i} | {c['name']} ({c['ticker']}) | {c['correlation_with_nasdaq']:.4f} "
            f"| {c['annual_return_pct']:.2f}% | {c['sharpe_ratio']:.4f} "
            f"| {c['diversification_score']:.4f} |"
        )

    # Key Findings
    lines.append("\n## 主要な発見\n")
    best = top[0]
    lines.append(
        f"1. **{best['name']}** が最も優秀 — NASDAQ相関 {best['correlation_with_nasdaq']:.2f}、"
        f"年率リターン {best['annual_return_pct']:.1f}%、シャープ比 {best['sharpe_ratio']:.2f}"
    )
    lines.append(
        "2. **Gold (GLD)** と **コモディティ (DBC)** は資産クラスが異なるため、"
        "テック主導のNASDAQとの相関が構造的に低い"
    )
    lines.append(
        "3. **日経225** は地理的分散により相関が低い一方、"
        "円安効果もありドル建てリターンが良好"
    )
    lines.append(
        "4. **インド (Sensex)** と **英国 (FTSE)** も相関0.25以下で"
        "安定したリターンを記録"
    )

    # Avoid list
    high_corr = [c for c in all_idx if c["correlation_with_nasdaq"] > 0.7]
    if high_corr:
        lines.append("\n### 分散効果が低い銘柄（NASDAQ相関 > 0.7）\n")
        lines.append("| 銘柄 | 相関係数 | 年率リターン |")
        lines.append("|------|---------|------------|")
        for c in high_corr:
            lines.append(
                f"| {c['name']} | {c['correlation_with_nasdaq']:.4f} "
                f"| {c['annual_return_pct']:.2f}% |"
            )
        lines.append("\nこれらはNASDAQとの組合せによる分散効果が限定的です。\n")

    # Full table
    lines.append("## 全インデックス一覧（分散スコア降順）\n")
    lines.append("| 銘柄 | 相関 | 年率リターン | ボラティリティ | シャープ比 | スコア |")
    lines.append("|------|------|------------|-------------|-----------|--------|")
    for c in all_idx:
        lines.append(
            f"| {c['name']} | {c['correlation_with_nasdaq']:.4f} "
            f"| {c['annual_return_pct']:.2f}% | {c['annual_volatility_pct']:.2f}% "
            f"| {c['sharpe_ratio']:.4f} | {c['diversification_score']:.4f} |"
        )

    # Methodology
    lines.append("\n## 分析手法\n")
    lines.append("- **データ**: Yahoo Finance 5年間デイリー終値（調整後）")
    lines.append("- **相関**: 日次リターンのピアソン相関係数")
    lines.append("- **年率リターン**: 複利ベース `(1+累積リターン)^(1/年数) - 1`")
    lines.append("- **ボラティリティ**: 日次標準偏差 × √252")
    lines.append("- **シャープ比**: 年率リターン / 年率ボラティリティ（無リスク金利=0と仮定）")
    lines.append("- **分散スコア**: `0.5 × (1-相関の正規化) + 0.5 × リターンの正規化`")

    report = "\n".join(lines)
    with open("REPORT.md", "w") as f:
        f.write(report)
    print(f"✅ Generated REPORT.md ({len(lines)} lines)")


if __name__ == "__main__":
    generate_report()
