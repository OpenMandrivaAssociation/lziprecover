Name:		lziprecover
Summary:	Data recovery tool and decompressor for lzipped files
Version:	1.13
Release:	2
License:	GPLv3+
Group:		Archiving/Compression
URL:		http://www.nongnu.org/lzip/lziprecover.html
Source0:	http://download.savannah.gnu.org/releases/lzip/%{name}-%{version}.tar.lz
BuildRequires:	lzip

%description
Lziprecover is a data recovery tool and decompressor for files in the lzip
compressed data format (.lz) able to repair slightly damaged files, recover
badly damaged files from two or more copies, extract undamaged members
from multi-member files, decompress files and test integrity of files.

Lziprecover is able to recover or decompress files produced by any
of the compressors in the lzip family; lzip, plzip, minilzip/lzlib, clzip
and pdlzip. This recovery capability contributes to make the lzip format one
of the best options for long-term data archiving.

Lziprecover is able to efficiently extract a range of bytes
from a multi-member file, because it only decompresses the members containing
the desired data.

Lziprecover can print correct total file sizes and ratios even for multi-member
files.

When recovering data, lziprecover takes as arguments the names of the damaged
files and writes zero or more recovered files depending on the operation
selected and whether the recovery succeeded or not. The damaged files
themselves are never modified.

When decompressing or testing file integrity, lziprecover behaves like lzip
or lunzip.

If the files are too damaged for lziprecover to repair them, data from damaged
members can be partially recovered writing it to stdout.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%{_bindir}/lziprecover
%{_mandir}/man1/lziprecover.1*
%{_infodir}/lziprecover.info*




%changelog
* Tue Mar 13 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.13-1
+ Revision: 784563
- imported package lziprecover

