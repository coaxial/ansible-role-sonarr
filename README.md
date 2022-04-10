# Sonarr role

[![CI](https://github.com/coaxial/ansible-role-sonarr/actions/workflows/ci.yml/badge.svg)](https://github.com/coaxial/ansible-role-sonarr/actions/workflows/ci.yml)

Galaxy: https://galaxy.ansible.com/coaxial/sonarr

## Variables and their defaults

| variable name       | default value     | description                                                                             |
| ------------------- | ----------------- | --------------------------------------------------------------------------------------- |
| sonarr\_\_version   | `latest` (stable) | See https://github.com/Radarr/Radarr/releases                                           |
| sonarr\_\_use_nginx | `yes`             | Whether to install and configure nginx (`no` if you're installing/managing it yourself) |
