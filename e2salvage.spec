Summary:	e2salvage - a utility which tries to recover a data from damaged ext2
Summary(pl):	e2salvage - narz�dzie pr�buj�ce odzyska� dane z uszkodzonego ext2
Name:		e2salvage
Version:	0.0.8a
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/e2salvage/%{name}-%{version}.tbz2
# Source0-md5:	029608f5f42890aabd1a2c889de859ad
Patch0:		%{name}-linux_types.patch
Patch1:		%{name}-gcc4.patch
Patch2:		%{name}-am.patch
URL:		http://e2salvage.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
e2salvage is a utility which tries to recover a data from damaged ext2
filesystems. Unlike e2fsck, it does not look for the data at
particular places and it don't tend to believe the data it finds; thus
it can handle much more damaged filesystem.

fsck connects the found i-nodes to lost+found directory; e2salvage
instead tries to recover the directory structure. If all else fails
the directories are linked to the root.

%description -l pl
e2salvage to narz�dzie, kt�re pr�buje odzyska� dane z uszkodzonych
system�w plik�w ext2. W przeciwie�stwie do e2fsck nie szuka danych w
okre�lonych miejscach i nie pr�buje zaufa� danym, kt�re znajdzie;
dzi�ki temu mo�e obs�u�y� du�o bardziej uszkodzone systemy plik�w.

fsck do��cza znalezione i-w�z�y do katalogu lost+found; e2salvage
zamiast tego pr�buje odtworzy� struktur� katalog�w. Je�li wszystko
inne zawiedzie, katalogi s� pod��czane do g��wnego katalogu.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
