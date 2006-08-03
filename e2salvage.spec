Summary:	e2salvage - a utility which tries to recover a data from damaged ext2
Summary(pl):	e2salvage - narzêdzie próbuj±ce odzyskaæ dane z uszkodzonego ext2
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
e2salvage to narzêdzie, które próbuje odzyskaæ dane z uszkodzonych
systemów plików ext2. W przeciwieñstwie do e2fsck nie szuka danych w
okre¶lonych miejscach i nie próbuje zaufaæ danym, które znajdzie;
dziêki temu mo¿e obs³u¿yæ du¿o bardziej uszkodzone systemy plików.

fsck do³±cza znalezione i-wêz³y do katalogu lost+found; e2salvage
zamiast tego próbuje odtworzyæ strukturê katalogów. Je¶li wszystko
inne zawiedzie, katalogi s± pod³±czane do g³ównego katalogu.

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
