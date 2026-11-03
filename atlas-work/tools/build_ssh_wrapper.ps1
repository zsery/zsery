param([Parameter(Mandatory=$true)][string]$OutputDirectory)
$ErrorActionPreference = 'Stop'
$atlasBundle = Split-Path -Parent $PSScriptRoot
$atlasOutput = [IO.Path]::GetFullPath($OutputDirectory)
$atlasRepository = Split-Path -Parent $atlasBundle
if ($atlasOutput.Equals($atlasRepository, [StringComparison]::OrdinalIgnoreCase) -or $atlasOutput.StartsWith($atlasRepository + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Output must be outside the repository. Private key must never be placed in the checkout.'
}
$atlasCompiler = Join-Path $env:WINDIR 'Microsoft.NET/Framework64/v4.0.30319/csc.exe'
if (-not (Test-Path -LiteralPath $atlasCompiler)) {
    $atlasCompiler = Join-Path $env:WINDIR 'Microsoft.NET/Framework/v4.0.30319/csc.exe'
}
if (-not (Test-Path -LiteralPath $atlasCompiler)) { throw 'Installed .NET Framework C# compiler not found. Do not download/run another compiler automatically.' }
$atlasExecutable = Join-Path $atlasOutput 'git-ssh.exe'
if (Test-Path -LiteralPath $atlasExecutable) { throw 'git-ssh.exe already exists. Keep the existing transport or choose a fresh directory.' }
New-Item -ItemType Directory -Path $atlasOutput -Force | Out-Null
& $atlasCompiler /nologo /target:exe ("/out:" + $atlasExecutable) (Join-Path $atlasBundle 'connection/GitSsh.cs')
if ($LASTEXITCODE -ne 0) { throw 'C# compilation failed.' }
$atlasKnownHosts = Join-Path $atlasOutput 'github_known_hosts'
if (Test-Path -LiteralPath $atlasKnownHosts) { throw 'known_hosts already exists; inspect it rather than overwrite.' }
Copy-Item -LiteralPath (Join-Path $atlasBundle 'connection/github_known_hosts') -Destination $atlasKnownHosts
Write-Output 'Wrapper compiled and pinned public host copied. No private key was copied or created. Verify ls-remote only after authorized private-key provisioning.'
