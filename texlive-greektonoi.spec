Name:		texlive-greektonoi
Version:	39419
Release:	2
Summary:	Facilitates writing/editing of multiaccented greek
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/greektonoi
License:	lgpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greektonoi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greektonoi.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The greektonoi mapping extends the betababel package or the
babel polutonikogreek option to provide a simple way to insert
ancient Greek texts with diacritical characters into your
document using a similar method to the commonly used Beta Code
transliteration, but with much more freedom. It is designed
especially for the XeTeX engine and it could also be used for
fast and easy modification of monotonic greek texts to
polytonic. The output text is natively encoded in Unicode, so
it can be reused in any possible way. The greektonoi package
provides, in addition to inserting greek accents and
breathings, many other symbols used in greek numbers and
arithmetic or in the greek archaic period. It could be used
with greektonoi mapping or indepedently.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/greektonoi
%{_texmfdistdir}/fonts/map/dvips/greektonoi
%doc %{_texmfdistdir}/doc/latex/greektonoi

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
