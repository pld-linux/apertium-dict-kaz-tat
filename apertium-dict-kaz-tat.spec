Summary:	Kazakh-Tatar language pair for Apertium
Summary(pl.UTF-8):	Para języków kazaski-tatarski dla Apertium
%define	lpair	kaz-tat
Name:		apertium-dict-%{lpair}
Version:	0.2.1
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	e7c61df877d3a5d9362f84732843297d
Patch0:		%{name}-hfst-fix.patch
URL:		http://www.apertium.org/
BuildRequires:	apertium-devel >= 3.2.0
BuildRequires:	apertium-lex-tools
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	hfst
BuildRequires:	libxslt-progs
BuildRequires:	lttoolbox >= 3.2.0
BuildRequires:	vislcg3 >= 0.9.7.5129
BuildRequires:	pkgconfig
Requires:	apertium >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apertium language pair, which can be used for translating
between Kazakh and Tatar, morphological analysis or part-of-speech
tagging of both languages.

%description -l pl.UTF-8
Ten pakiet zawiera parę języków dla Apertium służącą do tłumaczenia
między kazaskim a tatarskim, a także analizy morfologicznej lub
oznaczania części mowy w obu językach.

%prep
%setup -q -n apertium-%{lpair}-%{version}
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/kaz-tat.mode
%{_datadir}/apertium/modes/tat-kaz.mode
