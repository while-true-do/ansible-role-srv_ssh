<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_ssh.svg)](https://github.com/while-true-do/ansible-role-srv_ssh/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_ssh.svg)](https://github.com/while-true-do/ansible-role-srv_ssh/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_ssh.svg)](https://github.com/while-true-do/ansible-role-srv_ssh/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_ssh.svg)](https://github.com/while-true-do/ansible-role-srv_ssh/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_ssh.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_ssh)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_ssh%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_ssh)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_ssh%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_ssh)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_ssh%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_ssh)

# Ansible Role: ssh

An Ansible to install and configure the ssh server.

## Motivation

The [Openssh Server](https://www.openssh.com/) is the default access to almost
all \*nix systems. Having a role, that installs and configures this core service
is mandatory for most operators.

## Description

This Ansible Role installs and configures the openssh server (sshd).

-   install needed packages
-   configure sshd
-   configure a banner
-   configure SELinux
-   configure firewalld
-   apply some compliance standards (OpensSCAP Standard System Security Profile)

## Requirements

Used Modules:

-   [Ansible package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible package_facts Module](https://docs.ansible.com/ansible/latest/modules/package_facts_module.html)
-   [Ansible service Module](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible template Module](https://docs.ansible.com/ansible/latest/modules/template_module.html)
-   [Ansible firewalld Module](https://docs.ansible.com/ansible/latest/modules/firewalld_module.html)
-   [Ansible seport Module](https://docs.ansible.com/ansible/latest/modules/seport_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_ssh)
```
ansible-galaxy install while_true_do.srv_ssh
```

Install from [Github](https://github.com/while-true-do/ansible-role-srv_ssh)
```
git clone https://github.com/while-true-do/ansible-role-srv_ssh.git while_true_do.srv_ssh
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_ssh

## Package Management
wtd_srv_ssh_package: "openssh-server"
# State can be present|latest|absent
wtd_srv_ssh_package_state: "present"

## Configuration Management
# Specify the banner file
wtd_srv_ssh_conf_banner: ""
# Per default some Compliance Standards are applied. You can review them in the
# README.md or the templates.
# You can specify addtional configuration.
wtd_srv_ssh_conf:
  Port: "22"
# You can define a banner [builtin|<path>], where "builtin" will use the
# template from this role.
  Banner: "builtin"
# key: "value"
# key: "value"
# Defining the banner this way will use the banner template, which is the
# default behavior.

## Service Management
wtd_srv_ssh_service: "sshd"
# State can be started|stopped
wtd_srv_ssh_service_state: "started"
wtd_srv_ssh_service_enabled: true

## Firewalld Management
wtd_srv_ssh_fw_mgmt: true
wtd_srv_ssh_fw_port: "{{ wtd_srv_ssh_conf.Port }}/tcp"
# State can be enabled|disabled
wtd_srv_ssh_fw_state: "enabled"
# Zone can be according to defined zones on your machine.
wtd_srv_ssh_fw_zone: "public"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.srv_ssh
```

#### Advanced

Configure another ssh port and disable password login.

```
- hosts: all
  roles:
    - role: while_true_do.srv_ssh
      wtd_srv_ssh_conf.Port: "19022"
      wtd_srv_ssh_conf.PasswordAuthentication: "no"

```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_ssh/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_ssh/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
