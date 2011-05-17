%define	fontname	Inconsolata
%define name		fonts-ttf-%{fontname}
%define version		1.010
%define	release		%mkrel 5

%define fontdir		%{_datadir}/fonts/TTF/%{fontname}
%define fontconfdir 	%{_sysconfdir}/X11/fontpath.d

Summary:		Inconsolata monospace font
Name:			%{name}
Version:		%{version}
Release: 		%{release}
License:		OFL
Group:			System/Fonts/True type
URL:			http://www.levien.com/type/myfonts/inconsolata.html
Source0:		http://www.levien.com/type/myfonts/Inconsolata.otf
Source1:		OFL.txt
Source2:		OFL-FAQ.txt
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:		noarch
BuildRequires: fontconfig

%description
A monospace font designed by Ralph Levien for code listings and the like in print.

%prep
cp %{SOURCE1} %{SOURCE2} .

%install
%__rm -fr %{buildroot}

%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 -p %{SOURCE0} %{buildroot}%{fontdir}
ttmkfdir %{buildroot}%{fontdir} > %{buildroot}%{fontdir}/fonts.dir
ln -s fonts.dir %{buildroot}%{fontdir}/fonts.scale

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/ttf-%{fontname}:pri=50

%clean
%__rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc OFL*
%dir %{fontdir}
%{fontdir}/*.otf
%{fontdir}/fonts.*
%{fontconfdir}/*
