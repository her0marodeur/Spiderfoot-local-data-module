# Dataset and source catalogue

Reference list of the datasets and feeds that can extend, corroborate or automate this
database, with an honest note on what each one will and will not give you. Marked
**Free**, **Free (registration)**, **Mixed** or **Paid**.

The starting point for this catalogue was the source list in
[Admitting the Elephantine Void Between Kinetic and Cyber Threats](https://www.flyingpenguin.com/elephantine-void/),
whose central argument shaped the schema used here: record confidence **per variable**
rather than issuing one blended score for a record, because collapsing existence,
attribution and tasking into a single field overstates cases where only presence is
established and understates cases where tasking is evidenced but execution was
outsourced. That article specifically cites the Soufan Center and EuRepoC datasets as
examples of designs that avoid the problem. The `assessments` block in `schema.json` is
a direct implementation of that idea.

---

## Incident and conflict event datasets

### Global Terrorism Database (GTD) — START, University of Maryland
- <https://www.start.umd.edu/data-tools/GTD>
- **Free (registration)**, academic use terms.
- 200,000+ terrorist incidents with perpetrator, target type, weapon and casualty coding.
- **Useful for:** the ideological actors here — BRN, CCF, FAI, dissident republicans, ELN.
  The `targtype` field includes a dedicated business/financial target classification, so
  you can extract a historical base rate for attacks on banks by country.
- **Caveat:** update cadence has been irregular and coverage of recent years lags. Treat it
  as a historical baseline, not a current feed.

### ACLED — Armed Conflict Location & Event Data
- <https://acleddata.com/>
- **Mixed.** Free for academic, non-profit and limited use; commercial access is paid.
- Near-real-time coded political violence and protest events with actor names, locations
  and dates, updated weekly.
- **Useful for:** the highest-value single feed for this database. It covers riots, protests
  and armed group activity, which maps onto the protest/direct-action, insurgent and
  cartel-territorial actors here. ACLED also publishes dedicated analysis on Russia's
  shadow fleet and maritime hybrid threats.
- **Caveat:** actor naming is its own taxonomy and will not join cleanly to yours without a
  mapping table. Budget for that work.

### UCDP — Uppsala Conflict Data Program
- <https://ucdp.uu.se/downloads/>
- **Free**, open licence.
- Organised violence with a 25-battle-death threshold for conflict inclusion, plus the
  Georeferenced Event Dataset (GED) at individual event level.
- **Useful for:** structural context on the insurgent actors (BRN, ELN, FARC dissidents,
  Haiti). Its non-state conflict dataset covers cartel and gang violence.
- **Caveat:** the fatality threshold excludes most crime-driven violence. It will not see
  ATM attacks, extortion or robbery at all.

### GDELT Project
- <https://www.gdeltproject.org>
- **Free**, BigQuery access at Google Cloud cost.
- Machine-coded global news in near real time, with themes, tone, actors and locations.
- **Useful for:** early warning and volume trending, especially for local-language reporting
  on ATM attacks, CIT robberies and extortion that never reaches curated datasets. The
  GKG theme taxonomy has usable financial and terror themes.
- **Caveat:** it is machine-coded news, not verified events. Duplicate and false-positive
  rates are high, and coverage tracks media attention rather than incidence. Use it to
  find things to verify, never as a count.

### Deep South Watch (Thailand)
- <https://deepsouthwatch.org/>
- **Free.**
- Incident-level dataset for Thailand's southern insurgency, the source of the 23,000+
  incident and 7,700+ fatality figures cited in the BRN record.
- **Useful for:** the single best source for the only actor in this database that
  systematically bombs bank infrastructure for political reasons.

---

## Industry crime statistics

### EAST — European Association for Secure Transactions
- <https://www.association-secure-transactions.eu/>
- **Mixed.** Headline statistics published free in press releases; full reports are for
  members.
- Europe-wide ATM and payment terminal crime statistics: explosive attacks, gas attacks,
  card and cash trapping, logical attacks, data relay attacks, with losses in euros.
- **Useful for:** the quantitative backbone for every European ATM and terminal record in
  this database. The 2025 data-relay-attack surge (381 to 7,282 incidents) came from here.
- **Caveat:** reporting is voluntary by national members, so country coverage is uneven and
  absolute counts understate.

### National payment industry bodies
- UK Finance (<https://www.ukfinance.org.uk/>), **Free** summary reports.
- AusPayNet (<https://www.auspaynet.com.au/>), **Free** annual fraud data.
- FBI Bank Crime Statistics (<https://www.fbi.gov/investigate/violent-crime/bank-robbery>), **Free**.
- **Useful for:** national base rates for branch robbery, ATM crime and card fraud, and for
  showing the long-term decline in classic branch robbery that makes the newer patterns in
  this database relatively more important.

---

## Government designations and sanctions

All **Free**, all authoritative, all machine-readable in some form. These are the highest-quality
attribution source available and should be polled rather than read.

| Source | URL | Content |
| --- | --- | --- |
| OFAC SDN and consolidated lists | <https://sanctionslist.ofac.treas.gov/> | US designations; the source for Foxtrot, Kinahan, CJNG, TdA listings |
| US State Dept FTO list | <https://www.state.gov/foreign-terrorist-organizations/> | Los Choneros, Los Lobos, Viv Ansanm, Gran Grif, EGC, cartels |
| UN Security Council consolidated list | <https://main.un.org/securitycouncil/en/content/un-sc-consolidated-list> | UN designations including Haiti |
| EU consolidated sanctions list | <https://www.sanctionsmap.eu/> | EU designations |
| UK OFSI consolidated list | <https://www.gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets> | UK designations |
| OpenSanctions | <https://www.opensanctions.org/> | **Free** aggregation of the above with entity resolution; the practical way to consume all of them |
| Rewards for Justice / TOCRP | <https://rewardsforjustice.net/> | US reward offers, often the earliest public naming of a group |

**Useful for:** these are what turn a `moderate` attribution confidence into `high` in this
database. Every actor here with `attribution: high` has a designation, an indictment or a
conviction behind it.

---

## Law enforcement and multilateral reporting

| Source | URL | Access | Note |
| --- | --- | --- | --- |
| Europol (SOCTA, IOCTA, press) | <https://www.europol.europa.eu/> | Free | SOCTA is the best single European organised crime baseline |
| Eurojust | <https://www.eurojust.europa.eu/> | Free | Case-level detail on cross-border ATM, CIT and robbery operations |
| Interpol (Project Millennium, notices) | <https://www.interpol.int/> | Free | Thieves-in-law and Eurasian organised crime |
| UNODC | <https://www.unodc.org/> | Free | Source of the ~USD 40bn/year Southeast Asian scam industry estimate |
| FinCEN advisories and alerts | <https://www.fincen.gov/resources/advisories> | Free | Bulk cash smuggling, cartel typologies; directly actionable for AML teams |
| CISA advisories | <https://www.cisa.gov/news-events/cybersecurity-advisories> | Free | FASTCash and other hybrid cyber-physical bank attacks |
| AUSTRAC | <https://www.austrac.gov.au/> | Free | Australian typologies and enforcement |
| Bank Negara Malaysia | <https://www.bnm.gov.my/> | Free | Malaysian mule account and illegal moneylending enforcement |
| Bank of Thailand / AMLO | <https://www.bot.or.th/> | Free | Thai mule account and gold/FX control measures |

---

## Research and NGO analysis

| Source | URL | Access | Strength |
| --- | --- | --- | --- |
| InSight Crime | <https://insightcrime.org/> | Free | Best open-source coverage of Latin American organised crime; actor profiles are the reference standard |
| Global Initiative Against Transnational Organized Crime (GI-TOC) | <https://globalinitiative.net/> | Free | Risk bulletins, Haiti observatory, South Caucasus organised crime mapping |
| International Crisis Group | <https://www.crisisgroup.org/> | Free | Haiti, Colombia, Sahel conflict analysis |
| Small Wars Journal (Third Generation Gangs series) | <https://smallwarsjournal.com/> | Free | The definitive open analysis of novo cangaço and Brazilian gang tactics |
| RUSI | <https://www.rusi.org/> | Free | Dissident republican threat, financial crime policy |
| Carnegie Endowment | <https://carnegieendowment.org/> | Free | Baltic subsea cable sabotage and shadow fleet |
| ECFR | <https://ecfr.eu/> | Free | European undersea infrastructure vulnerability |
| OCCRP | <https://www.occrp.org/> | Free | Investigative work on Balkan, Kinahan and laundering networks |
| The Soufan Center | <https://thesoufancenter.org/> | Free | Cited in the Elephantine Void article as a model for per-variable confidence coding |
| EuRepoC | <https://eurepoc.eu/> | Free | European Repository of Cyber Incidents; the schema model this database borrows from |
| OSAC country security reports | <https://www.osac.gov/> | Free (registration) | Practical country-level crime and security baselines for corporate security teams |

---

## Commercial platforms

Included for completeness. None are required to use this database, and everything in it was
built from free sources.

| Source | URL | Note |
| --- | --- | --- |
| Janes Intelligence | <https://www.janes.com/> | **Paid.** Non-state armed group order of battle and equipment; strongest on insurgent groups, weaker on financial crime |
| Recorded Future Geopolitical Intelligence | <https://www.recordedfuture.com/products/geopolitical-intelligence> | **Paid.** Combined cyber and geopolitical feed; the closest commercial equivalent to a hybrid actor database |
| Flashpoint Ignite | <https://flashpoint.io/ignite/> | **Paid.** Strong on illicit communities, Com-adjacent networks and physical security intelligence |
| Dragos | <https://www.dragos.com/> | **Paid.** OT threat groups (VOLTZITE et al.); relevant only to the data centre and infrastructure records here |
| Crisis24 / Sibylline / Control Risks | various | **Paid.** Country risk and travel security; useful for executive protection planning |
| Kroll, Pinkerton | various | **Paid.** Kidnap-for-ransom incident data, relevant to the KFR-coded actors |

---

## What none of these give you

There is no single dataset covering the scope of this database, which is why it was built
by hand. Specifically:

- **No dataset codes ATM explosive attacks, CIT robberies or jugging as a category.** EAST
  gives European totals with no actor attribution. GTD codes only politically motivated
  attacks. ACLED codes only political violence and protest.
- **Activity clusters have no natural home.** Device theft, courier fraud, cash trapping and
  technician ambush are behaviours, not organisations, so actor-centric datasets omit them
  entirely. This is why `actor_class: activity_cluster` exists in the schema.
- **The insider dimension is almost never coded anywhere**, despite appearing in most
  high-value physical attacks.
- **Attribution quality varies enormously by region.** European and North American records
  here rest on prosecutions; Southeast Asian and Haitian records often rest on a single
  investigative outlet. The `assessments` block is where that difference is recorded rather
  than smoothed over.
