Summary:	A GNU stream text editor
Summary(de):	GNU Stream-Text Editor
Summary(fr):	Éditeur de flot de GNU
Summary(pl):	Edytor GNU strumienia tekstu
Summary(tr):	GNU dosya iþleme aracý
Name:		sed
Version:	3.02
Release:	11
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	ftp://prep.ai.mit.edu/pub/gnu/sed/%{name}-%{version}.tar.gz
Patch0:		%{name}.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-autoconf_fix.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor. Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text. The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%description -l de
sed (Stream EDitor) ist ein Stream- oder Batch- (nicht-interaktiver)
Editor. Sed nimmt als Eingabe einen Text, führt darauf Operationen
aus, und gibt einen veränderten Text aus. Die Operationen, die sed
ausführt (Ersetzen, Löschen, Einfügen, usw.) können über eine
Skriptdatei oder über die Kommandozeile angegeben werden.

%description -l fr
sed copie les fichiers indiqués (l'entrée standard par défaut),
modifiés en fonction d'un script de commandes, vers la sortie
standard.

%description -l pl
Sed (Stream EDitor) jest edytorem strumieni lub wsadowym
(nieinteraktywnym) edytorem. Sed pobiera tekst na wej¶ciu, przetwarza
go wed³ug zestawu operacji i oddaje na wyj¶ciu przetworzony tekst.
Operacje, które ma wykonywaæ, mog± byæ zapisane w postaci skryptu lub
podane w linii poleceñ.

%description -l tr
Sed, belirtilen dosyalarý, verilen komutlara göre iþleyerek standart
çýktýya kopyalar. Genellikle, metin dosyalarýnda bir katarýn yerine
baþka bir katar yazmakta kullanýlýr.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ANNOUNCE AUTHORS BUGS ChangeLog NEWS README THANKS TODO dc.sed \
	testsuite/*

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/sed.info*
