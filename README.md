This is a demo project show integration with Lambda SignalFx dashboards.

Checkout the project.
```bash
git clone https://github.com/rabbah/sfx.git
```

To deploy this project first export your SignalFx API token.
```bash
export SIGNALFX_INGEST_ENDPOINT=<your ingest endpoint> # e.g., https://ingest.us1.signalfx.com
export SIGNALFX_ACCESS_TOKEN=<your secret token>
```

You may also save the API ingest endpoint and token to a `.env` file.
Note: `https://` is required on your ingest endpoint.

Then deploy the project:
```bash
nim project deploy sfx
```

The output from `nim project deploy` will look like this:
```
Deploying project '/Users/demo/signalfx'
  to namespace 'guest-abcxyz'
  on host 'https://apigcp.nimbella.io'
Deployment status recorded in '.nimbella'

Deployed actions:
  - hello
```

Now there is a function deploy that you can invoke with the `nim` CLI:
```bash
nim action invoke hello --result
```
```json
{
  "body": "Hello from Nimbella!",
  "statusCode": 200
}
```

Maybe you want to do that a few times... on your Bash terminal, you can execute the following command:
```bash
for run in {1..10}; do nim action invoke hello; done
```

You can also `curl` the function:
```bash
curl `nim action get hello --url`
```
```
Hello from Nimbella!
```

Now check your SignalFx dashboard for some goodies.
