
%define realname   Alien-GvaScript
%define version    1.11
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Gva extension to the prototype javascript framework
Source:     http://www.cpan.org/modules/by-module/Alien/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Path)
BuildRequires: perl(Pod::POM)
BuildRequires: perl(Pod::POM::View)
BuildRequires: perl(Pod::POM::View::HTML)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
GvaScript (pronounce "gee-vascript") is a javascript framework born in
Geneva, Switzerland (GVA is the IATA code for Geneva Cointrin
International Airport).

It is built on top of the prototype object-oriented javascript framework
(http://prototype.conio.net) and offers a number of extensions and
widgets, such as keymap handling, application-specific events,
autocompletion on input field, tree navigation, and forms with autofocus
and repeated sections. These functionalities are described in separate
documentation pages (see Alien::GvaScript::Intro).

GvaScript is distributed using Perl tools, but the actual content of the
library is pure javascript; hence its location in the Alien namespace
(see the Alien manifesto).

GvaScript runtime library does not need Perl; you can integrate it in
any other Web programming framework. Perl is only needed for developers
who want to modify GvaScript sources and recreate a distribution
package.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install --destdir %buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*

