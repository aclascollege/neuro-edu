import urllib.request
import json
import ssl
import sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    req = urllib.request.Request('https://api.github.com/repos/aclascollege/neuro-edu/actions/runs')
    req.add_header('User-Agent', 'Mozilla/5.0')
    res = urllib.request.urlopen(req, context=ctx)
    data = json.loads(res.read())
    runs = data.get('workflow_runs', [])
    if not runs:
        print("No workflow runs found.")
        sys.exit(1)
        
    latest = runs[0]
    jobs_url = latest.get('jobs_url')
    if jobs_url:
        req_jobs = urllib.request.Request(jobs_url)
        req_jobs.add_header('User-Agent', 'Mozilla/5.0')
        res_jobs = urllib.request.urlopen(req_jobs, context=ctx)
        jobs_data = json.loads(res_jobs.read())
        jobs = jobs_data.get('jobs', [])
        for job in jobs:
            print(f"Job: {job.get('name')} - {job.get('conclusion')}")
            for step in job.get('steps', []):
                if step.get('conclusion') == 'failure':
                    print(f"  Failed Step: {step.get('name')}")
                    # Fetching logs is a bit more involved because GitHub API requires a redirect to S3 for logs,
                    # but we can see the run ID and job ID.
                    job_id = job.get('id')
                    print(f"  Job ID: {job_id}")
                    
except Exception as e:
    print(f"Error: {e}")
