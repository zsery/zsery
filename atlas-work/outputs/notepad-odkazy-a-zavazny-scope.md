# Odkazy z Notepad++ a závazný scope

Datum: 1. 11. 2026. Uživatel výslovně potvrdil: „Atlas CZ Launch – Architecture Board Confirmation of Phased Implementation Approach.docx“ je závazná poslední verze a scope projektu. Tato informace má při posuzování scope přednost před staršími pracovními dokumenty, návrhy a výsledky Copilotu. Dřívější poznámka o nepotvrzené závaznosti je tímto vyřešena potvrzením uživatele.

Ve VDI pouze čtení. Seznam v Notepad++ nebyl upraven ani uložen. Všechny URL položky seznamu byly otevřeny; nejde o úplnou obsahovou revizi každého navazujícího souboru a celého stromu všech knihoven.

## Prohlédnuté cíle

| Položka seznamu | Otevřený cíl a význam | Rozsah kontroly |
|---|---|---|
| 1–2 Marketplace od Ludvíka | Oba odkazy vedou na stejnou SharePoint knihovnu MarketPlace / Documents / General. | Přehled; dále 02 Solution Design → Solution_Overview. Obsahuje EAR, Interface Specification, Marketplace API, OLD a Marketplace D1 Manual Solution Overview Word. Jednotlivé navazující dokumenty zatím nečteny. |
| Fyzické aplikace / dokumentace | Confluence OCP / System Documentation. | Index, pod ním Components (Campaign Management/AOM, OCP Components, Selfcare Components), DXL, Solutions, Vodafone One, MVW, MVA12 atd. Není to sám o sobě úplný kanonický katalog všech firemních aplikací. |
| SSO integration | Grow Squad / Development / SSO integration. | Deployment diagram OCP backoffice a infrastruktury, starší zdroj z roku 2022. Neprokazuje Atlas integraci. |
| IDaaS | IAG / IDaaS. | Identitní provider Vodafone ID, používán V4 WSC/MVA i V2 ONSC; CIAM API odkazy a sekvenční diagramy ONSC autentizace a SSO. |
| SSO and IDM | UCC / SSO and IDM. | Stránka s přílohami Solution Overview, IDM roles a Permissions. UCC kontext, nikoli přímý doklad Atlas role modelu; přílohy neprošly úplným čtením. |
| VFID 01.09 SSO | OCP / VFID 01.09 - SSO. | Přečten obecný shared-code tok: initiating/receiving aplikace, producer/consumer scopes, předem přidělený grant, jednorázový sdílený kód a authorize flow. Technická reference, nikoli schválení nového ONSC/WSC propojení Atlas MVP. Nekopírovat provozní hodnoty z ukázek do výstupů. |
| Solution overview | IAG / Solution overview. | Účel SO, Concept/HLSO/LLSO/WR typy a proces jejich vzniku a review. |
| Content of SO | IAG / Content of SO. | Struktura: Introducing; Architecture and Solution Description; Functional Design; System Impacts; Other Requirements; Open Points. Přímo otevřena také kapitola 4 System impacts. |
| Návod SO | IAG / Navod SO. | Přečten praktický postup, aktuální šablona „05_VRXY solution overview“, status dokumentu, propojení Jira/BRD, stabilní odkazy přes Share, číslované kapitoly, komentované milníky a archivace Wordu při případné migraci do Confluence. Jde o metodiku, nikoli pokyn k provedení změn v této relaci. |
| Solution Overview Template | TIB / Solution Overview - Template. | Přečtena struktura celé stránky včetně Document Control, Interfaces, Components, Functional Areas/UC, System Impacts, infrastruktury, Architecture Decisions, Assumptions/Limitations, Open Points. Bez vyplňování nebo vytvoření stránky. |
| Moje SO | SharePoint CZ local folder / Architecture / Solution_Overview_ServiceHub.docx. | Přímo otevřen 30stránkový Concept SO, přečten úvod, historie/reference a planned drops. Kompletní text a SREQ tabulky ještě neprošly kontrolou. |

## Důsledky pro model a FREQ/SREQ

- Projektový scope určuje výše uvedený Architecture Board dokument, jak potvrdil uživatel. Starší AppImpacts, Requirements a SO se proti němu revidují; nemění ho automaticky ani odkaz na obecný SSO vzor.
- Rozlišovat aplikaci/komponentu, rozhraní, funkci, proces a požadavek. OCP System Documentation je vstup do konkrétní dokumentace, nikoli důkaz, že každý uzel jeho stromu je samostatná fyzická aplikace.
- Metodika System Impacts žádá pro každý dotčený systém popis co a proč se mění a strukturované požadavky. E2E funkční logika patří do Functional Design, interní systémové chování do System Impacts. Project LLSO a WR mají různé zacházení s tabulkou related requirements; projekt vyžaduje samostatnou compliance matici.
- Šablona rozlišuje Integration Status a Interface Status a uvádí consuming/providing system, režim, technologii a security; stav vazby a stav rozhraní neslévat.
- Identitní dokumentace je referencí pro mechanismus; nezakládá CZ implementační požadavek na portálový handover mimo závazný scope.

## První pozorování projektového SO

Titul „Concept Solution Overview – ServiceHub + Atlas / PR25_0837“. Revizní historie uvádí 0.1 z 9. 6. 2026 a 0.4 z 27. 8. 2026, druhá pro doplnění aplikací/SREQ a FREQ traceability z Book1.xlsx. Úvod odkazuje i na pozdější podklady (ISS, customer roles, performance, V4 onboarding). Reference stále zahrnují červnovou UC verzi a srpnový Requirements. Tabulka approvals obsahuje starší verzi 0.3 a governance TBD. Tyto údaje nepovažovat za současné schválení scope; závaznost scope již potvrdil uživatel pro samostatný board dokument.

Planned drops uvádí Drop1/MVP a popis digitálního vstupu, Marketplace subscription visibility, podpory/SNOW, V2/V4 autorizačního kontextu a manuálního V4 onboardingu. Přesné sladění celé kapitoly se závazným board scope a říjnovým UC je další krok revize, nikoli hotový závěr.
