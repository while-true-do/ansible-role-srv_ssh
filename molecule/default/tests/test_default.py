# Some examples are given below.

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sshd_package(host):
    pkg = host.package('openssh-server')

    assert pkg.is_installed


def test_sshd_service(host):
    srv = host.service('sshd')

    assert srv.is_running
    assert srv.is_enabled
