# 结案盖章小票模板 (receipt)

判决 + 记账完成后,用这个模板给用户渲染一张**盖章小票**(仿热敏纸收据 + 橡皮印章)。

## 怎么用

1. **先**跑 `ledger.py add` 记账,拿到最新累计战绩数字(审讯/拦下/守住)。
2. 复制下面「主体模板」的整段 SVG,把所有 `{{占位符}}` 换成本单真实数据。
3. **按判决档位**,从「印章库」里挑对应那一枚 `<g>`(✅绿 / ⏳橙 / ❌红,各带不同表情),整段粘到 `{{STAMP}}` 的位置。
4. 用 `show_widget`(visualize 工具)渲染最终 SVG。最终代码里**不能残留任何 `{{}}`**。

## 规矩

- 维度名按品类换(耐用品 6 维 / 消耗品把"吃灰·操作税"换成"复购·囤货")。
- 分数照实填,**缺数据维度别为了凑小票编分**——没填满就别出小票,或把缺的维度分数写"—"。
- 否决项在维度名里带「〔否决〕」;最低分那维可在名字后缀「← 软肋」。
- 这步是锦上添花,用户不想要可以不做。

## 占位符

| 占位符 | 含义 | 示例 |
|---|---|---|
| `{{NO}}` | 单号(日期+序号) | `20260617-001` |
| `{{DATE}}` | 日期 | `2026-06-17` |
| `{{ITEM}}` | 商品名 | `半自动咖啡机 + 意式磨豆机` |
| `{{TIER}}` | 规格/档 副标 | `参数说得过去档` |
| `{{PRICE}}` | 价格 | `¥3,000–5,000` |
| `{{DIM1}}`–`{{DIM6}}` | 维度名(可带〔否决〕/← 软肋) | `① 使用频率 / 吃灰` |
| `{{S1}}`–`{{S6}}` | 各维分数(0–5 的数字) | `3` |
| `{{TOTAL}}` | 总分(0–30) | `18` |
| `{{COST}}` | 真实成本/杯或/年 | `≈ ¥10` |
| `{{NA}}` `{{NB}}` `{{SAVED}}` | 累计审讯 / 拦下 / 守住金额 | `1` `1` `¥0` |
| `{{FOOT}}` | 底部一句毒舌结语 | `恕不为冲动消费背书` |
| `{{STAMP}}` | 判决印章(从下方印章库选一枚粘入) | — |

---

## 印章库(按判决选一枚,替换 `{{STAMP}}`)

### ✅ 可以买(绿)

```svg
<g transform="translate(356,378) rotate(-11)" opacity="0.9" font-family="var(--font-sans)">
<circle r="43" fill="none" stroke="#3B6D11" stroke-width="2.6"/>
<circle r="36" fill="none" stroke="#3B6D11" stroke-width="1"/>
<path id="stamparc" d="M-32,0 A 32 32 0 0 1 32,0" fill="none"/>
<text font-size="8" letter-spacing="1.5" fill="#3B6D11"><textPath href="#stamparc" startOffset="50%" text-anchor="middle">消费降级监督所</textPath></text>
<path d="M-10,-14 Q-7,-17 -4,-14" stroke="#3B6D11" stroke-width="1.4" fill="none" stroke-linecap="round"/>
<path d="M4,-14 Q7,-17 10,-14" stroke="#3B6D11" stroke-width="1.4" fill="none" stroke-linecap="round"/>
<path d="M-7,-3 Q0,5 7,-3" stroke="#3B6D11" stroke-width="1.6" fill="none" stroke-linecap="round"/>
<text x="0" y="17" font-size="15" font-weight="500" text-anchor="middle" letter-spacing="3" fill="#3B6D11">可以买</text>
<text x="0" y="31" font-size="7" text-anchor="middle" letter-spacing="2" fill="#3B6D11">APPROVED · 去吧</text>
<line x1="-38" y1="-14" x2="33" y2="26" stroke="#F4F2EC" stroke-width="1.6" opacity="0.55" stroke-linecap="round"/>
<line x1="-26" y1="30" x2="38" y2="-22" stroke="#F4F2EC" stroke-width="1.3" opacity="0.45" stroke-linecap="round"/>
</g>
```

### ⏳ 缓一缓(橙)

```svg
<g transform="translate(356,378) rotate(-13)" opacity="0.9" font-family="var(--font-sans)">
<circle r="43" fill="none" stroke="#C2542F" stroke-width="2.6"/>
<circle r="36" fill="none" stroke="#C2542F" stroke-width="1"/>
<path id="stamparc" d="M-32,0 A 32 32 0 0 1 32,0" fill="none"/>
<text font-size="8" letter-spacing="1.5" fill="#C2542F"><textPath href="#stamparc" startOffset="50%" text-anchor="middle">消费降级监督所</textPath></text>
<path d="M-12,-19 L-4,-20" stroke="#C2542F" stroke-width="1.3" fill="none" stroke-linecap="round"/>
<path d="M4,-21 L12,-19" stroke="#C2542F" stroke-width="1.3" fill="none" stroke-linecap="round"/>
<circle cx="-7" cy="-13" r="2" fill="#C2542F"/>
<circle cx="7" cy="-13" r="2" fill="#C2542F"/>
<path d="M-6,-3 Q1,-6 7,-2" stroke="#C2542F" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<path d="M15,-16 q-3,4 0,6 q3,-2 0,-6 z" fill="#C2542F"/>
<text x="0" y="17" font-size="15" font-weight="500" text-anchor="middle" letter-spacing="3" fill="#C2542F">缓一缓</text>
<text x="0" y="31" font-size="7" text-anchor="middle" letter-spacing="2" fill="#C2542F">PENDING · 再想想</text>
<line x1="-38" y1="-14" x2="33" y2="26" stroke="#F4F2EC" stroke-width="1.6" opacity="0.55" stroke-linecap="round"/>
<line x1="-26" y1="30" x2="38" y2="-22" stroke="#F4F2EC" stroke-width="1.3" opacity="0.45" stroke-linecap="round"/>
</g>
```

### ❌ 别买(红)

```svg
<g transform="translate(356,378) rotate(-15)" opacity="0.9" font-family="var(--font-sans)">
<circle r="43" fill="none" stroke="#A32D2D" stroke-width="2.6"/>
<circle r="36" fill="none" stroke="#A32D2D" stroke-width="1"/>
<path id="stamparc" d="M-32,0 A 32 32 0 0 1 32,0" fill="none"/>
<text font-size="8" letter-spacing="1.5" fill="#A32D2D"><textPath href="#stamparc" startOffset="50%" text-anchor="middle">消费降级监督所</textPath></text>
<path d="M-12,-17 L-4,-14" stroke="#A32D2D" stroke-width="1.4" fill="none" stroke-linecap="round"/>
<path d="M4,-14 L12,-17" stroke="#A32D2D" stroke-width="1.4" fill="none" stroke-linecap="round"/>
<circle cx="-7" cy="-12" r="2" fill="#A32D2D"/>
<circle cx="7" cy="-12" r="2" fill="#A32D2D"/>
<path d="M-7,-1 Q0,-7 7,-1" stroke="#A32D2D" stroke-width="1.6" fill="none" stroke-linecap="round"/>
<text x="0" y="17" font-size="15" font-weight="500" text-anchor="middle" letter-spacing="3" fill="#A32D2D">别　买</text>
<text x="0" y="31" font-size="7" text-anchor="middle" letter-spacing="2" fill="#A32D2D">REJECTED · 收手</text>
<line x1="-38" y1="-14" x2="33" y2="26" stroke="#F4F2EC" stroke-width="1.6" opacity="0.55" stroke-linecap="round"/>
<line x1="-26" y1="30" x2="38" y2="-22" stroke="#F4F2EC" stroke-width="1.3" opacity="0.45" stroke-linecap="round"/>
</g>
```

---

## 主体模板(替换占位符 + 粘入 `{{STAMP}}`,再 show_widget)

```svg
<svg viewBox="0 0 560 606" xmlns="http://www.w3.org/2000/svg" role="img" width="100%">
<title>消费降级判决书·盖章小票</title>
<desc>仿购物小票的六维评分与累计战绩,判决处盖橡皮印章</desc>
<path d="M98,22 L111,13 L124,22 L137,13 L150,22 L163,13 L176,22 L189,13 L202,22 L215,13 L228,22 L241,13 L254,22 L267,13 L280,22 L293,13 L306,22 L319,13 L332,22 L345,13 L358,22 L371,13 L384,22 L397,13 L410,22 L423,13 L436,22 L449,13 L462,22 Z" fill="#F4F2EC"/>
<rect x="98" y="22" width="364" height="566" fill="#F4F2EC"/>
<path d="M98,588 L111,597 L124,588 L137,597 L150,588 L163,597 L176,588 L189,597 L202,588 L215,597 L228,588 L241,597 L254,588 L267,597 L280,588 L293,597 L306,588 L319,597 L332,588 L345,597 L358,588 L371,597 L384,588 L397,597 L410,588 L423,597 L436,588 L449,597 L462,588 Z" fill="#F4F2EC"/>
<g font-family="var(--font-mono)">
<text x="280" y="39" font-size="15" font-weight="500" text-anchor="middle" letter-spacing="4" fill="#2B2B28">消费降级监督所</text>
<text x="280" y="54" font-size="9" text-anchor="middle" letter-spacing="2" fill="#77756D">CONSUMPTION DOWNGRADE BUREAU</text>
<text x="280" y="70" font-size="10" text-anchor="middle" fill="#77756D">—— 反剁手审讯收据 ——</text>
<line x1="110" y1="81" x2="450" y2="81" stroke="#B6B4AC" stroke-dasharray="2 3"/>
<text x="120" y="98" font-size="10" fill="#2B2B28">单号  {{NO}}</text>
<text x="120" y="113" font-size="10" fill="#2B2B28">日期  {{DATE}}</text>
<text x="440" y="113" font-size="10" text-anchor="end" fill="#2B2B28">审讯员 监督员</text>
<line x1="110" y1="124" x2="450" y2="124" stroke="#B6B4AC" stroke-dasharray="2 3"/>
<text x="120" y="143" font-size="11" fill="#2B2B28">{{ITEM}}</text>
<text x="120" y="158" font-size="9.5" fill="#77756D">{{TIER}}</text>
<text x="440" y="158" font-size="11" text-anchor="end" fill="#2B2B28">{{PRICE}}</text>
<line x1="110" y1="170" x2="450" y2="170" stroke="#B6B4AC" stroke-dasharray="2 3"/>
<text x="120" y="186" font-size="9.5" fill="#77756D">评分明细 / 满分 30 分</text>
<text x="120" y="207" font-size="11" fill="#2B2B28">{{DIM1}}</text>
<text x="440" y="207" font-size="11" text-anchor="end" fill="#2B2B28">{{S1}} / 5</text>
<text x="120" y="228" font-size="11" fill="#2B2B28">{{DIM2}}</text>
<text x="440" y="228" font-size="11" text-anchor="end" fill="#2B2B28">{{S2}} / 5</text>
<text x="120" y="249" font-size="11" fill="#2B2B28">{{DIM3}}</text>
<text x="440" y="249" font-size="11" text-anchor="end" fill="#2B2B28">{{S3}} / 5</text>
<text x="120" y="270" font-size="11" fill="#2B2B28">{{DIM4}}</text>
<text x="440" y="270" font-size="11" text-anchor="end" fill="#2B2B28">{{S4}} / 5</text>
<text x="120" y="291" font-size="11" fill="#2B2B28">{{DIM5}}</text>
<text x="440" y="291" font-size="11" text-anchor="end" fill="#2B2B28">{{S5}} / 5</text>
<text x="120" y="312" font-size="11" fill="#2B2B28">{{DIM6}}</text>
<text x="440" y="312" font-size="11" text-anchor="end" fill="#2B2B28">{{S6}} / 5</text>
<line x1="110" y1="325" x2="450" y2="325" stroke="#B6B4AC" stroke-dasharray="2 3"/>
<text x="120" y="346" font-size="13" font-weight="500" fill="#2B2B28">合　计</text>
<text x="440" y="347" font-size="16" font-weight="500" text-anchor="end" fill="#2B2B28">{{TOTAL}} / 30</text>
<text x="120" y="368" font-size="11" fill="#2B2B28">判　决</text>
<text x="120" y="388" font-size="10" fill="#77756D">真实成本 / 杯</text>
<text x="440" y="388" font-size="11" text-anchor="end" fill="#2B2B28">{{COST}}</text>
<line x1="110" y1="400" x2="450" y2="400" stroke="#B6B4AC" stroke-dasharray="2 3"/>
<line x1="110" y1="403" x2="450" y2="403" stroke="#B6B4AC" stroke-dasharray="2 3"/>
<text x="280" y="420" font-size="10" text-anchor="middle" letter-spacing="3" fill="#77756D">会 员 战 绩 卡</text>
<text x="120" y="438" font-size="10.5" fill="#2B2B28">累计审讯</text>
<text x="440" y="438" font-size="10.5" text-anchor="end" fill="#2B2B28">{{NA}} 件</text>
<text x="120" y="454" font-size="10.5" fill="#2B2B28">成功拦下</text>
<text x="440" y="454" font-size="10.5" text-anchor="end" fill="#2B2B28">{{NB}} 件</text>
<text x="120" y="471" font-size="11" fill="#2B2B28">守住金额</text>
<text x="440" y="471" font-size="13" font-weight="500" text-anchor="end" fill="#2B2B28">{{SAVED}}</text>
<line x1="110" y1="485" x2="450" y2="485" stroke="#B6B4AC" stroke-dasharray="2 3"/>
<g fill="#2B2B28">
<rect x="210" y="495" width="2" height="28"/><rect x="217" y="495" width="1" height="28"/><rect x="224" y="495" width="3" height="28"/><rect x="231" y="495" width="1" height="28"/><rect x="238" y="495" width="2" height="28"/><rect x="245" y="495" width="3" height="28"/><rect x="252" y="495" width="1" height="28"/><rect x="259" y="495" width="2" height="28"/><rect x="266" y="495" width="1" height="28"/><rect x="273" y="495" width="3" height="28"/><rect x="280" y="495" width="2" height="28"/><rect x="287" y="495" width="1" height="28"/><rect x="294" y="495" width="3" height="28"/><rect x="301" y="495" width="1" height="28"/><rect x="308" y="495" width="2" height="28"/><rect x="315" y="495" width="3" height="28"/><rect x="322" y="495" width="1" height="28"/><rect x="329" y="495" width="2" height="28"/><rect x="336" y="495" width="1" height="28"/><rect x="343" y="495" width="3" height="28"/>
</g>
<text x="280" y="539" font-size="10" text-anchor="middle" letter-spacing="3" fill="#77756D">6 901234 567890</text>
<text x="280" y="558" font-size="9.5" text-anchor="middle" fill="#2B2B28">谢谢惠顾 · {{FOOT}}</text>
<text x="280" y="572" font-size="9" text-anchor="middle" fill="#77756D">—— 三日后此票仍有效，冷静期愉快 ——</text>
</g>
{{STAMP}}
</svg>
```
