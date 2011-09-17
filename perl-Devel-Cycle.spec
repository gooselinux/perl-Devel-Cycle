Name:           perl-Devel-Cycle
Version:        1.10
Release:        3.1%{?dist}
Summary:        Find memory cycles in objects
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-Cycle/
Source0:        http://www.cpan.org/authors/id/L/LD/LDS/Devel-Cycle-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(PadWalker) >= 1.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(PadWalker) >= 1.0

%description
This is a simple developer's tool for finding circular references in
objects and other types of references. Because of Perl's reference-count
based memory management, circular references will cause memory leaks.

%prep
%setup -q -n Devel-Cycle-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 1.10-3.1
- Rebuilt for RHEL 6
Related: rhbz#566527

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Steven Pritchard <steve@kspei.com> 1.10-1
- Update to 1.10.

* Thu May 15 2008 Steven Pritchard <steve@kspei.com> 1.09-1
- Update to 1.09.
- Reformat to match cpanspec output.
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-3
- Rebuild for perl 5.10 (again)

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-2
- rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-1.2
- add BR: perl(Test::More)

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-1.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Wed May 24 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.07-1
- Update to 1.07.
- Requirement version: perl(PadWalker) >= 1.0.

* Mon May 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-1
- Update to 1.05.
- New requirement: perl(PadWalker).

* Thu Feb 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.04-4
- Rebuild for FC5 (perl 5.8.8).

* Sat May 14 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.04-3
- Add dist tag.

* Mon May 02 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.04-2
- Update to 1.04.

* Fri Apr 22 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.03-2
- Fedora Extras: FC-4 version.

* Mon Jan 24 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.03-0.fdr.1
- Update to 1.03.

* Sun Jul 04 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.02-0.fdr.1
- First build.
