# Ověření prvního výsledku Teams Copilotu

Datum 1. 11. 2026. VDI pouze čtením. Odpověď Copilotu není sama primární důkaz.

## Nalezené odkazy – zatím neověřená metadata Copilotu

Copilot nabídl projektový Service Hub+Atlas – Requirements (Martin Dostál, změna 21. 8. 2026) a osobní kopii (Zdeněk Šerý, 6. 8. 2026). Projektový sešit je třeba otevřít a porovnat s říjnovým scope; datum neprokazuje aktuální baseline. U BRD upozornil na revizní historii s verzí 0.2 k 23. 10. oproti titulní 0.1. Schválenou baseline nedoložil.

## Primární ověření citace k RBAC

Z odpovědi byl otevřen odkaz do Teams chatu „SNOW - Otto Zeman - synchro s ředitelem projektu“. Byly přímo přečteny zprávy navázané na dotaz Dany Košťálové z úterý 27. 10.; odpovědi jsou označeny Thursday (29. 10. 2026), Martin 7:56 a Dragomir 11:11, edited. Nejde o přímo přečtený transcript, ale o chatové zprávy.

Martin uvádí, že ServiceHub nemá v MVP RBAC a všichni mohou všechno. Současně jeho zpráva obsahuje tabulku „Roles required access to Service Hub portal“:

| Segment | Systém | Role | SH Access |
|---|---|---|---|
| V2 | ONSC | Admin, Group Admin, Associate Admin | Required full access |
| V4 | WSC | Admin | Required full access |
| V2 | ONSC | End user | Not Required |
| V4 | WSC | End user & Billing Account User | Not Required |

Dragomir následně píše, že zákazničtí uživatelé v projektu SNOW mají stejná práva vytvářet, číst a upravovat cases/tickets a liší se vazbou přístupových oprávnění na companies. Odkazuje na BRD PR25_0744-F-REQ-014. Toto ID nebylo otevřeno a nesmí se přenést do projektu Atlas jako nový požadavek bez ověření.

## Dopad na interpretaci

Copilot označil možný rozpor s UC005. Přímý chat však ukazuje, že je nutné oddělit vstupní způsobilost podle ONSC/WSC role, oprávnění k zákaznické společnosti a rozdílná funkční práva uvnitř portálu. „Bez RBAC“ samo neprokazuje přístup všem autentizovaným uživatelům: přiložená tabulka současně vyjmenovává admin role a end-user role označuje Not Required.

Výklad, že způsobilí administrátoři mají shodná funkční práva při zachování omezení na společnosti, je pracovní syntéza těchto zdrojů; není to samostatně doložené schválené rozhodnutí. UC005 zatím neoznačovat za zrušený nebo chybný jen na základě shrnutí Copilotu.

Zbývá otevřít odkazovaný requirements sešit, ověřit celé rozhodnutí o scope/navigaci z 28. 10. a potřebná rozhraní pro account filtering. Přímé URL nebylo z obrazovky spolehlivě získáno; není doplněno odhadem.
