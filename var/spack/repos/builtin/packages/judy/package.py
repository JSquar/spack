# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Judy(AutotoolsPackage):
    """Judy: General-purpose dynamic array, associative array and hash-trie."""
    homepage = "http://judy.sourceforge.net/"
    url      = "http://downloads.sourceforge.net/project/judy/judy/Judy-1.0.5/Judy-1.0.5.tar.gz"

    version('1.0.5', '115a0d26302676e962ae2f70ec484a54')

    parallel = False
