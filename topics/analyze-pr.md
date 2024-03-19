# Analyze pull requests


We can now analyse “local-changes” in QDNET (but not QDNETC), which was previously not supported by this linter. As with our other first-party, this mode is used to run incremental analysis on a change set, i.e. on a pull-request. For users of the qodana-github-action, this change will be picked up automatically.

To be able to implement this,

We added this way of “local changes” analysis for other linters too. This new way of running is not enabled by default, but can be toggled using the CLI argument `--force-incremental-script=scope`, for QDNET it is enabled by default and cannot be disabled.