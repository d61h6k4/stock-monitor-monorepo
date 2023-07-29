from datetime import datetime, timezone

from stock_monitor_data.models import Arbitrage, Stock


def arbitrages(period: str):
    res = [
        Arbitrage(
            target=Stock(ticker_name="ATVI", period=period),
            buyer=Stock(ticker_name="MSFT", period=period),
            offer_price=95,
            additional_buyer_ratio=0,
            expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
            commentary="""**Main risk** - regulatory approval. The spread mainly exists due to regulatory
                                    concerns over MSFT's potential abuse of power and potential restriciton of ATVI
                                    games solely to Xbox console. UK and European antitrust watchdogs, among others
                                    have started their inquiries into the transaction. EU Commission has extended it's
                                    deadline for a decision til Apr'23. This month, Chinese regulators rejected the
                                    simplified filling request for the merger. Recent rumors on the merger suggest that
                                    FTC plans to block the merger. Warren Buffet's Berkshire is also participating in
                                    this merger arb play providing some confidence in the successful outcome and/or
                                    a well-protected downside on ATVI standalone basis.""",
        ),
        Arbitrage(
            target=Stock(ticker_name="IRBT", period=period),
            buyer=Stock(ticker_name="AMZN", period=period),
            offer_price=61,
            additional_buyer_ratio=0,
            expecting_closing=datetime(2023, 8, 31, tzinfo=timezone.utc),
            commentary="""**Main risk** - regulatory approval. The spread has widened from 5% to over 15% as market
                                started pricing in higher likelihood of regulatory hurdles. Two months ago the parties
                                received the 2nd request from the FTC. Soon after, several senators began pushing the FTC to
                                block the transaction. Concerns were raised regarding potential privacy infringements and
                                Amazon's history of anti-competitive acquisitions. FTC review is ongoing.""",
        ),
        Arbitrage(
            target=Stock(ticker_name="SAVE", period=period),
            buyer=Stock(ticker_name="JBLU", period=period),
            offer_price=31,
            additional_buyer_ratio=0,
            expecting_closing=datetime(2024, 6, 30, tzinfo=timezone.utc),
            commentary=r"""**Main risk** - regulatory approval. The current soread is mainly due to antitrust
                                    concerns. DOJ has issued a second request and is currently reviewing the merger.
                                    JBLU has proposed divestitures in overlapping areas - this could alleviate
                                    antitrust concerns. Moreover, SAVE recently reached agreement with pilots union.
                                    Another DOJ concern relates to JBLU's Northeast Alliance partnership (NEA) with
                                    American Airlines. In October, a motion to dismiss the DOJ case against NEA has been
                                    denied. Now the decision comes down to the judges reading of andtrust law which
                                    could signincantly delay the decision. Hence, SAVE_JBLU merge outcome might also
                                    depend on the outcome of NEA trial, last month. JBLU's management reiterated
                                    confidence in merger closing in H1'24""",
        ),
        Arbitrage(
            target=Stock(ticker_name="BKI", period=period),
            buyer=Stock(ticker_name="ICE", period=period),
            offer_price=68,
            additional_buyer_ratio=0.0682,
            expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
            commentary="""**Main risk** - regulatory approval. Shareholders have already approved the merger. However,
                                Community Home Lender Association has called regulators to block the merger over antitrust
                                concerns saying that the combined company will have too much pricing power in the small/medium
                                mortgage banking sector. The companies each hold dominant market shares in speicfic US mortgage
                                software segments - servicing (BKI) and origination (ICE) - suggesting the merger will lead to
                                substantial vertical integration. Recently ICE agreed to an extended FTC review with reiterating
                                its expectation merger completion by H1'23. Since then, however, a congresswoman came
                                out, urging the FTC to tightly scrutinize the transaction
                                """,
        ),
        Arbitrage(
            target=Stock(ticker_name="TSEM", period=period),
            buyer=Stock(ticker_name="INTC", period=period),
            offer_price=53,
            additional_buyer_ratio=0,
            expecting_closing=datetime(2023, 12, 31, tzinfo=timezone.utc),
            commentary="""**Main risk** - regulatory approval. The merger will require numerous antitrust
                                and foreign investment approvals. Intel's CEO has noted that regulatory clearance has
                                already been received in several geographies. The transaction continues to be held up
                                by Chinese regulators, which have been increasing scrutinty over the merger in a
                                strategically important semiconductor space. For the same reason there is uncertainty
                                regarding Israel's government approval. Israel withholding taxes will apply in case of
                                succesfull closing - to avoid tese foreign investors will be required to provide some
                                paperwork, which might delay the eventual payout of the merger consideration and might
                                explain part of the spread.
                                """,
        ),
        Arbitrage(
            target=Stock(ticker_name="VMW", period=period),
            buyer=Stock(ticker_name="AVGO", period=period),
            offer_price=71.25,
            additional_buyer_ratio=0.125,
            expecting_closing=datetime(2023, 10, 30, tzinfo=timezone.utc),
            commentary="""**Main risk** - long timeline/regulatory review. This is mammoth \\$61bn deal,
                                giving Broadcom a push into the software industry. A long and detailed probe from EU
                                regulators is expected. Broadcom's CEO has noted that regulatory filings have so far
                                seen good progress in numerous grographies. The merger could take more than a year to
                                complete.
                                """,
        ),
        Arbitrage(
            target=Stock(ticker_name="ACI", period=period),
            buyer=Stock(ticker_name="KR", period=period),
            offer_price=27.25,
            additional_buyer_ratio=0,
            expecting_closing=datetime(2024, 3, 30, tzinfo=timezone.utc),
            commentary="""**Main risk** - regulatory approval. US senators have raised anticompetitive concerns
                                to the FTC. To satisfy potential regulatory hurdles ACI and KR proposed divesting a
                                large number of stores. Also, as part of the merger agreement, ACI had to pay a
                                \\$6.85\\/share special dividend to its shareholders. However, several states filed a
                                lawsuit to block the payment arguing it would weaken the company's ability to compete
                                as the antitrust reviews proceed. Court's hearing has now been delayed till the 9th Dec.
                                Management remains confident that divestments will be enough to satisfy potential
                                regulatory concerns while also stating that a lawsuit related to divident payments is
                                groundless and should ger resolved in court.
                                """,
        ),
        Arbitrage(
            target=Stock(ticker_name="SIMO", period=period),
            buyer=Stock(ticker_name="MXL", period=period),
            offer_price=93.54,
            additional_buyer_ratio=0.388,
            expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
            commentary="""**Main risk** - Chinese regulatory approval. Approval from China's regulators is the main hurdle.
                                The buyer is based in the U.S, while the target is a US-listed Taiwanese company with China being
                                its largest market. Both parties had previously filed under the simplified procedures, but have
                                now re-filed under a normal procedure as advised by Chinese regulators. This month the documents
                                have been accepted and regulatory review is underway.
                                Management reiterated the expected closing date to be in mid-late 2023.""",
        ),
        Arbitrage(
            target=Stock(ticker_name="FORG", period=period),
            buyer="Thoma Bravo",
            offer_price=23.25,
            additional_buyer_ratio=0,
            expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
            commentary="""**Main risk** - antitrust approval. FORG is getting acquired by PE firm Thoma Bravo.
                                The main risk is regulatory approval due to increased market concentration. Just this
                                year Thomas Bravo has already acquired 2 players in the IAM space - one of which is a
                                direct peer to FORG. Recently, reports came out that Thomas Bravo plans to pull and
                                refile its merger docs with DOJ. Merger is expected to close in the first half of 2023.
                                """,
        ),
        Arbitrage(
            target=Stock(ticker_name="GSMG", period=period),
            buyer="Management",
            offer_price=1.55,
            additional_buyer_ratio=0,
            expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
            commentary=r"""**Main risk** - Privatization offer withdrawal.
                                    The spread hovered at less than 5% since shareholder approval in Sep'22 as
                                    the market expected prompt merger closing. More than half a year later, the
                                    merger is still pending, meanwhile, the management did not provide any
                                    explanation for 118% why it is taking so long. This scared investors and
                                    the spread gradually widened to above 100%. With the recent annual results release,
                                    the company did not provide any updates on the transaction, noting that the
                                    privatization is "yet to be consummated". The market clearly does not believe the
                                    merger will close as the stock currently trades below pre-announcement levels.
                                    Historically US-listed Chinese privatizations in definitive agreement stage have
                                    had a very high succesful closing rate, However such a prolonged lag indicates elevated
                                    merger break risk.
                                """,
        ),
        Arbitrage(
            target=Stock(ticker_name="INFI", period=period),
            buyer=Stock(ticker_name="MEIP", period=period),
            offer_price=0,
            additional_buyer_ratio=1.0449,
            expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
            commentary=r"""**Tiny all-stock biopharma merger.**
                                    Main risk - buyer's shareholder approval.
                                    Merger spread stood at minimal levels upon anouncement in Feb'23 and then gradually widened to 50% in March.
                                    This seems to have been driven by the risk of MEIP's shareholder opposition as the transaction terms appear
                                    to be quite 60% unfavorable for the buyer. This is also indicated by MEIP's share price fall of 20% upon
                                    the announcement. As part of the transaction, the buyer is required to keep \$80m in net cash vs \$4m for
                                    INFI while giving away a 42% ownership of the combined entity to INFl's equity holders.
                                    MEIP would add INFI's phase 2 drug candidate to its early-stage pipeline. In liquidation scenario MEIP
                                    could be worth materially above the current share price levels.""",
        ),
        Arbitrage(
            target=Stock(ticker_name="FHN", period=period),
            buyer=Stock(ticker_name="TD", period=period),
            offer_price=25,
            additional_buyer_ratio=0,
            expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
            commentary=r"""**Largest Canadian bank acquiring a regional US peer.**
                                    **Main risk** - downward price adjustment. The spread on this regional bank merger used to stand at minimal
                                    levels despite still pending regulatory approvals. The spread widen to 20% in March on the news that the
                                    parties will not be able to receive regulatory approvals by the merger 40% outside date of May'23.
                                    The spread increased further to over 40% amid the subsequent banking industry fall-out.
                                    Aside from the pending regulatory aprrovals, the current spread also reflects the risk of a downward price
                                    adjustment given that US bank indices are down significantly since the merger agreement was signed more
                                    than a year ago. The buyer's management has mentioned that negotiations regarding a merger consideration
                                    adjustment are ongoing. TD has remained committed to closing the transaction and the parties are in
                                    discussions to extend the outside date US-listed Chinese company privatization""",
        ),
        Arbitrage(
            target=Stock(ticker_name="ACI", period=period),
            buyer=Stock(ticker_name="KR", period=period),
            offer_price=27.25,
            additional_buyer_ratio=0,
            expecting_closing=datetime(2024, 3, 30, tzinfo=timezone.utc),
            commentary=r"""**Merger of two grocery store chains.**
                                    **Main risk** - regulatory approval. Merger of two grocery store chains coming after AC announced strategic
                                    alternatives in 2022. The transaction is synergistic from a geographical perspective - management states
                                    that AC operates in several parts of the country with very few or no Kroger stores. The main risk is
                                    antitrust approvals as the merger would combine the two of the biggest supermarket companies in the country.
                                    US senators as well as a couple of farmer/consumer groups have raised anticompetitive concerns to the FTC.
                                    The buyer KR has already received a second request from the FTC. However, both sides are confident of
                                    circumventing the regulatory hurdles with proposed divestitures of a large number of stores. The companies
                                    have recently started to look for potential buyers of stores in overlapping areas.""",
        ),
        Arbitrage(
            target=Stock(ticker_name="SGEN", period=period),
            buyer=Stock(ticker_name="PFE", period=period),
            offer_price=229,
            additional_buyer_ratio=0,
            expecting_closing=datetime(2024, 3, 30, tzinfo=timezone.utc),
            commentary=r"""**Prizer's large acquisition in the cancer treatment space.**
                                    **Main risk** - regulatory approval. The current spread seems to exist due to the likely scrutiny from
                                    antitrust regulators and potentially prolonged closing timeline. The transaction would give Pfizer a
                                    leading position in cancer treatment space where the company already owns a sizable portfolio of drugs.
                                    This might increase the combined company's power to negotiate with insurers. Industry analysts have
                                    noted that divestitures in some areas, such as bladder cancer treatment, might be needed. SGEN's shareholder
                                    approval seems likely, given a massive premium to pre-announcement levels. The merger is expected to close
                                    in late 2023-early 2024""",
        ),
        Arbitrage(
            target=Stock(ticker_name="TCRR", period=period),
            buyer=Stock(ticker_name="ADAP", period=period),
            offer_price=0,
            additional_buyer_ratio=1.5117,
            expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
            commentary=r"""**All-stock merger between two clinical-stage biopharmas**
                                    **Main risk** - small capitalization, steep downside, shareholder approvals
                                    The spread exists due to shareholder approval risks. ADAP's share price dropped 25% upon the announcement,
                                    indicating potential equity holder opposition to the deal. Any pushback, however, seems unlikely given that
                                    the transaction is primarily an equity raise for the buyer which is acquiring \$149m of the target's gross cash
                                    for \$64m worth of its stock. The merger would provide ADAP with additional liquidity required to pursue
                                    commercialization of its drug portfolio. TCRR is a cash-burning machine with no commercial-stage assets,
                                    suggesting its shareholders would face dilutive equity raises and/or a prolonged strategic review if the
                                    current deal breaks. TCRR insiders own a sizable 25% of the company. ADAP management owns 17%.""",
        ),
    ]
    return sorted(res, key=lambda x: x.expecting_closing)
