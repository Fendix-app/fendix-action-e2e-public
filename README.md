# Fendix E2E fixture: clean

Test infrastructure only. Contains no real secrets or credentials.

## v3.7.0 round

Every fixture runs the composite Action at the v3.7.0 release commit, 90adf6a,
not the moving v1 tag, which still names v3.6.2. The v370-e2e branches mirror
the v3.6.5 round. Four cases are new, and test that the Action fails closed
when an analyzer it requires cannot run; a fifth is supplementary.

- old-glibc-required: the BLOCK fixture in a Debian 11 container
  (python:3.11-bullseye, glibc 2.31), with the default require-analyzers.
  Semgrep has no wheel there, so setup must fail with exit 2 and an error
  naming Semgrep and glibc 2.31: no scan, no SARIF upload, no clean line.
- old-glibc-none: the same container with require-analyzers none. The scan
  must complete without Semgrep, record it unavailable and warn that coverage
  is not enforced. The analyzers that ran decide the outcome.
- arm64: the BLOCK fixture on ubuntu-24.04-arm. The preflight must pass,
  Semgrep must run, and the findings must equal the amd64 BLOCK run.
- fast-bypass: the BLOCK fixture with extra-args --fast and the default
  requirement. The engine must exit 2 because the required analyzer semgrep
  was not delivered, and the partial report must not be uploaded.
- old-glibc-none-clean (supplementary): old-glibc-none on the clean tree, so
  the opt-out reaches a passing scan, which must warn and never print the
  clean line.

The negative cases run the Action with continue-on-error, then assert its
outcome, its exit-code output and its report, and a second job checks the
finished job log and annotations. They pass only when the Action failed for
the stated reason. Two harness steps prepare the container: gettext-base for
the envsubst that cosign-installer needs, and the container's own Python 3.11
as the setup-python tool cache.
