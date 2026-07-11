@if "%DEVTO_API_KEY%"=="" (
  @echo Set DEVTO_API_KEY before running this script.
  @exit /b 1
)
curl.exe -X PUT "https://dev.to/api/articles/3550825" -H "Content-Type: application/json" -H "api-key: %DEVTO_API_KEY%" -d @update_article_payload.json
