$D3ActiveProgsPath = ".\_inputfiles\D3_ActiveProgs.txt"
$D3ActiveProgs = Get-Content -Path $D3ActiveProgsPath

$D3FileDestDir = ".\_inputfiles\D3Files"

foreach ($ProgPath in $D3ActiveProgs)
{
    $FullProgPath = $ProgPath + ".SEQ"
    Copy-Item -Path $FullProgPath -Destination $D3FileDestDir
}