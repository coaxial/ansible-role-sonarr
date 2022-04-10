import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user(host):
    u = host.user('sonarr')

    assert u.exists
    assert 'sonarr' in u.groups
    assert 'media' in u.groups
    assert u.password == '!'
    assert u.shell == '/usr/bin/env nologin'


def test_sonarr_service(host):
    s = host.service('sonarr')

    assert s.is_enabled
    assert s.is_running


def test_sonarr_http(host):
    html = host.run('curl http://localhost/sonarr').stdout

    assert 'Sonarr' in html


def test_firewall(host):
    i = host.iptables

    assert (
        '-A INPUT -p tcp -m tcp --dport 80 '
        '-m conntrack --ctstate NEW,ESTABLISHED '
        '-m comment --comment "Allow HTTP traffic" -j ACCEPT'
    ) in i.rules('filter', 'INPUT')
    assert (
        '-A OUTPUT -p tcp -m tcp --sport 80 '
        '-m conntrack --ctstate ESTABLISHED '
        '-m comment --comment "Allow HTTP traffic" -j ACCEPT'
    ) in i.rules('filter', 'OUTPUT')


def test_mono_repo(host):
    f = host.file("/etc/apt/sources.list.d/mono-official-stable.list")

    f.exists


def test_mediaarea_repo(host):
    f = host.file("/etc/apt/sources.list.d/mediaarea.list")

    f.exists
