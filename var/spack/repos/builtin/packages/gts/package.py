# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gts(AutotoolsPackage):
    """GTS stands for the GNU Triangulated Surface Library.

    It is an Open Source Free Software Library intended to provide a set of
    useful functions to deal with 3D surfaces meshed with interconnected
    triangles. The source code is available free of charge under the Free
    Software LGPL license.

    The code is written entirely in C with an object-oriented approach
    based mostly on the design of GTK+. Careful attention is paid to
    performance related issues as the initial goal of GTS is to provide a
    simple and efficient library to scientists dealing with 3D computational
    surface meshes.
    """

    homepage = "http://gts.sourceforge.net/index.html"
    url = "http://gts.sourceforge.net/tarballs/gts-snapshot-121130.tar.gz"

    version('121130', '023ebb6b13b8707534182a3ef0d12908')

    depends_on('glib')
