# Environment Configuration

## Overview

It is required to provide sensitive information to be able to provision
a H10K/Ambari cluster (e.g. api tokens and passwords).  As it can be easier
to work with environment variables, H10K allow and configuration variable to
be set via an environment variable.

## API Token

It is strongly recommended not to provide your API token via the command line
(although this is allowed if you really want to).  An alternative is to
provide it via a special environment variable called
`H10K_API_TOKEN`.

## Configuration Variables

Any variable in the configuration file can be specified via environment
variables.  This can be done with environment variables that have a name
beginning with `H10K_CONFIG_` and then separating what YAML it would be
with an underscore.  For example, setting an environment variable called
`H10K_CONFIG_AMBARI_PASSWORD` set to `topsecret` and then running H10K
against a configuration file containing:

```YAML
ambari:
  clustername: h10kdemo
  instancetype: t2.micro
  password: spameggs
```

would be the equivalent of having a configuration file containing the
following:

```YAML
ambari:
  clustername: h10kdemo
  instancetype: t2.micro
  password: spameggs
```
