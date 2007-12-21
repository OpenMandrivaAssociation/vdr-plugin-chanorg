
%define plugin	chanorg
%define name	vdr-plugin-%plugin
%define version	0.0.6
%define rel	11

Summary:	VDR plugin: Channels Organizer
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.freewebs.com/sadhome/
Source:		http://www.freewebs.com/sadhome/Plugin/Channelswitcher/vdr-%plugin-%version.tar.bz2
Patch1:		http://deela.cc.fh-lippe.de/files/vdr-chanorg/chanorg-0.0.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
With this plugin one can edit the channels.conf file via OSD.

%prep
%setup -q -n %plugin-%version
%patch1 -p1 -b .p

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


