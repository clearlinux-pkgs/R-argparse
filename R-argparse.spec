#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-argparse
Version  : 2.2.2
Release  : 60
URL      : https://cran.r-project.org/src/contrib/argparse_2.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/argparse_2.2.2.tar.gz
Summary  : Command Line Optional and Positional Argument Parser
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ Python-2.0
Requires: R-argparse-license = %{version}-%{release}
Requires: R-R6
Requires: R-findpython
Requires: R-jsonlite
BuildRequires : R-R6
BuildRequires : R-findpython
BuildRequires : R-jsonlite
BuildRequires : buildreq-R

%description
be used with 'Rscript' to write "#!" shebang scripts that gracefully
    accept positional and optional arguments and automatically generate usage.

%package license
Summary: license components for the R-argparse package.
Group: Default

%description license
license components for the R-argparse package.


%prep
%setup -q -n argparse
cd %{_builddir}/argparse

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678810904

%install
export SOURCE_DATE_EPOCH=1678810904
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-argparse
cp %{_builddir}/argparse/COPYING %{buildroot}/usr/share/package-licenses/R-argparse/b47456e2c1f38c40346ff00db976a2badf36b5e3 || :
cp %{_builddir}/argparse/inst/COPYRIGHTS %{buildroot}/usr/share/package-licenses/R-argparse/17c5faeadf67d11dde5dddcbe03d97119e8a37d3 || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/argparse/COPYRIGHTS
/usr/lib64/R/library/argparse/DESCRIPTION
/usr/lib64/R/library/argparse/INDEX
/usr/lib64/R/library/argparse/Meta/Rd.rds
/usr/lib64/R/library/argparse/Meta/features.rds
/usr/lib64/R/library/argparse/Meta/hsearch.rds
/usr/lib64/R/library/argparse/Meta/links.rds
/usr/lib64/R/library/argparse/Meta/nsInfo.rds
/usr/lib64/R/library/argparse/Meta/package.rds
/usr/lib64/R/library/argparse/Meta/vignette.rds
/usr/lib64/R/library/argparse/NAMESPACE
/usr/lib64/R/library/argparse/NEWS.md
/usr/lib64/R/library/argparse/R/argparse
/usr/lib64/R/library/argparse/R/argparse.rdb
/usr/lib64/R/library/argparse/R/argparse.rdx
/usr/lib64/R/library/argparse/doc/argparse.R
/usr/lib64/R/library/argparse/doc/argparse.Rmd
/usr/lib64/R/library/argparse/doc/argparse.html
/usr/lib64/R/library/argparse/doc/index.html
/usr/lib64/R/library/argparse/exec/display_file.R
/usr/lib64/R/library/argparse/exec/example.R
/usr/lib64/R/library/argparse/help/AnIndex
/usr/lib64/R/library/argparse/help/aliases.rds
/usr/lib64/R/library/argparse/help/argparse.rdb
/usr/lib64/R/library/argparse/help/argparse.rdx
/usr/lib64/R/library/argparse/help/figures/logo.png
/usr/lib64/R/library/argparse/help/figures/logo.svg
/usr/lib64/R/library/argparse/help/paths.rds
/usr/lib64/R/library/argparse/html/00Index.html
/usr/lib64/R/library/argparse/html/R.css
/usr/lib64/R/library/argparse/tests/run-all.R
/usr/lib64/R/library/argparse/tests/testthat/scripts/test_help.R
/usr/lib64/R/library/argparse/tests/testthat/scripts/test_version.R
/usr/lib64/R/library/argparse/tests/testthat/test-argparse.R

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-argparse/17c5faeadf67d11dde5dddcbe03d97119e8a37d3
/usr/share/package-licenses/R-argparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
