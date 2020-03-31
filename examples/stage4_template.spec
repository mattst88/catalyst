# stage4 example specfile
# used to build a stage4

# The subarch can be any of the supported catalyst subarches (like athlon-xp).
# Refer to "man catalyst" or <https://wiki.gentoo.org/wiki/Catalyst>
# for supported subarches
# example:
# subarch: athlon-xp
subarch:

# The version stamp is an identifier for the build.  It can be anything you wish
# it to be, but it is usually a date.
# example:
# version_stamp: 2006.1
version_stamp:

# The target specifies what target we want catalyst to do.  For building a CD,
# we start with stage4 as our target.
# example:
# target: stage4
target:

# The rel_type defines what kind of build we are doing.  This is merely another
# identifier, but it useful for allowing multiple concurrent builds.  Usually,
# default will suffice.
# example:
# rel_type: default
rel_type:

# This is the system profile to be used by catalyst to build this target.  It is
# specified as a relative path from /var/db/repos/gentoo/profiles.
# example:
# profile: default-linux/x86/2006.1
profile:

# This specifies which snapshot to use for building this target.
# example:
# snapshot: 2006.1
snapshot:

# This specifies where the seed stage comes from for this target,  The path is
# relative to $clst_sharedir/builds.  The rel_type is also used as a path prefix
# for the seed.
# example:
# default/stage3-x86-2006.1
source_subpath:

# These are the hosts used as distcc slaves when distcc is enabled in your
# catalyst.conf.  It follows the same syntax as distcc-config --set-hosts and
# is entirely optional.
# example:
# distcc_hosts: 127.0.0.1 192.168.0.1
distcc_hosts:

# This is an optional directory containing portage configuration files.  It
# follows the same syntax as /etc/portage and should be consistent across all
# targets to minimize problems.
# example:
# portage_confdir: /etc/portage
portage_confdir:

# This option specifies the location to a portage overlay that you would like to
# have used when building this target.
# example:
# portage_overlay: /usr/local/portage
portage_overlay:

# This allows the optional directory containing the output packages for
# catalyst.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# pkgcache_path: /tmp/packages
pkgcache_path:

# This allows the optional directory containing the output packages for kernel
# builds.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# kerncache_path: /tmp/kernel
kerncache_path:

# The stage4 target is where you will build packages for basically updated
# stage3.  These packages can be built with customized USE settings.  The
# settings here are additive to the default USE configured by the profile.
# Leaving this blank will default to the system use flags
# example:
# stage4/use: ipv6 socks5 fbcon ncurses readline ssl
stage4/use:

# This is the set of packages that we will merge into the stage4 tarball.  They
# will be built with the USE flags configured above.  These packages must not
# depend on a configured kernel.  If the package requires a configured kernel,
# then it will be defined elsewhere.
# example:
# stage4/packages: livecd-tools dhcpcd acpid apmd gentoo-sources coldplug fxload irssi gpm syslog-ng parted links raidtools dosfstools nfs-utils jfsutils xfsprogs e2fsprogs reiserfsprogs ntfsprogs pwgen rp-pppoe screen mirrorselect penggy iputils hwdata-knoppix hwsetup lvm2 evms vim pptpclient mdadm ethtool wireless-tools prism54-firmware wpa_supplicant
stage4/packages:

# A fsscript is simply a shell script that is copied into the chroot of the stage4
# after the kernel(s) and any external modules have been compiled and is
# executed within the chroot.  It can contain any commands that are available
# via the packages installed by our stages or by the packages installed during
# the stage4-stage1 build.  We do not use one for the official release media, so
# there will not be one listed below.  The syntax is simply the full path and
# filename to the shell script that you wish to execute.  The script is copied
# into the chroot by catalyst automatically.
# example:
# stage4/fsscript:
stage4/fsscript:

# This is where you set the splash theme.  This theme must be present in
# /etc/splash, before the kernel has completed building.
# example:
# stage4/splash_theme: livecd-2006.1
stage4/splash_theme:

# This is a set of arguments that will be passed to genkernel for all kernels
# defined in this target.  It is useful for passing arguments to genkernel that
# are not otherwise available via the stage4-stage2 spec file.
# example:
# stage4/gk_mainargs: --lvm --dmraid
stage4/gk_mainargs:

# This option allows you to specify your own linuxrc script for genkernel to use
# when building your CD.  This is not checked for functionality, so it is up to
# you to debug your own script.  We do not use one for the official release
# media, so there will not be one listed below.
# example:
# stage4/linuxrc:
stage4/linuxrc:

# This is for the message of the day.  It is not required
# release media, as catalyst builds a default motd when the stage4/type is set
# to one of the gentoo-* options.  This setting overrides the default motd even
# on official media.  Since we do not use this for the official releases, it is
# left blank below.
# example:
# stage4/motd:
stage4/motd:

# This is for blacklisting modules from being hotplugged that are known to cause
# problems.  Putting a module name here will keep it from being auto-loaded,
# even if ti is detected by hotplug.
# example:
# stage4/modblacklist: 8139cp
stage4/modblacklist:

# This is for adding init scripts to runlevels.  The syntax for the init script
# is the script name, followed by a pipe, followed by the runlevel in which you
# want the script to run.  It looks like acpid|default and is space delimited.
# We do not use this on the official media, as catalyst sets up the runlevels
# correctly for us.  Since we do not use this, it is left blank below.
# example:
# stage4/rcadd:
stage4/rcadd:

# This is for removing init script from runlevels.  It is executed after the
# defaults shipped with catalyst, so it is possible to remove the defaults using
# this option.  It can follow the same syntax as livcd/rcadd, or you can leave
# the runlevel off to remove the script from any runlevels detected.  We do not
# use this on the official media, so it is left blank.
# example:
# stage4/rcdel:
stage4/rcdel:

# This overlay is dropped onto the filesystem within the loop.  This can be used
# for such things as updating configuration files or adding anything else you
# would want within your stage4 filesystem.  Files added here are available when
# docache is used.  We do not use this on the official media, so we will leave
# it blank below.
# example:
# stage4/root_overlay:
stage4/root_overlay:

# This is used by catalyst to copy the specified file to /etc/X11/xinit/xinitrc
# and is used by the stage4/type generic-livecd.  While the file will still be
# copied for any stage4/type, catalyst will only create the necessary
# /etc/startx for those types, so X will not be automatically started.  This is
# useful also for setting up X on a CD where you do not wish X to start
# automatically.  We do not use this on the release media, so it is left blank.
# example:
# stage4/xinitrc:
stage4/xinitrc:

# This option is used to create non-root users on your CD.  It takes a space
# separated list of user names.  These users will be added to the following
# groups: users,wheel,audio,games,cdrom,usb
# If this is specified in your spec file, then the first user is also the user
# used to start X. Since this is not used on the release media, it is blank.
# example:
# stage4/users:
stage4/users:

# This option is used to specify the number of kernels to build and also the
# labels that will be used by the CD bootloader to refer to each kernel image.
# example:
# boot/kernel: gentoo
boot/kernel:

# This option tells catalyst which kernel sources to merge for this kernel
# label.  This can use normal portage atoms to specify a specific version.
# example:
# boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/sources:

# This option is the full path and filename to a kernel .config file that is
# used by genkernel to compile the kernel this label applies to.
# example:
# boot/kernel/gentoo/config: /tmp/2.6.11-smp.config
boot/kernel/gentoo/config:

# This option sets genkernel parameters on a per-kernel basis and applies only
# to this kernel label.  This can be used for building options into only a
# single kernel, where compatibility may be an issue.  Since we do not use this
# on the official release media, it is left blank, but it follows the same
# syntax as stage4/gk_mainargs.
# example:
# boot/kernel/gentoo/gk_kernargs:
boot/kernel/gentoo/gk_kernargs:

# This option sets the USE flags used to build the kernel and also any packages
# which are defined under this kernel label.  These USE flags are additive from
# the default USE for the specified profile.
# example:
# boot/kernel/gentoo/use: pcmcia usb -X
boot/kernel/gentoo/use:

# This option appends an extension to the name of your kernel, as viewed by a
# uname -r/  This also affects any modules built under this kernel label.  This
# is useful for having two kernels using the same sources to keep the modules
# from overwriting each other.  We do not use this on the official media, so it
# is left blank.
# example:
# boot/kernel/gentoo/extraversion:
boot/kernel/gentoo/extraversion:

# This option is for merging kernel-dependent packages and external modules that
# are configured against this kernel label.
# example:
# boot/kernel/gentoo/packages: pcmcia-cs speedtouch slmodem globespan-adsl hostap-driver hostap-utils ipw2100 ipw2200 fritzcapi fcdsl cryptsetup
boot/kernel/gentoo/packages:

# This is a list of packages that will be unmerged after all the kernels have
# been built.  There are no checks on these packages, so be careful what you
# add here.  They can potentially break your CD.
# example:
# stage4/unmerge: acl attr autoconf automake bin86 binutils libtool m4 bison ld.so make perl patch linux-headers man-pages sash bison flex gettext texinfo ccache distcc man groff lib-compat miscfiles rsync sysklogd bc lcms libmng genkernel diffutils libperl gnuconfig gcc-config gcc bin86 cpio cronbase ed expat grub lilo help2man libtool gentoo-sources
stage4/unmerge:

# This option is used to empty the directories listed.  It is useful for getting
# rid of files that don't belong to a particular package, or removing files from
# a package that you wish to keep, but won't need the full functionality.
# example:
# stage4/empty: /var/tmp /var/cache /var/db /var/empty /var/lock /var/log /var/run /var/spool /var/state /tmp /var/db/repos/gentoo /usr/share/man /usr/share/info /usr/share/unimaps /usr/include /usr/share/zoneinfo /usr/share/dict /usr/share/doc /usr/share/ss /usr/share/state /usr/share/texinfo /usr/lib/python2.2 /usr/lib/portage /usr/share/gettext /usr/share/i18n /usr/share/rfc /usr/lib/X11/config /usr/lib/X11/etc /usr/lib/X11/doc /usr/src /usr/share/doc /usr/share/man /etc/cron.daily /etc/cron.hourly /etc/cron.monthly /etc/cron.weekly /etc/logrotate.d /etc/rsync /usr/lib/awk /usr/lib/ccache /usr/lib/gcc-config /usr/lib/nfs /usr/local /usr/diet/include /usr/diet/man /usr/share/consolefonts/partialfonts /usr/share/consoletrans /usr/share/emacs /usr/share/gcc-data /usr/share/genkernel /etc/splash/gentoo /etc/splash/emergence /usr/share/gnuconfig /usr/share/lcms /usr/share/locale /etc/skel
stage4/empty:

# This option tells catalyst to clean specific files from the filesystem and is
# very usefu in cleaning up stray files in /etc left over after stage4/unmerge.
# example:
# stage4/rm: /lib/*.a /usr/lib/*.a /usr/lib/gcc-lib/*/*/libgcj* /etc/dispatch-conf.conf /etc/etc-update.conf /etc/*- /etc/issue* /etc/portage/make.conf /etc/man.conf /etc/*.old /root/.viminfo /usr/sbin/fb* /usr/sbin/fsck.cramfs /usr/sbin/fsck.minix /usr/sbin/mkfs.minix /usr/sbin/mkfs.bfs /usr/sbin/mkfs.cramfs /lib/security/pam_access.so /lib/security/pam_chroot.so /lib/security/pam_debug.so /lib/security/pam_ftp.so /lib/security/pam_issue.so /lib/security/pam_mail.so /lib/security/pam_motd.so /lib/security/pam_mkhomedir.so /lib/security/pam_postgresok.so /lib/security/pam_rhosts_auth.so /lib/security/pam_userdb.so /usr/share/consolefonts/1* /usr/share/consolefonts/7* /usr/share/consolefonts/8* /usr/share/consolefonts/9* /usr/share/consolefonts/A* /usr/share/consolefonts/C* /usr/share/consolefonts/E* /usr/share/consolefonts/G* /usr/share/consolefonts/L* /usr/share/consolefonts/M* /usr/share/consolefonts/R* /usr/share/consolefonts/a* /usr/share/consolefonts/c* /usr/share/consolefonts/dr* /usr/share/consolefonts/g* /usr/share/consolefonts/i* /usr/share/consolefonts/k* /usr/share/consolefonts/l* /usr/share/consolefonts/r* /usr/share/consolefonts/s* /usr/share/consolefonts/t* /usr/share/consolefonts/v* /etc/splash/livecd-2006.1/16* /etc/splash/livecd-2006.1/12* /etc/splash/livecd-2006.1/6* /etc/splash/livecd-2006.1/8* /etc/splash/livecd-2006.1/images/silent-16* /etc/splash/livecd-2006.1/images/silent-12* /etc/splash/livecd-2006.1/images/silent-6* /etc/splash/livecd-2006.1/images/silent-8* /etc/splash/livecd-2006.1/images/verbose-16* /etc/splash/livecd-2006.1/images/verbose-12* /etc/splash/livecd-2006.1/images/verbose-6* /etc/splash/livecd-2006.1/images/verbose-8* /etc/portage/make.conf.example /etc/make.globals /etc/resolv.conf
stage4/rm:
