#
# Conditional build:
%bcond_without	tests	# do not perform "make check"

Summary:	A GNU stream text editor
Summary(de.UTF-8):	GNU Stream-Text Editor
Summary(es.UTF-8):	Editor de stream de la GNU
Summary(fr.UTF-8):	Éditeur de flot de GNU
Summary(ja.UTF-8):	GNU ストリームテキストエディター
Summary(pl.UTF-8):	Edytor GNU strumienia tekstu
Summary(pt_BR.UTF-8):	Editor de stream da GNU
Summary(ru.UTF-8):	Потоковый редактор текста GNU
Summary(tr.UTF-8):	GNU dosya işleme aracı
Summary(uk.UTF-8):	Потоковий редактор тексту GNU
Name:		sed
Version:	4.2.2
Release:	1
License:	GPL v3+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/sed/%{name}-%{version}.tar.gz
# Source0-md5:	4111de4faa3b9848a0686b2f260c5056
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	5cd651063bfc00a82d820ba018672351
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/sed/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	libselinux-devel
BuildRequires:	texinfo
%if %{with tests}
%if "%(locale -a | grep -q '^ru_RU\.utf8$' ; echo $?)" == "1"
BuildRequires:	glibc-localedb-all
%endif
%endif
Obsoletes:	ssed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor. Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text. The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%description -l de.UTF-8
sed (Stream EDitor) ist ein Stream- oder Batch- (nicht-interaktiver)
Editor. Sed nimmt als Eingabe einen Text, führt darauf Operationen
aus, und gibt einen veränderten Text aus. Die Operationen, die sed
ausführt (Ersetzen, Löschen, Einfügen, usw.) können über eine
Skriptdatei oder über die Kommandozeile angegeben werden.

%description -l es.UTF-8
Sed copia los archivos nombrados (archivos de la entrada padrón por
por defecto) para la salida padrón, editado de acuerdo con un script
de comandos.

%description -l fr.UTF-8
sed copie les fichiers indiqués (l'entrée standard par défaut),
modifiés en fonction d'un script de commandes, vers la sortie
standard.

%description -l ja.UTF-8
sed (Stream Editor)
エディターはストリームまたはバッチ(非インタラクティブ)
エディターです。sed は入力としてテキストを用い、テキストの操作または
操作のセットをテキストとに対して行い、修正されたテキストを出力します。
sed が行う操作 (置換、削除、挿入、その他) はスクリプトファイルか、
コマンドラインから指定されます。

%description -l pl.UTF-8
Sed (Stream EDitor) jest edytorem strumieni lub wsadowym
(nieinteraktywnym) edytorem. Sed pobiera tekst na wejściu, przetwarza
go według zestawu operacji i oddaje na wyjściu przetworzony tekst.
Operacje, które ma wykonywać, mogą być zapisane w postaci skryptu lub
podane w linii poleceń.

%description -l pt_BR.UTF-8
O sed copia os arquivos indicados (ou a entrada padrão caso não
especificado) para a saída padrão, editado de acordo com um roteiro de
comandos.

%description -l ru.UTF-8
sed (Stream EDitor) - это потоковый или пакетный (не-интерактивный)
редактор. sed исполняет операции над подаваемым ему на вход текстом и
выдает модифицированный текст. Операции, которые sed выполняет
(подстановки, удаления, вставки и др.) могут быть заданы в файле
сценария или с командной строки.

%description -l tr.UTF-8
Sed, belirtilen dosyaları, verilen komutlara göre işleyerek standart
çıktıya kopyalar. Genellikle, metin dosyalarında bir katarın yerine
başka bir katar yazmakta kullanılır.

%description -l uk.UTF-8
sed (Stream EDitor) - це потоковий чи пакетний (не-інтерактивний)
редактор. sed виконує операції над текстом, що подається йому на вхід
та виводить модифікований текст. Операції, які sed виконує
(підстановки, видалення, вставки та ін.) можуть бути задані в файлі
сценарію чи з командного рядка.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

# LC_ALL=C overrides LANG which is required to run tests
unset LC_ALL
%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.sed-non-english-man-pages

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/sed
%{_mandir}/man1/sed.1*
%lang(de) %{_mandir}/de/man1/sed.1*
%lang(fi) %{_mandir}/fi/man1/sed.1*
%lang(hu) %{_mandir}/hu/man1/sed.1*
%lang(ja) %{_mandir}/ja/man1/sed.1*
%lang(pl) %{_mandir}/pl/man1/sed.1*
%{_infodir}/sed.info*
