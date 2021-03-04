import requests


class FeedsUrls:
    def __init__(self):
        self._perlz = "http://www.perzl.org/aix/index.php?n=Main.Libzip"
        self._archlinux = "https://archlinux.org/packages/extra/x86_64/libzip/"
        self._conan = "https://conan.io/center/libzip"
        self._moreinfo = "http://moreinfo.thebigboss.org/moreinfo/depiction.php?file=libzipData"
        self._cygwin_ports = "http://cygwin-ports.cvs.sourceforge.net/viewvc/cygwin-ports/ports/libs/libzip/"
        self._debian = "https://tracker.debian.org/pkg/libzip"
        self._fedoraproject = "https://apps.fedoraproject.org/packages/libzip"
        self._freshports = "https://www.freshports.org/archivers/libzip/"
        self._gentoo = "https://packages.gentoo.org/packages/dev-libs/libzip"
        self._hpux = "http://hpux.connect.org.uk/hppd/hpux/Misc/libzip-0.10.1/"
        self._openmandriva = "https://abf.openmandriva.org/search?utf8=%E2%9C%93&query=libzip"
        self._pkgsrc = "https://pkgsrc.se/archivers/libzip"
        self._hydra = "https://hydra.nixos.org/job/nixpkgs/trunk/libzip.x86_64-linux"
        self._os4depot = "http://os4depot.net/?function=showfile&file=development/library/misc/libzip.lha"
        self._t2sde = "http://t2sde.org/packages/libzip.html"
        self._launchpad = "https://launchpad.net/ubuntu/+source/libzip"
        self._rpmfind = "http://rpmfind.net/linux/rpm2html/search.php?query=libzip"
        self._repology = "https://repology.org/project/libzip/versions"
