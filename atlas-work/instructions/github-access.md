# Připojení samostatného agenta ke GitHubu

## Copilot ve VDI — závazné pravidlo uživatele

Ve VDI používej Copilot jako první volbu všude, kde je dostupný a použitelný pro zadaný úkol. Teams Copilot používej pro dohledání napříč SharePointem, Teams, e-maily a přepisy schůzek; Copilot ve Wordu a Excelu pro rozbor otevřených podkladů. Používej i další dostupné panely Copilotu. Před rozsáhlým ručním procházením ověř dostupnost Copilotu a zadej cílený dotaz. Vyžaduj odkazy a verze podkladů a závěry ověřuj proti primárním zdrojům. Detailní informace jsou v Confluence. Pro jejich vyhledávání v Teams používej konkrétního specializovaného agenta **Confluence Agent**, nikoli běžný Teams Copilot. Confluence čti přes tohoto agenta nebo přímo přes URL stránek. Pro přímý přístup přes URL musí být aktivní přihlášení účtem uživatele; ověř přihlášení a pokud chybí nebo vypršelo, dej uživateli vědět a požádej ho o ruční přihlášení. Přihlašovací dialogy neautomatizuj a nevyžaduj heslo do chatu. U výsledků Confluence Agentu vyžaduj URL primární stránky a dostupné údaje o verzi či datu; detail, který agent nevrátí, ověř přímým čtením stránky po přihlášení. Výsledek agenta není dokladem úplného průzkumu všech stránek a podsložek.

Platí zákaz změn zdrojových dat ve VDI: zadávání dotazů do Copilotu je povoleno, ale nepoužívej Apply/Insert/Edit ani jiné provedení změn do zdrojových dokumentů, sešitů či dat. Výjimku má pouze výslovně povolená projektová složka OneDrive AI. Při překážce zaznamenej konkrétní omezení a pokračuj jinou povolenou cestou. Běžně zadatelný dotaz nepřenášej na uživatele.

### Připojení

Repozitář je veřejný. Čtení nevyžaduje SSH klíč:

```sh
git clone --branch codex/atlas-stav-2026-11-01 --single-branch https://github.com/zsery/zsery.git
cd zsery
git status --short
```

Pokud máš checkout, nejprve ověř jeho větev a změny; nepřepisuj rozpracované soubory.

Pro zápis použij svůj připojený GitHub konektor nebo vlastní GitHub autorizaci. Ověř oprávnění k `zsery/zsery`; dostupnost veřejného čtení sama nezaručuje zápis. Přihlášení browseru nepovažuj za autorizaci Git klienta. Nepřenášej přístupové údaje jiné instance a nevkládej klíče do repozitáře.

GitHub konektor: načti metadata repozitáře, ověř oprávnění push, přečti větev. Pro dávkové uložení podporuje Git data operace create_blob → create_tree nad existujícím base tree → create_commit s existujícím parent SHA → update_ref pracovní větve s expected_sha. Nepoužívej force. Po zápisu znovu načti HEAD větve a ověř SHA.

Git s vlastní funkční autorizací:
```sh
git add -- atlas-work
git commit -m "Update Atlas working analysis"
git push origin HEAD:refs/heads/codex/atlas-stav-2026-11-01
git rev-parse HEAD
git ls-remote origin refs/heads/codex/atlas-stav-2026-11-01
```
Obě SHA musí souhlasit. Nezapisuj do main, obsahuje deployment workflow. Pokud zápis není povolen, dál čti veřejné podklady a přesně uveď chybějící oprávnění.

