%global tl_name greektonoi
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Facilitates writing/editing of multiaccented greek
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/greek/greektonoi
License:	lgpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greektonoi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greektonoi.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The greektonoi mapping extends the betababel package or the babel
polutonikogreek option to provide a simple way to insert ancient Greek
texts with diacritical characters into your document using a similar
method to the commonly used Beta Code transliteration, but with much
more freedom. It is designed especially for the XeTeX engine and it
could also be used for fast and easy modification of monotonic greek
texts to polytonic. The output text is natively encoded in Unicode, so
it can be reused in any possible way. The greektonoi package provides,
in addition to inserting greek accents and breathings, many other
symbols used in greek numbers and arithmetic or in the greek archaic
period. It could be used with greektonoi mapping or indepedently.

