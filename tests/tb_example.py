#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    15.10.2014 10:22:43 CEST
# File:    tbexample.py

import sys
sys.path.append('../')
import z2pack

from common import *

import types
import unittest


class TbExampleTestCase(CommonTestCase):

    def createH(self, t1, t2):

        self.H = z2pack.tb.Hamilton()

        # create the two atoms
        self.H.add_atom(([1, 1], 1), [0, 0, 0])
        self.H.add_atom(([-1, -1], 1), [0.5, 0.5, 0])

        # add hopping between different atoms
        self.H.add_hopping(((0, 0), (1, 1)),
                           z2pack.tb.vectors.combine([0, -1], [0, -1], 0),
                           t1,
                           phase=[1, -1j, 1j, -1])
        self.H.add_hopping(((0, 1), (1, 0)),
                           z2pack.tb.vectors.combine([0, -1], [0, -1], 0),
                           t1,
                           phase=[1, 1j, -1j, -1])

        # add hopping between neighbouring orbitals of the same type
        self.H.add_hopping((((0, 0), (0, 0)), ((0, 1), (0, 1))),
                           z2pack.tb.vectors.neighbours([0, 1],
                                                        forward_only=True),
                           t2,
                           phase=[1])
        self.H.add_hopping((((1, 1), (1, 1)), ((1, 0), (1, 0))),
                           z2pack.tb.vectors.neighbours([0, 1],
                                                        forward_only=True),
                           -t2,
                           phase=[1])

    # this test may produce false negatives due to small numerical differences
    def test_res1(self):
        self.createH(0.2, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_surface = tb_system.surface(lambda kx: [kx / 2, 0, 0], [0, 1, 0])
        tb_surface.wcc_calc(verbose=False, num_strings=20, use_pickle=False)
        
        res = {'t_par': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'wcc': [[0.49983964546467036, 0.50016035453532992], [0.49890749383729088, 0.50109250616270928], [0.49641395036486252, 0.50358604963513764], [0.49554883941587446, 0.50445116058412554], [0.49652567629394373, 0.5034743237060566], [0.49035854882904767, 0.50964145117095228], [0.48929271594465651, 0.51070728405534349], [0.48629705364229231, 0.51370294635770786], [0.48121568261281716, 0.51878431738718289], [0.47656990584661874, 0.52343009415338138], [0.46885612423665834, 0.53114387576334154], [0.45994586240888752, 0.54005413759111265], [0.44382468776376022, 0.55617531223623984], [0.42061785313061933, 0.57938214686938083], [0.38642332240609834, 0.61357667759390166], [0.32658906586480302, 0.67341093413519704], [0.25031056908157867, 0.74968943091842122], [0.16633894442945449, 0.83366105557054559], [0.081605641698089357, 0.91839435830191074], [0.0038664353524984706, 0.99613356464750147]], 'lambda_': [array([[ -9.99999492e-01 -9.92567525e-04j,
          1.56195090e-04 -7.44566277e-05j],
       [ -1.56195090e-04 -7.44566277e-05j,
         -9.99999492e-01 +9.92567525e-04j]]), array([[ -9.99976440e-01+0.00685828j,   1.65042418e-04-0.00023731j],
       [ -1.65042418e-04-0.00023731j,  -9.99976440e-01-0.00685828j]]), array([[ -9.99746169e-01+0.02229083j,   9.82852061e-04-0.00312242j],
       [ -9.82852061e-04-0.00312242j,  -9.99746169e-01-0.02229083j]]), array([[ -9.99608936e-01+0.0277925j ,  -8.67704424e-04-0.00296634j],
       [  8.67704424e-04-0.00296634j,  -9.99608936e-01-0.0277925j ]]), array([[-0.99976174+0.01898529j,  0.00679502-0.00835775j],
       [-0.00679502-0.00835775j, -0.99976174-0.01898529j]]), array([[-0.99816565+0.06034263j, -0.00489521+0.00036763j],
       [ 0.00489521+0.00036763j, -0.99816565-0.06034263j]]), array([[ -9.97737833e-01+0.06722225j,  -4.88660382e-04+0.00038147j],
       [  4.88660382e-04+0.00038147j,  -9.97737833e-01-0.06722225j]]), array([[-0.99629584+0.08591383j,  0.00357199-0.00080513j],
       [-0.00357199-0.00080513j, -0.99629584-0.08591383j]]), array([[-0.99304309+0.11754962j, -0.00686562-0.00060986j],
       [ 0.00686562-0.00060986j, -0.99304309-0.11754962j]]), array([[-0.98918334+0.14653749j, -0.00648987-0.00098632j],
       [ 0.00648987-0.00098632j, -0.98918334-0.14653749j]]), array([[-0.98091515+0.19277782j, -0.02529956-0.00145494j],
       [ 0.02529956-0.00145494j, -0.98091515-0.19277782j]]), array([[-0.96849851+0.2487902j , -0.01066998+0.00046992j],
       [ 0.01066998+0.00046992j, -0.96849851-0.2487902j ]]), array([[-0.93835366+0.34552154j, -0.00360836+0.00970883j],
       [ 0.00360836+0.00970883j, -0.93835366-0.34552154j]]), array([[-0.87817028 +4.76122251e-01j, -0.04609146 +3.69386018e-04j],
       [ 0.04609146 +3.69386018e-04j, -0.87817028 -4.76122251e-01j]]), array([[-0.75599511+0.6176916j ,  0.21651530+0.00704393j],
       [-0.21651530+0.00704393j, -0.75599511-0.6176916j ]]), array([[-0.46286388+0.88565229j,  0.03554074-0.01067226j],
       [-0.03554074-0.01067226j, -0.46286388-0.88565229j]]), array([[-0.00195136+0.99154875j,  0.03266646+0.12553949j],
       [-0.03266646+0.12553949j, -0.00195136-0.99154875j]]), array([[ 0.50178221+0.83696389j,  0.20143160-0.08444747j],
       [-0.20143160-0.08444747j,  0.50178221-0.83696389j]]), array([[ 0.87140197+0.490531j  , -0.00191005-0.00585538j],
       [ 0.00191005-0.00585538j,  0.87140197-0.490531j  ]]), array([[ 0.99970493+0.02151996j, -0.00708934-0.0087574j ],
       [ 0.00708934-0.0087574j ,  0.99970493-0.02151996j]])], 'kpt': [[0.0, 0, 0], [0.026315789473684209, 0, 0], [0.052631578947368418, 0, 0], [0.078947368421052627, 0, 0], [0.10526315789473684, 0, 0], [0.13157894736842105, 0, 0], [0.15789473684210525, 0, 0], [0.18421052631578946, 0, 0], [0.21052631578947367, 0, 0], [0.23684210526315788, 0, 0], [0.26315789473684209, 0, 0], [0.28947368421052633, 0, 0], [0.31578947368421051, 0, 0], [0.34210526315789469, 0, 0], [0.36842105263157893, 0, 0], [0.39473684210526316, 0, 0], [0.42105263157894735, 0, 0], [0.44736842105263153, 0, 0], [0.47368421052631576, 0, 0], [0.5, 0, 0]], 'gap': [0.0, 0.0, 0.0, 0.0, 2.2204460492503131e-16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5]}

        self.assertDictAlmostEqual(tb_surface.get_res(), res)

    def test_res2(self):
        """ test no_iter=True """
        self.createH(0, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_surface = tb_system.surface(lambda kx: [kx / 2, 0, 0], [0, 1, 0])
        tb_surface.wcc_calc(verbose=False,
                          num_strings=20,
                          use_pickle=False,
                          no_iter=True)

        res = {'t_par': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'wcc': [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.71428571428571419, 0.71428571428571419], [0.71428571428571419, 0.71428571428571419], [0.71428571428571419, 0.71428571428571419], [0.71428571428571419, 0.71428571428571419], [0.71428571428571419, 0.71428571428571419]], 'lambda_': [array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-1. -2.22044605e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -2.22044605e-16j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]]), array([[-0.22252093+0.97492791j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.22252093+0.97492791j]])], 'kpt': [[0.0, 0, 0], [0.026315789473684209, 0, 0], [0.052631578947368418, 0, 0], [0.078947368421052627, 0, 0], [0.10526315789473684, 0, 0], [0.13157894736842105, 0, 0], [0.15789473684210525, 0, 0], [0.18421052631578946, 0, 0], [0.21052631578947367, 0, 0], [0.23684210526315788, 0, 0], [0.26315789473684209, 0, 0], [0.28947368421052633, 0, 0], [0.31578947368421051, 0, 0], [0.34210526315789469, 0, 0], [0.36842105263157893, 0, 0], [0.39473684210526316, 0, 0], [0.42105263157894735, 0, 0], [0.44736842105263153, 0, 0], [0.47368421052631576, 0, 0], [0.5, 0, 0]], 'gap': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.21428571428571419, 0.21428571428571419, 0.21428571428571419, 0.21428571428571419, 0.21428571428571419]}

        self.assertDictAlmostEqual(tb_surface.get_res(), res)

    def test_res3(self):
        """ test no_neighbour_check=True """
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_surface = tb_system.surface(lambda kx: [kx / 2, 0, 0], [0, 1, 0])
        tb_surface.wcc_calc(verbose=False,
                          num_strings=20,
                          use_pickle=False,
                          no_neighbour_check=True)

        res = {'t_par': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'wcc': [[0.49996369258458911, 0.50003630741541083], [0.49969937950042137, 0.5003006204995788], [0.49921787497304743, 0.50078212502695296], [0.49870591461585301, 0.50129408538414699], [0.49847531395097933, 0.50152468604902101], [0.49764676757501669, 0.50235323242498353], [0.49681898534071861, 0.50318101465928156], [0.49599416659067369, 0.50400583340932625], [0.49472217792911855, 0.50527782207088145], [0.49276712834767228, 0.50723287165232778], [0.49022033200632836, 0.5097796679936718], [0.48587842661714503, 0.51412157338285491], [0.47823278374021649, 0.52176721625978362], [0.46251894588556092, 0.53748105411443925], [0.41753936610692016, 0.58246063389307956], [0.32876827340304077, 0.6712317265969594], [0.2378563145103029, 0.76214368548969713], [0.14764583792827177, 0.85235416207172832], [0.069572386836641423, 0.93042761316335876], [0.00064245928837270067, 0.99935754071162741]], 'lambda_': [array([[ -9.99999974e-01 -2.23545327e-04j,
          4.27619395e-05 -1.55072288e-05j],
       [ -4.27619395e-05 -1.55072288e-05j,
         -9.99999974e-01 +2.23545327e-04j]]), array([[ -9.99998216e-01+0.00188341j,   1.07083012e-05-0.00014284j],
       [ -1.07083012e-05-0.00014284j,  -9.99998216e-01-0.00188341j]]), array([[ -9.99987925e-01+0.00489331j,   8.24964719e-05+0.00044525j],
       [ -8.24964719e-05+0.00044525j,  -9.99987925e-01-0.00489331j]]), array([[ -9.99966944e-01+0.00811047j,  -7.95234595e-05-0.0005704j ],
       [  7.95234595e-05-0.0005704j ,  -9.99966944e-01-0.00811047j]]), array([[-0.99995411+0.00945613j,  0.00100862-0.00115568j],
       [-0.00100862-0.00115568j, -0.99995411-0.00945613j]]), array([[ -9.99890692e-01+0.01478066j,  -3.35399383e-04-0.00015281j],
       [  3.35399383e-04-0.00015281j,  -9.99890692e-01-0.01478066j]]), array([[ -9.99800268e-01 +1.99804456e-02j,
         -4.47837471e-04 +6.63243397e-05j],
       [  4.47837471e-04 +6.63243397e-05j,
         -9.99800268e-01 -1.99804456e-02j]]), array([[ -9.99683268e-01 +2.51647989e-02j,
         -3.11636362e-04 +1.98022133e-05j],
       [  3.11636362e-04 +1.98022133e-05j,
         -9.99683268e-01 -2.51647989e-02j]]), array([[-0.99945021 +3.31354094e-02j, -0.00115054 -7.20833867e-05j],
       [ 0.00115054 -7.20833867e-05j, -0.99945021 -3.31354094e-02j]]), array([[-0.99896753+0.04541153j, -0.00123325-0.00037616j],
       [ 0.00123325-0.00037616j, -0.99896753-0.04541153j]]), array([[-0.99811270 +6.13482024e-02j, -0.00272751 -8.45467378e-06j],
       [ 0.00272751 -8.45467379e-06j, -0.99811270 -6.13482024e-02j]]), array([[-0.99606621 +8.85955763e-02j, -0.00170786 -9.36480651e-05j],
       [ 0.00170786 -9.36480651e-05j, -0.99606621 -8.85955763e-02j]]), array([[ -9.90661901e-01+0.13632467j,  -5.20921706e-04+0.00207586j],
       [  5.20921706e-04+0.00207586j,  -9.90661901e-01-0.13632467j]]), array([[-0.97239770+0.23301292j, -0.01118212-0.00475878j],
       [ 0.01118212-0.00475878j, -0.97239770-0.23301292j]]), array([[-0.86875404+0.48596418j,  0.09509131-0.00792961j],
       [-0.09509131-0.00792961j, -0.86875404-0.48596418j]]), array([[-0.47495743+0.87996919j,  0.00827558-0.0010836j ],
       [-0.00827558-0.0010836j , -0.47495743-0.87996919j]]), array([[ 0.07622701+0.99364763j, -0.03905994-0.07299413j],
       [ 0.03905994-0.07299413j,  0.07622701-0.99364763j]]), array([[ 0.5996872+0.79929003j, -0.0283220+0.02661903j],
       [ 0.0283220+0.02661903j,  0.5996872-0.79929003j]]), array([[ 0.90596776+0.42328648j, -0.00274233-0.00659195j],
       [ 0.00274233-0.00659195j,  0.90596776-0.42328648j]]), array([[ 0.99999185-0.00324447j, -0.00104263-0.00216359j],
       [ 0.00104263-0.00216359j,  0.99999185+0.00324447j]])], 'kpt': [[0.0, 0, 0], [0.026315789473684209, 0, 0], [0.052631578947368418, 0, 0], [0.078947368421052627, 0, 0], [0.10526315789473684, 0, 0], [0.13157894736842105, 0, 0], [0.15789473684210525, 0, 0], [0.18421052631578946, 0, 0], [0.21052631578947367, 0, 0], [0.23684210526315788, 0, 0], [0.26315789473684209, 0, 0], [0.28947368421052633, 0, 0], [0.31578947368421051, 0, 0], [0.34210526315789469, 0, 0], [0.36842105263157893, 0, 0], [0.39473684210526316, 0, 0], [0.42105263157894735, 0, 0], [0.44736842105263153, 0, 0], [0.47368421052631576, 0, 0], [0.5, 0, 0]], 'gap': [0.0, 0.0, 2.2204460492503131e-16, 0.0, 2.2204460492503131e-16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99999999999999989, 0.0, 0.5, 0.5, 0.50000000000000011, 0.50000000000000011]}

        self.assertDictAlmostEqual(tb_surface.get_res(), res)

    def test_res4(self):
        """ test no_move_check=True """
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_surface = tb_system.surface(lambda kx: [kx / 2, 0, 0], [0, 1, 0])
        tb_surface.wcc_calc(verbose=False,
                          num_strings=20,
                          use_pickle=False,
                          no_move_check=True)

        res = {'t_par': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'wcc': [[0.49996369258458911, 0.50003630741541083], [0.49969937950042137, 0.5003006204995788], [0.49921787497304743, 0.50078212502695296], [0.49870591461585301, 0.50129408538414699], [0.49847531395097933, 0.50152468604902101], [0.49764676757501669, 0.50235323242498353], [0.49681898534071861, 0.50318101465928156], [0.49599416659067369, 0.50400583340932625], [0.49472217792911855, 0.50527782207088145], [0.49276712834767228, 0.50723287165232778], [0.49022033200632836, 0.5097796679936718], [0.48587842661714503, 0.51412157338285491], [0.47823278374021649, 0.52176721625978362], [0.46251894588556092, 0.53748105411443925], [0.41753936610692016, 0.58246063389307956], [0.32876827340304077, 0.6712317265969594], [0.2378563145103029, 0.76214368548969713], [0.14764583792827177, 0.85235416207172832], [0.069572386836641423, 0.93042761316335876], [0.00064245928837270067, 0.99935754071162741]], 'lambda_': [array([[ -9.99999974e-01 -2.23545327e-04j,
          4.27619395e-05 -1.55072288e-05j],
       [ -4.27619395e-05 -1.55072288e-05j,
         -9.99999974e-01 +2.23545327e-04j]]), array([[ -9.99998216e-01+0.00188341j,   1.07083012e-05-0.00014284j],
       [ -1.07083012e-05-0.00014284j,  -9.99998216e-01-0.00188341j]]), array([[ -9.99987925e-01+0.00489331j,   8.24964719e-05+0.00044525j],
       [ -8.24964719e-05+0.00044525j,  -9.99987925e-01-0.00489331j]]), array([[ -9.99966944e-01+0.00811047j,  -7.95234595e-05-0.0005704j ],
       [  7.95234595e-05-0.0005704j ,  -9.99966944e-01-0.00811047j]]), array([[-0.99995411+0.00945613j,  0.00100862-0.00115568j],
       [-0.00100862-0.00115568j, -0.99995411-0.00945613j]]), array([[ -9.99890692e-01+0.01478066j,  -3.35399383e-04-0.00015281j],
       [  3.35399383e-04-0.00015281j,  -9.99890692e-01-0.01478066j]]), array([[ -9.99800268e-01 +1.99804456e-02j,
         -4.47837471e-04 +6.63243397e-05j],
       [  4.47837471e-04 +6.63243397e-05j,
         -9.99800268e-01 -1.99804456e-02j]]), array([[ -9.99683268e-01 +2.51647989e-02j,
         -3.11636362e-04 +1.98022133e-05j],
       [  3.11636362e-04 +1.98022133e-05j,
         -9.99683268e-01 -2.51647989e-02j]]), array([[-0.99945021 +3.31354094e-02j, -0.00115054 -7.20833867e-05j],
       [ 0.00115054 -7.20833867e-05j, -0.99945021 -3.31354094e-02j]]), array([[-0.99896753+0.04541153j, -0.00123325-0.00037616j],
       [ 0.00123325-0.00037616j, -0.99896753-0.04541153j]]), array([[-0.99811270 +6.13482024e-02j, -0.00272751 -8.45467378e-06j],
       [ 0.00272751 -8.45467379e-06j, -0.99811270 -6.13482024e-02j]]), array([[-0.99606621 +8.85955763e-02j, -0.00170786 -9.36480651e-05j],
       [ 0.00170786 -9.36480651e-05j, -0.99606621 -8.85955763e-02j]]), array([[ -9.90661901e-01+0.13632467j,  -5.20921706e-04+0.00207586j],
       [  5.20921706e-04+0.00207586j,  -9.90661901e-01-0.13632467j]]), array([[-0.97239770+0.23301292j, -0.01118212-0.00475878j],
       [ 0.01118212-0.00475878j, -0.97239770-0.23301292j]]), array([[-0.86875404+0.48596418j,  0.09509131-0.00792961j],
       [-0.09509131-0.00792961j, -0.86875404-0.48596418j]]), array([[-0.47495743+0.87996919j,  0.00827558-0.0010836j ],
       [-0.00827558-0.0010836j , -0.47495743-0.87996919j]]), array([[ 0.07622701+0.99364763j, -0.03905994-0.07299413j],
       [ 0.03905994-0.07299413j,  0.07622701-0.99364763j]]), array([[ 0.5996872+0.79929003j, -0.0283220+0.02661903j],
       [ 0.0283220+0.02661903j,  0.5996872-0.79929003j]]), array([[ 0.90596776+0.42328648j, -0.00274233-0.00659195j],
       [ 0.00274233-0.00659195j,  0.90596776-0.42328648j]]), array([[ 0.99999185-0.00324447j, -0.00104263-0.00216359j],
       [ 0.00104263-0.00216359j,  0.99999185+0.00324447j]])], 'kpt': [[0.0, 0, 0], [0.026315789473684209, 0, 0], [0.052631578947368418, 0, 0], [0.078947368421052627, 0, 0], [0.10526315789473684, 0, 0], [0.13157894736842105, 0, 0], [0.15789473684210525, 0, 0], [0.18421052631578946, 0, 0], [0.21052631578947367, 0, 0], [0.23684210526315788, 0, 0], [0.26315789473684209, 0, 0], [0.28947368421052633, 0, 0], [0.31578947368421051, 0, 0], [0.34210526315789469, 0, 0], [0.36842105263157893, 0, 0], [0.39473684210526316, 0, 0], [0.42105263157894735, 0, 0], [0.44736842105263153, 0, 0], [0.47368421052631576, 0, 0], [0.5, 0, 0]], 'gap': [0.0, 0.0, 2.2204460492503131e-16, 0.0, 2.2204460492503131e-16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99999999999999989, 0.0, 0.5, 0.5, 0.50000000000000011, 0.50000000000000011]}

        self.assertDictAlmostEqual(tb_surface.get_res(), res)

    def test_res5(self):
        """ test no_neighbour_check=True and no_move_check=True"""
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_surface = tb_system.surface(lambda kx: [kx / 2, 0, 0], [0, 1, 0])
        tb_surface.wcc_calc(verbose=False,
                            num_strings=20,
                            use_pickle=False,
                            no_neighbour_check=True,
                            no_move_check=True)

        res = {'t_par': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'wcc': [[0.49996369258458911, 0.50003630741541083], [0.49969937950042137, 0.5003006204995788], [0.49921787497304743, 0.50078212502695296], [0.49870591461585301, 0.50129408538414699], [0.49847531395097933, 0.50152468604902101], [0.49764676757501669, 0.50235323242498353], [0.49681898534071861, 0.50318101465928156], [0.49599416659067369, 0.50400583340932625], [0.49472217792911855, 0.50527782207088145], [0.49276712834767228, 0.50723287165232778], [0.49022033200632836, 0.5097796679936718], [0.48587842661714503, 0.51412157338285491], [0.47823278374021649, 0.52176721625978362], [0.46251894588556092, 0.53748105411443925], [0.41753936610692016, 0.58246063389307956], [0.32876827340304077, 0.6712317265969594], [0.2378563145103029, 0.76214368548969713], [0.14764583792827177, 0.85235416207172832], [0.069572386836641423, 0.93042761316335876], [0.00064245928837270067, 0.99935754071162741]], 'lambda_': [array([[ -9.99999974e-01 -2.23545327e-04j,
          4.27619395e-05 -1.55072288e-05j],
       [ -4.27619395e-05 -1.55072288e-05j,
         -9.99999974e-01 +2.23545327e-04j]]), array([[ -9.99998216e-01+0.00188341j,   1.07083012e-05-0.00014284j],
       [ -1.07083012e-05-0.00014284j,  -9.99998216e-01-0.00188341j]]), array([[ -9.99987925e-01+0.00489331j,   8.24964719e-05+0.00044525j],
       [ -8.24964719e-05+0.00044525j,  -9.99987925e-01-0.00489331j]]), array([[ -9.99966944e-01+0.00811047j,  -7.95234595e-05-0.0005704j ],
       [  7.95234595e-05-0.0005704j ,  -9.99966944e-01-0.00811047j]]), array([[-0.99995411+0.00945613j,  0.00100862-0.00115568j],
       [-0.00100862-0.00115568j, -0.99995411-0.00945613j]]), array([[ -9.99890692e-01+0.01478066j,  -3.35399383e-04-0.00015281j],
       [  3.35399383e-04-0.00015281j,  -9.99890692e-01-0.01478066j]]), array([[ -9.99800268e-01 +1.99804456e-02j,
         -4.47837471e-04 +6.63243397e-05j],
       [  4.47837471e-04 +6.63243397e-05j,
         -9.99800268e-01 -1.99804456e-02j]]), array([[ -9.99683268e-01 +2.51647989e-02j,
         -3.11636362e-04 +1.98022133e-05j],
       [  3.11636362e-04 +1.98022133e-05j,
         -9.99683268e-01 -2.51647989e-02j]]), array([[-0.99945021 +3.31354094e-02j, -0.00115054 -7.20833867e-05j],
       [ 0.00115054 -7.20833867e-05j, -0.99945021 -3.31354094e-02j]]), array([[-0.99896753+0.04541153j, -0.00123325-0.00037616j],
       [ 0.00123325-0.00037616j, -0.99896753-0.04541153j]]), array([[-0.99811270 +6.13482024e-02j, -0.00272751 -8.45467378e-06j],
       [ 0.00272751 -8.45467379e-06j, -0.99811270 -6.13482024e-02j]]), array([[-0.99606621 +8.85955763e-02j, -0.00170786 -9.36480651e-05j],
       [ 0.00170786 -9.36480651e-05j, -0.99606621 -8.85955763e-02j]]), array([[ -9.90661901e-01+0.13632467j,  -5.20921706e-04+0.00207586j],
       [  5.20921706e-04+0.00207586j,  -9.90661901e-01-0.13632467j]]), array([[-0.97239770+0.23301292j, -0.01118212-0.00475878j],
       [ 0.01118212-0.00475878j, -0.97239770-0.23301292j]]), array([[-0.86875404+0.48596418j,  0.09509131-0.00792961j],
       [-0.09509131-0.00792961j, -0.86875404-0.48596418j]]), array([[-0.47495743+0.87996919j,  0.00827558-0.0010836j ],
       [-0.00827558-0.0010836j , -0.47495743-0.87996919j]]), array([[ 0.07622701+0.99364763j, -0.03905994-0.07299413j],
       [ 0.03905994-0.07299413j,  0.07622701-0.99364763j]]), array([[ 0.5996872+0.79929003j, -0.0283220+0.02661903j],
       [ 0.0283220+0.02661903j,  0.5996872-0.79929003j]]), array([[ 0.90596776+0.42328648j, -0.00274233-0.00659195j],
       [ 0.00274233-0.00659195j,  0.90596776-0.42328648j]]), array([[ 0.99999185-0.00324447j, -0.00104263-0.00216359j],
       [ 0.00104263-0.00216359j,  0.99999185+0.00324447j]])], 'kpt': [[0.0, 0, 0], [0.026315789473684209, 0, 0], [0.052631578947368418, 0, 0], [0.078947368421052627, 0, 0], [0.10526315789473684, 0, 0], [0.13157894736842105, 0, 0], [0.15789473684210525, 0, 0], [0.18421052631578946, 0, 0], [0.21052631578947367, 0, 0], [0.23684210526315788, 0, 0], [0.26315789473684209, 0, 0], [0.28947368421052633, 0, 0], [0.31578947368421051, 0, 0], [0.34210526315789469, 0, 0], [0.36842105263157893, 0, 0], [0.39473684210526316, 0, 0], [0.42105263157894735, 0, 0], [0.44736842105263153, 0, 0], [0.47368421052631576, 0, 0], [0.5, 0, 0]], 'gap': [0.0, 0.0, 2.2204460492503131e-16, 0.0, 2.2204460492503131e-16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99999999999999989, 0.0, 0.5, 0.5, 0.50000000000000011, 0.50000000000000011]}

        self.assertDictAlmostEqual(tb_surface.get_res(), res)

    def testkwargcheck1(self):
        """ test kwarg check on wcc_calc """
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        tb_surface = tb_system.surface(lambda kx: [kx / 2, 0, 0], [0, 1, 0])
        self.assertRaises(
            TypeError,
            tb_surface.wcc_calc,
            invalid_kwarg = 3)

    def testkwargcheck2(self):
        """ test kwarg check on __init__ """
        self.createH(0, 0.3)
        # call to Z2Pack
        tb_system = z2pack.tb.System(self.H)
        self.assertRaises(
            TypeError,
            tb_system.surface,
            1, 2, 0, invalid_kwarg = 3)

if __name__ == "__main__":
    unittest.main()
