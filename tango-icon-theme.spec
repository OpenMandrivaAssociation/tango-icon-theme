%define extraname tango-icon-theme-extras
%define extraversion 0.1.0

Summary: Tango icon theme
Name: tango-icon-theme
Version: 0.8.1
Release: %mkrel 2
License: Creative Commons Attribution-ShareAlike 2.5
Group: Graphical desktop/Other
URL: http://tango-project.org/Tango_Icon_Library#Download
Source0: http://tango-project.org/releases/%{name}-%{version}.tar.bz2
Source1: http://tango-project.org/releases/%{extraname}-%{extraversion}.tar.bz2
# http://www.gnome-look.org/content/show.php?content=41229
Source2: tango_addon-0.5b.tar.bz2
Source3: tango-icon-theme-xfce.tar.bz2
BuildArch: noarch
BuildRequires: perl-XML-Parser
BuildRequires: ImageMagick ImageMagick-devel
BuildRequires: icon-naming-utils >= 0.8.2
BuildRequires: librsvg librsvg-devel
Requires(post): gtk+2.0
Requires(postun): gtk+2.0

%description
This is an icon theme that follows the Tango visual guidelines.
It bundles with the extra icon set and additional Mandriva icons.

%package kde
Summary: Tango icon theme for KDE
Requires: %name = %version
Group: Graphical desktop/KDE

%description kde
This is an icon theme that follows the Tango visual guidelines.
It bundles with the extra icon set and additional Mandriva icons.

This contains the additional PNG image files that are required by KDE.

%prep
%setup -q -a 1 -a 2 -a 3
cp %extraname-%extraversion/README README.extra
cp %extraname-%extraversion/AUTHORS AUTHORS.extra
cp %extraname-%extraversion/ChangeLog ChangeLog.extra
mv "tango addon" tango_addon
chmod 644 tango_addon/readme.txt
rm tango_addon/apps/gtk-close.svg

%build
./configure --prefix=%_prefix --enable-png-creation
%make
cd %extraname-%extraversion
./configure --prefix=%_prefix --enable-png-creation
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
cd %extraname-%extraversion
%makeinstall_std
cd ../tango_addon
install -m 644 apps/* %buildroot%_datadir/icons/Tango/scalable/apps
install -m 644 categories/* %buildroot%_datadir/icons/Tango/scalable/categories
#manually create png files for Mandriva icons
for context in apps categories; do
  for i in 32 48 64 72 96 128; do
    pngdir=%buildroot%_datadir/icons/Tango/${i}x${i}/${context}
    mkdir -p $pngdir
    cd ${context}
    for icon in *; do
      ../../svg2png.sh $i $pngdir $icon
    done
    cd ..
  (cd $pngdir && %_prefix/lib/icon-name-mapping -c ${context})
  done
done

cd ../tango-icon-theme-xfce
install -m 644 scalable/apps/* %buildroot%_datadir/icons/Tango/scalable/apps

touch %buildroot%_datadir/icons/Tango/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache Tango

%postun
%clean_icon_cache Tango
%post kde
%update_icon_cache Tango

%postun kde
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
%_datadir/icons/Tango/scalable
%ghost %_datadir/icons/Tango/icon-theme.cache

%files kde
%defattr(-,root,root,-)
%doc README COPYING
%_datadir/icons/Tango/32x32
%_datadir/icons/Tango/48x48
%_datadir/icons/Tango/64x64
%_datadir/icons/Tango/72x72
%_datadir/icons/Tango/96x96
%_datadir/icons/Tango/128x128


