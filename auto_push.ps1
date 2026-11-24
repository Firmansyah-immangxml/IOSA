
$ErrorActionPreference = "Continue"

$ProjectPath = "C:\IOSA"
$Branch = "main"

Set-Location $ProjectPath

Write-Host "====================================" -ForegroundColor Cyan
Write-Host "       IOSA AUTO PUSH SYSTEM" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host "Memantau perubahan file IOSA..." -ForegroundColor Green

$Watcher = New-Object System.IO.FileSystemWatcher
$Watcher.Path = $ProjectPath
$Watcher.IncludeSubdirectories = $true
$Watcher.NotifyFilter = [System.IO.NotifyFilters]'FileName, DirectoryName, LastWrite, Size'
$Watcher.EnableRaisingEvents = $true

$LastPush = Get-Date

while ($true) {
    Start-Sleep -Seconds 5

    $Changes = git status --porcelain

    if ($Changes) {
        Write-Host "Perubahan terdeteksi. Menunggu proses selesai..." -ForegroundColor Yellow

        Start-Sleep -Seconds 10

        $Changes = git status --porcelain

        if ($Changes) {
            git add -A

            $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            git commit -m "IOSA Auto Update: $Timestamp"

            if ($LASTEXITCODE -eq 0) {
                git push origin $Branch

                if ($LASTEXITCODE -eq 0) {
                    Write-Host "Berhasil push ke GitHub!" -ForegroundColor Green
                }
                else {
                    Write-Host "Push gagal. Periksa koneksi atau konflik Git." -ForegroundColor Red
                }
            }
        }
    }
}
