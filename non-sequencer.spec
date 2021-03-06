%global snapshot 20120415
%global git 3a7d924
Name:		non-sequencer
Version:	1.9.4
Release:	1.%{snapshot}git%{git}%{?dist}
Summary:	A powerful, real-time, pattern-based MIDI sequencer	

Group:		Applications/Multimedia
License:	GPLv2+
URL:		http://non-sequencer.tuxfamily.org/
# The source for this package was pulled from upstream's VCS  Use the
# following commands to generate the tarball:
# git clone git://git.tuxfamily.org/gitroot/non/sequencer.git
# cd sequencer
# git checkout 3a7d924
# tar cjvf non-sequencer-20120415git3a7d924.tar.bz2 sequencer/ --exclude=.git*
Source0:	non-sequencer-%{snapshot}git%{git}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	fltk-devel 
BuildRequires:	fltk-fluid
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsigc++20-devel 
#BuildRequires:	cmake 
#BuildRequires:	lash-devel 
#BuildRequires:	git 
BuildRequires:	libpng-devel 
BuildRequires:	libjpeg-devel
BuildRequires:	liblo-devel
BuildRequires:	libXpm-devel

%description

The Non Sequencer is a powerful real-time, pattern-based MIDI
sequencer for Linux-released under the GPL. Filling the void left by
countless DAWs, piano-roll editors, and other purely performance based
solutions, it is a composition tool-one that transforms MIDI
music-making on Linux from a complex nightmare into a pleasurable,
efficient, and streamlined process.

%prep
%setup -q -n sequencer

sed -i '/^ifneq (\$(USE_DEBUG),yes)/,+4 d' Makefile

%build
%configure
 
make VERBOSE=1 SYSTEM_PATH=%{_datadir} DOCUMENT_PATH=%{_defaultdocdir}/%{name}-%{version}/doc/ %{?_smp_mflags}  


%install
rm -rf %{buildroot}
sed -i "/\.html/d" Makefile
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/non-sequencer
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/instruments/*
%{_datadir}/applications/%{name}.desktop
#TODO: clean up all the different generated icon versions?
%{_datadir}/icons/hicolor/*
%{_datadir}/pixmaps/%{name}/icon-256x256.png

%doc COPYING doc/



%changelog
* Sun Apr 15 2012 Adam Huffman <verdurin@fedoraproject.org> - 1.9.4-1.20120415git%{git}%{?dist}
- update to new upstream release 1.9.4
- add missing icon entries to files
- add BR for liblo and libXpm
- remove LASH BR and configure entry, following removal upstream

* Fri Apr  2 2010 Adam Huffman <bloch@verdurin.com> - 1.9.3-4.20100131git%{git}%{?dist}
- move docs back to main package
- fix build and install to ensure docs available at runtime

* Tue Mar 30 2010 Adam Huffman <bloch@verdurin.com> - 1.9.3-3.20100131gitba94d2c354145
- fix doc duplication

* Tue Mar 30 2010 Adam Huffman <bloch@verdurin.com> - 1.9.3-2.20100131gitba94d2c354145
- fix licence
- add TODO.mu
- ensure .debuginfo builds
- moves docs to -doc subpackage

* Sat Mar 13 2010 Adam Huffman <bloch@verdurin.com> - 1.9.3-1.20100131gitba94d2c354145
- fix version and source

* Tue Mar  9 2010 Adam Huffman <bloch@verdurin.com> - 0.0-1.20100131gitba94d2c354145
- fix CMake build and add more BR

* Sun Jan 31 2010 Adam Huffman <bloch@verdurin.com> - 0.0-0.20100131gitba94d2c354145
- initial version based on 20100131 snapshot

