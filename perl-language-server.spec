%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}

Name:           perl-language-server
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Language Server and Debug Protocol Adapter for Perl

License:        GPLv2+ or Artistic
URL:            https://metacpan.org/release/Getopt-Long
#Source0:

BuildRequires:  make git
BuildRequires:  perl

%description
Language Server and Debug Protocol Adapter for Perl

%prep
git clone --depth=1 https://github.com/richterger/Perl-LanguageServer

%build
cd Perl-LanguageServer/
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
cd Perl-LanguageServer/
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog