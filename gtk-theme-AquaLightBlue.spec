%define		_theme	AquaLightBlue

Summary:	Aqua Light Blue theme
Summary(pl):	Temat Aqua Light Blue
Name:		gtk-theme-%{_theme}
Version:	1.2.x
Release:	1
License:	GPL
Group:		Themes/Gtk
Source0:	http://download.freshmeat.net/themes/aqualightblue/aqualightblue-1.2.x.tar.gz
URL:		http://themes.freshmeat.net/projects/aqualightblue/
Requires:	gtk-engines
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
MacOS-like theme.

%description -l pl
Temat przypominaj±cy MacOS.

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
