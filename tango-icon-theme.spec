%define extraname tango-icon-theme-extras
%define extraversion 0.1.0

Summary:	Tango icon theme
Name:		tango-icon-theme
Version:	0.8.90
Release:	6
License:	Public Domain
Group:		Graphical desktop/Other
URL:		https://tango.freedesktop.org/Tango_Icon_Library#Download
Source0:	http://tango.freedesktop.org/releases/%{name}-%{version}.tar.bz2
Source1:	http://tango.freedesktop.org/releases/%{extraname}-%{extraversion}.tar.bz2
# http://www.gnome-look.org/content/show.php?content=41229
Source2:	tango_addon-0.5b.tar.bz2
Source3:	tango-icon-theme-xfce.tar.bz2
BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:	imagemagick
BuildRequires:	imagemagick-devel
BuildRequires:	icon-naming-utils >= 0.8.90
Requires(post):	gtk+2.0
Requires(postun):	gtk+2.0
Provides:	tango-icon-theme-kde = %{version}-%{release}
Obsoletes:	tango-icon-theme-kde < %{version}-%{release}

%description
This is an icon theme that follows the Tango visual guidelines.
It bundles with the extra icon set and additional Mandriva icons.

%prep
%setup -q -a 1 -a 2 -a 3
cp %extraname-%extraversion/README README.extra
cp %extraname-%extraversion/AUTHORS AUTHORS.extra
cp %extraname-%extraversion/ChangeLog ChangeLog.extra
mv "tango addon" tango_addon
chmod 644 tango_addon/readme.txt
rm tango_addon/apps/gtk-close.svg

%build
./configure --prefix=%_prefix
%make
cd %extraname-%extraversion
./configure --prefix=%_prefix
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
cd %extraname-%extraversion
%makeinstall_std
cd ../tango_addon
install -m 644 apps/* %buildroot%_datadir/icons/Tango/scalable/apps
install -m 644 categories/* %buildroot%_datadir/icons/Tango/scalable/categories

cd ../tango-icon-theme-xfce
install -m 644 scalable/apps/* %buildroot%_datadir/icons/Tango/scalable/apps

touch %buildroot%_datadir/icons/Tango/icon-theme.cache

ln -s mozilla-firefox.svg %{buildroot}%{_iconsdir}/Tango/scalable/apps/firefox.svg

%files
%defattr(-,root,root,-)
%doc README* AUTHORS* ChangeLog* COPYING
%doc tango_addon/readme.txt
%dir %_datadir/icons/Tango/
%_datadir/icons/Tango/index.theme
%_datadir/icons/Tango/16x16
%_datadir/icons/Tango/22x22
%_datadir/icons/Tango/24x24
%_datadir/icons/Tango/32x32
%_datadir/icons/Tango/scalable
%ghost %_datadir/icons/Tango/icon-theme.cache


%changelog
* Thu Sep 22 2011 Götz Waschk <waschk@mandriva.org> 0.8.90-4mdv2012.0
+ Revision: 700802
- rebuild

* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.90-3mdv2011.0
+ Revision: 445387
- Add firefox.svg because the icon was renamed in firefox packages too
  (bug #53214)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Mar 04 2009 Götz Waschk <waschk@mandriva.org> 0.8.90-1mdv2009.1
+ Revision: 348238
- new version
- update license
- update build deps

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Sep 08 2008 Götz Waschk <waschk@mandriva.org> 0.8.1-6mdv2009.0
+ Revision: 282486
- drop kde package
- update URL
- update build deps

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.8.1-5mdv2009.0
+ Revision: 261374
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.8.1-4mdv2009.0
+ Revision: 254111
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Dec 13 2007 Jérôme Soyer <saispo@mandriva.org> 0.8.1-2mdv2008.1
+ Revision: 119414
- Add Xfce enhancements

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 0.8.1-1mdv2008.0
+ Revision: 72562
- new version


* Wed Feb 28 2007 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdv2007.0
+ Revision: 126862
- new version
- bump deps
- Import tango-icon-theme

* Sat Sep 02 2006 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2007.0
- rebuild for new clean_icon_cache macro

* Thu Aug 31 2006 Götz Waschk <waschk@mandriva.org> 0.7.2-6mdv2007.0
- fix uninstallation

* Wed Aug 30 2006 Götz Waschk <waschk@mandriva.org> 0.7.2-5mdv2007.0
- update tango addon
- remove big red close icon
- fix buildrequires

* Thu Jul 27 2006 Götz Waschk <waschk@mandriva.org> 0.7.2-4mdv2007.0
- fix uninstallation

* Thu Jul 27 2006 Götz Waschk <waschk@mandriva.org> 0.7.2-3mdv2007.0
- add png icons for KDE

* Thu Jul 27 2006 Götz Waschk <waschk@mandriva.org> 0.7.2-2mdv2007.0
- add extra icons
- fix buildrequires

* Thu Jul 27 2006 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2007.0
- initial package

