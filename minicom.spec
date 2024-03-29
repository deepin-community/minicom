Summary:	TTY mode communications package ala Telix
Summary(de):	TTY-Modus-Kommunikationspaket (�hnlich Telix)
Summary(fi):	Tietoliikenneohjelma, kuten Telix
Summary(fr):	Package de communication en mode terminal � la Telix
Summary(pl):	Program komunikacyjny (podobny do Telix-a)
Summary(tr):	Telix benzeri, TTY kipi ileti�im paketi
Name:		minicom
Version:	2.8
Release:	1
Copyright:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
URL:		https://salsa.debian.org/minicom-team/minicom
Packager:	Daniel Tschan <tschan+rpm@devzone.ch>
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-root

%description
Minicom is a communications program that resembles the MSDOS Telix
somewhat. It has a dialing directory, color, full ANSI and VT100
emulation, an (external) scripting language and more.

Run 'minicom -s' as root to create a system wide configuration.
Users need read/write permissions on the serial port devices in
order to use minicom.

It's recommended to install lrzsz if you want to transfer files
with minicom.

%description -l de
Minicom ist ein Kommunikationsprogramm, das �hnlichkeiten mit Telix 
unter MSDOS aufweist. Es enth�lt ein W�hlverzeichnis, Farbe, vollst�ndige ANSI-
und VT100-Emulation, eine (externe) Scriptsprache usw.

%description -l fi
Minicom on MSDOS-Telixi� jossain m��rin muistuttava tietoliikenneohjelma.
Ohjelmassa on mm. puhelinluettelo, v�rit, ANSI- ja VT100-emulaatiot
ja ulkoinen script-kieli.

%description -l fr
Minicom est un programme de communication ressemblant � Telix sous
MSDOS. Il poss�de un r�pertoire de num�rotation, un affichage en couleurs, 
des �mulations ANSI et VT100, un langage de script externe...

%description -l pl
Minicom jest programem komunikacyjnym, przypominaj�cym DOSowy program
Telix. Posiada ksi��k� telefoniczn�, emulacj� terminali ANSI i VT100,
zewn�trzny j�zyk skryptowy, obs�ug� kolor�w i wiele innych zalet.

%description -l tr
Minicom, MSDOS Telix program�na benzeyen bir ileti�im program�d�r. Numara
�evirme dizini, renk, tam ANSI uyumu ve VT100 �yk�n�m� ile script gibi
�zellikleri vard�r.

%prep
%setup -q

%build
%configure
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT/etc

%find_lang %name

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc doc/*
%attr(755,root,root) %{_bindir}/minicom
%{_bindir}/runscript
%{_bindir}/xminicom
%{_bindir}/ascii-xfr
%{_mandir}/man1/*

%changelog
* Mon Jun 23 2003 Daniel Tschan <tschan+rpm@devzone.ch>
- updated to minicom 2.1
- rewrote spec file with the help of Martin Godisch <martin@godisch.de>

Revision 1.8  2002/05/18 13:35:44  walker
Changed my netmail address, and changed the version number to 2.00.1.

Revision 1.7  2001/12/21 19:09:19  walker
Changed the Finnish locale from fi_FI to fi. Updated the instructions for
adding new languages in doc/Locales to match the procedure with autoconf.

Revision 1.6  2001/05/25 14:39:21  walker
added Finnish description, removed lang(ko) and added lang(ru)

Revision 1.5  2000/06/16 09:27:23  misiek
- unify my email

Revision 1.4  2000/03/27 00:29:37  gael
- LINGUAS has to be unset to make rpm work
- replaced --sysconf by --sysconfdir for %configure

Revision 1.3  2000/02/09 22:37:28  gael
- fixed typos in French description

Revision 1.2  2000/01/03 13:22:54  misiek
- fixed Japanese locale

Revision 1.1  1999/12/20 12:22:50  misiek
- first try to `make rpm'

Revision 1.15  1999/07/20 11:04:34  baggins
- fixed usage of macros
- added/removed neccesary/obsolete patches
- FHS 2.0 compliance where needed
- gzipping docs where needed

Revision 1.14  1999/07/12 23:06:10  kloczek

- added using CVS keywords in %changelog (for automating them).


* Tue Jun 29 1999 Michal Margula <alchemyx@pld.org.pl>
  [1.82.1-3]
- fixed for compiling with ncurses
- FHS 2.0 ready
- minor fixes in spec

* Wed Feb 03 1999 Arkadiusz Mi�kiewicz <misiek@pld.org.pl>
  [1.82.1-1d]
- new upstream release

* Mon Jan 11 1999 Arkadiusz Mi�kiewicz <misiek@pld.org.pl>
  [1.82-3d]
- added 1.82.1 pre patch ;>
- updated pl translation in this patch

* Thu Dec 24 1998 Arkadiusz Mi�kiewicz <misiek@pld.org.pl>
  [1.82-2d]
- added defaul initstring,
- added /etc/profile.d/minicom.sh,
- added uninitialized patch.

* Sat Oct 10 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [1.82-1d]
- translations modified for pl,
- updated to 1.82.
- defined files permission,
- allow building from non root account,
- moved changelog to the end of spec.

* Tue Jun 30 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.81-7d]
- build against GNU libc-2.1.

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- security fixes (alan cox, but he forgot about the changelog)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- BuildRoot; updated .make patch to cope with the buildroot
- fixed the spec file

* Tue May 06 1998 Michael Maher <mike@redhat.com>
- update of package (1.81)

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed source url

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
