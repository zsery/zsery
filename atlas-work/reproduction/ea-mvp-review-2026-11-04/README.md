# Reprodukce dílčí EA revize

Použij vlastní aktuální runtime s lxml. V pracovním kořeni připrav work/ea-source/Atlas.xml z původního Atlas.7z a adresář outputs. revise_ea.py ověří přesný vstupní SHA-256, změní osm určených documentation hodnot a zkontroluje úplné zachování ostatních bajtů a identifikátorů. Výstup je v work/ea-revision a manifest také v outputs. Zdroj se nemění. Toto není automatický patch jiné nebo novější verze živého modelu.

Nativní EA import a vizuální QA diagramů nejsou provedené. Zdrojové API kontrakty nejsou domýšlené. Žádné přístupové údaje nejsou součástí reprodukce.
