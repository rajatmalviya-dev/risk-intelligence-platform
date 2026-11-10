# Security Policy

## Scope

This repository is a public educational and portfolio project.

Security concerns may include vulnerabilities in:

- Application code
- API endpoints
- Authentication or authorization logic
- Dependency configuration
- CI/CD workflows
- Container configuration
- Secret handling
- Data-processing pipelines
- Agent or tool integrations

## Reporting a Security Vulnerability

Please do **not** report security vulnerabilities through public GitHub Issues, pull requests, or other public discussions.

If GitHub Private Vulnerability Reporting is available for this repository, use that mechanism to submit the report privately.

When reporting a vulnerability, please provide:

- A clear description of the issue
- The affected component or file
- Steps required to reproduce the issue
- The potential security impact
- Any relevant logs or error messages that do not contain secrets
- A suggested remediation, if known

Please avoid including credentials, API keys, access tokens, private keys, personal information, or other sensitive data in the report.

## Secrets and Sensitive Information

Never commit the following to this repository:

- API keys
- Access tokens
- Passwords
- Private keys
- Cloud credentials
- Database credentials
- Authentication cookies
- Customer or personal information
- Confidential business information
- Proprietary datasets
- Internal documentation

If a secret is accidentally committed:

1. Do not assume that deleting the file is sufficient.
2. Revoke or rotate the exposed credential immediately.
3. Remove the secret from the repository history where appropriate.
4. Investigate whether the credential was accessed or misused.
5. Report the incident through the appropriate private security channel.

## Dependency Security

Dependencies are managed using `uv`.

The repository uses automated dependency auditing and GitHub security features to identify known vulnerabilities.

Security checks include:

- Dependency vulnerability auditing
- GitHub secret scanning
- Secret scanning push protection
- Dependabot security updates
- Automated CI checks

Dependencies should be kept reasonably current, and security updates should be reviewed before being merged.

## Responsible Disclosure

Please allow reasonable time for a security issue to be investigated and addressed before publicly disclosing details.

Security reports should focus on reproducible technical issues and should not contain sensitive information that is unnecessary to demonstrate the vulnerability.

## Security Limitations

This project is an educational and portfolio implementation.

It is not intended to represent a production security architecture for a specific organization, regulated environment, or critical infrastructure system.

Security controls demonstrated in this repository should not be interpreted as a complete security assessment or production security certification.