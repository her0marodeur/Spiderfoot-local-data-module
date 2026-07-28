# New Additions — Insurance-Sector and Foreign Intelligence Service Actors

13 records added to the database, taking it from 110 to 123. Six cover physical threats specific to insurers; seven cover components of foreign intelligence services and one state-proxy-adjacent network. Full records with TTPs, watch indicators and per-variable confidence are in [`ACTORS.md`](ACTORS.md).

---

## Insurance-sector physical threats (6)

### Grievance-driven targeted violence against insurance executives and claims staff

`AM-CLU-INSUREXEC` · activity cluster · ideological · active, capability low · since 2024

*US, CA*

**Aka:** healthcare executive targeting, claims-denial grievance violence, Thompson copycat threat

Lone actors motivated by grievance over claim denial, coverage rescission or medical debt who threaten or attack named insurance executives and claims personnel. The killing of UnitedHealthcare chief executive Brian Thompson outside a Manhattan investor conference on 4 December 2024 converted a diffuse, long-running background of threats into a named and celebrated template. Security consultants reported that violent threats against health executives were already rising before that attack; afterwards the volume and the public approval of it both changed character. Insurers pulled executive biographies from their websites, cancelled in-person shareholder events and moved staff to remote working within a week.

**Why it matters.** This is the defining physical security development for the insurance industry and it has no real analogue in banking. Attackers are customers, not criminals, they are motivated by the product itself rather than by money, and they select named individuals from public disclosure. Demand for executive protection assessments rose ten to fifteen times at one major provider, and median disclosed S&P 500 security expense rose from USD 69,180 to USD 94,276 in a single year. The controls that matter are disclosure hygiene, investor-event security and the handling of grievance correspondence in claims workflows, not building hardening.

**On the record**

- *2024-12-04, Manhattan, US* — UnitedHealthcare chief executive Brian Thompson shot dead outside a hotel hosting the company's investor conference. He was travelling without security despite previous threats.
- *2024-12, US* — Health insurers removed executive information from websites, cancelled in-person shareholder meetings and advised staff to work from home amid a surge of threats.
- *2025-03, US* — Johnson & Johnson and Eli Lilly disclosed increased executive security spending citing threats after the killing; at least a dozen S&P 500 companies flagged raised security risk.

**Confidence:** E high · A moderate · F high.

> Attribution basis: The precedent attack is attributed to a charged individual; the wider threat stream is diffuse lone-actor activity.

**Sources**

1. [Before UnitedHealthcare CEO Shooting, Violent Threats Against Health Execs Were Rising, Says Security Consultant](https://www.forbes.com/sites/thomasbrewster/2024/12/05/before-unitedhealthcare-ceo-shooting-violent-threats-against-health-execs-were-rising-says-security-consultant/) — news
1. [How Executive Protection is Changing One Year After UnitedHealthcare CEO Attack](https://www.asisonline.org/security-management-magazine/latest-news/today-in-security/2025/december/Executive-Protection-One-Year-After-UnitedHealthcare/) — industry
1. [Lilly, J&J boosted spending on executive security after UnitedHealth shooting](https://kfgo.com/2025/03/12/lilly-jj-boosted-spending-on-executive-security-after-unitedhealth-shooting/) — news
1. [Companies tighten security after a health care CEO's killing leads to a surge of threats](https://insurancenewsnet.com/oarticle/companies-tighten-security-after-a-health-care-ceos-killing-leads-to-a-surge-of-threats-2) — industry

---

### Climate direct action targeting insurers and reinsurers

`EU-MOV-INSURECLIMATE` · movement · ideological · active, capability low · since 2021

*GB, CH, FR, DE, US, JP, AU*

**Aka:** Insure Our Future, Extinction Rebellion insurance campaign, Lloyd's blockades

A coordinated international campaign targeting insurers and brokers for underwriting fossil fuel projects, run under the Insure Our Future banner with Extinction Rebellion and allied groups executing the physical actions. It has run across 27 countries including London, New York, Tokyo and Zurich. Tactics escalated from symbolic protest to physical denial of access: in February 2024 roughly 800 activists formed a 300-metre human chain around the Lloyd's building on Lime Street, permitting staff to leave but not to enter. In January 2025 the campaign shifted from buildings to individuals, occupying Marsh McLennan's offices and targeting the CEOs and offices of Lloyd's, Howden, Willis Towers Watson, AXA and Hiscox.

**Why it matters.** The insurance analogue of the bank-branch campaigns already in this database, but with a materially different geometry. Insurance has no branch network, so the pressure concentrates on a small number of head offices and market buildings, which makes a single blockade capable of denying access to a large share of a market. The January 2025 pivot to naming CEOs personally, framed around their potential criminal liability, is the development to watch: it moves the exposure from premises security to executive protection and overlaps with the grievance-violence cluster even though this movement is non-violent.

**On the record**

- *2022-04-12, London, GB* — Extinction Rebellion blockaded the Lloyd's of London headquarters under the Insure Climate Justice banner.
- *2024-02-28, London, GB* — Around 800 activists formed a 300-metre human chain around the Lloyd's building, allowing staff to leave but refusing entry.
- *2025-01-30, London, GB* — Protesters occupied Marsh McLennan's offices and targeted the CEOs and offices of Lloyd's, Howden, Willis Towers Watson, AXA and Hiscox, escalating to a strategy focused on personal criminal liability of executives.

**Confidence:** E high · A high · F high.

> Attribution basis: Actions publicly claimed by named organisations.

**Sources**

1. [City of London insurance CEOs targeted for climate crimes in a second day of action](https://extinctionrebellion.uk/2025/01/30/city-of-london-insurance-ceos-targeted-for-climate-crimes-in-a-second-day-of-action/) — ngo
1. [Insure Climate Justice: Extinction Rebellion Blockade Iconic Lloyd's of London HQ](https://extinctionrebellion.uk/2022/04/12/insure-climate-justice-extinction-rebellion-blockade-iconic-lloyds-of-london-hq/) — ngo
1. [Hundreds of climate protesters blockade Lloyd's of London](https://www.nationalworld.com/news/environment/extinction-rebellion-hundreds-of-climate-protesters-blockade-lloyds-of-london-4536547) — news
1. [Over 500 students refuse to work for climate-wrecking Lloyd's of London and others](https://global.insure-our-future.com/over-500-students-refuse-to-work-for-climate-wrecking-lloyds-of-london-and-others/) — ngo

---

### Staged collision and induced-accident networks

`GLB-CLU-STAGEDCOLLISION` · activity cluster · profit · active, capability moderate · since 1995

*GB, IE, PL, DE, ES, IT, US, CA, AU, MY, TH*

**Aka:** crash for cash, cash for crash, induced accident gangs, slam-on crews

Organised networks that deliberately cause road collisions in order to generate fraudulent injury and damage claims. The core methods are the induced accident, where the fraudster brakes suddenly in front of an innocent driver, the staged accident between colluding participants, and the ghost or phantom accident that never occurred. The UK figure is roughly GBP 1.5 billion a year on Association of British Insurers and Insurance Fraud Bureau data. A distinct and growing moped variant targeted over 4,000 people between June 2021 and July 2024, generating an estimated GBP 70 million in claims. Networks typically integrate recruiters, drivers, complicit medical and repair providers and claims management firms.

**Why it matters.** This is the only large-scale insurance fraud typology that deliberately manufactures physical violence against uninvolved members of the public, and it belongs in a physical threat database for that reason rather than as a fraud line item. Innocent drivers are injured and occasionally killed. For insurers it also produces a second-order physical problem: investigators and special investigation unit staff working these cases are dealing with organised crime networks, and intimidation of witnesses and claims handlers is a recurring feature.

**On the record**

- *2025-04-04, Leeds, GB* — Two-year suspended sentence for a GBP 60,000 crash-for-cash claim based on a fabricated collision purportedly in California.
- *2024-12, GB* — Man jailed over a GBP 100,000 crash-for-cash plot following a City of London Police investigation.
- *2021-2024, GB* — Over 4,000 people targeted in moped-based crash-for-cash offences, with an estimated GBP 70 million in fraudulent claims.

**Confidence:** E high · A low · F high.

> Attribution basis: Individual networks prosecuted; the pattern is highly fragmented with constant reconstitution.

**Sources**

1. ['Crash for cash' fraud - City of London Police](https://www.cityoflondon.police.uk/police-forces/city-of-london-police/areas/campaigns/crash-for-cash-fraud/) — law enforcement
1. [Man sentenced for GBP 60,000 'crash for cash' claim involving fake collision in California](https://www.cityoflondon.police.uk/news/city-of-london/news/2025/april/man-sentenced-for-60000-crash-for-cash-claim-involving-fake-collision-in-california/) — law enforcement
1. [Man jailed for GBP 100,000 'crash for cash' plot](https://www.cityoflondon.police.uk/news/city-of-london/news/2024/december/man-jailed-for-100000-crash-for-cash-plot/) — law enforcement
1. [Car insurance: 170,000 claims linked to 'crash for cash' gangs](https://feeds.bbci.co.uk/news/business-57058755) — news

---

### Arson-for-profit and serial insurance fire rings

`GLB-CLU-ARSONFORPROFIT` · activity cluster · profit · active, capability low · since 1970

*US, CA, GB, IT, ES, AU, MY*

**Aka:** binge burners, fraud fires, torch rings

Rings that repeatedly set fire to insured residential and commercial property to collect payouts, often over many years and many properties before detection. Prosecutions consistently reveal serial rather than one-off behaviour: a Southern District of Illinois ring ran from 2014 to 2023 before its leader received 15 years, and an Ohio scheme involved at least six fires and more than USD 2.3 million in claims between 2013 and 2019. Property is frequently acquired cheaply, over-insured, and then burned, sometimes with paid third-party torches.

**Why it matters.** Arson is the insurance fraud typology that most reliably kills people. Fires set in terraced, multi-occupancy or commercially adjoined property endanger occupants, neighbours and responding firefighters, and the fraudster has no control over the outcome once the fire is set. For insurers the exposure is both the claim and the liability, and the detection signal is almost always the pattern across the book rather than anything visible on a single claim. Underwriting is the effective control point, since over-insurance relative to purchase price is the recurring precursor.

**On the record**

- *2025, Southern District of Illinois, US* — Ring leader sentenced to 15 years in federal prison for a string of arsons and insurance fraud running from 2014 to 2023.
- *2026, Northern District of Ohio, US* — Couple sentenced over a scheme involving at least six fires and more than USD 2.3 million in fraudulent claims between 2013 and 2019.

**Confidence:** E high · A moderate · F high.

> Attribution basis: Named defendants convicted in specific rings; the wider pattern is dispersed.

**Sources**

1. [Leader of insurance fraud and arson scheme sentenced to 15 years](https://www.justice.gov/usao-sdil/pr/leader-insurance-fraud-and-arson-scheme-sentenced-15-years) — government
1. [Ohio Couple Sentenced for Arson in Profit Scheme to Fraudulently Collect Millions in Insurance Payouts](https://www.justice.gov/usao-ndoh/pr/ohio-couple-sentenced-prison-arson-profit-scheme-fraudulently-collect-millions) — government
1. [The Red Flags of Arson](https://ethosrisk.com/blog/insurance-fraud-red-flags-arson/) — industry

---

### Vessel scuttling and marine insurance fraud syndicates

`GLB-CLU-MARINEFRAUD` · activity cluster · profit · active, capability moderate · since 1970

*GR, TR, AE, SG, MY, TH, PA, LR, CY*

**Aka:** scuttling, rust bucket fraud, phantom cargo fraud

Deliberate sinking or wrecking of over-insured vessels, frequently combined with claims for high-value cargo that never existed. The economics are counter-cyclical: scuttling clusters during downturns in the shipping market, when an ageing vessel is worth more insured than trading. Recent cases carry a combined potential claims value approaching USD 100 million, and in the Atlantik Confidence matter insurers paid USD 22 million on a claim later found to be a deliberate act and could not recover it. Proof is exceptionally hard because the evidence sinks with the ship.

**Why it matters.** The insurance loss category where the fraudulent act is itself a large-scale physical event with crew lives at risk, and where the insurer must prove deliberate action to a high evidential standard against a defendant who has destroyed the evidence. It is directly relevant to marine hull, cargo and P&I underwriting, and to the trade finance banks lending against the same cargo, since phantom cargo fraud frequently defrauds both simultaneously.

**On the record**

- *2013, Indian Ocean* — Atlantik Confidence sank; insurers paid USD 22 million on a claim subsequently found to be a deliberate act, without recovery.

**Confidence:** E high · A low · F high.

> Attribution basis: Ownership is deliberately obscured; deliberate loss is proven in only a small minority of suspected cases.

**Sources**

1. [Marine Fraud - Scuttling by ship owners](https://keoghs.co.uk/keoghs-insight/marine-fraud-scuttling-by-ship-owners) — industry
1. [The Impact of Maritime Fraud on Developed Countries](https://ethosrisk.com/blog/the-impact-of-maritime-fraud-schemes-on-developed-countries/) — industry
1. [Shipping and scuttling: Criminogenesis in marine insurance](https://link.springer.com/article/10.1023/A:1008292912365) — research

---

### Violence and intimidation against claims field staff

`GLB-CLU-ADJUSTER` · activity cluster · opportunistic · active, capability low · since 1990

*US, CA, GB, AU, BR, MX, ZA*

**Aka:** adjuster assaults, loss adjuster targeting, CAT deployment risk

Assault, threat, stalking and hostage-taking directed at loss adjusters, claims investigators and catastrophe field staff, who work alone, unannounced, at private addresses, delivering unwelcome decisions to people in acute distress. Industry writing identifies physical assault, road rage, hostage-taking, stalking, verbal abuse, threatening correspondence and identity theft as established occupational risks, while also noting that they are systematically under-reported by both media and professional bodies. Catastrophe deployments compound the exposure by placing staff in areas with degraded policing, displaced populations and active looting.

**Why it matters.** The most common physical risk actually borne by insurance sector employees, and the least well documented anywhere. It is the insurance equivalent of branch staff safety, but the exposure sits in vehicles and on strangers' property rather than in a controlled building, so almost none of the standard corporate security toolkit applies. The honest position is that the evidence base is industry commentary rather than incident data, which is itself the finding: no one is counting.

**Confidence:** E moderate · A low · F high.

> Attribution basis: Individual claimants and third parties; no organised actor except where fraud networks are involved.

**Sources**

1. [Safety First - CLM Magazine](https://www.theclm.org/Magazine/articles/safety-first/108) — industry
1. [Challenges Facing Independent Catastrophe Adjusters](https://www.propertyinsurancecoveragelaw.com/blog/challenges-facing-independent-catastrophe-adjusters/) — industry
1. [Guide for Adjusting Property Claims in California After a Major Disaster](https://www.insurance.ca.gov/0200-industry/0050-renew-license/0200-requirements/upload/2025GuideAdjstPropClaimsinCA-After-a-Major-Disaster.pdf) — government

---

## Foreign intelligence service components and state proxies (7)

### GRU Unit 26165 close-access operations teams

`GLB-STATE-GRU26165` · state proxy program · state directed · active, capability advanced · since 2014

*RU, NL, CH, GB, DE, NO, BR, MY*

**Aka:** 85th Main Special Service Centre, GTsSS, APT28 close access, Fancy Bear on-site teams

The GRU's signals and cyber unit, better known for remote intrusion, also fields travelling teams that conduct on-site technical operations against targets whose networks cannot be reached remotely. The Hague operation of April 2018 is the definitive public example: four officers, two cyber operators and two HUMINT support, hired a car, parked it beside the OPCW headquarters with a concealed antenna, amplifiers and Wi-Fi interception equipment running from a battery in the boot, and had scouted and photographed the building for days before Dutch AIVD intercepted them. Close-access teams have been documented operating against hotels hosting targeted conferences and against organisations in several countries.

**Why it matters.** This is the intelligence-service activity most likely to occur physically at a financial institution's own premises, and the one its security model is least designed to see. The attack surface is the corporate Wi-Fi as observed from the pavement, the car park, the adjacent building or the conference hotel, not the perimeter door. It is directly relevant to institutions hosting international negotiations, sanctions-related work, or executive travel to conferences, and the countermeasures are wireless monitoring and travel tradecraft rather than guarding.

**On the record**

- *2018-04, The Hague, NL* — Four GRU officers intercepted beside OPCW headquarters with a car boot containing a panel antenna, interception devices, amplifiers and laptops, after several days of reconnaissance. Expelled to Moscow; later indicted in the US.

**Confidence:** E high · A high · F low · S high.

> Attribution basis: Four officers named and publicly identified; formal state attribution by the Netherlands, UK and US.

> State tasking basis: Unit is an organic element of Russian military intelligence.

**Sources**

1. [GRU 26165: The Russian cyber unit that hacks targets on-site](https://www.atlanticcouncil.org/content-series/tech-at-the-leading-edge/the-russian-cyber-unit-that-hacks-targets-on-site/) — research
1. [The GRU close access operation against the OPCW in perspective](https://www.electrospaces.net/2018/10/the-gru-close-access-operation-against.html) — research
1. [Minister for Europe statement: attempted hacking of the OPCW by Russian military intelligence](https://www.gov.uk/government/speeches/minister-for-europe-statement-attempted-hacking-of-the-opcw-by-russian-military-intelligence) — government
1. [How the Dutch foiled Russian 'cyber-attack' on OPCW](https://feeds.bbci.co.uk/news/world-europe-45747472) — news

---

### SVR Directorate S illegals programme

`GLB-STATE-SVRS` · state proxy program · state directed · active, capability advanced · since 1920

*RU, US, GB, BR, SI, NO, NL, GR, IT*

**Aka:** Directorate S, Line N, Russian illegals, non-official cover officers

The SVR directorate responsible for deep-cover officers who live for years or decades under fabricated foreign identities with no diplomatic protection, building genuine businesses, careers and social networks. Operation Ghost Stories produced ten arrests in the United States in June 2010; a further sequence of European arrests since 2022 has involved officers operating under Latin American cover identities and running real businesses as their cover. The programme's value to Moscow has risen as diplomatic expulsions have stripped out officers working under embassy cover.

**Why it matters.** Illegals need what any long-term resident needs, and more of it: bank accounts, corporate structures, credit history and professional employment, all obtained under a fabricated identity that will survive years of scrutiny. That makes financial institutions both a documentation target and, occasionally, an employment target. The realistic exposure is not a spy in the dealing room; it is that an institution's onboarding and identity assurance is what an illegal must defeat to exist at all, and that a cover business will pass every commercial test because it is a real business.

**On the record**

- *2010-06-27, US* — Ten SVR illegals arrested following the multi-year FBI counter-intelligence Operation Ghost Stories; all pleaded guilty to acting as unregistered agents of the Russian Federation.

**Confidence:** E high · A moderate · F low · S high.

> Attribution basis: Individual officers identified after arrest; the programme's current scale is by design unknown.

> State tasking basis: Directorate S is an organic element of the SVR.

**Sources**

1. [Illegals Program](https://en.wikipedia.org/wiki/Illegals_Program) — reference
1. [Foreign Intelligence Service (SVR) profile](https://plausibledenial.org/russia/svr) — research

---

### FSB Centre 16 and TsNIIKhM industrial control system programmes

`GLB-STATE-RUICS` · state proxy program · state directed · active, capability advanced · since 2012

*RU, US, GB, DE, NO, SA, TR*

**Aka:** Berserk Bear, Dragonfly, Energetic Bear, Crouching Yeti, TRITON, Xenotime

Two Russian government programmes charged together by the US Department of Justice in March 2022. FSB Centre 16 conducted long-running intrusion campaigns against global energy sector targets including nuclear generation, using supply-chain compromise of ICS vendor software and watering-hole attacks. The Central Scientific Research Institute of Chemistry and Mechanics (TsNIIKhM) was charged over the TRITON attack on a petrochemical facility's Triconex safety instrumented system, which is the clearest documented case anywhere of a state programme reaching into the safety layer designed to prevent explosions and loss of life.

**Why it matters.** TRITON is the reference case for cyber operations that produce physical harm, and it matters here for the same reason as the grid records: financial services depend on energy and industrial infrastructure it neither owns nor can inspect. The specific lesson is about safety systems. TRITON did not target production, it targeted the system that stops production killing people, which is the analytical equivalent of attacking a bank's controls rather than its money. Exposure is entirely indirect and should be treated as a continuity and concentration problem.

**On the record**

- *2017, Middle East* — TRITON malware deployed against a petrochemical plant's Triconex safety instrumented system, the safety layer intended to prevent catastrophic release.
- *2022-03, US* — Four Russian government employees charged over two historical hacking campaigns targeting critical infrastructure worldwide, including energy sector intrusions and the TRITON attack.

**Confidence:** E high · A high · F low · S high.

> Attribution basis: Named individuals charged and attributed to FSB Centre 16 and TsNIIKhM by the US government.

> State tasking basis: Defendants charged as employees of Russian government entities.

**Sources**

1. [Four Russian Government Employees Charged in Two Historical Hacking Campaigns Targeting Critical Infrastructure Worldwide](https://www.justice.gov/opa/pr/four-russian-government-employees-charged-two-historical-hacking-campaigns-targeting-critical) — government
1. [CISA Cybersecurity Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories) — government

---

### IRGC Quds Force Unit 840 and Iranian external operations networks

`GLB-STATE-IRGC840` · state proxy program · state directed · active, capability high · since 2010

*IR, DE, SE, GB, FR, NL, US, TR, AZ*

**Aka:** Unit 840, Quds Force Department 840, German Network, Iranian assassination cells

The Quds Force division responsible for assassination, kidnapping and attack planning against Westerners, Israelis and Iranian dissidents abroad. Its operational signature is outsourcing: rather than deploying Iranian officers, it contracts European organised crime networks to conduct surveillance, arson and killings, which provides deniability and access. UK security ministers have stated publicly that Tehran enlisted British organised crime groups to surveil Jewish communities. Iranian tasking of the Foxtrot Network, already in this database, is the clearest documented convergence of a state service and a criminal network in Europe.

**Why it matters.** This is the mechanism by which a state service can reach a named individual in a European city without ever sending an officer, and it is the reason the Nordic violence-as-a-service market is a national security problem rather than only a crime problem. For financial institutions the exposure is twofold: the criminal networks being contracted are in some cases existing customers or customer-adjacent, creating a sanctions and conduct problem; and Iranian-linked targeting of Jewish and Israeli-linked commercial premises places some branches and offices within a target set they did not choose.

**On the record**

- *2024-01, Stockholm, SE* — Attack on the Israeli embassy attributed by the US Treasury to the Foxtrot Network acting on behalf of the Iranian government.
- *2023, GB* — UK security minister stated publicly that Iran had enlisted British organised crime groups to surveil Jewish communities, assessed as a possible precursor to targeted attacks.
- *2025-01, DE* — Plot to assassinate an Iranian dissident artist in Germany exposed.

**Confidence:** E high · A moderate · F low · S moderate.

> Attribution basis: State linkage established in some cases including the US Treasury attribution of the Stockholm embassy attack; contested or unproven in others by design.

> State tasking basis: Established in leading cases; deniability through criminal intermediaries is the programme's central feature.

**Sources**

1. [Iran's ties to Western organized crime networks](https://www.longwarjournal.org/archives/2025/03/irans-ties-to-western-organized-crime-networks.php) — research
1. [Unit 840](https://en.wikipedia.org/wiki/Unit_840) — reference
1. [Unit 840: IRGC Assassination and Kidnap Arm](https://greydynamics.com/unit-840-irgc-assassination-and-kidnap-arm/) — research
1. [Iran's plot to assassinate dissident artist in Germany exposed](https://www.iranintl.com/en/202501045297) — news

---

### MSS transnational repression and Operation Fox Hunt networks

`GLB-STATE-MSSFOXHUNT` · state proxy program · state directed · active, capability high · since 2014

*CN, US, CA, GB, NL, ES, IT, AU, MY, TH*

**Aka:** Operation Fox Hunt, Operation Sky Net, overseas police service stations, MSS repatriation campaigns

Chinese state campaigns to locate, harass and coerce the return of nationals abroad, nominally an anti-corruption effort and in practice a mechanism for pressuring dissidents, business figures and those holding assets outside China. Operations are conducted through co-opted local proxies including private investigators, community figures and hired surveillance, which is what makes them prosecutable in host countries. Safeguard Defenders identified over 100 covert Chinese police service stations in more than 50 countries. A sequence of US prosecutions concluded in 2025 with custodial sentences for a campaign leader, a former police officer and several stalking participants.

**Why it matters.** Directly relevant to private banking and wealth management, because the targets are frequently people who moved substantial assets out of China and the campaign's object is to compel their return along with those assets. Institutions encounter it as surveillance and harassment of named clients, as pressure applied to clients' relatives, as unexplained instructions to repatriate funds under apparent duress, and as approaches to bank staff for client location information. It also intersects with sanctions and conduct risk when local intermediaries are institution customers.

**On the record**

- *2025, US* — Quanzhong An sentenced to 20 months for acting as an illegal agent of the PRC in a multi-year Fox Hunt repatriation campaign; former police officer Michael McMahon sentenced to 18 months for his participation.
- *2025-01, US* — Zhu Yong sentenced to two years and Zheng Congying to 16 months over an intimidation campaign including stalking a former Chinese official in New Jersey.
- *2022, Global* — Safeguard Defenders identified over 100 covert Chinese police service stations across more than 50 countries.

**Confidence:** E high · A high · F moderate · S high.

> Attribution basis: US courts convicted defendants of acting as illegal agents of the PRC government.

> State tasking basis: Judicially established direction by PRC government entities.

**Sources**

1. [Transnational Repression - FBI](https://www.fbi.gov/investigate/counterintelligence/transnational-repression) — government
1. [Leader of multiyear Operation Fox Hunt repatriation campaign directed by the PRC sentenced to 20 months in prison](https://www.irs.gov/compliance/criminal-investigation/leader-of-multiyear-operation-fox-hunt-repatriation-campaign-directed-by-the-peoples-republic-of-china-sentenced-to-20-months-in-prison) — government
1. [Operation Fox Hunt: How China Exports Repression Using a Network of Spies Hidden in Plain Sight](https://www.propublica.org/article/operation-fox-hunt-how-china-exports-repression-using-a-network-of-spies-hidden-in-plain-sight) — research
1. [Private investigator sentenced to prison for interstate stalking and harassment of Chinese nationals](https://www.justice.gov/opa/pr/private-investigator-sentenced-prison-interstate-stalking-and-harassment-chinese-nationals) — government

---

### DPRK fraudulent remote IT worker placement programme

`GLB-STATE-DPRKIT` · state proxy program · state directed · active, capability advanced · since 2018

*KP, CN, RU, US, GB, MY, TH, AE*

**Aka:** Jasper Sleet, Wagemole, UNC5267, North Korean IT workers, laptop farms

A North Korean state revenue programme that places thousands of IT workers into remote employment at foreign companies using stolen and fabricated identities, generating salaries that fund weapons programmes and, increasingly, providing insider access for extortion. The physical component is the facilitator network: US-based individuals who host company-issued laptops in their homes, so-called laptop farms, allowing the worker to appear to be connecting locally. US authorities searched 29 suspected laptop farms across 16 states and seized 29 financial accounts. Over 300 US companies including several Fortune 500 firms unknowingly employed such workers between 2020 and 2022, and one group generated over USD 88 million across six years undetected.

**Why it matters.** The most consequential insider threat programme currently operating against the sector, and it arrives through recruitment rather than through the perimeter. A financial institution that hires remote engineering contractors is in the target set by default. The exposure is not only espionage: it is sanctions breach through payroll, privileged access to production systems, and a documented escalation to extortion when the worker is discovered or terminated. Payroll and vendor onboarding, not security operations, are where this is actually detected or missed.

**On the record**

- *2024-12, US* — Fourteen DPRK nationals indicted over a fraudulent IT worker scheme.
- *2025, US* — Law enforcement searched 29 suspected laptop farms across 16 states and seized 29 financial accounts used to launder proceeds; five US residents later pleaded guilty to facilitating placements.
- *2020-2022, US* — Over 300 US companies, including several Fortune 500 firms, unknowingly employed DPRK IT workers; one group generated over USD 88 million over six years.

**Confidence:** E high · A high · F moderate · S high.

> Attribution basis: Formally attributed to DPRK by the US government; named defendants convicted.

> State tasking basis: Attributed to DPRK revenue generation for weapons programmes.

**Sources**

1. [Two North Korean Nationals and Three Facilitators Indicted for Multi-Year Fraudulent Remote IT Worker Scheme](https://www.justice.gov/opa/pr/two-north-korean-nationals-and-three-facilitators-indicted-multi-year-fraudulent-remote) — government
1. [Jasper Sleet: North Korean remote IT workers' evolving tactics to infiltrate organizations](https://www.microsoft.com/en-us/security/blog/2025/06/30/jasper-sleet-north-korean-remote-it-workers-evolving-tactics-to-infiltrate-organizations/) — industry
1. [Five people plead guilty to helping North Koreans infiltrate US companies as remote IT workers](https://techcrunch.com/2025/11/14/five-people-plead-guilty-to-helping-north-koreans-infiltrate-us-companies-as-remote-it-workers/) — news

---

### Bishnoi Gang

`AM-NET-BISHNOI` · network · hybrid · active, capability high · since 2010

*CA, IN, US, AE*

**Aka:** Lawrence Bishnoi gang, Bishnoi-Godara network

A transnational criminal syndicate directed from an Indian prison by Lawrence Bishnoi, with hundreds of members engaged in extortion, arson, shootings and targeted killings, and an established presence in Canada. Canada listed it as a terrorist entity on 29 September 2025, and the RCMP has stated it believes the group is connected to agents of the Government of India, alleging that Indian intelligence used Bishnoi associates to carry out killings and violent intimidation of Khalistan movement supporters abroad. India rejects the allegation. It is included here as a state-proxy-adjacent actor rather than a confirmed intelligence component, and coded accordingly.

**Why it matters.** Extortion of South Asian business communities in Canada, particularly in British Columbia and Ontario, is the group's principal domestic activity, enforced by arson and drive-by shootings at commercial premises. Institutions encounter it as SME customers under coercion, unexplained cash withdrawal patterns, fire and criminal damage claims clustered by community and sector, and requests for account information by intermediaries. The terrorist listing also means property and funds can be frozen or seized, which converts a customer relationship into an immediate sanctions and reporting obligation.

**On the record**

- *2025-09-29, CA* — Government of Canada listed the Bishnoi Gang as a terrorist entity, enabling freezing and seizure of its Canadian property, vehicles and funds.
- *2024-2025, British Columbia and Ontario, CA* — Sustained extortion campaign against South Asian businesses, enforced by arson and shootings, prompting provincial political intervention.

**Confidence:** E high · A high · F moderate · S low.

> Attribution basis: Formally listed by Canada; leadership publicly identified.

> State tasking basis: RCMP states it believes the group is connected to agents of the Government of India; the linkage is an official assessment, is denied by India, and has not been established judicially.

**Sources**

1. [Government of Canada lists the Bishnoi Gang as a terrorist entity](https://www.canada.ca/en/public-safety-canada/news/2025/09/government-of-canada-lists-the-bishnoi-gang-as-a-terrorist-entity.html) — government
1. [Federal government lists Bishnoi Gang as terrorist entity](https://www.cbc.ca/news/politics/bishnoi-gang-listed-as-terrorist-entity-1.7646153) — news
1. [Canada labels India's Bishnoi gang as 'terrorist' organisation](https://www.aljazeera.com/news/2025/9/29/canada-labels-indias-bishnoi-gang-as-terrorist-organisation) — news

---
