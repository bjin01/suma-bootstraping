#
# spec file for package suma-t-user
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global username suma-t

Name:           suma-t-user
Version:        1
Release:        0
Summary:	bootstraping user for suse manager
License:        (MIT or GPL-2.0) and LGPL-2.1+
Source: 	%{name}.tar.xz        
Requires(pre):  shadow

%description
nothing desc

%pre
getent passwd %{username} >/dev/null || \
    useradd -m %{username}

%prep
%setup -D -n .
    
%build

%install
mkdir -p %{buildroot}/etc/sudoers.d
mkdir -p %{buildroot}/home/%{username}/.ssh
mkdir -p %{buildroot}/admin/bin
install -m 440 suma-t %{buildroot}/etc/sudoers.d/%{name}
install -m 700 suma-bootstrap.sh %{buildroot}/admin/bin/suma-bootstrap.sh

%post
if getent passwd %{username}  > /dev/null 2>&1; then
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDGsgTRat8Fwp44p5JLwJyQiJCRpcJrmchMSqmIZKi6jlPHL5SnPGhIUin6D4mqEO/AZvBLAinjZv28ROJYLOfpgsp4jFAkPmDJv0tUWV8PAobggIEKK+7pbin5tjP4ePTd7Wvlui72U8jZ3YDJCPlzXHx8/BvAg2ehqwEMXonNM0kmQVR/e73oTyst1Kfj9QPJeNiZOudq2GlDWg9AClIr6W5vXulbOgIMAwigRr0U4zmV3N2C8e8XGwjJu7PypwOrliNTIBr53Zrghv8+UblHsn/WDxSTiLCj2/4cnMJHKFZ52iJgTilenQXCai+u5VN3Oygsv9FRL9PJ+W31RrCPH/nft2DDYuif4tqDTb5lxEKdh8/5WFpC9udjroRpKq6V8jP62UJlgoV9lcgJjL0z0Bz64lGMjvz+u+nZgen0Z/ERBHwyYU57MZmY0YmuN2fRmTX5NoXZ40TyIS7eyhpKJFIWc7NbHkoZgsCff2vSoOnBgGw02+byWekCTSv0kVM= test1@bjlx01" >> /home/%{username}/.ssh/authorized_keys
chown -R %{username}:users /home/%{username}/.ssh
chown %{username}:users /home/%{username}/.ssh/authorized_keys
fi

%files
%dir /etc/sudoers.d
/etc/sudoers.d/%{name}

%changelog
