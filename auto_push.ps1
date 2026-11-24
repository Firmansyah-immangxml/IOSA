
$ErrorActionPreference = "Continue"

Set-Location "C:\IOSA"

$Branch = "main"
$Interval = 2
$StableSeconds = 3

Write-Host "====================================" -ForegroundColor Cyan
Write-Host "       IOSA AUTO PUSH SYSTEM" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host "Pemantauan aktif..." -ForegroundColor Green
Write-Host "Tekan Ctrl+C untuk berhenti."

while ($true) {
    Start-Sleep -Seconds $Interval

    $Changes = git status --porcelain

    if ($Changes) {
        Write-Host "Perubahan terdeteksi!" -ForegroundColor Yellow

        Start-Sleep -Seconds $StableSeconds

        $Changes = git status --porcelain

        if ($Changes) {
            git add -A

            $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            git commit -m "IOSA Auto Update: $Timestamp"

            if ($LASTEXITCODE -eq 0) {
                git push origin $Branch

                if ($LASTEXITCODE -eq 0) {
                    Write-Host "Berhasil tersimpan ke GitHub!" -ForegroundColor Green
                }
                else {
                    Write-Host "Push gagal! Periksa koneksi GitHub." -ForegroundColor Red
                }
            }
        }
    }
}
