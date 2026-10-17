@if "%DEVTO_API_KEY%"=="" (
  @echo Set DEVTO_API_KEY before running this script.
  @exit /b 1
)
curl.exe -X POST "https://dev.to/api/articles" -H "Content-Type: application/json" -H "api-key: %DEVTO_API_KEY%" -d @article_payload.json
