from datetime import datetime, timezone
from stock_monitor_data.models import Expectation, Stock


def ideas(period: str, interval: str):
    ideas = [
        Stock(
            ticker_name="VONOY",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=30, date=datetime(2024, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Germany's biggest landlord $VNA is priced at a 70% discount to its net asset value.
                                  Its share price would need to 3x just to reach its net asset value.
                                  [Source](https://twitter.com/askjussi/status/1611358663754813440)""",
        ),
        Stock(
            ticker_name="DBRG",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=40, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Pure play alternative asset manager focused exclusively on network infrastructure
                                  investments. A transformed Colony Capital with nearly all legacy assets sold off.
                                  Significant step up in earnings expected in 2023 after the launch of several new
                                  funds. Market is pricing in zero success in fundraising and gives no credit for the
                                  carried interest. Sentiment is likely to reverse upon successful new fund launches.
                                  Insiders started buying stock recently. Infrastructure is a key growth engine for
                                  alternative asset managers. \$KKR, \$BX, etc., are all raising significant capital
                                  for infrastructure investments and \$DBRG is the fastest-growing manager out there.
                                  Valuing fee-related earnings at 22x, results in a SOTP valuation of \$32\/share with an
                                  additional \$5\/share from carried interest.
                                  **Exp. gain: +200\% to \$40\/share.**
                                  [Source](https://twitter.com/InvestSpecial/status/1610585909128302593)""",
        ),
        Stock(
            ticker_name="CRNT",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=3.08, date=datetime(2024, 5, 31, tzinfo=timezone.utc)
            ),
            description=r"""Vendor for global wireless network operators specializing in backhaul solutions.
                            Shareholders have recently rejected a hostile takeover by peer $AVNW at $3.8/share.
                            Renewed talks between AVNW and CRNT present the potential for near-term upside
                            realization. While $AVNW is the leader in NA backhaul, CRNT is now encroaching on
                            its territory, having secured contracts with every NA Tier 1 operator. AVNW used a
                            difficult equity market environment to try to opportunistically scoop up an
                            undervalued asset.Post proxy fight CRNT management is forced to drive shareholder
                            value.Trades near its historical 1x book value floor. Failed takeover attempt at
                            $3.08/share in Aug`22. Management`s internal value estimate of $5/share.
                            **Exp. gain: +70% to$3.08+**
                            [Source](https://twitter.com/InvestSpecial/status/1610585909128302593)
                        """,
        ),
        Stock(
            ticker_name="AMKR",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=87, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Semiconductor assembly services provider - the world`s most wonderfully boring
                            businesses to own. At 9x earnings and shifting into higher margin services.
                            For a semi business, it has very low cyclicality and low capex needs, and yet is
                            delivering above-industry revenue growth with 3 year CAGR of 20%. Oligopolistic
                            industry - AMKR is the No.2 player with a 25% share, behind ASX with 35%. Due to
                            increasing chip complexity, the industry is shifting towards less commoditized and
                            more advanced packaging/assembly solutions, requiring more R&D and tighter
                            integration with customers. This also drives increasing margins for key players.
                            Should trade at an above-market multiple of 20x vs 9x today. 23 and 24 EPS are
                            expected at $3 and $4. Easy double with $4 fwd EPS and 10.5x multiple. DCF model
                            results in $87/share. **Exp. gain: +100% by 2H23.**
                            [Source.](https://twitter.com/InvestSpecial/status/1612025171879010305)""",
        ),
        Stock(
            ticker_name="XMTR",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=45, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Marketplace for small batch manufacturing and prototyping. Currently trades at its
                                  Jun`21 IPO level and at 4.5x revenue, while comps are in the 1-2x range. Competitive
                                  and low-entry barrier industry that is significantly exposed to macro headwinds.
                                  Clients and suppliers can as easily connect directly.
                                  No clear operating leverage with increasing scale. Relies heavily on Google Adwords
                                  to drive traffic. Guidedown in pricing already happened with Q3`22 results,
                                  volume might drop in 2023.Trades at 4.5x revenues, still at the IPO price vs. a comp
                                  universe 3-D printers and short-run fabricators in the 1-2x range. **Exp. gain: 50%-75%**
                                  [Source.](https://twitter.com/InvestSpecial/status/1612387567302840320)""",
        ),
        Stock(
            ticker_name="FIP",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=7, date=datetime(2024, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""Recent spin-off from \$FTAI with 4 infrastructure assets: 3 energy terminals and a
                                  railroad business. EBITDA is set to increase from \$140m today to \$250m in the next
                                  12-18 months. FPI`s Jefferson terminal is now on cusp of generating strong earnings.
                                  Transtar railroad earnings have been consistently increasing through new business
                                  initiatives. Construction of the 485MW power plant at Long Ridge is complete.
                                  Downside is well protected at current share price levels.Base case EBITDA is set to
                                  grow from \$140 million today to \$250 million over the next 12-18 months.
                                  At 11x multiple, the target of \$6.7/share. **Exp. gain: +130% to \$7/share.**
                                  [Source](https://twitter.com/InvestSpecial/status/1613508259154984962)""",
        ),
        Stock(
            ticker_name="ALIT",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=11, date=datetime(2024, 5, 31, tzinfo=timezone.utc)
            ),
            description=r"""Provider of outsourced human capital management services/software with multiple
                            upcoming event catalysts. Steady business, with 3-5 year contracts, 15-year average
                            customer life, and 97% rev retention. Comp set is performing very well in the stock
                            market.Stock was down 20% after a botched secondary offering. However, Bill Foley
                            pulled out from selling. His lack of participation in the secondary was extremely
                            telling. His number two, Rick Massey, subsequently bought \$840k of stock around
                            current levelsPeers \$WTW and \$G with similar expected growth and financial profiles
                            trade at 11x-11.5x 1-year forward EBITDA.
                            At this multiple \$ALIT is worth \$10.5-11.0/share today.
                            **Exp. gain: +20% to \$11/share.**
                            [Source](https://twitter.com/InvestSpecial/status/1613508259154984962)
                        """,
        ),
        Stock(
            ticker_name="ZIMV",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=37, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Recent spin-off from Zimmer Biomet with shares down 80% from the first day of trading.
                                  Orthopedics company offering spine surgery solutions and dental implants. Stable,
                                  65% GM business, set to benefit from post-pandemic recovery in elective surgeries.
                                  Margin improvement potential from the current 9% to 15-20% peer levels. Trades far
                                  below peer group on a revenue multiple. Trailing revenues were weak due to distortion
                                  by several transitory factors.Current EV/Sales of 0.75x is far below the peer group`s
                                  3.3x. Full-recovery EV/EBIT of around 7x vs around 15x for the peer group.
                                  At 15x multiple would be valued at \$37/share. **Exp. gain: +300% to \$37/share.**
                                  [Source](https://twitter.com/InvestSpecial/status/1613508259154984962)""",
        ),
        Stock(
            ticker_name="BJ",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=140, date=datetime(2024, 5, 31, tzinfo=timezone.utc)
            ),
            description=r"""**What does BJ do?** The business is a discount wholesale club like Costco but
                            focused on a more middle-class income demographic (Costco tends to skew higher
                            income). BJ`s charges an annual membership fee of \$55 to \$110 and delivers
                            extreme savings of 30% on average compared to traditional grocery and general
                            merchandise stores. This is a strong value proposition for a family that shops
                            once or twice per month for household essentials.
                            **Why is it a good bet?** Discount retailers tend to outperform during
                            recessionary periods as well as inflationary periods when consumers are looking
                            for bargains. During the 2008/2009 recession, discounters such as Dollar General
                            posted strong sales comps. We studied several discount retail concepts this summer
                            and determined that BJ`s presents the best longterm opportunity
                            **Why does the opportunity exist?** With just 226 store units compared to Costco`s
                            847 units, BJ`s has a significant opportunity to grow its store base and is
                            currently accelerating new unit openings
                            **What`s the prize if you`re right?** Investors appreciate the quality of the
                            wholesale club model and have awarded Costco a 32x price-to-earnings multiple.
                            Despite BJ`s being a `Costco clone`, its stock only trades for 17.5x earnings -
                            a near 50% discount(!).
                            [Source](https://macro-ops.com)
                        """,
        ),
        Stock(
            ticker_name="HLS.TO",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=25, date=datetime(2024, 5, 31, tzinfo=timezone.utc)
            ),
            description=r"""Small cap Canadian pharma with shares near all-time lows and business fundamentals
                            finally inflecting to the positive. Investment case is mainly based on one of two
                            HLS`s drugs, Vascepa, that is in the initial stages of commercialization.
                            Vascepa is approved, clinically effective, and has reimbursement coverage
                            Pfizer Canada is the team pushing things forward for commercialization
                            Sales are growing 30%-40% QoQ and are only now approaching sufficient prescription
                            levels to break evenThe initial Vascepa commercialization difficulties were mainly
                            caused by Canada`s lengthy COVID lockdown.
                            Precedent drugs suggest management's estimate of 10% penetration is overly conservative
                            and that 20-40% levels could be reached.The already commercialized drug Clozaril alone
                            supports current HLS valuation, implying less than zero value for Vascepa.
                            With Vascepa roll-out, HLS is worth \$25/share.
                            **Exp. gain: +150% to \$25/share.**.
                            [Source](https://twitter.com/InvestSpecial/status/1615303074473451521)
                        """,
        ),
        Stock(
            ticker_name="APD",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=600, date=datetime(2027, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Large-cap producer of atmospheric and industrial gases (oxygen, nitrogen, hydrogen
                                   and etc). APD is in a great position to take advantage of the hydrogen future, and
                                   they have been the most aggressive of their peers in going after the opportunity.
                                   Expected high-teens IRR over the next 5 year, potentially above this range if
                                   hydrogen plays out as hoped. 52% of revenue is supplied on-customer-site with
                                   15-20 year contracts, while the rest comes from merchant channels typically under
                                   3-5y contracts. Stable cash flows with proven ability to pass through commodity
                                   cost increases. 50% of earnings paid out as dividends (2% yield).
                                   An oligopolistic industry that has historically provided stability and pricing power.
                                   Trades roughly in line with historical multiples at 28x fwd PE. Investors are not
                                   paying much for the tremendous optionality around hydrogen, gasification, and carbon
                                   capture. **Exp. gain: +100% to $600/share in 5 years.**
                                   [Source](https://twitter.com/InvestSpecial/status/1618241155103064071)""",
        ),
        Stock(
            ticker_name="MIR",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=10, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Industry leader in mission-critical radiation measuring devices and services.
                                   40-60% market share in the markets it participates. Has been beaten down
                                   mainly due to quarterly guidance misses from component shortages and canceled
                                   projects due to the Ukraine. SPAC provenance, poor execution, and its terrible
                                   public market performance have led investors to trade it like a low-quality
                                   industrial business. MIR`s acyclicality, market position, and margins argue for
                                   a better multiple. Expected to revert to normalized earnings after the
                                   aforementioned temporary pressures ease. The elevated order book indicates
                                   positive exposure to secular growth in nuclear power.Trades at 11x E2023 EBITDA
                                   of \$193m. Higher quality industrial peers trade at 15-25x EV/EBITDA.
                                   Mirion should at least reach the low-end of this range implying a
                                   \$10/share price target.
                                   [Source](https://twitter.com/InvestSpecial/status/1623987849052692482)""",
        ),
        Stock(
            ticker_name="BALL",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=70, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Beverage can producer with a 30% market share globally and 40% in the US.
                                   Primary customers are companies like \$BUD and \$KO. Stock sold off due to
                                   a combination of post-covid oversupply in the beverage can industry, increased
                                   aluminum prices, and moderating consumer demand. Operating margins contracted
                                   from 13% in 2020 to 10% in 2022.These factors are expected to unwind in 2023
                                   setting up the perfect storm for BALL. The supply/demand disbalance is expected
                                   to normalize in 2023, while decreases in aluminum prices are expected to bring margins
                                   to historical levels. EPS is expected to reach \$3.5/share in 2023 (7% above consensus).
                                   Historical 20x multiple implies a \$70/share price target.
                                   [Source](https://twitter.com/InvestSpecial/status/1627623767869386752)""",
        ),
        Stock(
            ticker_name="MATV",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=32, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Specialty materials business formed in 2022 as a result of merger with significant synergies.
                                   Good business with cyclically depressed EBITDA. Should be a ~MSD revenue grower and approaching
                                   high-teen EBITDA margins with low capex intensity (~3% of revenue).Extremely cheap trading 6.6x
                                   management`s EBITDA target. Good FCF generator with a 14% 2023 levered FCF yield. Expected to
                                   divest certain businesses to crystallize value. Last year insiders purchased nearly \$6mm in
                                   stock at an average price of \$23.5. Currently trading at 6.6x management`s \$450mm EBITDA target.
                                   On SOTP basis, with 10-12x EBITDA on ATS segment and 5-6x on the FBS segment, price target of
                                   \$32-43/share.
                                   [Source](https://twitter.com/InvestSpecial/status/1627984064601894915)""",
        ),
        Stock(
            ticker_name="NTDOY",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=30, date=datetime(2027, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Nintendo today offers a robust 3x upside to reach intrinsic value estimate of ~\$110bn EV.
                                   The market is massively mispricing Nintendo`s “App Store Platform” or third-party software
                                   business.Nintendo Switch is a thriving distribution channel that has already attracted a large
                                   thriving ecosystem of third-party games. This marks a major strategic shift in how Nintendo views
                                   its console business.As a result, Software sales have inflected in recent years, overtaking
                                   hardware for the first time in 2022. Primed for continued massive margin expansion, from already
                                   improved ~35% to 50%, based on reasonable extrapolations of the present trends.Game seg.
                                   is worth \$65bn on \$12bn fwd. rev, 33% EBIT margin and 23x NOPAT
                                   App Store Platform is worth \$45bn on \$3.5bn FY27 rev, 87% margin and 30x NOPAT
                                   Suming up to \$110bn vs \$37bn EV today.
                                   [Source](https://twitter.com/InvestSpecial/status/1629419792699383808).""",
        ),
        Stock(
            ticker_name="FTAI",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=94, date=datetime(2027, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Aircraft and engine lessor that has gone through a major transformation from a complex “mess”
                                   of assets to a pure-play aviation company. On the cusp of seeing substantial growth in its parts
                                   & service business and that should translate into a higher multiple. Product and services segment
                                   is set to contribute half of the profitability vs 15% currently. Trades materially below peers.
                                   Survived major setbacks of Covid and the Russia/Ukraine war with a number of aircrafts seized
                                   or destroyed. Recently spun-out infrastructure assets, which not only simplified and derisked the
                                   FTAI story but also improved the balance sheet. 6.3% dividend yield limits the downside.
                                   EBITDA set to grow from \$423m in 2022 to $1b in 2026. Multiple expected to expand from 9.7x today to 12x.
                                   Leasing peers trade at 10x `23 EBITDA and product comps at 15x.
                                   [Source](https://twitter.com/InvestSpecial/status/1629419792699383808)""",
        ),
        Stock(
            ticker_name="AE",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=120, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Transportation and logistics company serving the energy and chemical sectors, primarily onshore.
                                   Has momentum in each of its core business segments. Trades under 3x EBITDA.
                                   New management is turning the business around.Previously poorly managed for many years and run like
                                   a private company under Adams family control. In Nov`22 all 44% of the family`s ownership was cashed
                                   out at \$36/share. Current management team led by the current CEO was hired in 2018 to turn around
                                   operations. Despite the pandemic, since then the company has been meaningfully building adjusted FCF.
                                   Recently completed highly accretive acquisitions of Firebird Bulk Carriers and Phoenix Oil for about
                                   \$40m in cash. Repurchases and acquisitions, the net debt is close to zero. Expected to generate \$40m
                                   of adj. EBITDA in 2022 and \$50m+ in 2023. Trades at 3x 2022 adjusted EBITDA and 2.5x 2023 estimated
                                   adj. EBITDA. At 6x multiple would be worth $120/share.""",
        ),
        Stock(
            ticker_name="BTI",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=58, date=datetime(2024, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""British American Tabacco - at only 7.8x fwd earnings and nearing inflection point in terms of growth.
                                   At a lower valuation than during the worst of the GFC, and roughly in-line with COVID lows. As the company
                                   adds non-combustibles to their mix, margins should continue to move higher. The market is more willing to
                                   pay a premium multiple for a tobacco business with a larger % of non-smoking products in the portfolio
                                   (as happened with \$PM case). Inflation-proof non-cyclical stock with a stable 8% dividend yield.
                                   Together with EPS growth of 6-7% per year, BTI can be a 14-15% IRR stock for investors without rerating.
                                   That's before any EPS growth from non-combustibles. Bears point out that tobacco names will never trade
                                   at historical P/E multiples owing to heavy government regulation and the movement toward ESG investing.
                                   But the irony is that regulation only ensures that the supply side of the industry remains tight.BTI is
                                   expected to generate £4.26 of EPS in 2024. Historically traded at 12x EBITDA and 13x PE
                                   Re-rating to 10x 2024 eps results in a \$58/share price target.
                                   [Source](https://twitter.com/InvestSpecial/status/1633420824442019842)""",
        ),
        Stock(
            ticker_name="CZR",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=150, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""The largest gaming operator in the US with over 50 properties. 50% selloff from Oct'21 highs due to
                                   recession fears/risk aversion looks unwarranted as CZS offers a stable 15% FCF yield. Meanwhile,
                                   the downside looks protected by CZR`s owned real estate. Most importantly, there is the optionality
                                   of FCF expansion through normalization of growth CAPEX, interest expense reduction through debt repayments,
                                   and digital business inflection to profitability as it benefits from i-gaming growth.
                                   At 15x EBITDA (4x below average peer multiple over the last decade), the company would be valued at \$150/share.
                                   [Source](https://twitter.com/InvestSpecial/status/1633420824442019842)""",
        ),
        Stock(
            ticker_name="WBA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=70, date=datetime(2024, 8, 1, tzinfo=timezone.utc)
            ),
            description=r"""Wallgreens Boots Alliance - trades near all-time lows on virtually every metric. Fundamentals are
                            expected to inflect in the second half of FY23. Company`s YOY EPS trajectory is projected to flip
                            from about -31% in the first half, to 29% in the back-half. This will be driven by lower COVID headwinds,
                            improvements in WBA`s Healthcare business, the timing of reimbursements, and lower COGS. The company has
                            been transitioning under its new CEO into a multi-channel technology-driven healthcare provider and a
                            one-stop shop for all healthcare needs. This is expected to drive longer-term EPS growth in the 13-15% range.
                            Another catalyst is the potential sale of its large UK subsidiary Boots - rumors have been circulating
                            that it might get sold at the right price. Trades at an 8.1x PE for 2023 and 7.3x for 2024.
                            At historical discount levels (5-10%) would be \$70 stock.
                            [Source](https://twitter.com/InvestSpecial/status/1634143032609046530)
                        """,
        ),
        Stock(
            ticker_name="GPRE",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=60, date=datetime(2024, 4, 2, tzinfo=timezone.utc)
            ),
            description=r"""Green Plains is transitioning from a legacy ethanol company into a diversified bio-refinery after the
                                   acquisition of Fluid Quip in 2020. The company is now at an inflection point where the market will start
                                   to see a meaningful increase in financial performance. Half of GPRE`s facilities have already been converted
                                   to include these AgTech enhancements while the remainder should be converted within 18 months.
                                   Q1`23 earnings will mark the beginning where half of GPRE`s platform runs at planned production capacity
                                   Activist Ancora is now pushing for strategic alternatives, including a sale, suggesting a strategic acquirer
                                   could pay \$50/share or more. GPRE trades at <5x E2023 EBITDA of around \$450m.
                                   Company is worth around \$60-\$65/share over the next 12-18 months.
                                   [Source](https://twitter.com/InvestSpecial/status/1642450715284062208)""",
        ),
        Stock(
            ticker_name="RMBL",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=25, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""RumbleOn is the largest power sports dealership group in the US. Currently, RMBL is misunderstood and
                                   being viewed as yet another COVID beneficiary. However, RMBL is sufficiently resilient during near-term
                                   macro bumpiness and has a compelling LT strategy for value creation. RMBL`s organic growth, with used
                                   volume growth being the key component, will allow the company to outperform peers this year.RMBL has
                                   multiple levels to create value including accretive M&A, opening their fulfillment/distribution centers
                                   to the public, and focusing on effective servicing at dealerships. Despite high leverage, the risk of
                                   breaching debt covenants is low. 2024 EBITDA expected at around \$130m. Using a 6x EBITDA multiple results
                                   in a \$25/share price target.
                                   [Source](https://twitter.com/InvestSpecial/status/1642450715284062208)""",
        ),
        Stock(
            ticker_name="BAIN.PA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=150, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""SBM: A unique investment in the ultra-rich - with operating leverage and growth.
                                   If even part way accurate, this analysis suggests significant potential upside on a post-COVID recovery
                                   as the rentals are revalued. We view a more appropriate valuation as closer to €150/share for the group.
                                   [Source](https://east72.com.au/wp-content/uploads/2023/04/E72DT-QUARTERLY-REPORT-Mar-2023.pdf)""",
        ),
        Stock(
            ticker_name="APT",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=6, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Relatively mediocre business, however, it is cheap on all metrics. Trades at 7x EBIT, slightly above net
                            current assets. Well-protected downside and meaningful potential upside.The company manufactures/sells
                            single-use protective apparel products and building supply products. Net cash balance sheet and rational
                            capital allocation strategy. Uses all FCF to buy back stock, S/O declined from 27m in 2006 to 13m today.
                            Shares might skyrocket on the next viral outbreak, as has already happened due to H1N1 in 2009 and COVID in 2020.
                            Attractive M&A target for both financial and strategic buyers.Shares might skyrocket on the next viral outbreak,
                            as has already happened due to H1N1 in 2009 and COVID in 2020. Attractive M&A target for both financial and
                            strategic buyers. EV/sales at 0.52x, EV/EBIT is 6.8x, and EV/NOPAT is 8.6x.
                            NCAV per share is \$3.77 (1.14x) and TBVPS is \$4.85 (0.89x). Exp. gain: TBVPS is set to compound at 8%
                            annually in the absence of any viral outbreaks.
                            [Source](https://twitter.com/InvestSpecial/status/1643537169309483008)""",
        ),
        Stock(
            ticker_name="CEG",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=115, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Constellation Energy, a recent spinoff, operates 13 nuclear power plants in the US. As of the
                                   Inflation Reduction Act`s (IRA) subsidies, CEG thus offers a minimum FCF yield of around 8.5%
                                   while allowing for full upside potential at higher power prices.  Furthermore, the downside looks
                                   somewhat protected as the company trades at <50% below replacement cost. The stock offers additional
                                   optionality if the company takes advantage of IRA-supported tax-credit opportunities in clean hydrogen.
                                   12-13x EBITDA multiple on floor earnings implies a \$115-125/share stock price.
                                   [Source](https://twitter.com/InvestSpecial/status/1642823074541182976)
                                """,
        ),
        Stock(
            ticker_name="PENN",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=85, date=datetime(2025, 1, 30, tzinfo=timezone.utc)
            ),
            description=r"""Casino operator with 43 properties + digital assets. Since pre-pandemic, sales grew by 20% and
                                   margins significantly improved. Despite these positives, PENN trades at the same EV as pre-covid.
                                   Core business comprises 85% of revenue and provides solid downside protection.
                                   On top of that, PENN's digital assets present a call option on OSB/iCasino industry. Both digital
                                   assets continue to grow and are at breakeven now. Sustainable margin improvement has been mainly
                                   achieved through cost savings. Management's compensation is heavily tied to share price appreciation
                                   over the next 3 years. The company has started buying back shares. Land-based businesses are expected
                                   to deliver ~\$5/share of levered FCF by '25. At today's 11x multiple, that's \$55/share value.
                                   Digital assets are worth an additional \$30/share.
                                   [Source](https://twitter.com/InvestSpecial/status/1644625210794995713)""",
        ),
        Stock(
            ticker_name="LNW",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=150, date=datetime(2024, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Gaming content creator/manufacturer/distributor for land-based and digital casinos. Oligopoly with
                                   75% recurring revenue and high switching costs. Has now assembled an all-star team after hiring
                                   around 50 high-level executives from rival Aristrocrat. Core business is expected to benefit from
                                   an increase in casino CAPEX following two years of negligible spending. Also, market is currently
                                   ascribing nearly 0 value to LNW`s two digital assets - digital casino games and mobile/social gaming.
                                   Digital assets are highly synergistic to its main business and are expected to benefit from digital
                                   casino legalisation in the US and growing TAM for mobile/social gaming.
                                   LNW trades 6.5x 2024 EBITDA vs 10x for closest peer Aristocrat. Optionality to re-rate closer to
                                   video game focused peers (trade at 17-19x EBITDA). Stock is expected to return 3.7x MOIC.
                                   [Source](https://twitter.com/InvestSpecial/status/1644625210794995713)
                   """,
        ),
        Stock(
            ticker_name="SOMA.V",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=6, date=datetime(2033, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Imagine you can invest in gold as a safe haven, but with the characteristics of an exponential tech stock.
                                   If Soma Gold proves they have the resources, it could simply expand annual production from 36K to 75K.
                                   This growth is already permitted and should give us a 10 bagger. I believe Soma Gold is going to be
                                   Segovia 2.0 as they are also starting at 500K ounces of resource and 50K ounces of production.
                                   Over time this will grow to multimillion ounces of resource and 100K+ ounces of production.
                                   Catalysts: Drill results update coming. 3 drill rigs on site + 1 drill rig incoming this month.
                                   AISC will be below \$1000/ounce due to mechanized mining. Gold loan is fully repaid in January.
                                   Long term note repayment starts in July. Production will increase from 35K to 50K
                                   [Source](https://twitter.com/GoldForecast/status/1646418350996705283)
                  """,
        ),
        Stock(
            ticker_name="TM.V",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=0.6, date=datetime(2025, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Trigon Metals Inc. (TM:TSXV) is a Canadian exploration, development, and mining company focused on copper
                            and silver assets in Africa. Trigon`s current priority is the restart of its flagship project, the Kombat
                            Mine in Namibia. The Kombat Mine was once one of the largest copper producers in Namibia having historically
                            produced 12.5 Mt of ore at 2.6% Cu. Trigon plans to bring Kombat back into production in FY23 with 4.0 Mlbs
                            of copper expected to be mined in FY24 and growing to 22.1 Mlbs by FY26.
                            [Source](https://mcusercontent.com/4bc421505c66d079778a0d0be/files/95cf91a8-23ab-97c9-b8ba-0f921b470b3e/20230403_Atrium_TM_Initiation_Report.02.pdf)
                            [Update](https://mcusercontent.com/4bc421505c66d079778a0d0be/files/08e37aff-1ea8-1a1f-10e0-6b3da386e52f/20230725_Atrium_TM_Kombat_Update.01.pdf)
                   """,
        ),
        Stock(
            ticker_name="EHTH",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=25.38, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""eHealth is a digital health insurance broker with secular tailwinds from the continued Medicare Advantage
                                   growth till 2040. EHTH was classified as an un-investable stock in an un-investable industry on top of a
                                   damning short report from Muddy Waters. Report pointed to low-quality earnings due to mandatory ASC606
                                   adoption and abusing its constraints with aggressive growth tactics. EHTH is in a turnaround mode with new
                                   mgmt, reversing bad growth policies and industry players behaving more disciplined. Churn is expected to
                                   stabilize back to normalized levels. 100% upside opportunity protected by a floor valuation.
                                   The liquidation value of the commissions receivables is higher than the current market cap.
                                   Depending on the assumed churn levels, the stock has 70% upside in the base case and 400% upside for the
                                   bull case. BV of commissions receivables is \$25.38/share after net debt and preferred
                                   [Source](https://twitter.com/InvestSpecial/status/1649352951897415680)
                   """,
        ),
        Stock(
            ticker_name="OSW",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=22, date=datetime(2024, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Provider of spa services on cruise ships. Quasi-monopoly with over 90% of the cruise ship market.
                                   Long-term 7-10% topline growth. Trades at 10-12x 2024 FCF. Capital returns coming.
                                   100% upside. Onshore spa competitors face difficulty replicating OSW`s global breadth and scale.
                                   Due to relatively minimal expense, cruise ship operators have no incentives to switch or in-house services.
                                   Historically, churn has been almost nonexistent. Expected to initiate a dividend this year or next at the latest.
                                   Due to minimal capex needs, set to become a cash-flow return machine.
                                   [Source](https://twitter.com/InvestSpecial/status/1650422425018937345)
                   """,
        ),
        Stock(
            ticker_name="RGS",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=7, date=datetime(2025, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""Hair salon franchisor with 5,000 units. Covid-driven headwinds masked the fact that RGS has
                                   wrapped up a major business model transition to the franchised model The business has bottomed
                                   out and is on the path to recovery. Worth \$7, representing a 6x return A recession-proof,
                                   asset-light business that is generating 30%+ EBITDA. The new CEO joined in 2022 and is successfully
                                   turning the business around. Both the business model transition and liquidity profile improvement
                                   have gone unnoticed by the street.
                                   [Source](https://twitter.com/InvestSpecial/status/1650422425018937345)
                   """,
        ),
        Stock(
            ticker_name="CBD",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=6, date=datetime(2023, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""CBD is a Brazilian holding company that is spinning off its Colombian grocery chain, Grupo 
                            Exito, in the second quarter of 2023. Shareholders will receive 4 shares of Grupo Exito, 
                            which is currently trading at a higher value than CBD's remaining assets (referred to as 
                            the "stub"). However, the stub includes multiple assets that should be worth at least 
                            $0.50/share, as well as a high-end grocery chain in Brazil. Assuming the stub trades at 0 
                            and Exito is valued correctly, the potential upside is around 20%. The author believes 
                            that both the stub and Exito should be worth at least $6.00/share in the long term, which 
                            is at least a double from the current price.
                            [Source](https://www.clarksquarecapital.com/p/companhia-brasileira-de-distribuicao)
                  """,
        ),
        Stock(
            ticker_name="GOGO",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=28, date=datetime(2027, 12, 31, tzinfo=timezone.utc)
            ),
            description=r"""In conclusion, Gogo is a high-quality business operating in a structurally growing industry.
                                   The business is well- managed by highly incentivized insiders. The stock is not widely followed by investors
                                   and the investors that are aware of the company do not fully appreciate the business transformation and
                                   turnaround that has taken place. The market is also concerned about growing competitive risks; however,
                                   these fears are likely over-blown and provide an opportunity to buy shares in Gogo at attractive prices.
                                   [Source](https://mcusercontent.com/08f9a0d6280bf283b8bc58473/files/16fa3f9e-10cd-3666-5625-bad7f6c56620/LVS_Advisory_GOGO_Write_Up_April_2022_.pdf?utm_source=substack&utm_medium=email)
                  """,
        ),
        Stock(
            ticker_name="DEA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=17, date=datetime(2024, 8, 15, tzinfo=timezone.utc)
            ),
            description=r"""Cheap low-risk REIT that leases class A office properties to US govt agencies. The highest 
                            quality tenant in the world. Low renewal risk and vacancy of only 1.2%. 8% dividend is 
                            sustainable. Much higher return than treasuries, but with similar risk. Strong balance 
                            sheet with low-cost fixed-rate debt with no significant near-term maturities. 
                            Debt/EV at 46%. Solid management with longstanding relationships with various government 
                            agencies. Trades at 11.5x 2022 FFO and 12x E2023 FFO whilst offering an 8% dividend yield.
                            [Source](https://twitter.com/InvestSpecial/status/1651887289553780737)
                        """,
        ),
        Stock(
            ticker_name="GB",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=20, date=datetime(2024, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""A less visible and safer bet on China reopening. Provider of VAT tax refund services for international
                            travelers, ~70% market share. Essentially a small royalty on travelers purchasing luxury goods abroad.
                            As China re-opens profits will inflect above pre-COVID. Some re-opened regions are spending 3x on like
                            for like basis through GB vs what they were pre-COVID. This business has 80% incremental margins from
                            any new revenue, >40% EBITDA margins, and 85% FCF conversion. Trades <10x 2019 EBITDA, without any credit
                            for dramatically higher luxury goods prices or cost take-outs since then.
                            As China reopens, GB could do \$1+/share of FCFresulting in a \$20+ stock.
                            [Source](https://twitter.com/InvestSpecial/status/1653327568173400067)
                   """,
        ),
        Stock(
            ticker_name="IWG.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=430, date=datetime(2030, 1, 1, tzinfo=timezone.utc)
            ),
            description=r"""Global operator of flexible working spaces with 4x the locations of their next-largest competitor.
                                   Currently in the early stages of transferring the majority of the current business into the
                                   franchised operations. If successful, would result in the transfer of a significant part of lease
                                   liabilities and the cost base onto a 3rd parties. This would leave IWG with a far higher margin royalty
                                   stream likely to be valued by the market on a more generous multiple. The currently large operating lease
                                   liability (even if non-recourse and tied to individual properties) is a significant concern among investors.
                                   Set to generate 29p EPS by 2025, 55p by 2030. SOTP: mature estate + franchised business + The Instant Group,
                                   results in 430p fair value today.""",
        ),
        Stock(
            ticker_name="MTB",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=260, date=datetime(2028, 1, 1, tzinfo=timezone.utc)
            ),
            description=r"""The bank is oversold on fears caused by the collapse of SVB and other banks.
                                   However, MTB is run by a conservative mgmt team in markets with stickier deposit bases.
                                   That does not make them immune to dumb ideas, but it greatly reduces the risk to shareholders.
                                   MTB has consistently earned mid-teens ROTE. Pays out a healthy dividend, and uses excess capital
                                   to buyback stock. Last year's merger with People's United provides significant scale benefits,
                                   which should become evident shortly. In 2022, MTB earned \$14.42 per share.
                                   Expected to earn north of \$20/share in 4-5 years, with excess cash used for buybacks.
                                   At 13x multiple would be a \$260 stock.
                                   [Source](https://twitter.com/InvestSpecial/status/1656583775957008385)
                   """,
        ),
        Stock(
            ticker_name="GEO.TO",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=7.3, date=datetime(2024, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Drilling company providing sample extraction services for gold miners in Africa and South America.
                                   Trades at 2.4x TTM EV/EBITDA despite highly recurring revenue, and positive FCF while growing both
                                   the revenues and earnings at a decent clip. Low trading multiple should expand as investors realize
                                   we are at the beginning of a long cycle of growth for the industry. Increasing free cash flow allows
                                   GEO to continue returning capital to shareholders through dividends and share buybacks.
                                   An attractive target to other drillers due to its long-term relationships with mining companies.
                                   CEO with 39% ownership of GEO said openly that he is open to sale at 5x EBITDA or more.
                                   In a sale scenario GEO is worth at least 5x E2024 EBITDA, which implies a C\$7.3/share price target.""",
        ),
        Stock(
            ticker_name="PKN.WA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=180, date=datetime(2028, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""In my opinion ORLEN has the potential the be an investment comparable to PetroChina.
                            I am bullish on oil prices and ORLEN gives me trough the ridiculously low valuation a good downside protection.
                            Here is another quote from Buffet regarding PetroChina.
                            [Source](https://moderninvesting.substack.com/p/the-next-petrochina)""",
        ),
        Stock(
            ticker_name="KD",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=70, date=datetime(2028, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""IT services provider spun off from $IBM. Badco was often positioned as a loss leader by \$IBM to sell more hardware.
                                   As a result, KD has no pre-tax income today. By no longer being part of IBM, it can now gradually
                                   reprice loss-making contracts. \$KD may face increased customer churn as it works through a
                                   backlog of pre-spin contracts. However, its excellent reputation and low valuation more
                                   than compensate for the risk. KD trades at just 0.3x sales vs peers at least 2x that.
                                   [Source](https://drive.google.com/file/d/1NN2NPtT-OZ3-XT0h1Djx8yHrbV6g2mqh/view)""",
        ),
        Stock(
            ticker_name="ALOT",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=24, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Primarily a manufacturer of airplane cockpit printers plus a provider of label printers.
                            Cockpit business is an actual monopoly protected from larger peers due to a small and
                            niche enough market on top of the FAA's expensive regulatory framework.
                            Crux of thesis centers around the expected increase in airplane production to 
                            pre-Covid levels leading to continued growth in revenues and earnings. At 10x 2024E 
                            EBITDA multiple vs peers at 15x, ALOT is $24/share stock.
                            [Source](https://static1.squarespace.com/static/635cafa2259a125cc55eae33/t/64387c7cf1e5c4626d787d38/1681423485063/Atai+Capital+-+Q1-2023+Letter.pdf)
                        """,
        ),
        Stock(
            ticker_name="BNED",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=3, date=datetime(2023, 12, 15, tzinfo=timezone.utc)
            ),
            description=r"""Textbook retailer transitioning into a durable omnichannel player based on its First Day 
                            Complete (FDC) program. Via the FDC, $BNED provides the students with all their books 
                            directly through the school by bundling the costs into a tuition fee. Due to publishers' 
                            discounts, students save 30-50%, schools receive commissions on sales, and publishers 
                            actually get paid. While new economics are attractive only 20% of schools are on the 
                            platform. This is about to change with $BNED recently making the conversion mandatory. 
                            If transition is successful, there is a path to $125m+ in EBITDA. Given the attractive 
                            economics and presence of an activist with a 10% stake, the target seems achievable. 
                            Overlooked due to small $100m Mcap and minimal coverage.
                            [Source](https://static1.squarespace.com/static/5498841ce4b0311b8ddc012b/t/644bdf2a12435708a8affde7/1682693930744/Greenhaven+Road+2023+Q1+Quarterly+Letter%5B69%5D.pdf)""",
        ),
        Stock(
            ticker_name="PLYA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=15.20, date=datetime(2024, 8, 15, tzinfo=timezone.utc)
            ),
            description=r"""PLYA is the only publicly traded, all-inclusive resort owner-operator and has a portfolio of 25 all-inclusive
                                   resorts across Mexico, Jamaica, and the Dominican Republic.Management is being proactive in creating value
                                   for shareholders by exploring sale opportunities for the lower to mid-tier assets (presumably at valuations
                                   above the stock's current valuation in the public market) with the goal of buying back stock.
                                   [Source](https://static1.squarespace.com/static/601ae5e60b044d0313307aca/t/6463e51fc22ddc3d0b6189c9/1684268319477/2023+Q1_Voss+Value+Funds+Letter+to+Partners.pdf)
                   """,
        ),
        Stock(
            ticker_name="NIL-B.ST",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=120, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Profitable every year over the past 11 years. Conservative balance sheet with an equity ratio >50% and a net cash position.
                                   Yet even on current levels, the company is cheap, trading at around 6-7x EV/EBIT, 7x 2022 PE and a 8% dividend yield.
                                   In 2023, profits may be a bit lower than in 2022, as evidenced by the first quarter. Yet the further the year progresses,
                                   the easier comps will get and in the next 2 or 3 yearsNilorn is an interesting nanocap company which has proven it can
                                   generate high returns in a cyclical sector.
                                   [Source](https://augustusville.substack.com/p/nilorngruppen?utm_source=substack&utm_medium=email)
                   """,
        ),
        Stock(
            ticker_name="PAH3.DE",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=270, date=datetime(2028, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""If we value Porsche SE, we will simply add up everything the company owns, and subtract the debt.
                                   The 12.5% ownership of Porsche AG is worth around 13.4 billion euros. The 31.9% ownership of
                                   Volkswagen is worth approximately 21.7 billion euros. However, Porsche SE also has a debt of 6.6
                                   billion euros. If we add up the values: 13.4 billion + 21.7 billion - 6.6 billion, we get 28.5
                                   billion euros. At present, Porsche SE is worth around 28.5 billion euros or 93 euros per share.
                                   But these numbers may not be accurate because Volkswagen`s stock has dropped by 52% from its peak.
                                   [Source](https://moderninvesting.substack.com/p/porsche-excellence-or-value-trap?utm_source=substack&utm_medium=email)""",
        ),
        Stock(
            ticker_name="FGH",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=10, date=datetime(2025, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""The current value of the investments, cash, and real estate can be ballparked between ~$81.7M-$90.7M,
                            the book value sits at $42.7M and the market cap is $34M. Sum-of-the-parts story has been the stable
                            thesis for the better part of a year and a half now and hasn`t worked yet. So, the question begs, will it ever?
                            [Source](https://www.wsgresearch.com/p/fg-group-holdings-multiple-ways-to?utm_source=substack&utm_medium=email)""",
        ),
        Stock(
            ticker_name="OB",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=8, date=datetime(2024, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""Revenue and EBITDA are set to accelerate over the back half of 2023. OB has a defensible position in a
                                   duopoly industry. Furthermore, the move toward measurable results and greater user privacy should result
                                   in long-term tailwinds for the company. OB is incredibly asymmetric given that net cash makes up ~60%
                                   of the market cap and has an extremely low valuation of ~2.1x EBITDA on my 2023 estimate and ~1.3x on
                                   2024E. On guided numbers, it trades at ~3x EBITDA. Outbrain`s management team has proven to be skilled
                                   at capital allocation and is likely to continue to add value over time.
                                   [Source](https://www.clarksquarecapital.com/p/outbrain-ob?utm_source=substack&utm_medium=email)""",
        ),
        Stock(
            ticker_name="TOELF",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=200, date=datetime(2025, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""Tokyo Electron`s business can best be thought of in the following way. The company dominates in coating
                                   equipment with a market share in the industry of around 90%, a level similar to ASML in lithography.
                                   And the company has strong positions in etch, deposition, cleaning and probing tools with global market
                                   shares ranging from 25 to around 40 percent.
                                   [Source](https://www.techfund.one/p/tokyo-electron-a-strong-semicap-player)""",
        ),
        Stock(
            ticker_name="ANTM.JK",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=2700, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Our initial target range for ANTAM is between IDR 2,700-3,200 (currently at IDR 1,935). In our bull case,
                            our view is that the stock could double over the next 2-3 years. Factors driving business growth are strong
                            macro and fundamental demand for nickel and gold products, as well as stable to increasing commodity prices.
                            We are seeing surging demand for EV battery materials from manufacturers in China and ASEAN; a flourishing
                            EV supply chain in Indonesia will complement this.
                            [Source](https://www.pyramidsandpagodas.com/p/aneka-tambang-antmjk-indonesian-nickel?utm_source=substack&utm_medium=email)""",
        ),
        Stock(
            ticker_name="MAU.PA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=5, date=datetime(2024, 12, 15, tzinfo=timezone.utc)
            ),
            description=r"""E&P company focused in Africa, but with additional interests in France, Italy, Colombia and Venezuela.
                                   Combining some exciting prospects in Namibia with the upside from the sanction lifting in Venezuela plus
                                   an M&A halted in Nigeria pending resolution.
                                   [Source](https://moram.substack.com/p/moram-the-natural-gas-market-explained?utm_source=substack&utm_medium=email)
                   """,
        ),
        Stock(
            ticker_name="CUTR",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=365, date=datetime(2026, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Medial aesthetic company with a new groundbreaking acne treatment device AviClear.
                            Stock is oversold due to a recent boardroom brawl and a pullback in near-term guidance
                            due to the sales team focusing on AviClear instead of the base business. The recent boardroom
                            turmoil, although disruptive in the short term, is likely to pave the way for leadership upgrades.
                            AviClear is the first FDA-approved laser acne treatment device and has many advantages over its
                            main competitor Accure. AviClear has a unique business model where an annual fee of \$5k and \$1.5k
                            fee per patient is charged, instead of selling the device outright for \$100k+. Dermatologists and
                            key opinion leaders have expressed confidence in its potential to change the landscape of acne treatment.
                            The addressable market is substantial, with over 60 million people suffering from acne in the US alone.
                            If AviClear captures just 10% of the market, it could result in significant sales and earnings growth for Cutera.
                            [Source](https://ideahive.substack.com/p/new-pitch-cutera-cutr)
                   """,
        ),
        Stock(
            ticker_name="SDRL",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=105, date=datetime(2026, 4, 15, tzinfo=timezone.utc)
            ),
            description=r"""Seadrill is an offshore drilling contractor operating in key regions known as the Golden Triangle.
                                   Last year SDRL emerged from a restructuring that wiped out \$12bn of debt and put the company in a net cash position.
                                   The remaining debt is expected to be refinanced/paid down shortly paving the way for capital returns.
                                   The company has a robust order backlog, with approximately \$2.6 billion in contracts as of April 2023.
                                   This backlog provides stability in cash flows for the near term, while also allowing Seadrill to take
                                   advantage of higher day rates in 2025 and beyond. SDRL also stands out among its peers with one of the
                                   youngest and most technologically advanced fleets. Following a recent acquisition, SDRL's working
                                   drillship fleet has increased by 67\%. This provides increased upside potential in the ongoing offshore
                                   drilling upcycle. At current rates, Seadrill will likely generate a third of its current EV in FCF by 2025-2026.
                                   [Source](https://ideahive.substack.com/p/new-pitch-seadrill-srdl)""",
        ),
        Stock(
            ticker_name="LDO.MI",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=30, date=datetime(2026, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Leonardo Spa is an Italian multinational defense, security, and aerospace business. An improved
                                   backdrop for defense spending is expected to drive a significant acceleration in revenue and
                                   earnings for Leonardo over the next 3+ years. Historically low FCF conversion (~30\% of EBITA)
                                   has been one of the main reasons why investors have shied away from Leonardo in the past.
                                   The company has now completed a series of restructurings which have been a ~\€200m drag to
                                   free cash flow. Leonardo is now on a credible pathway to improve FCF conversion to ~70\%.
                                   This should drive a multiple re-rating as investors begin to see that FINMY is actually
                                   cheap on a free cash flow basis. Meanwhile, the company's real debt figure of \€1.7bn is
                                   manageable, coming in at slightly under 1.0x leverage. Management has noted debt paydown as
                                   its NO1 priority. Debt could be paid down in its entirety within the next 2-3 years.
                                   Recent public listing of a subsidiary will shine a light on the cheapness of the remaining core business.
                                   The replacement of the CEO, who was convicted of fraud, is likely to drive increased ownership by institutional funds.
                                   [Source](https://ideahive.substack.com/p/new-pitch-leonardo-spa-finmy)""",
        ),
        Stock(
            ticker_name="MMK.VI",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=193, date=datetime(2024, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""Therefore, MMK can be confidently considered between fairly valued to somewhat undervalued
                                   (definitely not overvalued in my opinion). Assuming a “normalised” 9x multiple of EBITDA,
                                   in a transaction with a strategic buyer MMK could be worth up to \€193 (+41% potential upside)
                                   on 2023 consensus numbers. If we believe it could go back to peak 2022 EBITDA, the target price
                                   can potentially be \€258 (+88% upside).
                                   To be clear, this is a 2 to 5 years investment story (no real catalyst for a quick re-rating on the horizon):
                                   the attractiveness of MMK packaging business models remains intact, but the full-realisation of the underlying
                                   potential of the investments in acquired and organic growth will require time.
                                   [Source](https://mrmarketmiscalculates.substack.com/p/mayr-melnhof-karton-ag)
                   """,
        ),
        Stock(
            ticker_name="UD.MI",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=80, date=datetime(2028, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""With a market cap below €125 million, Unidata is trading at a significant discount compared to the traded peers.
                                   Our play in Unidata is for the long term. During these years they will continue to build the fibre network which
                                   is expensive to build and significantly decreases the margins, but once it is finished, the operating leverage
                                   will play by their side, being the operator it is easy to make even better margins while gaining scale.
                                   [Source](https://moram.substack.com/p/moram-unidata-investment-thesis-jadestone?utm_source=substack&utm_medium=email)""",
        ),
        Stock(
            ticker_name="LMN.SW",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=55, date=datetime(2025, 12, 15, tzinfo=timezone.utc)
            ),
            description=r"""The governance overhang has been cleared as Lastminute has settled the issue of
                                   misused COVID funds and paid back the amount to the Swiss authorities. The company
                                   now has a new CEO and a completely new Board of Directors. This makes the stock
                                   investable again for investors. Reaching 2019 travel volumes at the current
                                   price/mix level should result in a meaningful upside to estimates. LMN is trading
                                   at an attractive valuation relative to itself and to peers. On my 2023 and 2024
                                   EBITDA numbers, LMN is trading at 4.2x and 3.3x. Adjusting out capitalized software,
                                   LMN is at ~4.5x 2024 EBITDA. The company is undergoing a strategic review that could
                                   lead to a sale. I believe that the latest trading update (Q1 2023) had some signs
                                   pointing to this scenario.
                                   [Source](https://www.clarksquarecapital.com/p/lastminutecom-lmnsw)
                   """,
        ),
        Stock(
            ticker_name="ADM.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=3100, date=datetime(2025, 12, 15, tzinfo=timezone.utc)
            ),
            description=r"""Shares are at 14.8x 2019 EPS and 40% down from peak. 2022 inflation may hit
                                   near-term profitability, likely moderately. Price hikes since 2022 mean
                                   long-term margins are secure. 2023 year-to-date datapoints show positive
                                   sector trends.
                                   [Source](https://librariancapital.substack.com/p/admiral-6-fall-after-citi-downgrade)
                   """,
        ),
        Stock(
            ticker_name="CNX",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=160, date=datetime(2030, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""They define success as generating and growing FCF per share, 30% of the
                                   company has been bought back in 2.5 years, and the Chairman wrote The Outsiders.
                                   Is CNX one of THOSE companies?
                                   [Source](https://www.wsgresearch.com/p/cnx-an-outsider-in-the-making)
                   """,
        ),
        Stock(
            ticker_name="WOLF",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=100, date=datetime(2027, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Wolfspeed is an interesting company to have a look at for several reasons.
                                   One, this is a pure play on silicon carbide, one of the highest growth areas
                                   in semiconductors. Two, Wolfspeed is vertically integrated across the entire
                                   silicon carbide value chain, from crystal growing, to wafer fabrication, to
                                   semiconductor manufacturing, while boasting strong market shares in each of
                                   these. Three, the shares are now trading at their lowest level in three years.
                                   [Source](https://www.techfund.one/p/wolfspeed-the-vertically-integrated)
                   """,
        ),
        Stock(
            ticker_name="MXCHF",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=5, date=datetime(2030, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""**Positives**: The company is very well diversified both geographically and across
                                   their 5 business segments.  Steady growth likely, with potential for significant
                                   growth is some businesses such as Fluorspar. **Negatives**: The company operates
                                   in highly competitive, cyclical markets. Global commodity prices can significantly
                                   impact margins. Balance sheet is leveraged increasing risk and potential losses to
                                   equity holders in a downturn.
                                   [Source](https://latamstocks.substack.com/p/orbia-latam-stocks-investment-analysis)
                   """,
        ),
        Stock(
            ticker_name="THO",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=123, date=datetime(2032, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""It operates in an industry where the demand is steady and growing.
                                   It`s difficult to see that people will stop choosing to go on cost-effective
                                   holidays in nature. In the past 20 years, the market has grown steadily by about 5%.
                                   [Source](https://sleepwellinvestments.substack.com/p/thor-industries-rv-monopoly-at-the)
                   """,
        ),
        Stock(
            ticker_name="UNTC",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=74, date=datetime(2024, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Economic prospects have improved due to tightening rig market conditions, leading to
                                   higher day rates and increased operating leverage.The new interim CEO, Phil Frohlich,
                                   Managing Partner of Prescott Capital Management and the company's largest shareholder
                                   with a 37% stake, is expected to drive shareholder value.The company also recently
                                   implemented a variable dividend program with an initial quarterly dividend payment
                                   of \$2.50/share (20% current yield) in Q2 2023.
                                   [Source](https://ideahive.substack.com/p/vic-pitch-summaries-june-17)
                   """,
        ),
        Stock(
            ticker_name="VMC",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=300, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""The industry is certainly cyclical, though the businesses that are more closely tied
                                   to public projects enjoy far more predictable demand. Around 35-40% of demand for the
                                   large industry players comes from the more stable publicly-funded projects.
                                   [Source](https://eaglepointcapital.substack.com/p/rock-pits)
                   """,
        ),
        Stock(
            ticker_name="MLM",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=500, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""The industry is certainly cyclical, though the businesses that are more closely tied
                                   to public projects enjoy far more predictable demand. Around 35-40% of demand for the
                                   large industry players comes from the more stable publicly-funded projects.
                                   [Source](https://eaglepointcapital.substack.com/p/rock-pits)
                   """,
        ),
        Stock(
            ticker_name="STHO",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=34, date=datetime(2027, 8, 15, tzinfo=timezone.utc)
            ),
            description=r"""Sub \$200m market cap spin-off resulting from the merger of iStar and Safehold
                                   (SAFE). The company primarily holds non-ground lease-related commercial real
                                   estate assets and has a mandate to monetize these holdings through development
                                   or asset sales. STHO holds \$320m SAFE shares, \$238m of debt, real estate and
                                   land development assets valued at \$337m (book value). \$50m of cash on the
                                   balance sheet is intended to cover four years' worth of expenses related to
                                   the management agreement with iStar, which manages STHO. If the property assets
                                   are successfully monetized at book value, Star Holdings would be worth \$34/share
                                   (140% upside). Downside looks somewhat protected as at current stock prices the
                                   property assets could be sold at just 30% book value to break even. Two primary
                                   assets of Star Holdings, Asbury Park and Magnolia Green, account for 80% of the
                                   property value. Completed properties in Asbury Park have shown strong demand
                                   while significant progress has already been made in terms of lot sales and
                                   contracts in Magnolia Green.
                                   [Source](https://ideahive.substack.com/p/vic-pitch-summaries-june-25)""",
        ),
        Stock(
            ticker_name="DWL.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=150, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""As the former GKN auto and powder metallurgy business, DWL was acquired by
                                  Melrose in 2018, restructured, and spun off. This spin-off has resulted in the
                                  undervaluation of DWL, creating an attractive investment opportunity. DWL boasts a
                                  conservative balance sheet, a strong management team, and the potential for
                                  substantial margin expansion. Company has a strong global position both with
                                  ICE and EV vehicles and should benefit from an expected recovery in the auto industry.
                                  DWL is a world leader in driveline components for automobiles and is also the
                                  #1 player globally in sinter and the second-largest player in powder metallurgy.
                                  Both segments have undergone substantial operational restructurings in recent years.
                                  Management is committed to 10% operating margins for Driveline segment at 2019 auto
                                  production levels (current margins sit around 5.5%). Company promises similar
                                  operating improvements in the Powder Metallurgy segment where EBIT margins could
                                  expand from 10% to 14%. Management's targets look achievable due to Melrose's
                                  excellent track record of creating shareholder value through its spin-offs.
                                  Melrose stock and associated spins have historically returned 1700% since their
                                  first acquisition, 10x the FTSE.
                                  [Source](https://ideahive.substack.com/p/vic-pitch-summaries-june-25)
                   """,
        ),
        Stock(
            ticker_name="SPR",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=80, date=datetime(2026, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""Primary supplier for Boeing 737 MAX fuselage and also does business with Airbus on
                            wings. With a solid outlook for 2025 and a backlog of $37bn, SPR is
                            well-positioned to benefit from a robust demand for commercial aircraft. The recent
                            quality issue and the slow ramp-up of the Boeing supply chain have caused the stock
                            price to decline, presenting an opportunistic entry point. These issues are
                            manageable and do not pose a significant threat to the company's future prospects.
                            The recent setback with quality issues, involving two fasteners on the fuselage,
                            led to a temporary and minor halt in production. This problem was not a safety
                            concern and has now been addressed, with repairs expected to be completed by July.
                            While the ramp-up of the Boeing supply chain has been slow, similar challenges
                            have been faced in the past during the 787 production period. The demand for
                            commercial aircraft is strong, with Boeing receiving new orders for the MAX and
                            Airbus growing its backlog. As production levels increase, Spirit is expected to
                            generate significant cash flow. Meanwhile, Spirit has a substantial cash reserve
                            of $568m and a debt profile that can be refinanced as it matures (most of Spirit's
                            bonds are currently trading at par). Labor contract negotiations also represent a
                            near-term challenge. However, an outcome is soon expected and management has
                            factored in wage increases similar to those agreed upon by other industry players,
                            such as Lockheed, into their guidance.
                            [Source](https://ideahive.substack.com/p/vic-pitch-summaries-june-25)
                        """,
        ),
        Stock(
            ticker_name="ARCO",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=15, date=datetime(2027, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""The opportunity to gain exposure to South America with a defensive approach.
                            This is, having a clear view on what is the dynamics affecting the company
                            (trends on food and labor inflation, customer demand, etc.), and limiting
                            the country risk that would have investing in only one country of Latin
                            America or the Caribbean. The strength of McDonald`s brand and the disparity
                            in valuations with other public restaurant chains.
                            [Source](https://moram.substack.com/p/moram-arcos-dorados-arco-investment)
                   """,
        ),
        Stock(
            ticker_name="APR.WA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=40, date=datetime(2025, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""The independent aftermarket (IAM) industry has an anti-cyclical component that generally
                            works well in any economic environment but especially in times of economic downturns.
                            When, due to a crisis, the sale of new vehicles decreases, this causes an increase in
                            the age of the vehicle fleet, resulting in the need for more maintenance.
                            [Source](https://moram.eu/investment-thesis-competition/autopartner/)
                            [Source](https://lukewolgram.substack.com/p/a-new-long-idea-auto-partner-sa)
                   """,
        ),
        Stock(
            ticker_name="FGF",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=20, date=datetime(2033, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""It`s a fool's game to try and guess how much growth we are looking at exactly but
                                   I wouldn`t be surprised if they are able to double the number of contracts over
                                   the next 2-3 years and bring in enough capital to achieve that number. This division
                                   has a ton of potential and each new contract is a piece of evidence supporting
                                   that thesis. The same can be said for the investments. The sponsor economics of
                                   raising SPACs is a lucrative business and if the company can continue to
                                   leverage their platform, I don`t see how money earned from the reinsurance division
                                   can`t be put to work here or in their merchant banking partnerships.
                                   But this doesn`t come without risk.
                                   [Source](https://www.wsgresearch.com/p/fg-financial-a-hidden-spawner)
                   """,
        ),
        Stock(
            ticker_name="SBRE.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=180, date=datetime(2025, 11, 30, tzinfo=timezone.utc)
            ),
            description=r"""Sabre shares are at 7.4x 2019 EPS and 11.3x 2021 EPS
                            The sector`s 2022 earnings downturn was exceptional and cyclical
                            EPS can double this year and be back at 2021 level by 2024
                            At 135.6p, we see 35% upside (13.6% p.a.) by end of 2025
                            But this is not attractive enough and we have long-term concerns
                            [Source](https://librariancapital.substack.com/p/sabre-insurance-shares-halved-since)
                   """,
        ),
        Stock(
            ticker_name="WCN",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=205, date=datetime(2026, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Industry structure benefits incumbents: the waste disposal business in North America
                                   is characterised by (a) high regulatory barriers (permits, extensive regulation) and
                                   (b) high capital intensity (landfills require hefty upfront capital investment).
                                   These features favour the landfills` owners` incumbents which, over time,
                                   consolidate the industry, further improving their pricing power and returns on
                                   capital.
                                   [Source](https://investmentmarathon.substack.com/p/waste-connections-wcn-us)""",
        ),
        Stock(
            ticker_name="ATEX",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=75, date=datetime(2028, 2, 15, tzinfo=timezone.utc)
            ),
            description=r"""Shares today imply just ~\$.34 MHz/Pop, which is less than the company was trading
                                   at before it received FCC approval a few years ago to execute this spectrum
                                   transition and much less than ATEX has priced its spectrum (all 5 contracts
                                   above \$1 MHz/Pop) in various signed contracts or comparable market transactions.
                                   The business is uncorrelated with the general market and has a great balance sheet.
                                   It will likely have contracted proceeds over just the next 2-3 years worth
                                   significantly more than the current EV with multiples of upside
                                   [Source](https://brightideas44.substack.com/p/unveiling-an-asymmetric-opportunity
                   """,
        ),
        Stock(
            ticker_name="MACK",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=15, date=datetime(2024, 5, 15, tzinfo=timezone.utc)
            ),
            description=r"""Special situation with the opportunity to earn a ~30% return over the next ~9
                                   months with little risk. MACK is a shell company that owns a contingent milestone
                                   payment related to the drug Onivyde, which it sold to Ipsen. The milestone
                                   payment is contingent upon FDA approval for the treatment of metastatic pancreatic
                                   ductal adenocarcinoma (mPDAC). This is an aggressive form of cancer with a short
                                   median overall survival period. Ipsen has presented compelling phase III data
                                   demonstrating the efficacy and safety of Onivyde in treating mPDAC, and intends to
                                   submit a new drug application. Given the strong phase III data, FDA approval for
                                   Onivyde's mPDAC treatment is expected to be a mere formality. Upon FDA approval,
                                   MACK is entitled to a substantial cash payment of \$225m from Ipsen, which
                                   translates to approximately \$15/share. MACK is controlled by a financially
                                   sophisticated board that owns almost 29% of the stock. Management plans to return
                                   this windfall cash to shareholders through special dividends.
                                   [Source](https://ideahive.substack.com/p/vic-pitch-summaries-july-2)
                   """,
        ),
        Stock(
            ticker_name="STG.CO",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=133, date=datetime(2025, 2, 15, tzinfo=timezone.utc)
            ),
            description=r"""STG is a relatively small company, with a current market capitalization of ~DKK9.85
                            billion (\$1.44 billion) and a current enterprise value of ~DKK14.16 billion
                            (\$2.07 billion). As a small cap, STG remains outside the purview of most investors.
                            Scandinavian Tobacco Group is headquartered in Copenhagen, Denmark, and is listed
                            under the ticker “STG” on the Nasdaq Copenhagen Stock Exchange, which further
                            restricts accessibility and interest. Cigars - especially premium handmade cigars -
                            are completely ignored by most investors and analysts, even those focused on the
                            tobacco industry. This niche isn`t just an afterthought; it receives practically
                            no thought.
                            [Source](https://invariant.substack.com/p/scandinavian-tobacco-group-serial-acquirer)
                   """,
        ),
        Stock(
            ticker_name="J4V.F",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=10, date=datetime(2027, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""All in all, Vår is a very attractive investment opportunity right now.
                            With a dividend of 15-20% this year, that I expect to grow over the next years.
                            With the acquisition of Neptune Energy and multiple projects that will be
                            finished over the next years, I expect very good shareholder returns over the
                            long run. Notably the sentiment for European oil & gas producers is bad, but
                            even with all the headwinds the stock will still perform well. Now imagine,
                            that some of these headwinds could go away.
                            [Source](https://moderninvesting.substack.com/p/var-energi-norways-dividend-monster)
                   """,
        ),
        Stock(
            ticker_name="V",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=400, date=datetime(2026, 9, 15, tzinfo=timezone.utc)
            ),
            description=r"""We believe Visa shares still offer the potential of a 20%+ annualized return
                                   by September 2026, driven by an approximately 14% EPS CAGR and its P/E re-rating
                                   from 30x to 35x. H1 FY23 results and management outlook imply Adjusted EPS will
                                   grow by 14% in FY23. Transaction volume has already been disclosed for 2 of the
                                   3 months in Q3 FY23, Q3 results should be in line with expectations, though there
                                   may be some non-operational headwinds from currency and a tax hike in Brazil.
                                   The U.S. consumer continues to be resilient. Visa`s “network of networks” strategy
                                   means it is well-placed against any new entrants, and the biggest risks to Visa are
                                   likely from governments.
                                   [Source](https://librariancapital.substack.com/p/visa-up-15-year-to-date-with-more)
                   """,
        ),
        Stock(
            ticker_name="GRVY",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=180, date=datetime(2026, 9, 15, tzinfo=timezone.utc)
            ),
            description=r"""Gravity`s sales and profit growth accelerated in Q4 2022 with the launch of
                                   Ragnarok Origin in Taiwan/HK. I expect that the momentum in top-line and EBIT
                                   will continue as the company releases RO in SE Asia and globally. GRVY`s valuation
                                   is extremely asymmetric. GRVY is currently trading at ~2.0x `24 EBITDA or a +35% FCF
                                   yield, but the downside is limited by the company`s net cash balance (\$50+ net
                                   cash/share vs. \$72 current price). The company`s growing cash pile provides for
                                   significant optionality through possible repurchases, dividends, or thoughtful M&A.
                                   The company`s game pipeline could provide valuable diversification of earnings and
                                   further upside if the company develops another hit game.
                                   [Source](https://www.clarksquarecapital.com/p/gravity-co-grvy)""",
        ),
        Stock(
            ticker_name="SFE.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=34, date=datetime(2025, 9, 15, tzinfo=timezone.utc)
            ),
            description=r"""This company might be a true hidden gem, relatively uncovered by investment
                                   professionals. The company`s new management in place since 2018 has shown great
                                   ability and has done a superb job ensuring efficient operations management,
                                   showing sound capital allocation skills. I would not be surprised if Safestyle
                                   UK plc`s capitalization multiplies by 6X in 5 years.
                                   [Source](https://valuefocusinvesting.substack.com/p/safestyle-uk-plc?)""",
        ),
        Stock(
            ticker_name="MODG",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=40, date=datetime(2028, 9, 15, tzinfo=timezone.utc)
            ),
            description=r"""Topgolf Callaway Brands is a leading golf company that provides golf
                                   entertainment experiences, designs and manufactures golf equipment, and
                                   sells golf and active lifestyle apparel and other accessories through
                                   its family of brand names.
                                   [Source](https://eloyfernandez.substack.com/p/topgolf-callaway-brands)
                   """,
        ),
        Stock(
            ticker_name="SONY",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=200, date=datetime(2027, 5, 15, tzinfo=timezone.utc)
            ),
            description=r"""Sony is a wonderful business trading at a reasonable price.
                                   The company is exposed to some of the strongest structural growth trends
                                   within entertainment and tech. Regarding investor perception, whilst Sony is
                                   comfortably out of the doghouse phase of circa 10 years ago, the company has
                                   a lot of further runway to increase its recognition as a truly leading global
                                   tech and entertainment major, and (buzzword!) as a leading “metaverse” play.
                                   [Source](https://insiderideas.substack.com/p/free-post-sony-group-6758-jp)
                   """,
        ),
        Stock(
            ticker_name="7J4.F",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=100, date=datetime(2025, 5, 14, tzinfo=timezone.utc)
            ),
            description=r"""Clasquin is operating in the global freight forwarding industry. It is a pure
                            play asset lite freight forwarding company. Clasquin has only 2.31 million shares
                            outstanding and we havent seen any dilution since the IPO in 2006. The founder owns
                            41.4% of the shares. This is a microcap with a total market value of 180 million
                            and an enterprise value of 159 million (net cash of 21 million) - based on 2022
                            year end results before the 2023 acquisition of Timar.
                            [Source](https://wintergems.substack.com/p/clasquin-epaalcla-a-french-microcap)
                        """,
        ),
        Stock(
            ticker_name="BELFB",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=83, date=datetime(2024, 9, 15, tzinfo=timezone.utc)
            ),
            description=r"""The thesis here is straightforward, just like AstroNova, we believe Bel Fuses
                            EBITDA is going to expand materially over the coming years, from $83M in 2022
                            ($100M LTM) to $120M in 2024, and we also donot think $140M is out of the cards
                            for 2025.
                            [Source](https://static1.squarespace.com/static/635cafa2259a125cc55eae33/t/64aeb0347a63bf404bec0f6f/1689169973044/Atai+Capital+-+Q2-2023+Letter.pdf)
                        """,
        ),
        Stock(
            ticker_name="7906.T",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=2109, date=datetime(2025, 9, 15, tzinfo=timezone.utc)
            ),
            description=r"""Strong growth in revenues: 15% CGAR 2019-2023.
                            The compound annual rate of the stock price (5y) is around 16%.
                            Recognizable brand in the badminton and tennis universes.
                            Geographic expansion plans in big markets such as India and the U.S.A.
                            Excellent management team, with the Yoneyama Family around 19% of shares.
                            [Source](https://eloyfernandez.substack.com/p/yonex)
                         """,
        ),
        Stock(
            ticker_name="DLA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=20, date=datetime(2025, 9, 15, tzinfo=timezone.utc)
            ),
            description=r"""Delta Apparel (DLA, \$77m market cap) has faced challenges due to the
                            COVID bullwhip effect. Despite short-term setbacks like high-cost inventory,
                            the company shows strong growth potential. It has two main segments: Salt Life,
                            a cultish brand popular among outdoorsy individuals in the Southeast U.S., and
                            Delta Group, consisting of a commoditized active wear business, and DTG2GO,
                            a digital printing specialist.
                            [Source](https://ideahive.substack.com/p/new-investment-ideas-july-16)""",
        ),
        Stock(
            ticker_name="IWB.MI",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=34.5, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""We consider IWB to be a fantastic business, well-managed, with a strong alignment
                            of interests between management and shareholders. Additionally, their capital-light
                            business model provides flexibility, and the new long-term supply contract with
                            Barbanera Family is expected to reduce the cost of goods sold from now on (last
                            year's cost was unusually high due to weather). In our opinion, there is a very
                            attractive upside with short-term catalysts, particularly with the release of
                            the 1H23 report in September.
                            [Source](https://moram.substack.com/p/moram-italian-wine-brands-iwbmi-investment)""",
        ),
        Stock(
            ticker_name="VNRX",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=10, date=datetime(2028, 3, 14, tzinfo=timezone.utc)
            ),
            description=r"""Did you know more dogs are diagnosed with cancer in the United States than humans?
                            Most dogs are diagnosed when it's too late - when physical signs are present.
                            In Q1 2023 \$VNRX is launching the first LOW COST screening test to detect cancer in dogs.
                            [Source](https://twitter.com/GalahadCapital/status/1595478489569939456)""",
        ),
        Stock(
            ticker_name="BAYN.DE",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=80, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Bayer definitely has it`s fair amount of problems. But over the last year the company
                            has shown signs of a possible turnaround.
                            [Source](https://moderninvesting.substack.com/p/bayer-the-ultimate-turnaround)""",
        ),
        Stock(
            ticker_name="8881.T",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=1000, date=datetime(2025, 9, 15, tzinfo=timezone.utc)
            ),
            description=r"""Value trap or not?
                            low institutional ownership, no analyst coverage since 2010, and only one mention
                            on social media (that I'm aware of). risks of an economic downturn
                            [Source](https://themikrokap.substack.com/p/adventures-in-the-value-trap-land)
                   """,
        ),
        Stock(
            ticker_name="AAF.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=150, date=datetime(2027, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""We think the company’s valuation suffers from what we call “lazy grouping bias”
                            — investors seem to value it like a traditional telecom company with low growth,
                            stiff competition, and high capex needs. But it’s growth profile and returns on
                            capital (even after depreciation) show that it is nothing like a mature
                            Western telecom firm.
                            [Source](https://www.biremecapital.com/cio-corner/airtel-africa)""",
        ),
        Stock(
            ticker_name="KIND-SDB.ST",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=158, date=datetime(2024, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""Kindred (KINDSDB, \$2.7bn market cap) is an online B2C sports betting and
                            iGaming operator, primarily operating in regulated markets in continental Europe
                            and the Nordics. Thesis revolves around the likelihood of Kindred being sold
                            to a strategic acquirer in the next 3-6 months
                            [Source](https://ideahive.substack.com/p/new-investment-ideas-july-23)
                   """,
        ),
        Stock(
            ticker_name="THX.V",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=1.0, date=datetime(2027, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Gold and Lithium miner from Nigeria.
                            [Source](https://twitter.com/YellowLabLife/status/1683461221687623680)
            """,
        ),
        Stock(
            ticker_name="RTX",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=120, date=datetime(2026, 8, 15, tzinfo=timezone.utc)
            ),
            description=r"""The structural growth drivers behind RTX, particularly the long-term growth
                            in global passenger air travel and rising national defense budgets, remain
                            powerful and should continue to drive strong underlying earnings growth.
                            [Source](https://librariancapital.substack.com/p/rtx-faqs-on-powdered-metal-issue)""",
        ),
        Stock(
            ticker_name="NETI",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=20, date=datetime(2025, 9, 15, tzinfo=timezone.utc)
            ),
            description=r"""Green energy transistion, Eneti announced a merger with Cadeler, another WTIV company
                            based out of Copenhagen, in June of this year. With the deal months away from closing,
                            the combined company is poised to be by far the most dominant player in an industry
                            with various tailwinds.
                            [Source](https://breeleycapital.substack.com/p/eneti-and-cadeler-offshore-oppurtunity)
                            """,
        ),
        Stock(
            ticker_name="MSFT",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=420, date=datetime(2026, 7, 15, tzinfo=timezone.utc)
            ),
            description=r"""There are signs of deceleration in some of Microsoft’s businesses, but mostly attributable
                            to temporary and/or cyclical macro factors. A more material concern is the near-term
                            cashflow headwinds from both an accelerated CapEx program and higher scheduled payments 
                            of the transition tax from the 2017 tax cut, but we expect these to be temporary.
                            At \$337.77, Microsoft shares have a 34.4x P/E and a 1.9% Free Cash Flow Yield relative 
                            to FY23. Our forecasts indicate a total return of 44% (13.5% annualized) by June 2026. Buy.
                            [Source](https://librariancapital.substack.com/p/microsoft-strong-fy23-finish-but)
                        """,
        ),
        Stock(
            ticker_name="BES.V",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=0.15, date=datetime(2026, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Braille Battery has shown consistent growth over the last four years, growing at a
                            56% CAGR. We expect this to continue as BES expands internationally and optimizes
                            its manufacturing facility. BES is planning to launch a residential backup power
                            system FYQ2/24, followed by its whole home energy storage system. Braille’s systems
                            will be the most cost-efficient in the market. BES recently purchased the exclusive
                            rights for Firebulb Technology, which is the industry’s first passive fire detection
                            system. This will be a key differentiator for Electrafy systems.
                            [Source](https://mcusercontent.com/4bc421505c66d079778a0d0be/files/7798d81a-11da-6e00-90b1-f1d6a27089ea/20230727_Atrium_BES_Operational_Update.pdf)
                        """,
        ),
        Stock(
            ticker_name="CHTR",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=600, date=datetime(2026, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""EBITDA margin should expand again in H2, revenue growth should accelerate further as
                            benefits from the current CapEx program materializes more fully, and CapEx normalizing
                            from 2026 will help FCF significantly
                            [Source](https://librariancapital.substack.com/p/charter-continuing-to-turn-the-corner)
                        """,
        ),
        Stock(
            ticker_name="S85.SI",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=1.029, date=datetime(2027, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""Straco Corporation Limited is a Singapore-based company of tourist attractions in
                            Singapore and China. The Company operates through two segments: Aquariums and
                            Observation Wheel. Recovery from COVID in China.
                            [Source](https://eloyfernandez.substack.com/p/straco-corp)
                        """,
        ),
        Stock(
            ticker_name="EDAC.MI",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=43, date=datetime(2027, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""EdiliziAcrobatica is a fast growing company with a dominant market position in the
                            industry of facades. Founder led business with high insider ownership. Expansion
                            into Spain, France, UAE, Nepal, etc. should be a massive boost for revenues.
                            [Source](https://moderninvesting.substack.com/p/ediliziacrobatica-italys-compounding)
                        """,
        ),
        Stock(
            ticker_name="KDP",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=47, date=datetime(2025, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""KDP is now a much cleaner story and the fundamental outlook is looking very 
                              promising. Coffee has begun its rebound and represents an early stage-margin 
                              recovery story on track for a major 2H inflection. Increased emphasis is being 
                              placed on the profitability of K-Cups where historically the priority has been 
                              market share at the expense of margins.
                              [Source](https://acrobat.adobe.com/id/urn:aaid:sc:VA6C2:cee563c1-084f-4c18-ab0f-ebbab6335ef9)
                              [Update](https://acrobat.adobe.com/id/urn:aaid:sc:VA6C2:f3d5f190-415b-4400-a193-5492f1bf38fe)
                           """,
        ),
        Stock(
            ticker_name="ATT.WA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=50, date=datetime(2025, 8, 15, tzinfo=timezone.utc)
            ),
            description=r"""For global live, Fertilizers are close to as important as water. Over the last 
                            75 years the human population has tripled. While the output of for example corn 
                            has grown by 450%, the land area used for farming corn hasn’t gone up at all ! 
                            This is the result of more efficient farming and importantly fertilizers.
                            [Source](https://moderninvesting.substack.com/p/1-fertilizer-market)
                        """,
        ),
        Stock(
            ticker_name="MOS",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=80, date=datetime(2025, 8, 15, tzinfo=timezone.utc)
            ),
            description=r"""For global live, Fertilizers are close to as important as water. Over the last 
                            75 years the human population has tripled. While the output of for example corn 
                            has grown by 450%, the land area used for farming corn hasn’t gone up at all ! 
                            This is the result of more efficient farming and importantly fertilizers.
                            [Source](https://moderninvesting.substack.com/p/1-fertilizer-market)
                        """,
        ),
        Stock(
            ticker_name="FXPO.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=140, date=datetime(2025, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""In conclusion, Ferrexpo presents a compelling investment opportunity given its 
                            strong financial performance, competitive advantages, and attractive valuation. 
                            While the geopolitical risks associated with its operations in Ukraine are a concern, 
                            we believe that a contrarian may see Ferrexpo with potential upside. If geopolitical 
                            tensions ease, Ferrexpo's financial performance could improve significantly from 
                            currently depressed levels. Iron ore prices may also recover over time as demand 
                            rebalances with supply, particularly with the rebuilding needs in Ukraine.
                            [Source](https://gilescapital.substack.com/p/our-new-investment-idea-ferrexpo)
                        """,
        ),
        Stock(
            ticker_name="RELL",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=40, date=datetime(2027, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""There will likely be significant volatility in the share price of Richardson 
                            in the short term, notably on/around the next two earnings reports.
                            Since 2024 it should get better.
                            [Source](https://thefondinvestor.substack.com/p/richardson-electronics-rell)
                        """,
        ),
        Stock(
            ticker_name="EL",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=234, date=datetime(2026, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""We believe EL is a great business with the valuation of a mediocre one. 
                            At \$156.59, relative to CY19 earnings (which do not include subsequent growth), 
                            shares are at 25.6x Non-GAAP EPS and have a 2.7% Free Cash Flow (“FCF”) Yield; 
                            relative to FY22 (which somewhat over-earned), the Non-GAAP P/E is 21.2x and the 
                            FCF Yield is 3.0%. Our updated forecasts show a total return of 49% 
                            (15.3% annualized) by June 2026; the actual annualized return may turn out to be 
                            higher, should EL shares re-rate upwards early once signs of recovery become visible.
                            [Source](https://librariancapital.substack.com/p/estee-lauder-near-covid-19-low-after)
                        """,
        ),
        Stock(
            ticker_name="HFG.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=1400, date=datetime(2027, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Hilton Food Group (HFG-L) presents an opportunity to buy a steadily-growing white-label 
                            meat and seafood supplier at a 40%+ discount to its historical EV/EBITDA multiple. HFG’s 
                            share price plummeted in 2022 as the company’s multi-customer segment (18% of revenues) 
                            was forced to issue two profit warnings due to spiking seafood prices following the Russian 
                            fish exports ban. The market seems to have overreacted as HFG's market cap dropped more than 
                            £500m on a £26m temporary profit reduction.
                            [Source](https://ideahive.substack.com/p/actionable-investment-ideas-5)
                        """,
        ),
        Stock(
            ticker_name="ASML",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=700, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""The semiconductor industry is expected to grow at a CAGR of +9% between 2020-2030E. 
                            I believe ASML is one of the potential beneficiaries of the growing semiconductor industry. 
                            [Source](https://www.from100kto1m.com/p/asml-holding-asml-deep-dive)
                        """,
        ),
        Stock(
            ticker_name="BAR.BR",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=50, date=datetime(2026, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Today’s company is Barco (€1.8bn market cap), a Belgian technology company with a focus on 
                            imaging technology. This is a high-quality, well-financed, cool company with a positive 
                            outlook for the next years. The shares are currently on sale due to a few specific reasons, 
                            providing an attractive opportunity into an original thesis at a heavily discounted price. 
                            Not often does decent size quality + growth + strong balance sheet trade at a large discount. 
                            As Barco continues to perform and the current uncertainty subsides, the share price should 
                            rerate back. A normalisation of the multiple on growing earnings indicates >100% upside 
                            over the next 2/3 years.
                            [Source](https://toffcap.substack.com/p/barco)
                        """,
        ),
        Stock(
            ticker_name="VEEE",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=3.0, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Twin Vee PowerCats (\$VEEE) is a company that manufactures recreational power sport boats 
                            and has been in operation for over 25 years. However, it went public recently (August 2021), 
                            raising \$18 MM to finance its growth. Subsequently, it spun off one of its three business 
                            lines, electric boats (Forza X1 \$FRZA), in August 2022, raising \$15 MM.
                            [Source](https://moram.substack.com/p/twin-vee-and-forza-x1-analysis-veee)""",
        ),
        Stock(
            ticker_name="FRZA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=3.0, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Twin Vee PowerCats (\$VEEE) is a company that manufactures recreational power sport boats 
                            and has been in operation for over 25 years. However, it went public recently (August 2021), 
                            raising \$18 MM to finance its growth. Subsequently, it spun off one of its three business 
                            lines, electric boats (Forza X1 \$FRZA), in August 2022, raising \$15 MM.
                            [Source](https://moram.substack.com/p/twin-vee-and-forza-x1-analysis-veee)""",
        ),
        Stock(
            ticker_name="AMZN",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=160, date=datetime(2026, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""At the end of the day, my investment in the name rests on the track record of the company 
                            being able to: 
                            1) Offer each customer an asymmetric value proposition
                            2) Reinvest their own cash flow into their operation at high rates of return
                            3) Spawn higher margin businesses from the launching pad of their retail operation
                            When it comes to my own expectations for the company, coming out of this massive Capex 
                            cycle I expect these investments to begin to bare fruit and for OCF to surpass $100B by 
                            the end of 2026. This would mean a growth rate of ~17.9% a year, I think it’s doable.
                            [Source](https://www.wsgresearch.com/p/amazon-musings)""",
        ),
        Stock(
            ticker_name="XPOF",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=34, date=datetime(2023, 12, 15, tzinfo=timezone.utc)
            ),
            description=r"""There’s an old saying, “Insiders sell for a lot of reasons, but they only buy for one 
                            reason (they think the stock is going up).” And it very well might be these small, 
                            short-swing insider buys are the exception that prove the rule (or I guess saying in 
                            this case).
                            [Source](https://www.yetanothervalueblog.com/p/weekend-thoughts-xpofs-insider-buy)""",
        ),
        Stock(
            ticker_name="TGNA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=21, date=datetime(2024, 11, 15, tzinfo=timezone.utc)
            ),
            description=r"""US president election.""",
        ),
        Stock(
            ticker_name="DGE.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=5420, date=datetime(2026, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""Diageo shares have now fallen 18% since 2021 year-end. FY23 results showed solid growth 
                            in sales and earnings. U.S. inventories have normalized; demand is healthy. Adjusted 
                            EBIT should grow at 6-9% annually as targeted. We see 62% total return (19.1% p.a.) 
                            by June 2026. Buy
                            [Source](https://librariancapital.substack.com/p/diageo-shares-fell-again-after-fy23)
                        """,
        ),
        Stock(
            ticker_name="SENEA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=110, date=datetime(2026, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""You can currently purchase shares of a profitable, market-leading consumer staples business 
                            below 40% of (tangible) book value and below net current asset value. Unlike most net-nets, 
                            this one has compounded book value per share at nearly 10% per year for the past 20 years, 
                            and the business has gotten better over the past few years aŌer a major compeƟtor pulled 
                            out of the market. The stock has no sell-side coverage and has recently experienced forced 
                            selling due to its removal from an index.
                            [Source](https://drive.google.com/file/d/1wAm1w3eEZCHCfY-e1Lzu0gvyGW7uN4KL/view)
                        """,
        ),
        Stock(
            ticker_name="CNO.V",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=15, date=datetime(2033, 3, 14, tzinfo=timezone.utc)
            ),
            description=r"""While the company is tiny, they are a leader in SPS and cryomilling technology and have spent 
                        the last decade building both technical expertise and a network of relationships with leading 
                        National Laboratories, venture-backed startups, and Fortune 500 companies via research and 
                        development projects.
                        [Source](https://whiteoutcapital.com/writeups/california-nanotechnologies)
                    """,
        ),
        Stock(
            ticker_name="AZEK",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=42.50, date=datetime(2024, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""AZEK is a well-managed maker of composite decking and exteriors that continues to have a 
                        tailwind as more buyers shift to composite materials from wood products Conversion from 
                        wood was strong in the past five years and there’s solid runway left that could make for 
                        strong cash flow in the next five years.
                        [Source](https://capitalincentives.substack.com/p/azek-azek)
                    """,
        ),
        Stock(
            ticker_name="VOLUE.OL",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=34, date=datetime(2025, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""Volue gives us the opportunity to profit fron the energy transmission not 
                            only in Europe but in the entire world. The company has a strong market position, 
                            which is proven by there large clients. With high recurring revenues and strong 
                            growth.
                            [Source](https://moderninvesting.substack.com/p/volue-asa-profiting-from-european)
                        """,
        ),
        Stock(
            ticker_name="EHAB",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=24, date=datetime(2024, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""Several recent developments suggest that the company sale is likely. EHAB has recently 
                            come under pressure from activist AREX Capital which has been pushing the company to start 
                            a strategic review and initiate a sale process. While the activist’s board nominees have 
                            since been rejected, the company has recently announced plans to launch a strategic 
                            review, indicating that the management might be open to a transaction. 
                            [Source](https://ideahive.substack.com/p/actionable-investment-ideas-7)
                        """,
        ),
        Stock(
            ticker_name="RI.PA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=296, date=datetime(2026, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""As with other Spirits stocks, we believe the current weakness in PR shares is due to 
                            investor fears of a deceleration in sector growth, made worse by volatile quarterly 
                            growth rates that followed unusual inventory moves last year. In PR’s case, management 
                            is expecting sales to decline in both the U.S. and China in Q1 FY24, but to show 
                            positive growth for the full year. 
                            [Source](https://librariancapital.substack.com/p/pernod-ricard-near-52-week-low-after)
                        """,
        ),
        Stock(
            ticker_name="APN.WA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=30, date=datetime(2024, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Aplisens is a Poland industrial sensor manufacturer trading at the Warsaw Stock 
                            Exchange (WSE:APN) who has seen a surge of sales in 2022 and 2023 (first 6 months) 
                            which has translated into an even higher increase in profits.
                            [Source](https://wintergems.substack.com/p/apn-aplisens-a-growing-industrial)
                        """,
        ),
        Stock(
            ticker_name="NESN.SW",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=150, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Over the years, NESN has generally been outperforming the S&P 500 up till 2020. 
                            Since then, the share price has underperformed the index by around 100%-pts due 
                            to an after-effect of the recent pandemic i.e. 1) record-level commodities prices, 
                            2) a decline in consumer sentiment and 3) ongoing supply chain disruptions.  Even 
                            then, I believe it is a good time to accumulate while the valuation seems to be 
                            attractive. Especially if I aim to invest and hold for the long term.
                            [Source](https://intvestor.substack.com/p/nestle-deep-dive)
                        """,
        ),
        Stock(
            ticker_name="ERA.PA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=80, date=datetime(2024, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""The biggest driver of growth for Eramet however will be the energy transition and in 
                            particular the battery metals it mines. Both nickel and lithium play an important part 
                            in battery manufacturing and thus the electric vehicle market. According to Goldman Sachs, 
                            global electric vehicle sales will jump to 73 million units by 2040 which compares to 
                            around 2 million for 2020. Electric vehicles will make up close to 61% of vehicles globally.
                            [Source](https://www.porchester.info/eramet-03092023)
                        """,
        ),
        Stock(
            ticker_name="EYE",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=30, date=datetime(2024, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""A recent short-term price dislocation at National Vision presents an opportunity to buy 
                            one of the leading eyewear retailers at a discount to its intrinsic value. EYE shares have 
                            plummeted over 30% since Walmart announced plans to end its shop-in-shops partnership with 
                            National Vision, accounting for 10% of EYE’s EBITDA. The market seems to have overreacted 
                            as the actual EBITDA loss is likely to be lower.
                            [Source](https://ideahive.substack.com/p/actionable-investment-ideas-9)
                        """,
        ),
        Stock(
            ticker_name="CNS.MI",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=7, date=datetime(2026, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""The opportunity to invest at a low valuation exists as CNS shares plummeted c. 20% in 
                            Dec’22 driven by a cut in 2023 topline growth guidance (31-44% vs 46-51% sales CAGR 
                            for 2021-2024 guided previously). The market seems to have overreacted as the guidance 
                            cut was primarily due to delays and supply chain shortages as opposed to any structural 
                            changes in the market. CNS is likely to continue displaying solid growth going forward 
                            due to increasing number of orders, as indicated by bookings growing 72% in Q1’23 
                            year-over-year. Other potential growth drivers include the expansion in the UK, a 
                            larger production facility in Italy and numerous R&D projects.
                            [Source](https://ideahive.substack.com/p/actionable-investment-ideas-9)
              """,
        ),
        Stock(
            ticker_name="SPR.WA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=792, date=datetime(2026, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""But Spyrosoft is also not without problems, in their last earnings report (H1 2023), 
                            we saw revenues rise 47%, but EBITDA margins dropped to 8% as a result of higher 
                            investments and higher salaries. So the most important factor to consider in our assumption 
                            is the margin. If I do the above calculation with 14% margins it will look out of this 
                            world. But if I do them with 7% it will look pretty bad. Another risk is that the dilation 
                            is getting out of hand and that shareholders basically throw money down a black hole.
                            [Source](https://moderninvesting.substack.com/p/the-most-valuable-resource-in-the)
                        """,
        ),
        Stock(
            ticker_name="ALTO",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=7, date=datetime(2024, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Alto Ingredients (ALTO) - Commodity ethanol producer that might get sold at a significant 
                            premium to current share price levels in the near-term. Activist Raper Capital has recently 
                            sent a letter to the company, pushing the management to explore a transaction. The sale 
                            seems likely given that the company lacks the liquidity to pull off the large ongoing 
                            transformation away from commodity ethanol towards higher-margin and value-added proteins 
                            and alcohols.
                            [Source](https://twitter.com/ideahive/status/1704058834514255958?s=12&t=QZ4ZwBXk6T2ciRZLXv-_Iw)
                        """,
        ),
        Stock(
            ticker_name="248070.KS",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=50000, date=datetime(2026, 9, 15, tzinfo=timezone.utc)
            ),
            description=r"""Solum is the worlds second largest provider of electronic shelf labels (ESL) which allow 
                            retail store managers to update product information remotely. The company is currently 
                            trading at 12x forward earnings - substantially below the 20-22x multiples for peers 
                            E-Ink Holdings and SES-imagotag. The discount is largely explained by the fact that 
                            Solum still generates two-thirds of its revenues from the mature and lower-margin 
                            electronic components segment. However, Solum shares are expected to gradually re-rate 
                            closer to peer multiples as the business mix continues to shift towards the 
                            higher-margin/growth ESL segment (two-thirds of Solums 2023E operating income). 
                            The ESL business seems to have plenty of growth runway as the recent partnership between 
                            SES-imagotag and Walmart is expected to increase ESL penetration substantially above the 
                            current 5%.
                            [Source](https://ideahive.substack.com/p/actionable-investment-ideas-10)
                        """,
        ),
        Stock(
            ticker_name="MRL.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=10, date=datetime(2024, 11, 15, tzinfo=timezone.utc)
            ),
            description=r"""Marlowe is a high-quality recurring services/software roll-up available at a significant 
                            discount to its peers and intrinsic value. The company currently trades at 8x run-rate 
                            EBITDA compared to 15-20x peer multiples. The opportunity exists as MRL shares have 
                            significantly de-rated since 2022 due to concerns about leverage, continuing one-off 
                            restructuring costs and lack of free cash flow generation. The bears have argued that 
                            Marlowes one-off acquisition restructuring costs are recurring and that the company will 
                            not able to generate meaningful cash flows. However, both of these concerns are expected 
                            to be disproved in the near-term.
                            [Source](https://ideahive.substack.com/p/actionable-investment-ideas-10)
                        """,
        ),
        Stock(
            ticker_name="GOOG",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=200, date=datetime(2024, 11, 15, tzinfo=timezone.utc)
            ),
            description=r"""Ad revenues grew 9.5% in Q3, including 12.5% in YouTube
                            Ad revenues had a 2019-23 CAGR of ~15% in each of Q1-3
                            Google Cloud revenue growth slowed, but was still 22%
                            EPS is up 18.8% YTD; P/E is 24.7x relative to LTM EPS
                            [Source](https://librariancapital.substack.com/p/alphabet-core-ad-revenue-growth-back)
                        """,
        ),
        Stock(
            ticker_name="CRWD",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=200, date=datetime(2024, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Crowd Strike - second (after MSFT) in cyber security.""",
        ),
        Stock(
            ticker_name="TSLA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=400, date=datetime(2024, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""EV cars.""",
        ),
        Stock(
            ticker_name="NVDA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=600, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""AI, Gaming boom.""",
        ),
        Stock(
            ticker_name="JEV.V",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=0.5, date=datetime(2025, 4, 15, tzinfo=timezone.utc)
            ),
            description=r"""Over the past month, Jericho Energy Ventures Inc. (JEV:TSXV, OTC:JROOF) has reported 
                            several promising updates which reaffirm our investment thesis and target price. This 
                            includes testing updates from H2U (portfolio company), an MOU between JEV’s EU partner, 
                            Exogen and hydrogen supplier, Lhyfe SA, as well as, receiving a new patent for the DCC 
                            boiler. 
                            [Source](https://mcusercontent.com/4bc421505c66d079778a0d0be/files/020f637a-4276-e5c6-325a-5fdcb3cc0ef7/20230926_Atrium_JEV_Recent_Developments.pdf)
                        """,
        ),
        Stock(
            ticker_name="GAN",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=3.0, date=datetime(2023, 12, 30, tzinfo=timezone.utc)
            ),
            description=r"""It would seem that the strategic review is progressing well and the company just needed 
                            some additional time to carry it through to the finish line. Sega Sammy, quite likely to be 
                            one of the interested parties, agreed to provide this financial flexibility. At the same 
                            time, Sega ensured itself a juicy payoff on the loan in case it is not a winning party in 
                            the bidding processes. In a sale scenario, I expect GAN to be worth $3-$5/share.
                            [Source](https://www.specialsituationinvestments.com/2023/06/gan-limited-gan-company-sale-upside-tbd/)
                        """,
        ),
        Stock(
            ticker_name="TEP.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=2500, date=datetime(2025, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Telecom Plus market themselves as Utility Warehouse - All of your home services in one 
                            place, the 8th largest utility supplier in the UK. They supply households and small 
                            businesses throughout the UK with a wide range of essential services under the Utility 
                            Warehouse brand.  They supply broadband, mobile, energy and insurance.  The business 
                            offers customers -Simplicity - just one simple bill for all your home services. Savings 
                            - compared with the prices they were previously paying. Service - delivered by 
                            award-winning UK-based support teams.
                            [Source](https://cockneyrebel.substack.com/p/telecom-plus-tep)
                        """,
        ),
        Stock(
            ticker_name="SYNA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=100, date=datetime(2024, 5, 15, tzinfo=timezone.utc)
            ),
            description=r"""Synaptics next frontier of semiconductor growth could be quite fruitful though I have my 
                            reservations the company can grow at a CAGR of 12% in the next five years. There’s going 
                            to be a new business cycle for Synaptics (they experience them frequently) and higher stock 
                            prices with that, at some point. The bear case is that Synaptics grows at a CAGR of 5% or 
                            less and EBITDA margins fall back to the historical norm near 15%. The bull case scenario 
                            would be that Synaptics realizes higher growth from its IoT portfolio and higher EBITDA 
                            margins than 20%. 
                            [Source](https://capitalincentives.substack.com/p/synaptics-syna)
                        """,
        ),
        Stock(
            ticker_name="ALCLA.PA",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=110, date=datetime(2024, 9, 15, tzinfo=timezone.utc)
            ),
            description=r"""Trades at a 30% discount to Peers its a microcap with lots of room left to grow both 
                            geographically and in density including the Africa trading routes. Can do small bolt-on 
                            acquisitions of local SMEs - too small for large cap. Addresses niches with pricing power 
                            (high value items) Net profit should grow with scale faster than gross profit - G&A 
                            overhead, new offices startup costs. Clasquin is finally reaching a certain scale. 
                            Shareholder friendly (large payout dividends) and founder with 40%+ ownership 
                            The balance sheet is pristine with a net cash balance of 3m (subtracting long term debt) 
                            which should allow to do bolt-on acquisition.
                            [Soruce](https://wintergems.substack.com/p/alcla-french-microcap-freight-forwarder)
                        """,
        ),
        Stock(
            ticker_name="YAK.V",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=2, date=datetime(2024, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""So, in short, either MGG finds something interesting to acquire and transforms itself or 
                            it will return capital. At the current share price we are only paying for roughly MGG’s 
                            listed investment portfolio and not much for the rest. Furthermore, if you like uranium 
                            and oil, you have a chance to gain exposure to the sector - and Kuppy's investment skills - 
                            via YAK at roughly the prices of before the recent run-up.
                            [Source](https://toffcap.substack.com/p/mongolia-growth-group)
                        """,
        ),
        Stock(
            ticker_name="CRDA.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=7000, date=datetime(2026, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Shares has limited downside but potentially dramatic upside
                            Customer de-stocking is industry-wide and one-off in nature
                            Shares are at 24x 2023 EPS even if H1 weakness continues
                            At 4,712p, base case is 58% upside (15.6% p.a.) by end of 2026
                            IRR can be much higher if sentiment improves or a buyer emerges
                            [Source](https://librariancapital.substack.com/p/croda-back-to-may-2020-levels-on)
                        """,
        ),
        Stock(
            ticker_name="LDB.MI",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=3, date=datetime(2024, 7, 15, tzinfo=timezone.utc)
            ),
            description=r"""Lindbergh’s services bring significant benefits to their customers’ productivity and reduce 
                            their environmental impact. Unique positioning in the in-night in-boot delivery service 
                            thanks to the proprietary technology platform that allows offering complementary services 
                            to increase the productivity of technicians. High standing and loyal client portfolio of 
                            multinational customers like Jungheinrich, Kion, Linde, Toyota, Kone, RICOH and 
                            Still illiquid micro-cap with high insider ownership of 67 %. Revenues in H1 ‘23 +19.5 %, 
                            EBIT +39.4%, Net Profit +40% successful (and faster than expected) turnaround of the 
                            French subsidiary should further increase the overall margins in the coming years 
                            EV/EBIT ‘23 of 10.3x, P/E of 11.6x  
                            [Source](https://underfollowedstocks.substack.com/p/lindbergh)
                        """,
        ),
        Stock(
            ticker_name="SQM",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=70, date=datetime(2025, 5, 15, tzinfo=timezone.utc)
            ),
            description=r"""Even if the prices of lithium stayed at these levels (-70% from the highs), companies 
                            like Albermarle or SQM are attractively priced and will have impressive growth over the 
                            coming years. My personal favorite is SQM, since the company is returning capital to 
                            shareholders. 
                            [Source](https://moderninvesting.substack.com/p/lithium-betting-on-the-inevitable)
                        """,
        ),
        Stock(
            ticker_name="SAVE",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=31, date=datetime(2024, 6, 30, tzinfo=timezone.utc)
            ),
            description=r"""The ongoing combination between JetBlue and Spirit Airlines offers a compelling merger 
                            arbitrage play with a potential 88% return in less than a year. This opportunity exists 
                            due to antitrust concerns as the DOJ has filed a lawsuit to stop the merger and the trial 
                            is set for October 16. The market appears to be mispricing the odds of a favorable 
                            litigation outcome as antitrust arguments seem overblown. The combined SAVE and JBLU would 
                            remain only the fifth largest airline in the US, with the four legacy carriers controlling 
                            80% of the market. 
                            [Source](https://ideahive.substack.com/p/actionable-investment-ideas-12)
                        """,
        ),
        Stock(
            ticker_name="HUMBLE.ST",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=24.5, date=datetime(2025, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""Decade driven by changing consumer preferences. Invest at half the EBITDA multiple of 
                            SMID-cap staple peers despite having ~2x the expected EBITDA growth. Invest alongside a 
                            management team and Board that has significant equity exposure and have been increasing 
                            their stake. Invest at a price we estimate is a ~50% discount from a private equity bid 
                            less than one year ago.
                            [Source](https://static1.squarespace.com/static/5aaacb57506fbe4636414126/t/651336f09fd2b91b8a91467f/1695758065852/Alta+Fox+HUMBLE+SS+Presentation+Sept+2023.pdf)
                        """,
        ),
        Stock(
            ticker_name="BLD",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=300, date=datetime(2025, 1, 15, tzinfo=timezone.utc)
            ),
            description=r"""BLD, a major player in the insulation industry, offers distinctive advantages for 
                            stakeholders. For manufacturers, BLD's extensive scale provides cost leverage and a 
                            valuable partnership, streamlining distribution and reducing costs. Contractors and 
                            home builders benefit from BLD's national reach, receiving a reliable and convenient 
                            one-stop-shopping experience with flexible delivery options and favorable payment terms. 
                            Moreover, BLD's acquisition strategy allows acquired businesses to maintain their local 
                            approach while gaining access to national resources, leading to enhanced efficiency and 
                            cost savings. Overall, BLD stands out in the insulation business by offering unique 
                            benefits to manufacturers, contractors, home builders, and acquired distributors.
                            [Source](https://justvalue.substack.com/p/topbuild-bld-mastering-the-insulation)
                        """,
        ),
        Stock(
            ticker_name="LRN",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=80, date=datetime(2026, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""Trend-setting business with significant potential: Growing demand for virtual education due 
                            to widespread acceptance (largely driven by COVID-19) and the new generation of parents who 
                            are digital natives. Additionally, the development of AI can further enhance scalability. 
                            Since 2018, revenue has grown from $918 million to $1.9 billion, expanding EBITDA and EBIT 
                            margins (operating leverage) and increasing EPS by 226% in the last 4 years. Development of 
                            a new division that has experienced organic growth of 91% and 71% in 2022 and 2023, 
                            respectively. Healthy financial situation with net debt close to $0MM
                            [Source](https://moram.substack.com/p/stride-thesis-detailed-analysis-of)
                        """,
        ),
        Stock(
            ticker_name="DRX.TO",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=8, date=datetime(2027, 3, 15, tzinfo=timezone.utc)
            ),
            description=r"""ADF is entering a multi-year growth phase due to major tailwinds in
                            infrastructure spending and non-residential construction.
                            ADF spent the last two years adding a robotic fabrication line to its
                            Terrebonne, Quebec facility, which has significantly expanded margins.
                            The Company has largely improved its balance sheet over the last year.
                            ADF currently trades at 3.6x FY25E EBITDA compared to steel fabricators
                            at 7.0x and Canadian industrials at 8.3x.
                            [Source](https://mcusercontent.com/4bc421505c66d079778a0d0be/files/60feaaca-daef-1830-9af3-ea2144fdb80e/20231016_Atrium_DRX_Initiation_Report.01.pdf)
                        """,
        ),
        Stock(
            ticker_name="BAC",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=50, date=datetime(2026, 11, 15, tzinfo=timezone.utc)
            ),
            description=r"""Deposits, Net Interest Margin and NII were all flattish q/q in Q3.
                            NII will decline modestly, but IB Fees and Expenses should improve.
                            YTD credit costs comparable to 2019; ROTCE of 16.1% is representative.
                            Basel III impact is less than the 20% headline due to excess capital now.
                            [Source](https://librariancapital.substack.com/p/bank-of-america-stable-q3-85x-pe)
                        """,
        ),
        Stock(
            ticker_name="U-UN.TO",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=50, date=datetime(2026, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""Over the next 12-18 months, which commodity has a more attractive demand picture? 
                            The one whose consumption is primarily tied to economic growth/development and maybe 
                            the Green Energy transition? Or the one that’s mission-critical and a small COG in a 
                            large, OPEX-driven demand cycle? 
                        """,
        ),
        Stock(
            ticker_name="YCA.L",
            period=period,
            interval=interval,
            expectation=Expectation(
                price=50, date=datetime(2026, 6, 15, tzinfo=timezone.utc)
            ),
            description=r"""Over the next 12-18 months, which commodity has a more attractive demand picture? 
                            The one whose consumption is primarily tied to economic growth/development and maybe 
                            the Green Energy transition? Or the one that’s mission-critical and a small COG in a 
                            large, OPEX-driven demand cycle? 
                        """,
        ),
    ]

    return reversed(ideas)
