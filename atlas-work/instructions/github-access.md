# Připojení samostatného agenta ke GitHubu

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

