#
# Conditional build:
%bcond_without	tests	# do not perform "make check"
#
Summary:	A GNU stream text editor
Summary(de):	GNU Stream-Text Editor
Summary(es):	Editor de stream de la GNU
Summary(fr):	Éditeur de flot de GNU
Summary(ja):	GNU ¥¹¥È¥ê¡¼¥à¥Æ¥­¥¹¥È¥¨¥Ç¥£¥¿¡¼
Summary(pl):	Edytor GNU strumienia tekstu
Summary(pt_BR):	Editor de stream da GNU
Summary(ru):	ðÏÔÏËÏ×ÙÊ ÒÅÄÁËÔÏÒ ÔÅËÓÔÁ GNU
Summary(tr):	GNU dosya iþleme aracý
Summary(uk):	ðÏÔÏËÏ×ÉÊ ÒÅÄÁËÔÏÒ ÔÅËÓÔÕ GNU
Name:		sed
Version:	4.1.4
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/sed/%{name}-%{version}.tar.gz
# Source0-md5:	2a62ceadcb571d2dac006f81df5ddb48
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	5cd651063bfc00a82d820ba018672351
Patch0:		%{name}-info.patch
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	gettext-devel >= 0.14
BuildRequires:	texinfo
Obsoletes:	ssed
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

%description -l es
Sed copia los archivos nombrados (archivos de la entrada padrón por
por defecto) para la salida padrón, editado de acuerdo con un script
de comandos.

%description -l fr
sed copie les fichiers indiqués (l'entrée standard par défaut),
modifiés en fonction d'un script de commandes, vers la sortie
standard.

%description -l ja
sed (Stream Editor)
¥¨¥Ç¥£¥¿¡¼¤Ï¥¹¥È¥ê¡¼¥à¤Þ¤¿¤Ï¥Ð¥Ã¥Á(Èó¥¤¥ó¥¿¥é¥¯¥Æ¥£¥Ö)
¥¨¥Ç¥£¥¿¡¼¤Ç¤¹¡£sed ¤ÏÆþÎÏ¤È¤·¤Æ¥Æ¥­¥¹¥È¤òÍÑ¤¤¡¢¥Æ¥­¥¹¥È¤ÎÁàºî¤Þ¤¿¤Ï
Áàºî¤Î¥»¥Ã¥È¤ò¥Æ¥­¥¹¥È¤È¤ËÂÐ¤·¤Æ¹Ô¤¤¡¢½¤Àµ¤µ¤ì¤¿¥Æ¥­¥¹¥È¤ò½ÐÎÏ¤·¤Þ¤¹¡£
sed ¤¬¹Ô¤¦Áàºî (ÃÖ´¹¡¢ºï½ü¡¢ÁÞÆþ¡¢¤½¤ÎÂ¾) ¤Ï¥¹¥¯¥ê¥×¥È¥Õ¥¡¥¤¥ë¤«¡¢
¥³¥Þ¥ó¥É¥é¥¤¥ó¤«¤é»ØÄê¤µ¤ì¤Þ¤¹¡£

%description -l pl
Sed (Stream EDitor) jest edytorem strumieni lub wsadowym
(nieinteraktywnym) edytorem. Sed pobiera tekst na wej¶ciu, przetwarza
go wed³ug zestawu operacji i oddaje na wyj¶ciu przetworzony tekst.
Operacje, które ma wykonywaæ, mog± byæ zapisane w postaci skryptu lub
podane w linii poleceñ.

%description -l pt_BR
O sed copia os arquivos indicados (ou a entrada padrão caso não
especificado) para a saída padrão, editado de acordo com um roteiro de
comandos.

%description -l ru
sed (Stream EDitor) - ÜÔÏ ÐÏÔÏËÏ×ÙÊ ÉÌÉ ÐÁËÅÔÎÙÊ (ÎÅ-ÉÎÔÅÒÁËÔÉ×ÎÙÊ)
ÒÅÄÁËÔÏÒ. sed ÉÓÐÏÌÎÑÅÔ ÏÐÅÒÁÃÉÉ ÎÁÄ ÐÏÄÁ×ÁÅÍÙÍ ÅÍÕ ÎÁ ×ÈÏÄ ÔÅËÓÔÏÍ É
×ÙÄÁÅÔ ÍÏÄÉÆÉÃÉÒÏ×ÁÎÎÙÊ ÔÅËÓÔ. ïÐÅÒÁÃÉÉ, ËÏÔÏÒÙÅ sed ×ÙÐÏÌÎÑÅÔ
(ÐÏÄÓÔÁÎÏ×ËÉ, ÕÄÁÌÅÎÉÑ, ×ÓÔÁ×ËÉ É ÄÒ.) ÍÏÇÕÔ ÂÙÔØ ÚÁÄÁÎÙ × ÆÁÊÌÅ
ÓÃÅÎÁÒÉÑ ÉÌÉ Ó ËÏÍÁÎÄÎÏÊ ÓÔÒÏËÉ.

%description -l tr
Sed, belirtilen dosyalarý, verilen komutlara göre iþleyerek standart
çýktýya kopyalar. Genellikle, metin dosyalarýnda bir katarýn yerine
baþka bir katar yazmakta kullanýlýr.

%description -l uk
sed (Stream EDitor) - ÃÅ ÐÏÔÏËÏ×ÉÊ ÞÉ ÐÁËÅÔÎÉÊ (ÎÅ-¦ÎÔÅÒÁËÔÉ×ÎÉÊ)
ÒÅÄÁËÔÏÒ. sed ×ÉËÏÎÕ¤ ÏÐÅÒÁÃ¦§ ÎÁÄ ÔÅËÓÔÏÍ, ÝÏ ÐÏÄÁ¤ÔØÓÑ ÊÏÍÕ ÎÁ ×È¦Ä
ÔÁ ×É×ÏÄÉÔØ ÍÏÄÉÆ¦ËÏ×ÁÎÉÊ ÔÅËÓÔ. ïÐÅÒÁÃ¦§, ÑË¦ sed ×ÉËÏÎÕ¤
(Ð¦ÄÓÔÁÎÏ×ËÉ, ×ÉÄÁÌÅÎÎÑ, ×ÓÔÁ×ËÉ ÔÁ ¦Î.) ÍÏÖÕÔØ ÂÕÔÉ ÚÁÄÁÎ¦ × ÆÁÊÌ¦
ÓÃÅÎÁÒ¦À ÞÉ Ú ËÏÍÁÎÄÎÏÇÏ ÒÑÄËÁ.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%{?with_tests: %{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/sed.info*
