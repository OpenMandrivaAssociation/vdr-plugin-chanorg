
%define plugin	chanorg
%define name	vdr-plugin-%plugin
%define version	0.0.6
%define rel	13

Summary:	VDR plugin: Channels Organizer
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.freewebs.com/sadhome/
Source:		http://www.freewebs.com/sadhome/Plugin/Channelswitcher/vdr-%plugin-%version.tar.bz2
Patch1:		http://deela.cc.fh-lippe.de/files/vdr-chanorg/chanorg-0.0.6.patch
Patch2:		03_chanorg-0.0.6_fix-EbS-crash.dpatch
Patch3:		chanorg-0.0.6-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
With this plugin one can edit the channels.conf file via OSD.

%prep
%setup -q -n %plugin-%version
%patch1 -p1 -b .p
%patch2 -p1
%patch3 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


