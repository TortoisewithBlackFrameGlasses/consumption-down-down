# 结案评分卡模板 (scorecard · 硬投影天平竖屏卡)

判决 + 记账后,给用户渲染一张**竖屏马卡龙判决卡**:硬边偏移投影、天平图标、六维柱状体检 + 处方 + 累计战绩。这是默认结案卡片样式(另一种趣味样式见 `receipt.md` 盖章小票)。

## 怎么用

1. 先跑 `ledger.py add` 记账,拿到最新累计战绩(审讯 / 拦下 / 守住)。
2. 复制下面「范例 SVG」,照本单真实数据**改写**:商品名 / 价格档、判决词、综合得分、真实成本、六维(分数+柱高+柱色)、处方三条、累计战绩、底部一句话。
3. **按判决档位换三处配色**(见下表):banner + 顶部图标块(天平色) + 判决 pill。
4. **六维柱子按柱高公式重算**(见下)。
5. 用 `show_widget`(visualize 工具)渲染。分数照实(**别为凑图编分**);维度名按品类换(消耗品把"吃灰/操作"换"复购/囤货")。

## 三档判决配色(改 banner / 图标块天平色 / pill 三处)

| 判决 | banner 底 / 硬影 | 图标块底 / 天平色 | pill 底 / 字 / pill硬影 |
|---|---|---|---|
| ⏳ 缓一缓 | `#8E7EE6` / `#6E5EC8` | `#C9C0F5` / `#6E5EC8` | `#FBF1D8` / `#9A7414` / `#E7C98F` |
| ✅ 可以买 | `#5FB89A` / `#46917A` | `#C9C0F5` / `#46917A` | `#E2F3EA` / `#2E7D55` / `#B6D9C4` |
| ❌ 别买 | `#E0758E` / `#BE5670` | `#C9C0F5` / `#BE5670` | `#FCE4EA` / `#B23052` / `#EEB9C6` |

> 天平图标是 `<g transform="translate(66,66)">…</g>` 那段,整组里所有 `#6E5EC8`(fill/stroke)都换成本档的「天平色」。
> 判决 stat 卡(第二张黄色那张)的判决词也随档改:可以买→`可以买 / 放心入`,别买→`别买 / 收手`。

## 柱高公式(六维体检)

- 基线 `baseline = 376`。第 i 维(i=0…5)柱子中心 `cx = 73 + i*59`(实例取整 73,132,190,249,308,366)。
- 柱 `<rect>`:`x = cx-10, width = 20, height = 分数*26, y = 376 - height, rx=9`。
- 分数数字 `<text>`:`x = cx, y = (376 - height) - 6, text-anchor=middle`。
- 维度简称 `<text>`:`x = cx, y = 390`(与卡底留 padding,不贴底)。
- 六维固定柱色:频率`#B9AEEE` 需求`#9FD8C8` 替代`#C9A9E8` 真伪`#BCDCA8` 价格`#F3D384` 操作`#F2A9BC`。否决项简称加 `·否`(字色用该柱深色),软肋维度简称 `·软肋`(字 `#D86A82`、分数也用 `#D86A82`)。

## 硬投影做法

每张卡 `<rect>` 之前,先画一个**同形状、往下偏 5px、颜色深一档的实心 `<rect>`**(露出底部硬边)。各卡影色:banner 见配色表、stat 三张 `#D4CCF0`/`#EFDCAF`/`#CADEF2`、白卡(六维/处方)`#DCD5F0`、战绩条 `#C6BBEF`、pill 见配色表。

## 范例 SVG(⏳缓一缓档 · 照此改数据)

```svg
<svg viewBox="0 0 440 700" xmlns="http://www.w3.org/2000/svg" role="img" width="100%">
<title>消费降级判决书（竖屏马卡龙 · 硬投影 · 天平图标）：半自动咖啡机 18/30，缓一缓</title>
<desc>竖屏马卡龙仪表盘，硬边偏移投影，标题图标为天平，六维柱状体检</desc>
<rect x="12" y="12" width="416" height="676" rx="30" fill="#EFEBFB"/>

<rect x="28" y="35" width="384" height="76" rx="20" fill="#6E5EC8"/>
<rect x="28" y="30" width="384" height="76" rx="20" fill="#8E7EE6"/>
<rect x="44" y="46" width="44" height="44" rx="14" fill="#C9C0F5"/>
<g transform="translate(66,66)">
<circle cx="0" cy="-15" r="2.3" fill="#6E5EC8"/>
<rect x="-1.4" y="-14" width="2.8" height="22" rx="1.4" fill="#6E5EC8"/>
<rect x="-13" y="-13.5" width="26" height="2.8" rx="1.4" fill="#6E5EC8"/>
<path d="M-5,6 L5,6 L8,12 L-8,12 Z" fill="#6E5EC8"/>
<path d="M-12,-11 L-16,-4 M-12,-11 L-8,-4" fill="none" stroke="#6E5EC8" stroke-width="1.5" stroke-linecap="round"/>
<path d="M-17,-4 Q-12,2 -7,-4 Z" fill="#6E5EC8"/>
<path d="M12,-11 L16,-4 M12,-11 L8,-4" fill="none" stroke="#6E5EC8" stroke-width="1.5" stroke-linecap="round"/>
<path d="M7,-4 Q12,2 17,-4 Z" fill="#6E5EC8"/>
</g>
<text x="100" y="62" font-size="17" font-weight="500" fill="#FFFFFF">消费降级判决书</text>
<text x="100" y="82" font-size="11.5" fill="#DAD2F7">半自动咖啡机 + 意式磨豆机</text>
<rect x="320" y="57" width="76" height="32" rx="14" fill="#E7C98F"/>
<rect x="320" y="52" width="76" height="32" rx="14" fill="#FBF1D8"/>
<text x="358" y="73" font-size="14" font-weight="500" text-anchor="middle" fill="#9A7414">缓一缓</text>

<rect x="28" y="121" width="121" height="82" rx="16" fill="#D4CCF0"/>
<rect x="28" y="116" width="121" height="82" rx="16" fill="#EDE9FB"/>
<text x="44" y="140" font-size="11" fill="#8B86A0">综合得分</text>
<text x="44" y="166" font-size="21" font-weight="500" fill="#4A4458">18<tspan font-size="12" fill="#A29DB5"> /30</tspan></text>
<text x="44" y="185" font-size="10" fill="#D98AA0">低于健康线 22</text>

<rect x="159" y="121" width="122" height="82" rx="16" fill="#EFDCAF"/>
<rect x="159" y="116" width="122" height="82" rx="16" fill="#FBF0DA"/>
<text x="175" y="140" font-size="11" fill="#9C8B66">判决</text>
<text x="175" y="166" font-size="21" font-weight="500" fill="#4A4458">缓一缓</text>
<text x="175" y="185" font-size="10" fill="#B59A55">30 天观察期</text>

<rect x="291" y="121" width="121" height="82" rx="16" fill="#CADEF2"/>
<rect x="291" y="116" width="121" height="82" rx="16" fill="#E6F0FB"/>
<text x="307" y="140" font-size="11" fill="#7E8BA0">真实成本</text>
<text x="307" y="166" font-size="21" font-weight="500" fill="#4A4458">¥10<tspan font-size="12" fill="#A29DB5"> /杯</tspan></text>
<text x="307" y="185" font-size="10" fill="#8FA2BC">维持频率下</text>

<rect x="28" y="217" width="384" height="190" rx="18" fill="#DCD5F0"/>
<rect x="28" y="212" width="384" height="190" rx="18" fill="#FFFFFF"/>
<text x="44" y="240" font-size="14" font-weight="500" fill="#4A4458">六维体检</text>
<text x="396" y="240" font-size="10" text-anchor="end" fill="#A29DB5">满分 5 · 参考 ≥4</text>
<text x="73" y="292" font-size="12" font-weight="500" text-anchor="middle" fill="#4A4458">3</text><rect x="63" y="298" width="20" height="78" rx="9" fill="#B9AEEE"/><text x="73" y="390" font-size="10" text-anchor="middle" fill="#8B86A0">频率</text>
<text x="132" y="292" font-size="12" font-weight="500" text-anchor="middle" fill="#4A4458">3</text><rect x="122" y="298" width="20" height="78" rx="9" fill="#9FD8C8"/><text x="132" y="390" font-size="10" text-anchor="middle" fill="#8B86A0">需求</text>
<text x="190" y="292" font-size="12" font-weight="500" text-anchor="middle" fill="#4A4458">3</text><rect x="180" y="298" width="20" height="78" rx="9" fill="#C9A9E8"/><text x="190" y="390" font-size="10" text-anchor="middle" fill="#B58FD0">替代·否</text>
<text x="249" y="266" font-size="12" font-weight="500" text-anchor="middle" fill="#4A4458">4</text><rect x="239" y="272" width="20" height="104" rx="9" fill="#BCDCA8"/><text x="249" y="390" font-size="10" text-anchor="middle" fill="#8B86A0">真伪</text>
<text x="308" y="292" font-size="12" font-weight="500" text-anchor="middle" fill="#4A4458">3</text><rect x="298" y="298" width="20" height="78" rx="9" fill="#F3D384"/><text x="308" y="390" font-size="10" text-anchor="middle" fill="#C9A24A">价格·否</text>
<text x="366" y="318" font-size="12" font-weight="500" text-anchor="middle" fill="#D86A82">2</text><rect x="356" y="324" width="20" height="52" rx="9" fill="#F2A9BC"/><text x="366" y="390" font-size="10" text-anchor="middle" fill="#D86A82">操作·软肋</text>

<rect x="28" y="421" width="384" height="138" rx="18" fill="#DCD5F0"/>
<rect x="28" y="416" width="384" height="138" rx="18" fill="#FFFFFF"/>
<text x="44" y="446" font-size="14" font-weight="500" fill="#4A4458">处方 · 更省的方案</text>
<circle cx="50" cy="478" r="4" fill="#B9AEEE"/><text x="64" y="482" font-size="12" fill="#5A5568">先上手压意式机 / 摩卡壶（¥几百）顶上</text>
<circle cx="50" cy="506" r="4" fill="#9FD8C8"/><text x="64" y="510" font-size="12" fill="#5A5568">连用一个月，验证频率与磨洗操作意愿</text>
<circle cx="50" cy="534" r="4" fill="#F2A9BC"/><text x="64" y="538" font-size="12" fill="#5A5568">30 天后复诊，再决定要不要升级正机</text>

<rect x="28" y="573" width="384" height="48" rx="16" fill="#C6BBEF"/>
<rect x="28" y="568" width="384" height="48" rx="16" fill="#DED6F6"/>
<text x="44" y="588" font-size="10.5" fill="#6A5B9A">累计战绩</text>
<text x="44" y="606" font-size="13" font-weight="500" fill="#4A4458">审讯 1 · 拦下 1 · 守住 ¥0</text>
<text x="396" y="598" font-size="10" text-anchor="end" fill="#7A6BAA">缓一缓不计省</text>

<text x="220" y="650" font-size="12" font-style="italic" text-anchor="middle" fill="#8B86A0">「你缺的不是机器，是那份还没验证的把握。」</text>
<text x="220" y="676" font-size="9" letter-spacing="1" text-anchor="middle" fill="#A8A2BC">适用 30 天冷静期 · 期满复核</text>
</svg>
```
