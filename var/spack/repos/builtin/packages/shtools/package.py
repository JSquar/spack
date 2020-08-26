# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Shtools(MakefilePackage):
    """SHTOOLS - Spherical Harmonic Tools"""

    homepage = "https://shtools.github.io/SHTOOLS/"
    url      = "https://github.com/SHTOOLS/SHTOOLS/archive/v4.5.tar.gz"

    maintainers = ['eschnett']

    version('4.6.2', tag='v4.6.2')
    version('4.6.1', tag='v4.6.1')
    version('4.6', tag='v4.6')
    version('4.5.4', tag='v4.5.4')
    version('4.5.3', tag='v4.5.3')
    version('4.5.2', tag='v4.5.2')
    version('4.5.1', tag='v4.5.1')
    version('4.5', tag='v4.5')

    # Note: This package also provides Python wrappers. We do not
    # install these properly yet, only the Fortran library is
    # installed.

    variant('openmp', default=True, description="Enable OpenMP support")

    depends_on('blas')
    depends_on('fftw')
    depends_on('lapack')

    # Options for the Makefile
    def makeopts(self, spec, prefix):
        return [
            "F95={0}".format(self.compiler.fc),
            ("F95FLAGS={0} -O3 -std=f2003 -ffast-math".
             format(self.compiler.fc_pic_flag)),
            "OPENMPFLAGS={0}".format(self.compiler.openmp_flag),
            "BLAS={0}".format(spec['blas'].libs),
            "FFTW={0}".format(spec['fftw'].libs),
            "LAPACK={0}".format(spec['lapack'].libs),
            "PREFIX={0}".format(prefix),
        ]

    def build(self, spec, prefix):
        target = 'fortran-mp' if spec.satisfies('+openmp') else 'fortran'
        make(target, *self.makeopts(self, spec, prefix))

    def install(self, spec, prefix):
        make('install', *self.makeopts(self, spec, prefix))
