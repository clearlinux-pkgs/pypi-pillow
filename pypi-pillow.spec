#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pillow
Version  : 9.1.1
Release  : 92
URL      : https://files.pythonhosted.org/packages/43/6e/59853546226ee6200f9ba6e574d11604b60ad0754d2cbd1c8f3246b70418/Pillow-9.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/43/6e/59853546226ee6200f9ba6e574d11604b60ad0754d2cbd1c8f3246b70418/Pillow-9.1.1.tar.gz
Summary  : Python Imaging Library (Fork)
Group    : Development/Tools
License  : Apache-2.0 HPND MIT NTP OFL-1.0
Requires: pypi-pillow-filemap = %{version}-%{release}
Requires: pypi-pillow-lib = %{version}-%{release}
Requires: pypi-pillow-license = %{version}-%{release}
Requires: pypi-pillow-python = %{version}-%{release}
Requires: pypi-pillow-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : freetype-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev
Patch1: 0001-Fix-build-Add-default-libdir.patch

%description
<p align="center">
<img width="248" height="250" src="https://raw.githubusercontent.com/python-pillow/pillow-logo/main/pillow-logo-248x250.png" alt="Pillow logo">
</p>

%package filemap
Summary: filemap components for the pypi-pillow package.
Group: Default

%description filemap
filemap components for the pypi-pillow package.


%package lib
Summary: lib components for the pypi-pillow package.
Group: Libraries
Requires: pypi-pillow-license = %{version}-%{release}
Requires: pypi-pillow-filemap = %{version}-%{release}

%description lib
lib components for the pypi-pillow package.


%package license
Summary: license components for the pypi-pillow package.
Group: Default

%description license
license components for the pypi-pillow package.


%package python
Summary: python components for the pypi-pillow package.
Group: Default
Requires: pypi-pillow-python3 = %{version}-%{release}

%description python
python components for the pypi-pillow package.


%package python3
Summary: python3 components for the pypi-pillow package.
Group: Default
Requires: pypi-pillow-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(pillow)

%description python3
python3 components for the pypi-pillow package.


%prep
%setup -q -n Pillow-9.1.1
cd %{_builddir}/Pillow-9.1.1
%patch1 -p1
pushd ..
cp -a Pillow-9.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653351453
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pillow
cp %{_builddir}/Pillow-9.1.1/Tests/fonts/DejaVuSans/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pillow/3d95e2c3b731545390f6888a3214cf7b51fb7971
cp %{_builddir}/Pillow-9.1.1/Tests/fonts/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pillow/9deb27f8f5fea69a2ab1624ed0698a0c8168ed49
cp %{_builddir}/Pillow-9.1.1/Tests/icc/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pillow/371117588643c602bb8f15b280424e938c34c369
cp %{_builddir}/Pillow-9.1.1/src/thirdparty/raqm/COPYING %{buildroot}/usr/share/package-licenses/pypi-pillow/0e373369e12062eb1d6f4f3df0c41086f8320eb3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-pillow

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pillow/0e373369e12062eb1d6f4f3df0c41086f8320eb3
/usr/share/package-licenses/pypi-pillow/371117588643c602bb8f15b280424e938c34c369
/usr/share/package-licenses/pypi-pillow/3d95e2c3b731545390f6888a3214cf7b51fb7971
/usr/share/package-licenses/pypi-pillow/9deb27f8f5fea69a2ab1624ed0698a0c8168ed49

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
