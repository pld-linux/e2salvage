Summary:	e2salvage - a utility which tries to recover a data from damaged ext2
Summary(pl.UTF-8):	e2salvage - narzędzie próbujące odzyskać dane z uszkodzonego ext2
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
Patch3:		%{name}-no-geob.patch
Patch4:		%{name}-fs_include.patch
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

%description -l pl.UTF-8
e2salvage to narzędzie, które próbuje odzyskać dane z uszkodzonych
systemów plików ext2. W przeciwieństwie do e2fsck nie szuka danych w
określonych miejscach i nie próbuje zaufać danym, które znajdzie;
dzięki temu może obsłużyć dużo bardziej uszkodzone systemy plików.

fsck dołącza znalezione i-węzły do katalogu lost+found; e2salvage
zamiast tego próbuje odtworzyć strukturę katalogów. Jeśli wszystko
inne zawiedzie, katalogi są podłączane do głównego katalogu.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

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
