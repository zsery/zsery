# GitHub připojení a autorizovaný rozsah

Repo `git@github.com:zsery/zsery.git`, branch `codex/atlas-stav-2026-11-01`. Uživatel výslovně povolil ukládání dílčích výstupů a předání. `main` obsahuje deployment workflow; pushovat jen uvedenou pracovní větev. Browser login není autentizace shellového Git SSH a Windows účty dvou PC se nemusí propojovat.

## Původní PC – ověřený transport

Pracovní checkout: `C:/Users/zsery/Documents/Codex/2026-10-31/jse/work/github-zsery`.
Adresář připojení: `C:/Users/zsery/Documents/Codex/2026-10-31/jse/work/auth/`.
Soukromý deploy key `zsery_zsery_deploy_ed25519`, veřejný `.pub`, wrapper `git-ssh.exe`, pinned `github_known_hosts`. **Soukromý soubor není v GitHubu ani ZIPu.** Nečti/neprintuj jeho obsah při diagnostice. Wrapper předává stdin/stdout/stderr pro binární Git transport; nepoužívej starší experimentální git-ssh-pipe.exe.

PowerShell, nejprve pouze čtení:

```powershell
git -C 'C:/Users/zsery/Documents/Codex/2026-10-31/jse/work/github-zsery' -c core.sshCommand=C:/Users/zsery/Documents/Codex/2026-10-31/jse/work/auth/git-ssh.exe -c ssh.variant=ssh ls-remote origin refs/heads/codex/atlas-stav-2026-11-01
git -C 'C:/Users/zsery/Documents/Codex/2026-10-31/jse/work/github-zsery' status --short
```

Po přípravě a kontrole konkrétních změn:

```powershell
git -C 'C:/Users/zsery/Documents/Codex/2026-10-31/jse/work/github-zsery' add -- atlas-work
git -C 'C:/Users/zsery/Documents/Codex/2026-10-31/jse/work/github-zsery' commit -m 'Update Atlas working evidence and handoff'
git -C 'C:/Users/zsery/Documents/Codex/2026-10-31/jse/work/github-zsery' -c core.sshCommand=C:/Users/zsery/Documents/Codex/2026-10-31/jse/work/auth/git-ssh.exe -c ssh.variant=ssh push origin HEAD:refs/heads/codex/atlas-stav-2026-11-01
git -C 'C:/Users/zsery/Documents/Codex/2026-10-31/jse/work/github-zsery' rev-parse HEAD
git -C 'C:/Users/zsery/Documents/Codex/2026-10-31/jse/work/github-zsery' -c core.sshCommand=C:/Users/zsery/Documents/Codex/2026-10-31/jse/work/auth/git-ssh.exe -c ssh.variant=ssh ls-remote origin refs/heads/codex/atlas-stav-2026-11-01
```

Porovnej obě SHA. Nedávej add celé nadřazené workspace. DNS chyba „Could not resolve hostname“ v sandboxu byla odstraněna povolením sítě přes request_permissions; není důkaz neplatného klíče. Žádej jen skutečně potřebné síťové oprávnění.

## Druhé PC / nová instance

Nejprve zjisti, zda je již připojený GitHub connector nebo lokální určený deploy key. Existující funkční autorizaci použij. Uživatel preferoval určený deploy key, protože jiné metody dříve nefungovaly. Pokud soukromý klíč na druhém PC není, samotné toto předání ho nezpřístupní. Zajistit ho mimo Git/chat běžnou uživatelem schválenou bezpečnou cestou; nevytvářet nový klíč nebo měnit GitHub permissions bez autorizace.

Ve složce `connection/` je přenositelný **zdroj** wrapperu `GitSsh.cs` (bez tajemství) a stávající pinned known_hosts. Wrapper očekává soukromý klíč se stejným názvem **vedle výsledného EXE mimo repo**. Na Windows lze připravit soukromý task auth adresář a zkompilovat zdroj:

```powershell
./atlas-work/tools/build_ssh_wrapper.ps1 -OutputDirectory 'C:/path/outside-repository/atlas-auth'
```

Adresu uprav podle skutečného prostředí, nic nevkládej do VDI. Skript používá již instalovaný .NET Framework compiler, odmítá výstup uvnitř repa a existující EXE. Kompilace a kopie veřejného host pin byly otestovány v nové lokální složce; transport s novým EXE na jiném PC dosud není ověřen. Po schváleném umístění původního klíče do tohoto soukromého adresáře proveď `ls-remote` pomocí nového wrapperu a stejné větve. Pro cestu obsahující mezery použij správné Git/shell quoting.

Na Linux/macOS lze použít OpenSSH přímo (cesty uprav, key i known_hosts mimo repo):

```sh
export GIT_SSH_COMMAND='ssh -F /dev/null -i /private/path/zsery_zsery_deploy_ed25519 -o IdentitiesOnly=yes -o BatchMode=yes -o StrictHostKeyChecking=yes -o UserKnownHostsFile=/private/path/github_known_hosts -o HostKeyAlgorithms=ssh-ed25519'
git ls-remote git@github.com:zsery/zsery.git refs/heads/codex/atlas-stav-2026-11-01
git clone --branch codex/atlas-stav-2026-11-01 --single-branch git@github.com:zsery/zsery.git
```

Nepřepisovat existující checkout příkazem clone. Nezakazovat ověřování host key. Pinned soubor je převzatý z dříve fungujícího task transportu, ne nově získaný neověřený scan. Při změně host key řešit konkrétní ověření, ne vypnout kontrolu.
