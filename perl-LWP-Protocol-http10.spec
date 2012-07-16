# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	LWP
%define		pnam	Protocol-http10
%include	/usr/lib/rpm/macros.perl
Summary:	LWP::Protocol::http10 - Legacy HTTP/1.0 support for LWP
#Summary(pl.UTF-8):	
Name:		perl-LWP-Protocol-http10
Version:	6.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/LWP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c3d2f6efc2ce06066cf95a24fed6fff1
# add this for completeness, resurrected from libwww sources
# http://cpansearch.perl.org/src/GAAS/libwww-perl-6.01/lib/LWP/Protocol/https10.pm
Source1:	https10.pm
URL:		http://search.cpan.org/dist/LWP-Protocol-http10/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LWP::Protocol::http10 module provide support for using HTTP/1.0
protocol with LWP.  To use it you need to call
LWP::Protocol::implementor() to override the standard handler for
http URLs.

This module used to be bundled with the libwww-perl, but it was
unbundled in v6.02 as part of the general cleanup for the 6-series.
LWP::Protocol::http10 is deprecated.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{perl_vendorlib}/LWP/Protocol

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/LWP/Protocol/http10.pm
%{perl_vendorlib}/LWP/Protocol/https10.pm
%{_mandir}/man3/*

%changelog
