# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RVctrs(RPackage):
    """Defines new notions of prototype and size that are used to provide tools
    for consistent and well-founded type-coercion and size-recycling, and are
    in turn connected to ideas of type- and size-stability useful for analyzing
    function interfaces."""

    homepage = "https://github.com/r-lib/vctrs"
    url      = "https://cloud.r-project.org/src/contrib/vctrs_0.3.1.tar.gz"
    list_url = "https://cloud.r-project.org/src/contrib/Archive/vctrs"

    version('0.3.1', sha256='17e6358735504166ecb1aab581e5fa5e565ffb6f10e8a12c4d476a8e1f8aba08')
    version('0.3.0', sha256='f6ee13245e2507049706d3f45efa8d63cadae5359de3bfdcb5cccc5ac074c12b')
    version('0.2.4', sha256='dcc8b6bfd2d951d48d338a3d4deaaabfee356c0ee43169a6d6b06ea78cfe4f97')
    version('0.2.3', sha256='1c716d100a6c8e7f5aaa025ff4a5bd001b4da72ab71b85070259f31b6eb7d2de')
    version('0.2.2', sha256='0dab9120ba88ad98acd91248568f541c5715e93a4c753ec0a8bba82269951d01')
    version('0.2.1', sha256='e04f0b16c265fd0af8660b8768c8f53fded638a61c624a642d7a6cb8b7939c66')
    version('0.2.0', sha256='5bce8f228182ecaa51230d00ad8a018de9cf2579703e82244e0931fe31f20016')
    version('0.1.0', sha256='cc28febd74b4c7800076ac4d2c628755125981bdd3ebf295bb3952753fca818f')

    depends_on('r@3.2:', type=('build', 'run'))
    depends_on('r-backports', type=('build', 'run'))
    depends_on('r-ellipsis@0.2.0:', type=('build', 'run'))
    depends_on('r-digest', type=('build', 'run'))
    depends_on('r-glue', type=('build', 'run'))
    depends_on('r-rlang@0.4.0:', type=('build', 'run'))
    depends_on('r-zeallot', type=('build', 'run'))
