%define extraname tango-icon-theme-extras
%define extraversion 0.1.0

Summary: Tango icon theme
Name: tango-icon-theme
Version: 0.8.1
Release: %mkrel 6
License: Creative Commons Attribution-ShareAlike 2.5
Group: Graphical desktop/Other
URL: http://tango.freedesktop.org/Tango_Icon_Library#Download
Source0: http://tango.freedesktop.org/releases/%{name}-%{version}.tar.bz2
Source1: http://tango.freedesktop.org/releases/%{extraname}-%{extraversion}.tar.bz2
# http://www.gnome-look.org/content/show.php?content=41229
Source2: tango_addon-0.5b.tar.bz2
Source3: tango-icon-theme-xfce.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: intltool
BuildRequires: ImageMagick ImageMagick-devel
BuildRequires: icon-naming-utils >= 0.8.2
Requires(post): gtk+2.0
Requires(postun): gtk+2.0
Provides: tango-icon-theme-kde
Obsoletes: tango-icon-theme-kde

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

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache Tango

%postun
%clean_icon_cache Tango

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
