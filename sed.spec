Summary:     GNU Stream Editor
Summary(de): GNU Stream Editor
Summary(fr): Éditeur de flot de GNU
Summary(pl): Edytor strumienowy GNU
Summary(tr): GNU dosya iþleme aracý
Name:        sed
Version:     3.02
Release:     3
Copyright:   GPL
Group:       Utilities/Text
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch:       sed.patch
Prereq:      /sbin/install-info
Buildroot:   /tmp/%{name}-%{version}-root

%description
Sed copies the named files (standard input default) to the standard output, 
edited according to a script of commands.

%description -l de
Sed kopiert die genannten Dateien (Standardeingabe-Einstellung) nach
Bearbeitung anhand eines Befehlsskripts auf die Standardausgabe.  

%description -l fr
sed copie les fichiers indiqués (l'entrée standard par défaut), modifiés en 
fonction d'un script de commandes, vers la sortie standard.

%description -l pl
Sed kopiuje podane pliki (domy¶lnie ze standardowego wej¶cia) na standardowe 
wyj¶cie, edytuj±c je wed³ug poleceñ skryptu. 

%description -l tr
Sed, belirtilen dosyalarý, verilen komutlara göre iþleyerek standart çýktýya
kopyalar. Genellikle, metin dosyalarýnda bir katarýn yerine baþka bir katar
yazmakta kullanýlýr.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" ./configure \
	--prefix=/usr \
	--exec-prefix=/
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/bin

make prefix=$RPM_BUILD_ROOT/usr exec_prefix=$RPM_BUILD_ROOT/ install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/sed.info /usr/info/dir

%preun
/sbin/install-info --delete /usr/info/sed.info /usr/info/dir

%files
%defattr(644, root, root)
%doc ANNOUNCE AUTHORS BUGS ChangeLog NEWS README THANKS TODO dc.sed testsuite
%attr(755, root, root) /bin/sed 
%attr(644, root,  man) /usr/man/man1/sed.1
/usr/info/sed.info*

%changelog
* Sun Nov 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.02-3]
- fixed dc.sed script which have incorrect patch to sed (must be /bin/sed).

* Mon Oct 12 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.02-2]
- changed passing way LDFLAGS (as a configure enviroment variable).

* Tue Sep 29 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- added pl translation,
- added using %%{name} and %%{version} in Source.

* Tue Aug 18 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.02

* Sun Jul 26 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.01

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- removed references to the -g option from the man page that we add

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups
- added BuildRoot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
