@echo off
curl.exe -s -X POST -H "Authorization: Bearer YOUR_HF_TOKEN" -H "Content-Type: application/json" -d @hf_final_docker_payload.json https://huggingface.co/api/spaces/ACLASCollege/aclas-neuro-dashboard/commit/main
echo Commit executed.
