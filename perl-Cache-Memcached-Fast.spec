#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Cache
%define	pnam	Memcached-Fast
Summary:	Cache::Memcached::Fast - Perl client for memcached, in C language
Summary(pl.UTF-8):	Cache::Memcached::Fast - perlowy klient memcached napisany w C
Name:		perl-Cache-Memcached-Fast
Version:	0.19
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Cache/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b1d7b4e7efc692804df559f494ac0fe7
URL:		http://search.cpan.org/dist/Cache-Memcached-Fast/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cache::Memcached::Fast is a Perl client for memcached, a memory
cache daemon (http://www.danga.com/memcached/). Module core is
implemented in C and tries hard to minimize number of system calls and
to avoid any key/value copying for speed. As a result, it has very
low CPU consumption.

API is largely compatible with Cache::Memcached, original pure Perl
client, most users of the original module may start using this module
by installing it and adding "::Fast" to the old name in their scripts.

%description -l pl.UTF-8
Cache::Memcached::Fast to perlowy klient memcached - demona pamięci
podręcznej (http://www.danga.com/memcached/). Główna część modułu jest
zaimplementowana w C i usiłuje zminimalizować liczbę wywołań
systemowych i zapobiegać kopiowaniu kluczy/wartości. W efekcie ma
bardzo małe zużycie procesora.

API jest w dużej części kompatybilne z Cache::Memcached - oryginalnym
kliencie w czystym Perlu; większość użytkowników oryginalnego modułu
może zacząć używać tego modułu poprzez zainstalowanie go i dodanie
"::Fast" do starej nazwy w skryptach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Cache/Memcached/Fast/*.so
%{_mandir}/man3/*
