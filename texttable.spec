#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : texttable
Version  : 0.9.1
Release  : 13
URL      : https://github.com/foutaise/texttable/archive/v0.9.1.tar.gz
Source0  : https://github.com/foutaise/texttable/archive/v0.9.1.tar.gz
Summary  : module for creating simple ASCII tables
Group    : Development/Tools
License  : LGPL-3.0
Requires: texttable-license = %{version}-%{release}
Requires: texttable-python = %{version}-%{release}
Requires: texttable-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
characters.

%package license
Summary: license components for the texttable package.
Group: Default

%description license
license components for the texttable package.


%package python
Summary: python components for the texttable package.
Group: Default
Requires: texttable-python3 = %{version}-%{release}

%description python
python components for the texttable package.


%package python3
Summary: python3 components for the texttable package.
Group: Default
Requires: python3-core
Provides: pypi(texttable)

%description python3
python3 components for the texttable package.


%prep
%setup -q -n texttable-0.9.1
cd %{_builddir}/texttable-0.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603406061
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/texttable
cp %{_builddir}/texttable-0.9.1/LICENSE %{buildroot}/usr/share/package-licenses/texttable/f45ee1c765646813b442ca58de72e20a64a7ddba
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/texttable/f45ee1c765646813b442ca58de72e20a64a7ddba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
