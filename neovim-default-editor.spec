Name:           neovim-default-editor
Version:        0.11.1
Release:        1%{?dist}
Summary:        Set neovim as the default editor

License:        MIT
URL:            https://neovim.io
Source0:        https://github.com/skoved/neovim-default-editor-rpm/archive/refs/heads/main.tar.gz

Conflicts:      system-default-editor
Provides:       system-default-editor
Requires:       neovim

BuildArch:      noarch

%description
This package contains files needed to set Neovim as the default editor.

%prep
%autosetup

%build

%install
mkdir   -p       %{buildroot}/%{_sysconfdir}/profile.d
install -p -m644 nvim-default-editor.sh   %{buildroot}/%{_sysconfdir}/profile.d/nvim-default-editor.sh
install -p -m644 nvim-default-editor.csh  %{buildroot}/%{_sysconfdir}/profile.d/nvim-default-editor.csh
mkdir   -p       %{buildroot}/%{_datadir}/fish/vendor_conf.d
install -p -m644 nvim-default-editor.fish %{buildroot}/%{_datadir}/fish/vendor_conf.d/nvim-default-editor.fish

%files
%license LICENSE
%doc     README.md
%dir     %{_datadir}/fish/vendor_conf.d
%{_datadir}/fish/vendor_conf.d/nvim-default-editor.fish
%config  %{_sysconfdir}/profile.d/nvim-default-editor.sh
%config  %{_sysconfdir}/profile.d/nvim-default-editor.csh


%changelog
%autochangelog
