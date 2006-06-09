#
# Conditional build:
%bcond_without	tests	# do not perform "make check"
#
Summary:	A GNU stream text editor
Summary(de):	GNU Stream-Text Editor
Summary(es):	Editor de stream de la GNU
Summary(fr):	иditeur de flot de GNU
Summary(ja):	GNU ╔╧╔х╔Й║╪╔Ю╔ф╔╜╔╧╔х╔╗╔г╔ё╔©║╪
Summary(pl):	Edytor GNU strumienia tekstu
Summary(pt_BR):	Editor de stream da GNU
Summary(ru):	Потоковый редактор текста GNU
Summary(tr):	GNU dosya iЧleme aracЩ
Summary(uk):	Потоковий редактор тексту GNU
Name:		sed
Version:	4.1.5
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/sed/%{name}-%{version}.tar.gz
# Source0-md5:	7a1cbbbb3341287308e140bd4834c3ba
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	5cd651063bfc00a82d820ba018672351
Patch0:		%{name}-info.patch
Patch1:		%{name}-pl.po-update.patch
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
Editor. Sed nimmt als Eingabe einen Text, fЭhrt darauf Operationen
aus, und gibt einen verДnderten Text aus. Die Operationen, die sed
ausfЭhrt (Ersetzen, LЖschen, EinfЭgen, usw.) kЖnnen Эber eine
Skriptdatei oder Эber die Kommandozeile angegeben werden.

%description -l es
Sed copia los archivos nombrados (archivos de la entrada padrСn por
por defecto) para la salida padrСn, editado de acuerdo con un script
de comandos.

%description -l fr
sed copie les fichiers indiquИs (l'entrИe standard par dИfaut),
modifiИs en fonction d'un script de commandes, vers la sortie
standard.

%description -l ja
sed (Stream Editor)
╔╗╔г╔ё╔©║╪╓о╔╧╔х╔Й║╪╔Ю╓ч╓©╓о╔п╔ц╔а(хС╔╓╔С╔©╔И╔╞╔ф╔ё╔ж)
╔╗╔г╔ё╔©║╪╓г╓╧║ёsed ╓офЧно╓х╓╥╓ф╔ф╔╜╔╧╔х╓Рмя╓╓║╒╔ф╔╜╔╧╔х╓наЮ╨Н╓ч╓©╓о
аЮ╨Н╓н╔╩╔ц╔х╓Р╔ф╔╜╔╧╔х╓х╓кбп╓╥╓ф╧т╓╓║╒╫╓ю╣╓╣╓Л╓©╔ф╔╜╔╧╔х╓Р╫пно╓╥╓ч╓╧║ё
sed ╓╛╧т╓╕аЮ╨Н (цж╢╧║╒╨О╫Э║╒ачфЧ║╒╓╫╓нб╬) ╓о╔╧╔╞╔Й╔в╔х╔у╔║╔╓╔К╓╚║╒
╔Ё╔ч╔С╔и╔И╔╓╔С╓╚╓И╩ьдЙ╓╣╓Л╓ч╓╧║ё

%description -l pl
Sed (Stream EDitor) jest edytorem strumieni lub wsadowym
(nieinteraktywnym) edytorem. Sed pobiera tekst na wej╤ciu, przetwarza
go wedЁug zestawu operacji i oddaje na wyj╤ciu przetworzony tekst.
Operacje, ktСre ma wykonywaФ, mog╠ byФ zapisane w postaci skryptu lub
podane w linii poleceЯ.

%description -l pt_BR
O sed copia os arquivos indicados (ou a entrada padrЦo caso nЦo
especificado) para a saМda padrЦo, editado de acordo com um roteiro de
comandos.

%description -l ru
sed (Stream EDitor) - это потоковый или пакетный (не-интерактивный)
редактор. sed исполняет операции над подаваемым ему на вход текстом и
выдает модифицированный текст. Операции, которые sed выполняет
(подстановки, удаления, вставки и др.) могут быть заданы в файле
сценария или с командной строки.

%description -l tr
Sed, belirtilen dosyalarЩ, verilen komutlara gЖre iЧleyerek standart
ГЩktЩya kopyalar. Genellikle, metin dosyalarЩnda bir katarЩn yerine
baЧka bir katar yazmakta kullanЩlЩr.

%description -l uk
sed (Stream EDitor) - це потоковий чи пакетний (не-╕нтерактивний)
редактор. sed викону╓ операц╕╖ над текстом, що пода╓ться йому на вх╕д
та виводить модиф╕кований текст. Операц╕╖, як╕ sed викону╓
(п╕дстановки, видалення, вставки та ╕н.) можуть бути задан╕ в файл╕
сценар╕ю чи з командного рядка.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_mandir}/README.sed-non-english-man-pages

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

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
