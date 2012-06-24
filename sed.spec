Summary:	A GNU stream text editor
Summary(de):	GNU Stream-Text Editor
Summary(fr):	�diteur de flot de GNU
Summary(pl):	Edytor GNU strumienia tekstu
Summary(tr):	GNU dosya i�leme arac�
Name:		sed
Version:	3.02
Release:	8
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narz�dzia/Tekst
Source:		ftp://prep.ai.mit.edu/pub/gnu/sed/%{name}-%{version}.tar.gz
Patch0:		sed.patch
Patch1:		sed-info.patch
Patch2:		sed-autoconf_fix.patch
Prereq:		/usr/sbin/fix-info-dir
Buildroot:	/tmp/%{name}-%{version}-root

%define _bindir /bin

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor. Sed takes text as input, performs an operation or set of operations
on the text and outputs the modified text.  The operations that sed performs
(substitutions, deletions, insertions, etc.) can be specified in a script
file or from the command line.

%description -l de
sed (Stream EDitor) ist ein Stream- oder Batch- (nicht-interaktiver) Editor.
Sed nimmt als Eingabe einen Text, f�hrt darauf Operationen aus, und gibt
einen ver�nderten Text aus. Die Operationen, die sed ausf�hrt (Ersetzen,
L�schen, Einf�gen, usw.) k�nnen �ber eine Skriptdatei oder �ber die
Kommandozeile angegeben werden.

%description -l fr
sed copie les fichiers indiqu�s (l'entr�e standard par d�faut), modifi�s en 
fonction d'un script de commandes, vers la sortie standard.

%description -l pl
Sed (Stream EDitor) jest edytorem strumieni lub wsadowym (nieinteraktywnym)
edytorem. Sed pobiera pobiera tekst na wej�ciu, przetwarza go wed�ug zestawu
operacji i oddaje na wyj�ciu przetworzony tekst. Operacje wykonywane z
u�yciem seda moga by� wyspecyfikowane w postaci skryptu lub z linii polece�.

%description -l tr
Sed, belirtilen dosyalar�, verilen komutlara g�re i�leyerek standart ��kt�ya
kopyalar. Genellikle, metin dosyalar�nda bir katar�n yerine ba�ka bir katar
yazmakta kullan�l�r.

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
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%preun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root)
%doc *.gz
%attr(755,root,root) /bin/*
%{_mandir}/man1/*
%{_infodir}/sed.info*
