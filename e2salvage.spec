Summary:	e2salvage is a utility which tries to recover a data from damaged ext2.
Name:		e2salvage
Version:	0.0.8a
Release:	0.1
License:	GPL
Group:		cos
######		Unknown group!
Source0:	http://dl.sourceforge.net/e2salvage/%{name}-%{version}.tbz2
# Source0-md5:	029608f5f42890aabd1a2c889de859ad
Patch0:		%{name}-BLKGETSIZE64.patch
URL:		http://e2salvage.sourceforge.net/
#BuildRequires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
e2salvage is a utility which tries to recover a data from damaged ext2
filesystems. Unlike e2fsck, it does not look for the data at
particular places and it don't tend to believe the data it finds; thus
it can handle much more damaged filesystem.

fsck connects the found i-nodes to lost+found directory e2salvage
instead tries to recover the directory structure. If all else fails
the directories are linked to the root.

%prep
%setup -q
%patch0 -p1

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
