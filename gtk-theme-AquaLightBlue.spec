%define		_theme	AquaLightBlue

Summary:	Aqua Light Blue theme
Summary(pl):	Motyw Aqua Light Blue
Name:		gtk-theme-%{_theme}
Version:	1.2.x
Release:	2
License:	GPL
Group:		Themes/GTK+
Source0:	http://download.freshmeat.net/themes/aqualightblue/aqualightblue-1.2.x.tar.gz
# Source0-md5:	3243a5c9c500caef74e7f236487a2bf8
URL:		http://themes.freshmeat.net/projects/aqualightblue/
Requires:	gtk-engines
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MacOS-like theme.

%description -l pl
Motyw przypominaj±cy MacOS.

%prep
%setup  -q -n %{_theme}

%build
rm -f missing

%install
rm -rf $RPM_BUILD_ROOT

install -d "$RPM_BUILD_ROOT%{_datadir}/themes/%{_theme}"

cp -pR * $RPM_BUILD_ROOT%{_datadir}/themes/%{_theme}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/themes/%{_theme}
%{_datadir}/themes/%{_theme}/*
