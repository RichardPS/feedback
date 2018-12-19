# encoding: utf-8
# -*- mode: ruby -*-
# vi: set ft=ruby :

VM_NAME = "cuckoo"
VAGRANT_BOX = "ubuntu/cosmic64"
SYNC_FOLDER = "/home/vagrant/" + VM_NAME

# Project specific script
PROVISIONING_SCRIPT = <<EOF
  apt-get update
  apt-get install -y git
  apt-get install -y \
    build-essential \
    ifupdown \
    postgresql postgresql-contrib \
    libjpeg-turbo8 libjpeg-turbo8-dev libfreetype6 libfreetype6-dev zlib1g-dev
  update-rc.d postgresql enable
  service postgresql start
  apt-get -y \
    install python-dev \
    postgresql-server-dev-all \
    python-pip python3-pip python3-venv
  apt-get update
  apt-get upgrade -y
  apt-get autoremove -y
EOF


VIRTUALENV_SCRIPT = <<EOF
  python3 -m venv .venv
  cp #{VM_NAME}/etc/.profile .
EOF

Vagrant.configure("2") do |config|
  required_plugins = %w( vagrant-notify-forwarder )
  required_plugins.each do |plugin|
      exec "vagrant plugin install #{plugin};vagrant #{ARGV.join(" ")}" unless Vagrant.has_plugin? plugin || ARGV[0] == 'plugin'
  end

  config.vm.hostname = VM_NAME + "-vagrant"
  config.vm.box = VAGRANT_BOX

  config.vm.network "forwarded_port", guest: 8000, host: 8121
  config.vm.network "forwarded_port", guest: 3000, host: 3000
  config.vm.network "private_network", type: "dhcp"
  config.vm.synced_folder ".", SYNC_FOLDER, id: "vagrant-root", :nfs => true

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
    vb.customize ["modifyvm", :id, "--cpus", "2"]
    vb.customize ["modifyvm", :id, "--hwvirtex", "on"]
    vb.customize ["modifyvm", :id, "--audio", "none"]
    vb.customize ["modifyvm", :id, "--ioapic", "on"]
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end

  config.ssh.shell = "bash"
  config.ssh.forward_agent = true

  config.vm.base_mac = ""

  config.vm.provision "provisioning", type: "shell", inline: PROVISIONING_SCRIPT
  config.vm.provision "virtualenv", type: "shell", privileged: false, inline: VIRTUALENV_SCRIPT
end
