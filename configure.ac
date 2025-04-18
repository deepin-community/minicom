dnl $Id: configure.in,v 1.52 2009-11-16 21:06:05 al-guest Exp $
dnl configure.in autoconf/automake input script
dnl for minicom
dnl

AC_INIT([minicom],[2.10],[minicom-devel@lists.alioth.debian.org])
AC_CONFIG_SRCDIR([src/minicom.c])
AC_CONFIG_HEADERS([config.h])
AC_PREREQ([2.71])

AM_INIT_AUTOMAKE([1.7])

AC_USE_SYSTEM_EXTENSIONS

dnl Checks for programs.
AC_PROG_CC
AM_PROG_AR

AC_SYS_LARGEFILE

AC_USE_SYSTEM_EXTENSIONS
AC_USE_SYSTEM_EXTENSIONS

AC_PROG_INSTALL
dnl AC_PROG_LIBTOOL
AC_PROG_RANLIB

AC_SEARCH_LIBS([strerror],[cposix])
AM_ICONV_LINK

PKG_PROG_PKG_CONFIG

AC_ARG_ENABLE([lockdev],
        AS_HELP_STRING([--enable-lockdev],
                       [Enable lockdev support (def: enabled)]),
        [], [enable_lockdev="yes"])

if test -n "$PKG_CONFIG" && test "x$enable_lockdev" = xyes; then
	PKG_CHECK_MODULES([LOCKDEV], [lockdev], AC_DEFINE([HAVE_LOCKDEV],[1],[Define if you have lockdev]),[:])
fi

AC_ARG_ENABLE([lock-dir],
	AS_HELP_STRING([--enable-lock-dir=DIR],
	               [Set com line lock directory (def: try common locations)]),
	[], [enable_lock_dir="yes"])
if test "x$enable_lock_dir" = xyes; then
	UUCPLOCK=""
else
	if test "x$enable_lock_dir" = xno; then
		AC_MSG_ERROR(Lock directory required)
	else
		UUCPLOCK="$enable_lock_dir"
	fi
fi

AC_ARG_ENABLE([dfl-port],
	AS_HELP_STRING([--enable-dfl-port=DEVFILE],
	               [Set default /dev/.. modem device (def: try common locations)]),
	[], [enable_dfl_port="yes"])
if test "x$enable_dfl_port" = xyes; then
	DFL_PORT=""
else
	if test "x$enable_dfl_port" = xno; then
		AC_MSG_ERROR(Default port required)
	else
		DFL_PORT="$enable_dfl_port"
	fi
fi

AC_ARG_ENABLE([dfl-baud],
	AS_HELP_STRING([--enable-dfl-baud=NNNNN],
	               [Set default baud rate (def: 115200)]),
	[], [enable_dfl_baud="yes"])
if test "x$enable_dfl_baud" = xyes; then
	DEF_BAUD="115200"
else
	if test "x$enable_dfl_baud" = xno; then
		AC_MSG_ERROR(Default baud rate required)
	else
		DEF_BAUD="$enable_dfl_baud"
	fi
fi

AC_ARG_ENABLE([cfg-dir],
	AS_HELP_STRING([--enable-cfg-dir=DIR],
	               [Set minicom cfg file path (def: sysconfdir)]),
	[], [enable_cfg_dir="yes"])
if test "x$enable_cfg_dir" = xyes; then
	MINICOM_CONFDIR="$sysconfdir"
else
	if test "x$enable_cfg_dir" = xno; then
		AC_MSG_ERROR(Config directory required)
	else
		MINICOM_CONFDIR="$enable_cfg_dir"
	fi
fi
AC_SUBST([MINICOM_CONFDIR])

AC_ARG_ENABLE([kermit],
	AS_HELP_STRING([--enable-kermit=FILE],
	               [Set default path to kermit (def: search PATH)]),
	[], [enable_kermit="yes"])
if test "x$enable_kermit" = xyes; then
	PATH_KERMIT=""
else
	if test "x$enable_kermit" = xno; then
		PATH_KERMIT=""
	else
		PATH_KERMIT="$enable_kermit"
	fi
fi

dnl Set of available languages.
ALL_LINGUAS="cs da de es fr fi hu id ja ka ko nb pl pt_BR ro ru rw sr sv vi zh_CN zh_TW"

dnl Checks for programs.
AM_GNU_GETTEXT([external])
AM_GNU_GETTEXT_VERSION([0.21])

dnl This is a hacky workaround as the m4 scripts for iconv seem to set
dnl LIBICONV to '-liconv' despite that this lib is not available if iconv
dnl functionality is coming out of libc. But we need -liconv for other
dnl systems, such as Mac OS. Other projects I looked seem to have their own
dnl set of iconv m4 macros... why?
dnl if test "x$gt_use_preinstalled_gnugettext" = "xyes" -o "x$USE_NLS" = "no"
dnl then
dnl    LIBICONV=''
dnl    LTLIBICONV=''
dnl fi

if test "x$enable_kermit" != xno && test "x$PATH_KERMIT" = x
then
AC_PATH_PROG(PATH_KERMIT, kermit, no, $PATH:/bin:/usr/bin:/usr/local/bin:/opt/gnu/bin)
else
	AC_MSG_CHECKING(manual Kermit setting)
	AC_MSG_RESULT($PATH_KERMIT)
fi
if test "x$PATH_KERMIT" = x -o "x$PATH_KERMIT" = xno
then
	AC_DEFINE(KERMIT, "", [Path to kermit])
else
	AC_DEFINE_UNQUOTED(KERMIT, "$PATH_KERMIT -l %l -b %b", [Kermit command])
fi


TERMLIBS=
for termlib in tinfow tinfo curses termcap terminfo termlib ; do
   AC_CHECK_LIB(${termlib}, tputs,
     [TERMLIBS="${TERMLIBS} -l${termlib}"; break])
done

LIBS="$LIBS $TERMLIBS"

dnl Checks for header files.
dnl Do not use <ncurses/termcap.h> unless we're linking with ncurses.
if test "x$termlib" = xncurses -o "x$termlib" = xncursesw ; then
  dnl Use AC_CHECK_HEADERS so the HAVE_*_H symbol gets defined.
  AC_CHECK_HEADERS(ncurses/termcap.h, [found_termcap_h=1])
fi
if test "x$found_termcap_h" != "x1"; then
  AC_CHECK_HEADERS(termcap.h)
fi

AC_CHECK_LIB(socket, socket)

dnl Checks for header files.
AC_HEADER_DIRENT
AC_HEADER_SYS_WAIT
AC_HEADER_STAT


AC_SYS_POSIX_TERMIOS
AC_HEADER_TIOCGWINSZ
if test $ac_cv_sys_posix_termios = yes; then
  AC_DEFINE(POSIX_TERMIOS, [1], [Define if your system supports POSIX termios])
fi

AC_CHECK_HEADERS(stdarg.h varargs.h termio.h termios.h \
	setjmp.h pwd.h signal.h fcntl.h sgtty.h locale.h \
	sys/stat.h sys/file.h sys/ioctl.h sys/time.h \
	sys/ttold.h sys/param.h unistd.h posix1_lim.h sgtty.h features.h)

dnl Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST
AC_TYPE_UID_T
AC_TYPE_MODE_T
AC_TYPE_PID_T
AC_TYPE_SIZE_T
AC_STRUCT_TM

dnl Checks for library functions.
AC_FUNC_ERROR_AT_LINE
AC_FUNC_CLOSEDIR_VOID
AM_WITH_DMALLOC
AC_CHECK_FUNCS(getcwd getwd memmove strerror strstr vsnprintf vprintf select)
#KEYSERV="minicom.keyserv"
KEYSERV=""
AC_SUBST(KEYSERV)
AC_REPLACE_FUNCS(snprintf usleep getopt getopt_long)

dnl system capabilities
AC_SYS_LONG_FILE_NAMES

dnl ---------------------------------------------------------------

AC_MSG_CHECKING(for com line lock directory)

if test "x$UUCPLOCK" != x
then
	AC_MSG_RESULT($UUCPLOCK)
	AC_DEFINE_UNQUOTED(UUCPLOCK, "$UUCPLOCK", [Lock directory])
fi

if test "x$UUCPLOCK" = x
then
	for ac_uucplock in /etc/locks /var/lock /usr/spool/locks /var/spool/locks /var/spool/lock /usr/spool/uucp /var/spool/uucp /var/run; do
		UUCPLOCK=$ac_uucplock
		if test -d $UUCPLOCK; then
			AC_MSG_RESULT($UUCPLOCK)
			AC_DEFINE_UNQUOTED(UUCPLOCK, "$UUCPLOCK")
			break
		else
			UUCPLOCK=""
		fi
	done
fi

if test "x$UUCPLOCK" = x
then
	AC_MSG_ERROR(No suitable lock directory)
fi

dnl ---------------------------------------------------------------

AC_MSG_CHECKING(for default serial port device)

if test "x$DFL_PORT" != x
then
	if test -c $DFL_PORT
	then
		AC_MSG_RESULT($DFL_PORT)
		AC_DEFINE_UNQUOTED(DFL_PORT, "$DFL_PORT",
		                   [Default /dev/... device])
	else
		DFL_PORT=""
	fi
fi

if test "x$DFL_PORT" = x
then
	for ac_port in /dev/modem /dev/cua/b /dev/cua2p0 /dev/ttyS1 /dev/com0 /dev/tty01 /dev/tty8; do
		DFL_PORT=$ac_port
		if test -c $DFL_PORT; then
			AC_MSG_RESULT($DFL_PORT)
			AC_DEFINE_UNQUOTED(DFL_PORT, "$DFL_PORT")
			break
		else
			DFL_PORT=""
		fi
	done
fi

if test "x$DFL_PORT" = x
then
	DFL_PORT=/dev/modem
	AC_MSG_RESULT($DFL_PORT)
	AC_DEFINE_UNQUOTED(DFL_PORT, "$DFL_PORT", [Default device])
fi

dnl ---------------------------------------------------------------

AC_MSG_CHECKING(for default baud rate)

tmp_match=no
for tmp_baud_rate in 300 1200 2400 4800 9600 19200 38400 57600 115200 230400
do
	if test "x$DEF_BAUD" = "x$tmp_baud_rate"
	then
		tmp_match=yes
		AC_DEFINE_UNQUOTED(DEF_BAUD, "$DEF_BAUD", [Default baud rate])
		AC_MSG_RESULT($DEF_BAUD)
	fi
done

if test "x$tmp_match" != xyes
then
	AC_MSG_ERROR(No suitable default baud rate)
fi

if test "x$ac_cv_header_getopt_h" = xno
then
	CFLAGS="$CFLAGS -I\$(top_srcdir)/lib"
fi

if test "x$ac_cv_c_compiler_gnu" = xyes
then
	CFLAGS="$CFLAGS -W -Wall -Wextra -std=gnu99 -fno-common -Wno-format-truncation"
fi

# this is a hack, if we need getopt_long we also need getopt
# but I don't know how to express that dependency in lib/Makefile.am
AC_SUBST(LIBPORT_GETOPT_LONG_DEP)
if test "x$ac_cv_func_getopt_long" = xno
then
	LIBPORT_GETOPT_LONG_DEP="getopt.o"
fi

dnl ---------------------------------------------------------------

AH_BOTTOM([
/* Defines from old config.h */
#define LOGFILE "minicom.log"        /* Not defined = not used */
#define CALLOUT ""                   /* Gets run to get into dialut mode */
#define CALLIN  ""                   /* Gets run to get into dial in mode */

/* This defines a special mode in the wwxgetch() routine. The
 * basic idea behind this probably works on the consoles of
 * most PC-based unices, but it's only implemented for Linux.
 */
#if defined (__linux__)
#  define KEY_KLUDGE 1
#endif
])

dnl --------------------------------------------------------------

AC_CONFIG_FILES([Makefile
                 doc/Makefile \
                 extras/Makefile \
		 extras/linux/Makefile \
		 extras/tables/Makefile \
		 extras/termcap/Makefile \
		 extras/terminfo/Makefile \
		 man/Makefile \
		 lib/Makefile \
		 src/Makefile \
		 po/Makefile.in \
		 minicom.spec])
AC_OUTPUT
