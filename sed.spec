Summary:	GNU Stream Editor
Summary(de):	GNU Stream Editor
Summary(fr):	�diteur de flot de GNU
Summary(pl):	Edytor strumienowy GNU
Summary(tr):	GNU dosya i�leme arac�
Name:		sed
Version:	3.02
Release:	7
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narz�dzia/Tekst
Source:		ftp://prep.ai.mit.edu/pub/gnu/sed/%{name}-%{version}.tar.gz
Patch0:		sed.patch
Patch1:		sed-info.patch
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

%description
Sed copies the named files (standard input default) to the standard output, 
edited according to a script of commands.

%description -l de
Sed kopiert die genannten Dateien (Standardeingabe-Einstellung) nach
Bearbeitung anhand eines Befehlsskripts auf die Standardausgabe.  

%description -l fr
sed copie les fichiers indiqu�s (l'entr�e standard par d�faut), modifi�s en 
fonction d'un script de commandes, vers la sortie standard.

%description -l pl
Sed kopiuje podane pliki (domy�lnie ze standardowego wej�cia) na standardowe 
wyj�cie, edytuj�c je wed�ug polece� skryptu. 

%description -l tr
Sed, belirtilen dosyalar�, verilen komutlara g�re i�leyerek standart ��kt�ya
kopyalar. Genellikle, metin dosyalar�nda bir katar�n yerine ba�ka bir katar
yazmakta kullan�l�r.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf && %configure

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/bin

make \
    bindir=$RPM_BUILD_ROOT/bin \
    mandir=$RPM_BUILD_ROOT%{_mandir} \
    infodir=$RPM_BUILD_ROOT%{_infodir} \
    install install-strip

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/{info/*info*,man/man1/*} \
	ANNOUNCE AUTHORS BUGS ChangeLog NEWS README THANKS TODO dc.sed \
	testsuite/*

%post
/sbin/install-info %{_infodir}/sed.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/sed.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root)
%doc *.gz
%attr(755,root,root) /bin/*
%{_mandir}/man1/*
%{_infodir}/sed.info*

%changelog
* Mon Apr 19 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.02-6]
- recompiles on new rpm.

* Wed Apr 14 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.02-5]
- standarized {un}registering info pages (added sed-info.patch).

* Mon Apr 12 1999 Micha� Kuratczyk <kura@pld.org.pl>
- added Group(pl)
- removed man group from man pages
- added gzipping documentation
- added stripping binaries

* Wed Dec 23 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.02-4]
- standarized {un}registering info pages,
- added gzipping man and info pages.

* Sun Nov 15 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.02-3]
- fixed dc.sed script witch have incorrect patch to sed (must be /bin/sed).

* Mon Oct 12 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.02-2]
- changed passing way LDFLAGS (as a configure enviroment variable).

* Tue Sep 29 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- added pl translation,
- added using %%{name} and %%{version} in Source.
