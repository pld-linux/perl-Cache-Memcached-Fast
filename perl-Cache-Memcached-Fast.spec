#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Cache
%define	pnam	Memcached-Fast
Summary:	Cache::Memcached::Fast - Perl client for memcached, in C language
#Summary(pl):	
Name:		perl-Cache-Memcached-Fast
Version:	0.06
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0a2b27f9910bf720f085fc5a2952f75c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cache::Memcahced::Fast is a Perl client for memcached, a memory
cache daemon (http://www.danga.com/memcached/).  Module core is
implemented in C and tries hard to minimize number of system calls and
to avoid any key/value copying for speed.  As a result, it has very
low CPU consumption.

API is largely compatible with Cache::Memcached,
original pure Perl client, most users of the original module may start
using this module by installing it and adding "::Fast" to the old
name in their scripts (see /"Compatibility with Cache::Memcached"
below for full details).




# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Cache/Memcached/*.pm
%dir %{perl_vendorarch}/auto/Cache/Memcached/Fast
%{perl_vendorarch}/auto/Cache/Memcached/Fast/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Cache/Memcached/Fast/*.so
%{_mandir}/man3/*
