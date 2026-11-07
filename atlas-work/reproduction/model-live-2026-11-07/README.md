# Pracovní model z živého exportu

Spusť rebase_model_docs.py dodaným Pythonem s lxml. Skript pracuje pouze s lokálními soubory. Vyžaduje přesný SHA256 ATLASLIVE.xml a shodu osmi původních dokumentačních polí s historickými before hodnotami; jinak skončí bez přepsání zdroje.

Výstup outputs/EA_SO_2026-11-05/Atlas_MVP_live_working_2026-11-07.xml přenáší osm již doložených oprav na aktuální projektový export. Všechny ostatní bajty, GUID, XMI id/idref, konektory a diagramy jsou zachovány. Bez přidané auditní/review vrstvy. Není to hotový strukturální model ani ověření nativního importu. Do připojeného EA repository nic neimportovat.

Doložení jednotlivých změn zůstává v původní Kontrola_EA_revize_2026-11-04.json a primární Confluence_AuthX_overeni_2026-11-05.md. Historické modely ani staré audity nejsou nová baseline. SHA256 výstupu: 8809b4dcf96e47e2a996bc339c506eddc5acbb5bccb4a9293b698f9483562ab6.
