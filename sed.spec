#
# Conditional build:
%bcond_without	tests	# do not perform "make check"
#
Summary:	A GNU stream text editor
Summary(de):	GNU Stream-Text Editor
Summary(es):	Editor de stream de la GNU
Summary(fr):	�diteur de flot de GNU
Summary(ja):	GNU ���ȥ꡼��ƥ����ȥ��ǥ�����
Summary(pl):	Edytor GNU strumienia tekstu
Summary(pt_BR):	Editor de stream da GNU
Summary(ru):	��������� �������� ������ GNU
Summary(tr):	GNU dosya i�leme arac�
Summary(uk):	��������� �������� ������ GNU
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
Editor. Sed nimmt als Eingabe einen Text, f�hrt darauf Operationen
aus, und gibt einen ver�nderten Text aus. Die Operationen, die sed
ausf�hrt (Ersetzen, L�schen, Einf�gen, usw.) k�nnen �ber eine
Skriptdatei oder �ber die Kommandozeile angegeben werden.

%description -l es
Sed copia los archivos nombrados (archivos de la entrada padr�n por
por defecto) para la salida padr�n, editado de acuerdo con un script
de comandos.

%description -l fr
sed copie les fichiers indiqu�s (l'entr�e standard par d�faut),
modifi�s en fonction d'un script de commandes, vers la sortie
standard.

%description -l ja
sed (Stream Editor)
���ǥ������ϥ��ȥ꡼��ޤ��ϥХå�(�󥤥󥿥饯�ƥ���)
���ǥ������Ǥ���sed �����ϤȤ��ƥƥ����Ȥ��Ѥ����ƥ����Ȥ����ޤ���
���Υ��åȤ�ƥ����ȤȤ��Ф��ƹԤ����������줿�ƥ����Ȥ���Ϥ��ޤ���
sed ���Ԥ���� (�ִ������������������¾) �ϥ�����ץȥե����뤫��
���ޥ�ɥ饤�󤫤���ꤵ��ޤ���

%description -l pl
Sed (Stream EDitor) jest edytorem strumieni lub wsadowym
(nieinteraktywnym) edytorem. Sed pobiera tekst na wej�ciu, przetwarza
go wed�ug zestawu operacji i oddaje na wyj�ciu przetworzony tekst.
Operacje, kt�re ma wykonywa�, mog� by� zapisane w postaci skryptu lub
podane w linii polece�.

%description -l pt_BR
O sed copia os arquivos indicados (ou a entrada padr�o caso n�o
especificado) para a sa�da padr�o, editado de acordo com um roteiro de
comandos.

%description -l ru
sed (Stream EDitor) - ��� ��������� ��� �������� (��-�������������)
��������. sed ��������� �������� ��� ���������� ��� �� ���� ������� �
������ ���������������� �����. ��������, ������� sed ���������
(�����������, ��������, ������� � ��.) ����� ���� ������ � �����
�������� ��� � ��������� ������.

%description -l tr
Sed, belirtilen dosyalar�, verilen komutlara g�re i�leyerek standart
��kt�ya kopyalar. Genellikle, metin dosyalar�nda bir katar�n yerine
ba�ka bir katar yazmakta kullan�l�r.

%description -l uk
sed (Stream EDitor) - �� ��������� �� �������� (��-�������������)
��������. sed �����դ �����æ� ��� �������, �� ��������� ���� �� �Ȧ�
�� �������� ����Ʀ������� �����. �����æ�, �˦ sed �����դ
(Ц���������, ���������, ������� �� ��.) ������ ���� ����Φ � ���̦
�����Ҧ� �� � ���������� �����.

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
