#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-geometry
Version  : 0.4.6
Release  : 51
URL      : https://cran.r-project.org/src/contrib/geometry_0.4.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/geometry_0.4.6.tar.gz
Summary  : Mesh Generation and Surface Tessellation
Group    : Development/Tools
License  : GPL-3.0 Qhull
Requires: R-geometry-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppProgress
Requires: R-linprog
Requires: R-lpSolve
Requires: R-magic
BuildRequires : R-Rcpp
BuildRequires : R-RcppProgress
BuildRequires : R-linprog
BuildRequires : R-lpSolve
BuildRequires : R-magic
BuildRequires : buildreq-R

%description
available in R, in a similar manner as in Octave and MATLAB. Qhull
    computes convex hulls, Delaunay triangulations, halfspace
    intersections about a point, Voronoi diagrams, furthest-site
    Delaunay triangulations, and furthest-site Voronoi diagrams. It
    runs in 2D, 3D, 4D, and higher dimensions. It implements the
    Quickhull algorithm for computing the convex hull. Qhull does not
    support constrained Delaunay triangulations, or mesh generation of
    non-convex objects, but the package does include some R functions
    that allow for this.

%package lib
Summary: lib components for the R-geometry package.
Group: Libraries

%description lib
lib components for the R-geometry package.


%prep
%setup -q -c -n geometry
cd %{_builddir}/geometry

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650296312

%install
export SOURCE_DATE_EPOCH=1650296312
rm -rf %{buildroot}
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library geometry
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library geometry
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library geometry
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc geometry || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/geometry/DESCRIPTION
/usr/lib64/R/library/geometry/INDEX
/usr/lib64/R/library/geometry/Meta/Rd.rds
/usr/lib64/R/library/geometry/Meta/demo.rds
/usr/lib64/R/library/geometry/Meta/features.rds
/usr/lib64/R/library/geometry/Meta/hsearch.rds
/usr/lib64/R/library/geometry/Meta/links.rds
/usr/lib64/R/library/geometry/Meta/nsInfo.rds
/usr/lib64/R/library/geometry/Meta/package.rds
/usr/lib64/R/library/geometry/Meta/vignette.rds
/usr/lib64/R/library/geometry/NAMESPACE
/usr/lib64/R/library/geometry/NEWS
/usr/lib64/R/library/geometry/R/geometry
/usr/lib64/R/library/geometry/R/geometry.rdb
/usr/lib64/R/library/geometry/R/geometry.rdx
/usr/lib64/R/library/geometry/WORDLIST
/usr/lib64/R/library/geometry/demo/intersectn.R
/usr/lib64/R/library/geometry/doc/LICENSE-NOTES
/usr/lib64/R/library/geometry/doc/MODIFIED.txt
/usr/lib64/R/library/geometry/doc/index.html
/usr/lib64/R/library/geometry/doc/qhull-eg.R
/usr/lib64/R/library/geometry/doc/qhull-eg.Rnw
/usr/lib64/R/library/geometry/doc/qhull-eg.pdf
/usr/lib64/R/library/geometry/doc/qhull/Announce.txt
/usr/lib64/R/library/geometry/doc/qhull/COPYING.txt
/usr/lib64/R/library/geometry/doc/qhull/File_id.diz
/usr/lib64/R/library/geometry/doc/qhull/README.txt
/usr/lib64/R/library/geometry/doc/qhull/REGISTER.txt
/usr/lib64/R/library/geometry/doc/qhull/html/index.html
/usr/lib64/R/library/geometry/doc/qhull/html/normal_voronoi_knauss_oesterle.jpg
/usr/lib64/R/library/geometry/doc/qhull/html/qconvex.html
/usr/lib64/R/library/geometry/doc/qhull/html/qdelau_f.html
/usr/lib64/R/library/geometry/doc/qhull/html/qdelaun.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh--4d.gif
/usr/lib64/R/library/geometry/doc/qhull/html/qh--cone.gif
/usr/lib64/R/library/geometry/doc/qhull/html/qh--dt.gif
/usr/lib64/R/library/geometry/doc/qhull/html/qh--geom.gif
/usr/lib64/R/library/geometry/doc/qhull/html/qh--half.gif
/usr/lib64/R/library/geometry/doc/qhull/html/qh--rand.gif
/usr/lib64/R/library/geometry/doc/qhull/html/qh-code.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh-eg.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh-faq.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh-get.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh-impre.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh-optc.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh-optf.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh-optg.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh-opto.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh-optp.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh-optq.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh-optt.html
/usr/lib64/R/library/geometry/doc/qhull/html/qh-quick.html
/usr/lib64/R/library/geometry/doc/qhull/html/qhalf.html
/usr/lib64/R/library/geometry/doc/qhull/html/qhull-cpp.xml
/usr/lib64/R/library/geometry/doc/qhull/html/qhull.html
/usr/lib64/R/library/geometry/doc/qhull/html/qhull.man
/usr/lib64/R/library/geometry/doc/qhull/html/qhull.txt
/usr/lib64/R/library/geometry/doc/qhull/html/qvoron_f.html
/usr/lib64/R/library/geometry/doc/qhull/html/qvoronoi.html
/usr/lib64/R/library/geometry/doc/qhull/html/rbox.html
/usr/lib64/R/library/geometry/doc/qhull/html/rbox.man
/usr/lib64/R/library/geometry/doc/qhull/html/rbox.txt
/usr/lib64/R/library/geometry/doc/qhull/index.html
/usr/lib64/R/library/geometry/extdata/error_15_620.RData
/usr/lib64/R/library/geometry/extdata/halfspacen.RData
/usr/lib64/R/library/geometry/extdata/intersectn4D.RData
/usr/lib64/R/library/geometry/extdata/issue35-intersectn.RData
/usr/lib64/R/library/geometry/extdata/ordination.Rdata
/usr/lib64/R/library/geometry/extdata/overlap260-5034.RData
/usr/lib64/R/library/geometry/extdata/save-overlap149-9428.RData
/usr/lib64/R/library/geometry/extdata/save-overlap32-176.RData
/usr/lib64/R/library/geometry/extdata/save-overlap68-557.RData
/usr/lib64/R/library/geometry/help/AnIndex
/usr/lib64/R/library/geometry/help/aliases.rds
/usr/lib64/R/library/geometry/help/geometry.rdb
/usr/lib64/R/library/geometry/help/geometry.rdx
/usr/lib64/R/library/geometry/help/paths.rds
/usr/lib64/R/library/geometry/html/00Index.html
/usr/lib64/R/library/geometry/html/R.css
/usr/lib64/R/library/geometry/tests/spelling.R
/usr/lib64/R/library/geometry/tests/testthat.R
/usr/lib64/R/library/geometry/tests/testthat/test-cart2pol.R
/usr/lib64/R/library/geometry/tests/testthat/test-cart2sph.R
/usr/lib64/R/library/geometry/tests/testthat/test-convhulln.R
/usr/lib64/R/library/geometry/tests/testthat/test-delaunayn.R
/usr/lib64/R/library/geometry/tests/testthat/test-distmesh2d.R
/usr/lib64/R/library/geometry/tests/testthat/test-extprod3d.R
/usr/lib64/R/library/geometry/tests/testthat/test-halfspacen.R
/usr/lib64/R/library/geometry/tests/testthat/test-inhulln.R
/usr/lib64/R/library/geometry/tests/testthat/test-intersectn.R
/usr/lib64/R/library/geometry/tests/testthat/test-parallel.R
/usr/lib64/R/library/geometry/tests/testthat/test-pol2cart.R
/usr/lib64/R/library/geometry/tests/testthat/test-polyarea.R
/usr/lib64/R/library/geometry/tests/testthat/test-sph2cart.R
/usr/lib64/R/library/geometry/tests/testthat/test-tsearch-tsearchn-comparison.R
/usr/lib64/R/library/geometry/tests/testthat/test-tsearch.R
/usr/lib64/R/library/geometry/tests/testthat/test-tsearchn.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/geometry/libs/geometry.so
/usr/lib64/R/library/geometry/libs/geometry.so.avx2
/usr/lib64/R/library/geometry/libs/geometry.so.avx512
