%define upstream_name    Alien-GvaScript
%define upstream_version 1.43

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Gva extension to the prototype javascript framework
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Alien/Alien-GvaScript-%{upstream_version}.tar.gz

BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Path)
BuildRequires: perl(Pod::POM)
BuildRequires: perl(Pod::POM::View)
BuildRequires: perl(Pod::POM::View::HTML)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)
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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install --destdir %buildroot

%clean

%files
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.220.0-2mdv2011.0
+ Revision: 658563
- add br
- rebuild for updated spec-helper

* Thu Jul 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.220.0-1mdv2011.0
+ Revision: 553571
- update to 1.22

* Mon Jan 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.210.0-1mdv2010.1
+ Revision: 492948
- update to 1.21

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.180.0-1mdv2010.1
+ Revision: 460779
- update to 1.18

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.0
+ Revision: 401789
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.11-2mdv2010.0
+ Revision: 375969
- rebuild

* Tue Mar 31 2009 Jérôme Quelin <jquelin@mandriva.org> 1.11-1mdv2009.1
+ Revision: 362901
- import perl-Alien-GvaScript


* Tue Mar 31 2009 jquelin 1.11-1mdv
- initial mdv release



