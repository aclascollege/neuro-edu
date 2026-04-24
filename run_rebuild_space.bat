@echo off
echo Deleting existing Space...
curl.exe -s -X DELETE -H "Authorization: Bearer YOUR_HF_TOKEN" -H "Content-Type: application/json" -d @hf_delete_payload.json https://huggingface.co/api/repos/delete
echo.
echo Recreating Space...
curl.exe -s -X POST -H "Authorization: Bearer YOUR_HF_TOKEN" -H "Content-Type: application/json" -d @hf_create_payload.json https://huggingface.co/api/repos/create
echo.
echo Space recreation executed.
