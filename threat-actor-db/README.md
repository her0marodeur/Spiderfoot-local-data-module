# Physical and Hybrid Threat Actor Database — Financial Sector

A structured, sourced database of **physical and hybrid threat actors relevant to banks,
payment providers, cash logistics operators, exchanges and their customers**, covering
Europe, the Americas, Malaysia, Thailand and Australia.

**105 actor records · 76 countries · 219 sources · built entirely from free, open sources.**

| | |
| --- | --- |
| Machine-readable | [`dist/actors.json`](dist/actors.json) |
| Human-readable | [`ACTORS.md`](ACTORS.md) |
| Record format | [`schema.json`](schema.json) |
| Source datasets & feeds | [`sources/datasets.md`](sources/datasets.md) |
| Editable data | [`data/actors_*.json`](data/) |

```bash
python3 build.py           # validate, then regenerate dist/actors.json and ACTORS.md
python3 build.py --check   # validate only (CI-friendly, non-zero exit on failure)
```

No dependencies beyond Python 3.9+.

---

## What counts as an actor here

Deliberately broader than a conventional "threat group" list, because the request was for
actors that are relevant, not actors that are conveniently named.

**Named groups and networks** — the PCC, Mocro Maffia, Foxtrot, Pink Panthers, BRN,
Tren de Aragua, Comancheros, Viv Ansanm, GRU Unit 29155, and so on.

**Activity clusters** — recurring, coherent behaviour with no reliable group attribution.
Device theft to account takeover. Cash trapping. ATM technician ambush. Jugging. Crypto
wrench attacks. Tiger kidnapping. Coerced insiders. These are 58 of the 105 records, and
they are frequently the ones that actually generate loss. The schema has a dedicated
`activity_cluster` class specifically so that no one is tempted to invent a group name for
a behaviour.

**Movements** — climate and divestment direct action, anarchist collectives. Included
because they are the largest source of physical disruption at European bank premises by
volume, even though almost none of it is violent.

**State proxy programs** — where physical attack capability is tasked rather than owned.

| Class | Records |
| --- | ---: |
| Activity cluster | 58 |
| Network | 24 |
| Named group | 15 |
| Insurgent group | 4 |
| State proxy program | 2 |
| Movement | 2 |

| Primary region | Records |
| --- | ---: |
| Europe | 43 |
| Americas | 32 |
| Southeast Asia | 14 |
| Global / cross-cutting | 9 |
| Oceania | 7 |

Records are filed under a primary region but many carry several: 24 operate globally,
39 touch the Americas, 15 Southeast Asia, 9 Oceania.

---

## Confidence is recorded per variable, not per record

This is the single most important design decision, and it comes straight from
[Admitting the Elephantine Void Between Kinetic and Cyber Threats](https://www.flyingpenguin.com/elephantine-void/),
one of the sources supplied with the request. Its argument is that merging a hardware
claim, an actor claim and a tasking claim into one database field overstates cases where
only presence is established and understates cases where tasking is evidenced but execution
was outsourced. It points at the Soufan Center and EuRepoC as designs that avoid the
problem by recording confidence per variable.

So every record carries an `assessments` block:

```json
"assessments": {
  "existence":           { "confidence": "high",     "basis": "..." },
  "attribution":         { "confidence": "moderate", "basis": "..." },
  "financial_targeting": { "confidence": "low",      "basis": "..." },
  "state_tasking":       { "confidence": "low",      "basis": "..." }
}
```

This lets a record say what is actually true, which is usually something like *"these
attacks definitely happen, the executors are identified, the commissioner is not, and
nothing suggests the financial sector was specifically selected."* A single blended score
cannot express that, and papering over it is how threat intelligence ends up asserting more
than it knows.

Worked examples from the data:

- **Baltic subsea cable interference** — `existence: high` (eleven-plus documented incidents,
  vessels detained), `attribution: low` (vessels identified, intent contested and largely
  unproven in court), `financial_targeting: low` (shared infrastructure, no finance-specific
  selection), `state_tasking: low` (deniability intact by design).
- **Russia-tasked disposable saboteurs** — `existence: high`, `attribution: moderate`
  (executors identified, tasking chain judicially established in the Polish rail case and
  inferred elsewhere), `financial_targeting: low` (target selection follows accessibility,
  not sector).
- **Dutch ATM explosive crews** — `existence: high`, `attribution: moderate` (individual
  crews prosecuted, but the cluster is a behavioural grouping, not a command structure),
  `financial_targeting: high`.

Across the database only 30 of 105 records reach `attribution: high` — those with a
designation, indictment or conviction behind them. That ratio is the honest state of open
knowledge, not a gap to be filled with confident-sounding prose.

Confidence definitions: **high** = multiple independent official or judicial sources;
**moderate** = credible reporting with some corroboration; **low** = single-source,
contested, or inference.

---

## Record structure

Each record answers four questions a defender actually has.

**Who and where** — `name`, `aliases`, `actor_class`, `primary_motivation`, `status`,
`active_since`, `regions`, `countries`, `capability`.

**Why it matters to a financial institution** — `financial_sector_relevance` is a required
free-text field, and it is where a record has to justify its own inclusion. If the
connection is indirect, the field says so. `targets` codes the asset classes at risk
(ATM estate, CIT vehicle, bank staff, crypto holders, subsea cable, correspondent agents,
insiders, and so on) and `categories` codes the behaviour.

**How they operate** — `ttps` in plain language, plus `notable_incidents` with dates and
locations.

**What you can actually collect on** — `watch_indicators` are deliberately restricted to
observables a bank, acquirer or CIT operator can realistically see: alarm patterns, fault
clusters, transaction signatures, staff reports, contractor access anomalies. Not
"increased chatter".

Plus `linked_actors` for cross-references (validated at build time), `sources`, and
`last_reviewed`.

---

## Some findings that fell out of building it

**Insider involvement is the common factor in the severe cases.** Nearly every high-value
physical attack in this database that succeeded against a hardened target had one:
CIT ambushes, cash-centre raids, the Toronto Pearson bullion theft (executed with a
fraudulent airway bill and no weapons at all), jackpotting, novo cangaço raids. Two records
cover it directly — `EU-CLU-INSIDER` and `GLB-CLU-SECINDUSTRY` — and the second one matters
because the exposure usually sits inside a contractor's vetting process, not the bank's.

**The fastest-growing attacks convert street crime into account takeover.** London device
theft, NFC data relay (up 1,811 percent in a year on EAST's numbers), Malaysian snatch
theft. All of them defeat possession-based authentication for the same reason: the attacker
genuinely possesses the enrolled device and has observed the passcode.

**Violence is being brokered as a commodity.** The Nordic model — fixed-price attacks
advertised on encrypted channels, executed by recruited minors who never learn who
commissioned them — appears with local variations in the Melbourne tobacco war arson
campaign, in Russia's Telegram-recruited saboteurs, and in Sydney. It removes the
attribution and deterrence assumptions that executive protection planning was built on, and
it means a physical attack on a named employee now costs a few thousand euros.

**Wealth is increasingly attacked at the residence, not the institution.** Crypto wrench
attacks (France recorded at least 41 kidnappings and home invasions in a year and charged
88 people), South American Theft Groups working across 25 US states, Australian aggravated
home invasion crews now coercing crypto transfers. For private banking this is a client
security problem that no branch control touches.

**Controls decay when they are removed.** Chile's ATM attacks resurged after banks abandoned
dye staining as ineffective. Dutch crews exported to Germany and Switzerland only after
Dutch banks hardened. Tiger kidnapping collapsed because of duress protocols and dual
control, not because criminal intent disappeared — which is why that record is coded
`dormant` rather than `historical`.

---

## Known limits

Read these before relying on it.

- **Open sources only.** No classified, proprietary or paid-platform material. Where the
  commercial platforms suggested in the request (Janes, Recorded Future, Flashpoint) would
  add materially, [`sources/datasets.md`](sources/datasets.md) says so.
- **Attribution quality is regionally uneven.** European and North American records rest on
  prosecutions and designations. Several Southeast Asian and Haitian records rest on a
  single investigative outlet. The `assessments` block records that difference rather than
  smoothing it away.
- **Activity clusters are analytical constructs.** They are behavioural groupings drawn by
  the compiler, not entities recognised by any law enforcement agency. Two analysts would
  draw some of these boundaries differently. They are explicitly not a naming scheme.
- **Reference-grade sources are used where they are appropriate.** Some records cite
  encyclopaedic sources for uncontested factual background alongside primary sources for
  the claims that matter. Where a record leans on a lighter source, its `attribution`
  confidence reflects that.
- **This is a snapshot.** Every record carries `last_reviewed: 2026-07-24`. Sanctions
  listings, threat levels and group structures move fast; the designation records in
  particular should be re-polled against OFAC, State, UN and OFSI rather than trusted here.
- **Estimated figures are attributed, not endorsed.** Where a record cites a number
  (USD 120 million from novo cangaço raids, USD 40 billion in annual scam revenue), it is
  reported as the cited source gives it. Several are contested estimates.
- **Coverage is not proportional to risk.** Europe has the most records partly because
  European reporting is the most granular, not because European institutions face the most
  danger. Haiti has two records and arguably the most constrained banking environment in the
  hemisphere.

---

## Extending it

Add a record to the appropriate `data/actors_*.json`, then run `python3 build.py`. The
validator checks required fields, enum membership, ISO country codes, ID format and
uniqueness, per-variable assessment completeness, source URLs, and that every
`linked_actors` reference resolves. It fails the build on any of them.

Conventions worth keeping:

- IDs are `REGION-CLASS-SLUG` and are permanent. Never reuse one for a different actor.
- If you cannot name the actor, use `activity_cluster`. Do not invent a group name.
- `financial_sector_relevance` must be specific. If an actor is only tangentially relevant,
  the field should say so plainly — that is more useful than an inflated claim.
- `watch_indicators` must be things somebody can actually collect.
- Every claim of a designation, conviction or specific incident needs a source in `sources`.
