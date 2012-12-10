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
BuildRequires:		ttmkfdir
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


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.010-5mdv2011.0
+ Revision: 675788
- add br
- use upstream generated file
- br fontconfig for fc-query used in new rpm-setup-build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.010-4mdv2011.0
+ Revision: 610730
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.010-3mdv2010.1
+ Revision: 494142
- fc-cache is now called by an rpm filetrigger

* Wed May 06 2009 Lev Givon <lev@mandriva.org> 1.010-2mdv2010.0
+ Revision: 372617
- Fix font config path.

* Wed May 06 2009 Lev Givon <lev@mandriva.org> 1.010-1mdv2010.0
+ Revision: 372609
- imported package fonts-ttf-Inconsolata


