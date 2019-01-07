# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Psmc(MakefilePackage):
    """mplementation of the Pairwise Sequentially Markovian Coalescent
    (PSMC) model"""

    homepage = "https://github.com/lh3/psmc"
    git      = "https://github.com/lh3/psmc.git"

    version('2016-1-21', commit='e5f7df5d00bb75ec603ae0beff62c0d7e37640b9')

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', prefix.bin.utils)

    def build(self, spec, prefix):
        make()
        with working_dir('utils'):
            make()

    def install(self, spec, prefix):
        install_tree(self.build_directory, prefix.bin)
