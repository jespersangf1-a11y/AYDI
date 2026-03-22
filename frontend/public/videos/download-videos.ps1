# AYDI Video Download Script (PowerShell)
# Run this from frontend/public/videos/ directory
# Downloads free stock videos from Pexels for local serving

$videos = @{
    "ocean-calm.mp4"     = "https://www.pexels.com/download/video/1918465/"
    "sailing-aerial.mp4" = "https://www.pexels.com/download/video/2491284/"
    "ocean-waves.mp4"    = "https://www.pexels.com/download/video/1093662/"
    "yacht-sunset.mp4"   = "https://www.pexels.com/download/video/857251/"
    "yacht-sailing.mp4"  = "https://www.pexels.com/download/video/7333913/"
    "boat-sea.mp4"       = "https://www.pexels.com/download/video/11864823/"
    "sailing-ocean.mp4"  = "https://www.pexels.com/download/video/5124098/"
}

Write-Host "AYDI Video Downloader" -ForegroundColor Cyan
Write-Host "=====================" -ForegroundColor Cyan
Write-Host "Downloading 7 videos to $(Get-Location)..." -ForegroundColor Yellow
Write-Host ""

foreach ($file in $videos.GetEnumerator()) {
    if (Test-Path $file.Key) {
        Write-Host "[SKIP] $($file.Key) already exists" -ForegroundColor DarkGray
        continue
    }
    Write-Host "[DOWN] $($file.Key)..." -ForegroundColor Green -NoNewline
    try {
        Invoke-WebRequest -Uri $file.Value -OutFile $file.Key -UseBasicParsing
        $size = [math]::Round((Get-Item $file.Key).Length / 1MB, 1)
        Write-Host " OK (${size} MB)" -ForegroundColor Green
    } catch {
        Write-Host " FAILED: $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Done! Videos are ready for AYDI." -ForegroundColor Cyan
