#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-argparse
Version  : 1.1.1
Release  : 9
URL      : https://cran.r-project.org/src/contrib/argparse_1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/argparse_1.1.1.tar.gz
Summary  : Command Line Optional and Positional Argument Parser
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ Python-2.0
Requires: R-evaluate
Requires: R-findpython
Requires: R-getopt
Requires: R-jsonlite
Requires: R-proto
Requires: R-stringi
BuildRequires : R-evaluate
BuildRequires : R-findpython
BuildRequires : R-getopt
BuildRequires : R-jsonlite
BuildRequires : R-proto
BuildRequires : R-stringi
BuildRequires : clr-R-helpers

%description
be used with Rscript to write "#!" shebang scripts that gracefully
    accept positional and optional arguments and automatically generate usage.

%prep
%setup -q -c -n argparse

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523288328

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523288328
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library argparse
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library argparse
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library argparse
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library argparse|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/argparse/NEWS
/usr/lib64/R/library/argparse/R/argparse
/usr/lib64/R/library/argparse/R/argparse.rdb
/usr/lib64/R/library/argparse/R/argparse.rdx
/usr/lib64/R/library/argparse/doc/argparse.R
/usr/lib64/R/library/argparse/doc/argparse.Rrst
/usr/lib64/R/library/argparse/doc/argparse.html
/usr/lib64/R/library/argparse/doc/index.html
/usr/lib64/R/library/argparse/exec/display_file.R
/usr/lib64/R/library/argparse/exec/example.R
/usr/lib64/R/library/argparse/help/AnIndex
/usr/lib64/R/library/argparse/help/aliases.rds
/usr/lib64/R/library/argparse/help/argparse.rdb
/usr/lib64/R/library/argparse/help/argparse.rdx
/usr/lib64/R/library/argparse/help/paths.rds
/usr/lib64/R/library/argparse/html/00Index.html
/usr/lib64/R/library/argparse/html/R.css
