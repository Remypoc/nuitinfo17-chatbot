VAGRANT_FILE_API_VERSION = '1.0.0'

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.hostname = "psi"
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.provider :virtualbox do |vb|
        vb.name = "react-template-virtual-machine"
        vb.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/v-root", "1"]
        vb.memory = "2048"
        vb.cpus = "2"
  end
  config.vm.provision 'shell', path: 'scripts/install.sh'
end