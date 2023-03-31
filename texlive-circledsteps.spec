Name:		texlive-circledsteps
Version:	63255
Release:	2
Summary:	Typeset circled numbers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/circledsteps
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/circledsteps.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/circledsteps.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package generates circled numbers (or other kinds of
markers or small text) to mark "steps" in procedures,
exercises, and so on.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/circledsteps
%doc %{_texmfdistdir}/doc/latex/circledsteps

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
