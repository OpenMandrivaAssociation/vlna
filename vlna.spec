%define name vlna
%define version 1.4
%define release %mkrel 1

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
%{_mandir}/man1/%{name}.1.lzma
