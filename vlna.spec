%define name vlna
%define version 1.4
%define release %mkrel 2

Summary: Add the \nobreak by Czech typesetting conventions
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://math.feld.cvut.cz/pub/olsak/vlna/%{name}-%{version}.tar.gz
License: GPLv2
Group: Text tools
Url: http://petr.olsak.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
Program vlna adds ties (Czech vlna or vlnka) after nonsyllabic prepositions
(instead of spaces) in the TeX source files. This prevents line breaks
at undesirable spaces.


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
%doc ChangeLog  README README.en vlna.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Wed Dec 08 2010 Funda Wang <fwang@mandriva.org> 1.4-2mdv2011.0
+ Revision: 615970
- update file list

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri Jan 08 2010 Peťoš Šafařík <petos@mandriva.org> 1.4-1mdv2010.1
+ Revision: 487815
- Documentation added: README in Czech (autors native) and English and manual (vlna.txt)
- Description in SPEC updated
- import vlna


