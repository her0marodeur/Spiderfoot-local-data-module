# Dataset and source catalogue

Datasets and feeds that can extend, corroborate or automate this database, with an honest
note on what each will and will not give you.

Access is marked **Open**, **Open (registration)**, **Mixed**, **Member** or **Paid**.
Entries marked † are from the source list in
[Admitting the Elephantine Void Between Kinetic and Cyber Threats](https://www.flyingpenguin.com/elephantine-void/),
which is also the origin of this database's central design decision.

## Why the schema looks the way it does

The Elephantine Void argument is that merging a hardware claim, an actor claim and a
tasking claim into one database field overstates cases where only presence is established
and understates cases where tasking is evidenced but execution was outsourced. It cites
the Soufan Center and EuRepoC as designs that avoid the problem by recording confidence
per variable.

The `assessments` block in [`schema.json`](../schema.json) implements that directly:
`existence`, `attribution`, `financial_targeting` and `state_tasking` are assessed
separately and never collapsed. Two records show why it matters. `GLB-STATE-OTPREPOS`
(Volt Typhoon / VOLTZITE) reads existence high, attribution high, financial targeting low,
state tasking high — presence and sponsorship are established, finance-sector selection is
not. `GLB-CLU-HWIMPLANT` reads existence moderate, attribution low, state tasking low,
because firmware tampering and rogue device addition are demonstrated while the most
publicised server-implant claim remains unverified and denied. A single blended score
would flatten both into something false.

---

## Conceptual and doctrinal

### Hybrid CoE † — European Centre of Excellence for Countering Hybrid Threats
- <https://www.hybridcoe.fi/> — **Open**
- Research publications and, with the EU Joint Research Centre, the conceptual model that
  is the closest thing to a shared hybrid-threat vocabulary.
- **Useful for:** the vocabulary problem this database runs into constantly — where
  "hybrid" stops meaning anything. If you extend the schema's category enum, align it here
  rather than inventing terms.

### NATO StratCom COE †
- <https://stratcomcoe.org/> — **Open**
- The influence and information dimension of hybrid operations.
- **Useful for:** context on why sabotage campaigns are conducted deniably. Marginal for
  the criminal actors, which are the bulk of this database.

---

## Incident and event datasets

### The Soufan Center, *Russian Hybrid Tactics in Europe 2022–2025* †
- <https://thesoufancenter.org/> — **Open**
- Incident-level dataset, 2022–2025, **attribution-confidence coded**.
- **Useful for:** the highest-value single corroboration source for `EU-STATE-GRU29155`,
  `EU-PROXY-RU-DISPOSABLE` and `EU-CLU-SHADOWFLEET`. Because it codes attribution
  confidence per incident it joins to this schema's `assessments` block almost directly,
  rather than needing a mapping judgement.

### EuRepoC — European Repository of Cyber Incidents †
- <https://eurepoc.eu/> — **Open**
- Cyber incidents from 2000, roughly sixty variables, with critical-infrastructure and
  attribution trackers.
- **Useful for:** the schema model this database borrowed. Also the reference set for the
  hybrid records — `GLB-STATE-DPRK-CASHOUT`, `GLB-STATE-OTPREPOS` — where an incident is
  cyber in execution and physical in effect.

### ACLED † — Armed Conflict Location & Event Data
- <https://acleddata.com/> — **Mixed** (free for academic/non-profit; commercial is paid)
- Weekly-updated coded political violence and protest events with actor names and locations.
- **Useful for:** the best operational feed here. Covers riots, protests and armed group
  activity, mapping onto the protest, insurgent and cartel-territorial records. ACLED also
  publishes dedicated analysis on Russia's shadow fleet as a maritime hybrid threat.
- **Caveat:** its actor taxonomy will not join to yours without a mapping table. Budget for it.

### GDELT †
- <https://www.gdeltproject.org> — **Open** (BigQuery at Google Cloud cost)
- Machine-coded global news in near real time.
- **Useful for:** early warning and trend detection, especially local-language reporting on
  ATM attacks, CIT robberies and extortion that never reaches curated datasets.
- **Caveat:** machine-coded news, not verified events. High duplicate and false-positive
  rates, and coverage tracks media attention rather than incidence. Use it to find things
  to verify, never as a count.

### Global Terrorism Database (START) †
- <https://www.start.umd.edu/data-tools/GTD> — **Open (registration)**
- 200,000+ attacks from 1970, 100+ coded variables including infrastructure target types.
  Coverage runs through 2020.
- **Useful for:** historical base rates. The target-type coding includes business and
  utilities categories, so you can extract a per-country baseline for attacks on financial
  premises. Relevant to `EU-GRP-CCF`, `EU-NET-FAI`, `APAC-GRP-BRN`, `EU-GRP-NEWIRA`,
  `AM-GRP-ELN`.
- **Caveat:** the 2020 cutoff means it says nothing about the current period. Baseline only.

### UCDP — Uppsala Conflict Data Program
- <https://ucdp.uu.se/downloads/> — **Open**
- Organised violence above a 25-battle-death threshold, plus event-level GED.
- **Useful for:** structural context on the insurgent records.
- **Caveat:** the fatality threshold excludes essentially all crime-driven violence. It will
  not see ATM attacks, extortion or robbery at all.

### Deep South Watch (Thailand)
- <https://deepsouthwatch.org/> — **Open**
- Incident dataset for Thailand's southern insurgency; source of the 23,000+ incident and
  7,700+ fatality figures in `APAC-GRP-BRN`.

---

## Grid and physical infrastructure

This block is the largest gap the supplied list closed. It supports the new
`AM-CLU-GRIDATTACK`, `GLB-NET-ACCELERATIONIST` and `GLB-STATE-OTPREPOS` records, and it is
unusual in this database for being **quantitative, public and joinable to your own site
list** — you can compute a bank's actual grid exposure rather than assert it.

### DOE OE-417 annual summaries †
- <https://www.oe.netl.doe.gov/OE417_annual_summary.aspx> — **Open**
- Mandatory US grid disturbance reporting including physical attacks, vandalism, sabotage
  and suspicious activity, archived to 2000.
- **Useful for:** the underlying numbers in `AM-CLU-GRIDATTACK` — 25 actual physical attacks
  in 2022 against six in 2021; roughly 200 vandalism/sabotage/suspicious reports in 2023,
  about 58 percent of all disturbances, against 9.3 percent in 2017.
- **Caveat:** the form does not code intent, which is exactly why that record carries
  `attribution: low`. A rifle attack and a copper theft can land in the same bucket.

### PNNL event-correlated outage dataset †
- <https://data.openei.org/> (OEDI) — **Open**
- OE-417 joined to EAGLE-I county-level outage data.
- **Useful for:** the join that turns a reported attack into an actual customer-impact
  duration. This is what lets you test whether your generator autonomy and cash-resupply
  assumptions survive a real event rather than a planning assumption.

### Michael Mabee's OE-417 consolidation †
- <https://michaelmabee.info/> — **Open**
- The DOE annual summaries cleaned into a single CSV.
- **Useful for:** skipping the tedium. DOE publishes per-year files with drifting schemas;
  this is the practical way to get a usable time series.

### NERC E-ISAC †
- <https://www.eisac.com/> — **Member**
- Grid physical-security reporting and sector alerts.
- **Useful for:** the operational layer OE-417 does not carry. Requires sector membership,
  so most financial institutions reach it via their utility rather than directly.

### ICPC — International Cable Protection Committee †
- <https://www.iscpc.org/> — **Open**
- Submarine cable protection, infrastructure and international-law reference.
- **Useful for:** `GLB-CLU-CABLELANDING` and `EU-CLU-SHADOWFLEET`. The key figure is that
  150+ cable faults occur annually with roughly 70 percent from fishing and anchoring —
  which is both reassuring and the reason a deliberate cut is easy to hide.

### TeleGeography Submarine Cable Map †
- <https://www.submarinecablemap.com/> — **Open**
- **Useful for:** the geography underneath every cable-cut attribution argument, and the
  practical way to discover that your carrier's "diverse" routes converge at one landing
  station.

### CRS, *Protection of Undersea Telecommunication Cables*
- <https://www.congress.gov/crs-product/R47648> — **Open**
- **Useful for:** the legal and jurisdictional constraints on responding to cable damage.

---

## Industry crime statistics

### EAST — European Association for Secure Transactions
- <https://www.association-secure-transactions.eu/> — **Mixed** (headline figures free)
- Europe-wide ATM and payment terminal crime: explosive and gas attacks, card and cash
  trapping, logical attacks, data relay attacks, with euro losses.
- **Useful for:** the quantitative backbone of every European ATM and terminal record here.
  The 2025 data-relay surge (381 → 7,282 incidents) came from EAST.
- **Caveat:** voluntary member reporting, so country coverage is uneven and counts understate.

### National bodies
- UK Finance <https://www.ukfinance.org.uk/> — **Open**
- AusPayNet <https://www.auspaynet.com.au/> — **Open**
- FBI Bank Crime Statistics <https://www.fbi.gov/investigate/violent-crime/bank-robbery> — **Open**

---

## Government designations and sanctions

All **Open**, all authoritative. These are what move a record's attribution confidence from
moderate to high — every `attribution: high` record here has a designation, indictment or
conviction behind it.

| Source | URL |
| --- | --- |
| OFAC SDN and consolidated lists | <https://sanctionslist.ofac.treas.gov/> |
| US State Dept FTO list | <https://www.state.gov/foreign-terrorist-organizations/> |
| UN Security Council consolidated list | <https://main.un.org/securitycouncil/en/content/un-sc-consolidated-list> |
| EU consolidated sanctions list | <https://www.sanctionsmap.eu/> |
| UK OFSI consolidated list | <https://www.gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets> |
| OpenSanctions (aggregation, entity-resolved) | <https://www.opensanctions.org/> |
| Rewards for Justice / TOCRP | <https://rewardsforjustice.net/> |

OpenSanctions is the practical consumption path — it aggregates the rest with entity
resolution, so you poll one source rather than seven.

---

## Law enforcement and multilateral

| Source | URL | Access | Note |
| --- | --- | --- | --- |
| Europol (SOCTA, IOCTA) | <https://www.europol.europa.eu/> | Open | Best European organised crime baseline |
| Eurojust | <https://www.eurojust.europa.eu/> | Open | Case-level cross-border ATM, CIT and robbery detail |
| Interpol (Project Millennium) | <https://www.interpol.int/> | Open | Thieves-in-law and Eurasian organised crime |
| UNODC | <https://www.unodc.org/> | Open | Source of the ~USD 40bn/year SE Asian scam estimate |
| FinCEN advisories | <https://www.fincen.gov/resources/advisories> | Open | Bulk cash smuggling, cartel typologies; directly actionable |
| CISA advisories | <https://www.cisa.gov/news-events/cybersecurity-advisories> | Open | FASTCash (AA20-239A), Volt Typhoon (AA24-038A) |
| MITRE ATT&CK | <https://attack.mitre.org/> | Open | T1200 Hardware Additions underpins `GLB-CLU-HWIMPLANT` |
| AUSTRAC | <https://www.austrac.gov.au/> | Open | Australian typologies |
| Bank Negara Malaysia | <https://www.bnm.gov.my/> | Open | Mule accounts, illegal moneylending |
| Bank of Thailand / AMLO | <https://www.bot.or.th/> | Open | Mule accounts, gold and FX controls |

---

## Research and NGO

| Source | URL | Strength |
| --- | --- | --- |
| InSight Crime | <https://insightcrime.org/> | Latin American organised crime; the reference standard |
| GI-TOC | <https://globalinitiative.net/> | Risk bulletins, Haiti observatory, South Caucasus mapping |
| International Crisis Group | <https://www.crisisgroup.org/> | Haiti, Colombia conflict analysis |
| Small Wars Journal (Third Generation Gangs) | <https://smallwarsjournal.com/> | Definitive open analysis of novo cangaço |
| CTC West Point | <https://ctc.westpoint.edu/> | Fifty years of infrastructure terrorism; underpins `GLB-NET-ACCELERATIONIST` |
| SPLC Hatewatch | <https://www.splcenter.org/hatewatch/> | Terrorgram and grid-attack prosecutions |
| RUSI | <https://www.rusi.org/> | Dissident republican threat, financial crime policy |
| Carnegie Endowment | <https://carnegieendowment.org/> | Baltic subsea cable sabotage |
| ECFR | <https://ecfr.eu/> | European undersea infrastructure vulnerability |
| OCCRP | <https://www.occrp.org/> | Balkan, Kinahan and laundering networks |
| OSAC country reports | <https://www.osac.gov/> | Practical country crime baselines (registration) |

---

## Commercial platforms

None are required. Everything in this database was built from open sources. Listed with a
frank note on what each would actually add.

| Source | Access | What it adds here |
| --- | --- | --- |
| Janes † <https://www.janes.com/> | Paid | Strongest structured coverage of the kinetic and military-hybrid side. Would materially improve `APAC-GRP-BRN`, `AM-GRP-ELN`, `APAC-GRP-KARENBGF`. Weak on financial crime |
| Recorded Future Geopolitical Intelligence † <https://www.recordedfuture.com/products/geopolitical-intelligence> | Paid | Real-time facility and physical-threat monitoring. The closest commercial equivalent to this database, and the one that would most reduce the `last_reviewed` staleness problem |
| Flashpoint Ignite † <https://flashpoint.io/ignite/> | Paid | Illicit communities and Com-adjacent networks. The single best commercial addition for `AM-NET-THECOM`, `EU-CLU-VIOLENCESERV` and `EU-CLU-CRYPTOWRENCH`, where open reporting lags badly |
| Dragos † <https://www.dragos.com/> | Paid | OT/ICS where cyber produces physical effect. Source of the VOLTZITE tracking in `GLB-STATE-OTPREPOS` |
| Nozomi Networks † <https://www.nozominetworks.com/> | Paid | OT/ICS visibility |
| Claroty † <https://claroty.com/> | Paid | OT/ICS visibility |
| Eclypsium † <https://eclypsium.com/> | Paid | Firmware and hardware integrity — the `GLB-CLU-HWIMPLANT` corner directly, and the only category here where a product genuinely substitutes for intelligence |
| Interos † <https://www.interos.ai/> | Paid | Supply-chain exposure mapping |
| Fortress Information Security † <https://www.fortressinfosec.com/> | Paid | Supply-chain exposure mapping, strong in energy sector vendor risk |
| Control Risks † <https://www.controlrisks.com/> | Paid | Geopolitical and physical risk with incident feeds |
| Crisis24 † <https://crisis24.garda.com/> | Paid | Geopolitical and physical risk with incident feeds |
| S-RM † <https://www.s-rminform.com/> | Paid | Geopolitical and physical risk; strong on KFR and investigations |
| Sibylline † <https://sibylline.co.uk/> | Paid | Geopolitical and physical risk with incident feeds |
| Kroll, Pinkerton | Paid | Kidnap-for-ransom incident data for the KFR-coded records |

Three of the four OT/supply-chain vendors (Nozomi, Claroty, Dragos) cover overlapping
ground; for a financial institution the question is usually whether you own OT at all, and
mostly you do not — your exposure is your utility's OT, which none of these products gives
you visibility into. Eclypsium and the supply-chain mappers are the more directly
applicable purchases because banks do own the hardware.

---

## What none of these give you

There is still no single dataset covering the scope of this database, which is why it was
built by hand.

- **No dataset codes ATM explosive attacks, CIT robbery or jugging as a category.** EAST
  gives European totals with no actor attribution. GTD codes only politically motivated
  attacks and stops at 2020. ACLED codes only political violence and protest. OE-417 codes
  only US grid events, without intent.
- **Activity clusters have no home anywhere.** Device theft, courier fraud, cash trapping,
  technician ambush and coerced insiders are behaviours, not organisations, so
  actor-centric datasets omit them. 58 of the 110 records here are in that category, and
  they generate a large share of the loss.
- **The insider dimension is coded almost nowhere**, despite appearing in nearly every
  successful high-value physical attack in this dataset.
- **Nothing joins physical and cyber cleanly.** EuRepoC is the closest, and it is
  cyber-first. The Soufan hybrid dataset is the closest to a genuine bridge, and it is
  Russia-and-Europe scoped.
- **Attribution quality varies enormously by region.** European and North American records
  rest on prosecutions; several Southeast Asian and Haitian records rest on a single
  investigative outlet. The `assessments` block records that difference rather than
  smoothing it away.
