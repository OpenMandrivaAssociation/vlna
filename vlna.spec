%define name vlna
%define version 1.4
%define release %mkrel 1

Summary: Vlna makes tildaes into TeX a LaTeX source codes
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://math.feld.cvut.cz/pub/olsak/vlna/%{name}-%{version}.tar.gz
License: GPL
Group: Text tools
Url: http://petr.olsak.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
Program vlna replaces spaces via tildaes (~) into non-breakable places (ie in Czech language).

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.lzma

