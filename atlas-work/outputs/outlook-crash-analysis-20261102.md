# Analýza pádu Outlooku – 2. 11. 2026

## Doložené údaje z dumpu

- Soubor: outlook-crash-20261102.dmp
- Vlákno: 45604
- Výjimka: 0xC0000005, čtení adresy 0xCC
- Místo: MSO.DLL + 0x572CBC
- Instrukce (48 8B 80 C0 00 00 00): mov rax, qword ptr [rax+0xC0]
- RAX při výjimce: 0xC; 0xC + 0xC0 = 0xCC.

## Nativní řetězec volání

Rekonstrukce z kontextu výjimky a x64 unwind metadat PE obrazů uložených v dumpu; nejde o pouhé hledání adres na zásobníku. Bez veřejných PDB nejsou přiřazené názvy interních funkcí.

```text
mso.dll + 0x572cbc
mso.dll + 0x142c40c
mso.dll + 0xa7b31c
mso.dll + 0xa4c661
uiautomationcore.dll + 0x1ca63
uiautomationcore.dll + 0x1dbe7
uiautomationcore.dll + 0x1d6dc
OneCoreCommonProxyStub.dll + 0x10bf
rpcrt4.dll + 0xd5882
rpcrt4.dll + 0x4c000
combase.dll + 0x9443d
rpcrt4.dll + 0x67ca6
combase.dll + 0x93eee
combase.dll + 0x936b8
combase.dll + 0x11ad00
combase.dll + 0x95d42
combase.dll + 0x94951
combase.dll + 0x41686
```

## Vyhodnocení

Pád nastal v MSO při obsluze volání přes UIAutomationCore a COM/RPC. To je konkrétní stopa k rozhraní přístupnosti / automatizace UI Office. Samotný dump neurčuje, který klient volání vyvolal. Mezi klienty může patřit i nástroj, kterým asistent čte strom UI Outlooku; jeho účast není tímto dumpem prokázaná.

Dřívější odhad nulového ukazatele není přesný: registrovaná hodnota je 0xC, nikoli nula. Příčina vzniku této hodnoty zatím není určena.

Událost Outlook 38 a chyba synchronizace Yandex 0x800CCC0E tuto cestu pádu nevysvětlují.

## Další ověření

Nyní neprovádět čtení UI stromu Outlooku. Porovnat běžnou práci v Outlooku bez klienta automatizace se stavem při pádu; izolovat další klienty přístupnosti jen na základě důkazů. Pro definitivní názvy funkcí a přesné určení operace doplnit symboly MSO a UIAutomationCore a ověřit zásobník standardním nativním debuggerem.
