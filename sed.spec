Summary:	GNU Stream Editor
Summary(de):	GNU Stream Editor
Summary(fr):	Éditeur de flot de GNU
Summary(pl):	Edytor strumienowy GNU
Summary(tr):	GNU dosya iþleme aracý
Name:		sed
Version:	3.02
Release:	7
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source:		ftp://prep.ai.mit.edu/pub/gnu/sed/%{name}-%{version}.tar.gz
Patch0:		sed.patch
Patch1:		sed-info.patch
Patch2:		sed-autoconf_fix.patch
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

%define _bindir /bin

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
%patch1 -p1
%patch2 -p1

%build
automake
autoconf
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/bin

make install-strip DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*info*,%{_mandir}/man1/*} \
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
* Thu Jun 17 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.02-7]
- based on RH spec,
- spec rewrited by PLD team,
- pl translation Marcin Korzonek <mkorz@shadow.eu.org>.
