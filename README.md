# setup-crossplane-cli

[![CI](https://github.com/nimjor/setup-crossplane-cli/actions/workflows/ci.yaml/badge.svg)](https://github.com/nimjor/setup-crossplane-cli/actions/workflows/ci.yaml)

Install the [Crossplane CLI](https://docs.crossplane.io/latest/cli/command-reference/) for use in GitHub Workflows.

## Inputs

| Param | Description | Required | Default |
| ----- | ----------- | -------- | ------- |
| channel | The release channel from which to install. | `false` | `"stable"` |
| version | The version of the Crossplane CLI to install. | `false` | `"latest"` |

## Usage

```yaml
# Install the latest stable release
- name: Setup Crossplane CLI
  uses: nimjor/setup-crossplane-cli@v1
```

```yaml
# Install a specific version
- name: Setup Crossplane CLI
  uses: nimjor/setup-crossplane-cli@v1
  with:
    version: v1.15.0
```

```yaml
# Install from a channel other than stable
- name: Setup Crossplane CLI
  uses: nimjor/setup-crossplane-cli@v1
  with:
    channel: master
```
