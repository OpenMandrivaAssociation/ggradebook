%define name	ggradebook
%define version 0.91
%define release %mkrel 4

Summary:	The GNU teacher's gradebook
Name:		%{name}
Version:	%{version}
Release:	%{release}

Source:		%{name}-%{version}.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
URL:		http://www.gnu.org/software/ggradebook/
License:	GPL
Group:		Office
BuildRequires:	libgnome-devel

%description
Ggradebook is the fully-featured GNU gradebook, an application for tracking
student grades for teachers. It uses GTK+ and can optionally be compiled to
use GNOME.
                                                                                               
%prep
%setup -q -n Ggradebook-%version

%build
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#mdk menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="GNU Gradebook" longtitle="Teacher's gradebook" section="Office/Accessories" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Teacher's gradebook
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Office-Accessories;Office;Utility
Encoding=UTF-8
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png
 
%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/%name
%_datadir/Ggradebook
%{_datadir}/applications/mandriva-%{name}.desktop
%_menudir/%name
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png

