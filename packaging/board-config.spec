Name:           renesas_rcar-board-config
Version:        1.0.0
Release:	0
License:	MIT
Summary:	Board dependent config files
Source:       %{name}-%{version}.tar.gz
BuildRequires:  make

%description
This package contains the board dependent configuration files that are
not included as part of other packages.  

%prep
%setup

%install
%make_install

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_localstatedir}/*
