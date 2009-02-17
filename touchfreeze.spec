Summary:	Tray applet that disables touchpad automatically while you are typing text
Name:		touchfreeze
Version:	0.2.3
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://qsynaptics.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	819d382dd176e5b14eafc5f1633601ad
URL:		http://qsynaptics.sourceforge.net/
BuildRequires:	QtCore-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	xorg-driver-input-synaptics
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Annoyed when you are typing a document and accidentally the palm of
your hand brushes the touchpad, changing the position of the cursor in
your document or accidentally clicking on an option. TouchFreeze is
simple utility that solves this problem. It automatically disables
touchpad while you are typing text.

%prep
%setup -q

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install touchfreeze $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/touchfreeze
