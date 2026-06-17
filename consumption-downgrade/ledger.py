#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""消费降级战绩账本 (ledger) —— 记录每次判决并播报累计战绩。

用法:
  python3 ledger.py add --item "戴森吹风机" --price 3000 --verdict dont
  python3 ledger.py add --item "Kindle" --price 800 --verdict buy --saved 150 --note "比官网便宜的渠道"
  python3 ledger.py stats        # 只播报累计战绩,不记新账

verdict: buy(放行) / wait(缓一缓) / dont(别买)
--saved 不传时按规则推断: dont -> price(本来要花的钱省下了), wait/buy -> 0(可显式覆盖)。
数据存在同目录 ledger.jsonl,一行一条,坏行会被跳过而不是毁掉整个账本。
"""
import argparse
import datetime
import json
import os

LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ledger.jsonl")

VERDICT_LABEL = {"buy": "✅ 放行", "wait": "⏳ 缓一缓", "dont": "❌ 拦下"}


def load():
    rows = []
    if not os.path.exists(LEDGER):
        return rows
    with open(LEDGER, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue  # 跳过坏行,不让一行毁掉整个账本
    return rows


def fmt(n):
    return f"{float(n):,.0f}"


def print_stats(rows=None):
    rows = load() if rows is None else rows
    total = len(rows)
    if total == 0:
        print("📓 战绩账本还是空的 —— 这是第一次审讯,今天开张。")
        return
    bought = sum(1 for r in rows if r.get("verdict") == "buy")
    blocked = sum(1 for r in rows if r.get("verdict") in ("dont", "wait"))
    saved = sum(float(r.get("saved") or 0) for r in rows)
    print("━━━━━━━━━━━━━━━━━━━━━━")
    print("📓 消费降级战绩(累计)")
    print(f"  审讯 {total} 件 · 拦下 {blocked} 件 · 放行 {bought} 件")
    print(f"  累计帮你守住 ¥{fmt(saved)}")
    print("━━━━━━━━━━━━━━━━━━━━━━")


def cmd_add(a):
    saved = a.saved
    if saved is None:
        saved = a.price if a.verdict == "dont" else 0.0
    row = {
        "date": datetime.date.today().isoformat(),
        "item": a.item,
        "price": a.price,
        "verdict": a.verdict,
        "saved": saved,
    }
    if a.tax is not None:
        row["tax_index"] = a.tax
    if a.note:
        row["note"] = a.note
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    label = VERDICT_LABEL.get(a.verdict, a.verdict)
    print(f"已记账:{label} · {a.item} · ¥{fmt(a.price)} · 本次省 ¥{fmt(saved)}")
    print()
    print_stats()


def main():
    p = argparse.ArgumentParser(description="消费降级战绩账本")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("add", help="记一次判决并播报累计战绩")
    pa.add_argument("--item", required=True, help="商品名")
    pa.add_argument("--price", type=float, default=0.0, help="价格(不确定就填估值)")
    pa.add_argument("--verdict", required=True, choices=["buy", "wait", "dont"])
    pa.add_argument("--saved", type=float, default=None, help="本次省下的钱;不传则按 verdict 推断")
    pa.add_argument("--tax", type=int, default=None, choices=[0, 1, 2, 3, 4, 5], help="智商税指数 0-5")
    pa.add_argument("--note", default=None, help="备注(可选)")
    pa.set_defaults(func=cmd_add)

    ps = sub.add_parser("stats", help="只播报累计战绩,不记新账")
    ps.set_defaults(func=lambda a: print_stats())

    a = p.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
