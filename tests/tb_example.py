#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    15.10.2014 10:22:43 CEST
# File:    tb_example.py

from common import *

import os
import types
import shutil

class TbExampleTestCase(BuildDirTestCase):

    def createH(self, t1, t2):

        builder = z2pack.em.tb.Builder()

        # create the two atoms
        builder.add_atom([1, 1], [0, 0, 0], 1)
        builder.add_atom([-1, -1], [0.5, 0.5, 0], 1)

        # add hopping between different atoms
        builder.add_hopping(((0, 0), (1, 1)),
                           z2pack.em.tb.vectors.combine([0, -1], [0, -1], 0),
                           t1,
                           phase=[1, -1j, 1j, -1])
        builder.add_hopping(((0, 1), (1, 0)),
                           z2pack.em.tb.vectors.combine([0, -1], [0, -1], 0),
                           t1,
                           phase=[1, 1j, -1j, -1])

        # add hopping between neighbouring orbitals of the same type
        builder.add_hopping((((0, 0), (0, 0)), ((0, 1), (0, 1))),
                           z2pack.em.tb.vectors.neighbours([0, 1],
                                                        forward_only=True),
                           t2,
                           phase=[1])
        builder.add_hopping((((1, 1), (1, 1)), ((1, 0), (1, 0))),
                           z2pack.em.tb.vectors.neighbours([0, 1],
                                                        forward_only=True),
                           -t2,
                           phase=[1])
        self.model = builder.create()

    # this test may produce false negatives due to small numerical differences
    def test_res1(self):
        self.createH(0.2, 0.3)
        # call to Z2Pack
        tb_system = z2pack.em.tb.System(self.model)
        tb_surface = tb_system.surface(lambda kx, ky: [kx / 2, ky, 0])
        tb_surface.wcc_calc(verbose=False, num_strings=20, pickle_file=None)
        
        res = {'t_par': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'wcc': [[0.4996901520694727, 0.50030984793052746], [0.49876253242148111, 0.50123746757851895], [0.4976728615885303, 0.50232713841147003], [0.49600000936166949, 0.50399999063833056], [0.49409333798573685, 0.50590666201426315], [0.49135230436336974, 0.50864769563663026], [0.48785649797599739, 0.51214350202400283], [0.48552307044038812, 0.51447692955961188], [0.48189158683153055, 0.51810841316846945], [0.47639375434269693, 0.52360624565730318], [0.47033541279590518, 0.52966458720409493], [0.45747179380673442, 0.54252820619326569], [0.44332613985033992, 0.55667386014966014], [0.41864128648804338, 0.58135871351195667], [0.3803220517880781, 0.61967794821192201], [0.32505166800848173, 0.67494833199151827], [0.24926997659285657, 0.75073002340714345], [0.16110614508591162, 0.83889385491408852], [0.080615635852378603, 0.91938436414762137], [0.00209549872986634, 0.99790450127013386]], 'lambda_': [array([[ -9.99998105e-01-0.00191907j,   1.85644068e-04+0.0002699j ],
       [ -1.85644068e-04+0.0002699j ,  -9.99998105e-01+0.00191907j]]), array([[ -9.99969773e-01 +7.76838982e-03j,
          3.13815396e-04 +8.21519065e-05j],
       [ -3.13815396e-04 +8.21519065e-05j,
         -9.99969773e-01 -7.76838982e-03j]]), array([[ -9.99893103e-01+0.01448243j,   8.85179984e-06+0.00201054j],
       [ -8.85179984e-06+0.00201054j,  -9.99893103e-01-0.01448243j]]), array([[ -9.99684191e-01+0.02508734j,   2.88625050e-05+0.00146394j],
       [ -2.88625050e-05+0.00146394j,  -9.99684191e-01-0.02508734j]]), array([[ -9.99311405e-01+0.03708939j,  -3.17688547e-04-0.00099626j],
       [  3.17688547e-04-0.00099626j,  -9.99311405e-01-0.03708939j]]), array([[-0.99852421+0.05413202j, -0.00387104+0.00203367j],
       [ 0.00387104+0.00203367j, -0.99852421-0.05413202j]]), array([[-0.99709058+0.07614251j, -0.00323052+0.00150485j],
       [ 0.00323052+0.00150485j, -0.99709058-0.07614251j]]), array([[ -9.95865879e-01+0.090594j  ,   5.86100045e-04-0.00659816j],
       [ -5.86100045e-04-0.00659816j,  -9.95865879e-01-0.090594j  ]]), array([[-0.99353420+0.11336773j, -0.00611698-0.00035377j],
       [ 0.00611698-0.00035377j, -0.99353420-0.11336773j]]), array([[-0.98902038+0.14759775j, -0.00708663-0.00183578j],
       [ 0.00708663-0.00183578j, -0.98902038-0.14759775j]]), array([[-0.98267997+0.18396082j, -0.02043786-0.00898849j],
       [ 0.02043786-0.00898849j, -0.98267997-0.18396082j]]), array([[-0.96451064+0.26369883j, -0.01342762+0.00136194j],
       [ 0.01342762+0.00136194j, -0.96451064-0.26369883j]]), array([[-0.93726623+0.34846361j, -0.00347279+0.00964656j],
       [ 0.00347279+0.00964656j, -0.93726623-0.34846361j]]), array([[-0.87216204+0.48722332j, -0.04407323+0.00208698j],
       [ 0.04407323+0.00208698j, -0.87216204-0.48722332j]]), array([[-0.73035232+0.64392037j,  0.22789441+0.0040216j ],
       [-0.22789441+0.0040216j , -0.73035232-0.64392037j]]), array([[-0.45427973+0.89061258j,  0.02086096+0.00199573j],
       [-0.02086096+0.00199573j, -0.45427973-0.89061258j]]), array([[ 0.00458686+0.99115955j,  0.02714388+0.12978794j],
       [-0.02714388+0.12978794j,  0.00458686-0.99115955j]]), array([[ 0.52994573+0.82201656j,  0.19018024-0.08530988j],
       [-0.19018024-0.08530988j,  0.52994573-0.82201656j]]), array([[ 0.87443663+0.48477553j, -0.00533307+0.01802283j],
       [ 0.00533307+0.01802283j,  0.87443663-0.48477553j]]), array([[ 0.99991332+0.0116777j ,  0.00224800-0.00564996j],
       [-0.00224800-0.00564996j,  0.99991332-0.0116777j ]])], 'kpt': [[0.0, 0.0, 0], [0.026315789473684209, 0.0, 0], [0.052631578947368418, 0.0, 0], [0.078947368421052627, 0.0, 0], [0.10526315789473684, 0.0, 0], [0.13157894736842105, 0.0, 0], [0.15789473684210525, 0.0, 0], [0.18421052631578946, 0.0, 0], [0.21052631578947367, 0.0, 0], [0.23684210526315788, 0.0, 0], [0.26315789473684209, 0.0, 0], [0.28947368421052633, 0.0, 0], [0.31578947368421051, 0.0, 0], [0.34210526315789469, 0.0, 0], [0.36842105263157893, 0.0, 0], [0.39473684210526316, 0.0, 0], [0.42105263157894735, 0.0, 0], [0.44736842105263153, 0.0, 0], [0.47368421052631576, 0.0, 0], [0.5, 0.0, 0]], 'gap': [0.0, 0.0, 2.2204460492503131e-16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.50000000000000011, 0.5, 0.50000000000000011]}

        self.assertFullAlmostEqual(tb_surface.get_res(), res)

    def test_res2(self):
        """ test pos_check=False """
        self.createH(0, 0.3)
        # call to Z2Pack
        tb_system = z2pack.em.tb.System(self.model)
        tb_surface = tb_system.surface(lambda kx, ky: [kx / 2, ky, 0])
        tb_surface.wcc_calc(verbose=False,
                            num_strings=20,
                            pickle_file=None,
                            pos_tol=None)

        res = {'t_par': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'wcc': [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.625, 0.625], [0.625, 0.625], [0.625, 0.625], [0.625, 0.625], [0.75, 0.75], [0.75, 0.75]], 'lambda_': [array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-1. -1.66533454e-16j,  0. +0.00000000e+00j],
       [ 0. +0.00000000e+00j, -1. -1.66533454e-16j]]), array([[-0.70710678+0.70710678j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.70710678+0.70710678j]]), array([[-0.70710678+0.70710678j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.70710678+0.70710678j]]), array([[-0.70710678+0.70710678j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.70710678+0.70710678j]]), array([[-0.70710678+0.70710678j,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.70710678+0.70710678j]]), array([[ -1.11022302e-16+1.j,   0.00000000e+00+0.j],
       [  0.00000000e+00+0.j,  -1.11022302e-16+1.j]]), array([[ -1.11022302e-16+1.j,   0.00000000e+00+0.j],
       [  0.00000000e+00+0.j,  -1.11022302e-16+1.j]])], 'kpt': [[0.0, 0.0, 0], [0.026315789473684209, 0.0, 0], [0.052631578947368418, 0.0, 0], [0.078947368421052627, 0.0, 0], [0.10526315789473684, 0.0, 0], [0.13157894736842105, 0.0, 0], [0.15789473684210525, 0.0, 0], [0.18421052631578946, 0.0, 0], [0.21052631578947367, 0.0, 0], [0.23684210526315788, 0.0, 0], [0.26315789473684209, 0.0, 0], [0.28947368421052633, 0.0, 0], [0.31578947368421051, 0.0, 0], [0.34210526315789469, 0.0, 0], [0.36842105263157893, 0.0, 0], [0.39473684210526316, 0.0, 0], [0.42105263157894735, 0.0, 0], [0.44736842105263153, 0.0, 0], [0.47368421052631576, 0.0, 0], [0.5, 0.0, 0]], 'gap': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.125, 0.125, 0.125, 0.125, 0.25, 0.25]}

        self.assertFullAlmostEqual(tb_surface.get_res(), res)

    def test_res3(self):
        """ test gap_tol=None """
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.em.tb.System(self.model)
        tb_surface = tb_system.surface(lambda kx, ky: [kx / 2, ky, 0])
        tb_surface.wcc_calc(verbose=False,
                            num_strings=20,
                            pickle_file=None,
                            gap_tol=None)

        res = {'t_par': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'wcc': [[0.49991770091337534, 0.50008229908662472], [0.49968126598293366, 0.50031873401706628], [0.4992104974293225, 0.50078950257067789], [0.49871381470273785, 0.50128618529726232], [0.49804447287205544, 0.50195552712794456], [0.49724082022680699, 0.50275917977319329], [0.49711582350367939, 0.50288417649632078], [0.49574994866506122, 0.50425005133493883], [0.49487871121476157, 0.50512128878523843], [0.49279223903105446, 0.50720776096894538], [0.48950969540882477, 0.51049030459117528], [0.48587599826742339, 0.51412400173257655], [0.47765362516422472, 0.52234637483577551], [0.46048888254755654, 0.53951111745244373], [0.41527235890704178, 0.58472764109295827], [0.32443256353158906, 0.67556743646841111], [0.22812573517974574, 0.77187426482025434], [0.14311538314097094, 0.85688461685902917], [0.06848074969043165, 0.93151925030956839], [0.00080745884482689274, 0.99919254115517309]], 'lambda_': [array([[ -9.99999866e-01 -5.14131664e-04j,
          3.22265436e-05 +4.49765933e-05j],
       [ -3.22265436e-05 +4.49765933e-05j,
         -9.99999866e-01 +5.14131664e-04j]]), array([[ -9.99997995e-01 +2.00149487e-03j,
          6.83890250e-05 -1.58707183e-06j],
       [ -6.83890250e-05 -1.58707183e-06j,
         -9.99997995e-01 -2.00149487e-03j]]), array([[ -9.99987696e-01+0.00495541j,   2.67751188e-05+0.00022464j],
       [ -2.67751188e-05+0.00022464j,  -9.99987696e-01-0.00495541j]]), array([[ -9.99967346e-01+0.00807712j,   6.90869872e-05-0.00024911j],
       [ -6.90869872e-05-0.00024911j,  -9.99967346e-01-0.00807712j]]), array([[ -9.99924517e-01+0.01227853j,   2.56835259e-04+0.00036487j],
       [ -2.56835259e-04+0.00036487j,  -9.99924517e-01-0.01227853j]]), array([[ -9.99849728e-01+0.01732057j,  -6.83100297e-04+0.00023087j],
       [  6.83100297e-04+0.00023087j,  -9.99849728e-01-0.01732057j]]), array([[ -9.99835804e-01+0.01811461j,  -3.50651515e-04+0.00031976j],
       [  3.50651515e-04+0.00031976j,  -9.99835804e-01-0.01811461j]]), array([[ -9.99643473e-01+0.02667417j,  -5.56218704e-04-0.00105158j],
       [  5.56218704e-04-0.00105158j,  -9.99643473e-01-0.02667417j]]), array([[ -9.99482333e-01 +3.21599185e-02j,
         -8.95014169e-04 -7.32802674e-05j],
       [  8.95014169e-04 -7.32802674e-05j,
         -9.99482333e-01 -3.21599185e-02j]]), array([[-0.99897469+0.04525061j, -0.00134747-0.00037476j],
       [ 0.00134747-0.00037476j, -0.99897469-0.04525061j]]), array([[-0.99782856+0.06584245j, -0.00136041-0.00104605j],
       [ 0.00136041-0.00104605j, -0.99782856-0.06584245j]]), array([[-0.99606486 +8.86172810e-02j, -0.00132924 -7.72978244e-05j],
       [ 0.00132924 -7.72978244e-05j, -0.99606486 -8.86172810e-02j]]), array([[-0.99015920+0.13992055j, -0.00193183+0.001806j  ],
       [ 0.00193183+0.001806j  , -0.99015920-0.13992055j]]), array([[-0.96934250+0.24543567j, -0.01089432-0.00421451j],
       [ 0.01089432-0.00421451j, -0.96934250-0.24543567j]]), array([[-0.86161188+0.49618605j,  0.10670361+0.00622186j],
       [-0.10670361+0.00622186j, -0.86161188-0.49618605j]]), array([[-0.45081091+0.89261237j,  0.00324402+0.00146624j],
       [-0.00324402+0.00146624j, -0.45081091-0.89261237j]]), array([[ 0.13700777+0.98699585j, -0.03894407-0.0745079j ],
       [ 0.03894407-0.0745079j ,  0.13700777-0.98699585j]]), array([[ 0.62222040+0.78191942j, -0.02902613+0.024521j  ],
       [ 0.02902613+0.024521j  ,  0.62222040-0.78191942j]]), array([[  9.08850141e-01+0.41712231j,   2.45178668e-05+0.00062861j],
       [ -2.45178668e-05+0.00062861j,   9.08850141e-01-0.41712231j]]), array([[  9.99987130e-01+0.00342628j,   5.60131360e-04-0.00369949j],
       [ -5.60131360e-04-0.00369949j,   9.99987130e-01-0.00342628j]])], 'kpt': [[0.0, 0.0, 0], [0.026315789473684209, 0.0, 0], [0.052631578947368418, 0.0, 0], [0.078947368421052627, 0.0, 0], [0.10526315789473684, 0.0, 0], [0.13157894736842105, 0.0, 0], [0.15789473684210525, 0.0, 0], [0.18421052631578946, 0.0, 0], [0.21052631578947367, 0.0, 0], [0.23684210526315788, 0.0, 0], [0.26315789473684209, 0.0, 0], [0.28947368421052633, 0.0, 0], [0.31578947368421051, 0.0, 0], [0.34210526315789469, 0.0, 0], [0.36842105263157893, 0.0, 0], [0.39473684210526316, 0.0, 0], [0.42105263157894735, 0.0, 0], [0.44736842105263153, 0.0, 0], [0.47368421052631576, 0.0, 0], [0.5, 0.0, 0]], 'gap': [0.0, 0.0, 2.2204460492503131e-16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99999999999999989, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5, 0.5]}

        self.assertFullAlmostEqual(tb_surface.get_res(), res)

    def test_res4(self):
        """ test move_tol=None """
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.em.tb.System(self.model)
        tb_surface = tb_system.surface(lambda kx, ky: [kx / 2, ky, 0])
        tb_surface.wcc_calc(verbose=False,
                          num_strings=20,
                          pickle_file=None,
                          move_tol=None)

        res = {'t_par': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'wcc': [[0.49991770091337534, 0.50008229908662472], [0.49968126598293366, 0.50031873401706628], [0.4992104974293225, 0.50078950257067789], [0.49871381470273785, 0.50128618529726232], [0.49804447287205544, 0.50195552712794456], [0.49724082022680699, 0.50275917977319329], [0.49711582350367939, 0.50288417649632078], [0.49574994866506122, 0.50425005133493883], [0.49487871121476157, 0.50512128878523843], [0.49279223903105446, 0.50720776096894538], [0.48950969540882477, 0.51049030459117528], [0.48587599826742339, 0.51412400173257655], [0.47765362516422472, 0.52234637483577551], [0.46048888254755654, 0.53951111745244373], [0.41527235890704178, 0.58472764109295827], [0.32443256353158906, 0.67556743646841111], [0.22812573517974574, 0.77187426482025434], [0.14311538314097094, 0.85688461685902917], [0.06848074969043165, 0.93151925030956839], [0.00080745884482689274, 0.99919254115517309]], 'lambda_': [array([[ -9.99999866e-01 -5.14131664e-04j,
          3.22265436e-05 +4.49765933e-05j],
       [ -3.22265436e-05 +4.49765933e-05j,
         -9.99999866e-01 +5.14131664e-04j]]), array([[ -9.99997995e-01 +2.00149487e-03j,
          6.83890250e-05 -1.58707183e-06j],
       [ -6.83890250e-05 -1.58707183e-06j,
         -9.99997995e-01 -2.00149487e-03j]]), array([[ -9.99987696e-01+0.00495541j,   2.67751188e-05+0.00022464j],
       [ -2.67751188e-05+0.00022464j,  -9.99987696e-01-0.00495541j]]), array([[ -9.99967346e-01+0.00807712j,   6.90869872e-05-0.00024911j],
       [ -6.90869872e-05-0.00024911j,  -9.99967346e-01-0.00807712j]]), array([[ -9.99924517e-01+0.01227853j,   2.56835259e-04+0.00036487j],
       [ -2.56835259e-04+0.00036487j,  -9.99924517e-01-0.01227853j]]), array([[ -9.99849728e-01+0.01732057j,  -6.83100297e-04+0.00023087j],
       [  6.83100297e-04+0.00023087j,  -9.99849728e-01-0.01732057j]]), array([[ -9.99835804e-01+0.01811461j,  -3.50651515e-04+0.00031976j],
       [  3.50651515e-04+0.00031976j,  -9.99835804e-01-0.01811461j]]), array([[ -9.99643473e-01+0.02667417j,  -5.56218704e-04-0.00105158j],
       [  5.56218704e-04-0.00105158j,  -9.99643473e-01-0.02667417j]]), array([[ -9.99482333e-01 +3.21599185e-02j,
         -8.95014169e-04 -7.32802674e-05j],
       [  8.95014169e-04 -7.32802674e-05j,
         -9.99482333e-01 -3.21599185e-02j]]), array([[-0.99897469+0.04525061j, -0.00134747-0.00037476j],
       [ 0.00134747-0.00037476j, -0.99897469-0.04525061j]]), array([[-0.99782856+0.06584245j, -0.00136041-0.00104605j],
       [ 0.00136041-0.00104605j, -0.99782856-0.06584245j]]), array([[-0.99606486 +8.86172810e-02j, -0.00132924 -7.72978244e-05j],
       [ 0.00132924 -7.72978244e-05j, -0.99606486 -8.86172810e-02j]]), array([[-0.99015920+0.13992055j, -0.00193183+0.001806j  ],
       [ 0.00193183+0.001806j  , -0.99015920-0.13992055j]]), array([[-0.96934250+0.24543567j, -0.01089432-0.00421451j],
       [ 0.01089432-0.00421451j, -0.96934250-0.24543567j]]), array([[-0.86161188+0.49618605j,  0.10670361+0.00622186j],
       [-0.10670361+0.00622186j, -0.86161188-0.49618605j]]), array([[-0.45081091+0.89261237j,  0.00324402+0.00146624j],
       [-0.00324402+0.00146624j, -0.45081091-0.89261237j]]), array([[ 0.13700777+0.98699585j, -0.03894407-0.0745079j ],
       [ 0.03894407-0.0745079j ,  0.13700777-0.98699585j]]), array([[ 0.62222040+0.78191942j, -0.02902613+0.024521j  ],
       [ 0.02902613+0.024521j  ,  0.62222040-0.78191942j]]), array([[  9.08850141e-01+0.41712231j,   2.45178668e-05+0.00062861j],
       [ -2.45178668e-05+0.00062861j,   9.08850141e-01-0.41712231j]]), array([[  9.99987130e-01+0.00342628j,   5.60131360e-04-0.00369949j],
       [ -5.60131360e-04-0.00369949j,   9.99987130e-01-0.00342628j]])], 'kpt': [[0.0, 0.0, 0], [0.026315789473684209, 0.0, 0], [0.052631578947368418, 0.0, 0], [0.078947368421052627, 0.0, 0], [0.10526315789473684, 0.0, 0], [0.13157894736842105, 0.0, 0], [0.15789473684210525, 0.0, 0], [0.18421052631578946, 0.0, 0], [0.21052631578947367, 0.0, 0], [0.23684210526315788, 0.0, 0], [0.26315789473684209, 0.0, 0], [0.28947368421052633, 0.0, 0], [0.31578947368421051, 0.0, 0], [0.34210526315789469, 0.0, 0], [0.36842105263157893, 0.0, 0], [0.39473684210526316, 0.0, 0], [0.42105263157894735, 0.0, 0], [0.44736842105263153, 0.0, 0], [0.47368421052631576, 0.0, 0], [0.5, 0.0, 0]], 'gap': [0.0, 0.0, 2.2204460492503131e-16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99999999999999989, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5, 0.5]}

        self.assertFullAlmostEqual(tb_surface.get_res(), res)

    def test_res5(self):
        """ test gap_tol=None and move_tol=None"""
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.em.tb.System(self.model)
        tb_surface = tb_system.surface(lambda kx, ky: [kx / 2, ky, 0])
        tb_surface.wcc_calc(verbose=False,
                            num_strings=20,
                            pickle_file=None,
                            gap_tol=None,
                            move_tol=None)

        res = {'t_par': [0.0, 0.052631578947368418, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.26315789473684209, 0.31578947368421051, 0.36842105263157893, 0.42105263157894735, 0.47368421052631576, 0.52631578947368418, 0.57894736842105265, 0.63157894736842102, 0.68421052631578938, 0.73684210526315785, 0.78947368421052633, 0.84210526315789469, 0.89473684210526305, 0.94736842105263153, 1.0], 'wcc': [[0.49991770091337534, 0.50008229908662472], [0.49968126598293366, 0.50031873401706628], [0.4992104974293225, 0.50078950257067789], [0.49871381470273785, 0.50128618529726232], [0.49804447287205544, 0.50195552712794456], [0.49724082022680699, 0.50275917977319329], [0.49711582350367939, 0.50288417649632078], [0.49574994866506122, 0.50425005133493883], [0.49487871121476157, 0.50512128878523843], [0.49279223903105446, 0.50720776096894538], [0.48950969540882477, 0.51049030459117528], [0.48587599826742339, 0.51412400173257655], [0.47765362516422472, 0.52234637483577551], [0.46048888254755654, 0.53951111745244373], [0.41527235890704178, 0.58472764109295827], [0.32443256353158906, 0.67556743646841111], [0.22812573517974574, 0.77187426482025434], [0.14311538314097094, 0.85688461685902917], [0.06848074969043165, 0.93151925030956839], [0.00080745884482689274, 0.99919254115517309]], 'lambda_': [array([[ -9.99999866e-01 -5.14131664e-04j,
          3.22265436e-05 +4.49765933e-05j],
       [ -3.22265436e-05 +4.49765933e-05j,
         -9.99999866e-01 +5.14131664e-04j]]), array([[ -9.99997995e-01 +2.00149487e-03j,
          6.83890250e-05 -1.58707183e-06j],
       [ -6.83890250e-05 -1.58707183e-06j,
         -9.99997995e-01 -2.00149487e-03j]]), array([[ -9.99987696e-01+0.00495541j,   2.67751188e-05+0.00022464j],
       [ -2.67751188e-05+0.00022464j,  -9.99987696e-01-0.00495541j]]), array([[ -9.99967346e-01+0.00807712j,   6.90869872e-05-0.00024911j],
       [ -6.90869872e-05-0.00024911j,  -9.99967346e-01-0.00807712j]]), array([[ -9.99924517e-01+0.01227853j,   2.56835259e-04+0.00036487j],
       [ -2.56835259e-04+0.00036487j,  -9.99924517e-01-0.01227853j]]), array([[ -9.99849728e-01+0.01732057j,  -6.83100297e-04+0.00023087j],
       [  6.83100297e-04+0.00023087j,  -9.99849728e-01-0.01732057j]]), array([[ -9.99835804e-01+0.01811461j,  -3.50651515e-04+0.00031976j],
       [  3.50651515e-04+0.00031976j,  -9.99835804e-01-0.01811461j]]), array([[ -9.99643473e-01+0.02667417j,  -5.56218704e-04-0.00105158j],
       [  5.56218704e-04-0.00105158j,  -9.99643473e-01-0.02667417j]]), array([[ -9.99482333e-01 +3.21599185e-02j,
         -8.95014169e-04 -7.32802674e-05j],
       [  8.95014169e-04 -7.32802674e-05j,
         -9.99482333e-01 -3.21599185e-02j]]), array([[-0.99897469+0.04525061j, -0.00134747-0.00037476j],
       [ 0.00134747-0.00037476j, -0.99897469-0.04525061j]]), array([[-0.99782856+0.06584245j, -0.00136041-0.00104605j],
       [ 0.00136041-0.00104605j, -0.99782856-0.06584245j]]), array([[-0.99606486 +8.86172810e-02j, -0.00132924 -7.72978244e-05j],
       [ 0.00132924 -7.72978244e-05j, -0.99606486 -8.86172810e-02j]]), array([[-0.99015920+0.13992055j, -0.00193183+0.001806j  ],
       [ 0.00193183+0.001806j  , -0.99015920-0.13992055j]]), array([[-0.96934250+0.24543567j, -0.01089432-0.00421451j],
       [ 0.01089432-0.00421451j, -0.96934250-0.24543567j]]), array([[-0.86161188+0.49618605j,  0.10670361+0.00622186j],
       [-0.10670361+0.00622186j, -0.86161188-0.49618605j]]), array([[-0.45081091+0.89261237j,  0.00324402+0.00146624j],
       [-0.00324402+0.00146624j, -0.45081091-0.89261237j]]), array([[ 0.13700777+0.98699585j, -0.03894407-0.0745079j ],
       [ 0.03894407-0.0745079j ,  0.13700777-0.98699585j]]), array([[ 0.62222040+0.78191942j, -0.02902613+0.024521j  ],
       [ 0.02902613+0.024521j  ,  0.62222040-0.78191942j]]), array([[  9.08850141e-01+0.41712231j,   2.45178668e-05+0.00062861j],
       [ -2.45178668e-05+0.00062861j,   9.08850141e-01-0.41712231j]]), array([[  9.99987130e-01+0.00342628j,   5.60131360e-04-0.00369949j],
       [ -5.60131360e-04-0.00369949j,   9.99987130e-01-0.00342628j]])], 'kpt': [[0.0, 0.0, 0], [0.026315789473684209, 0.0, 0], [0.052631578947368418, 0.0, 0], [0.078947368421052627, 0.0, 0], [0.10526315789473684, 0.0, 0], [0.13157894736842105, 0.0, 0], [0.15789473684210525, 0.0, 0], [0.18421052631578946, 0.0, 0], [0.21052631578947367, 0.0, 0], [0.23684210526315788, 0.0, 0], [0.26315789473684209, 0.0, 0], [0.28947368421052633, 0.0, 0], [0.31578947368421051, 0.0, 0], [0.34210526315789469, 0.0, 0], [0.36842105263157893, 0.0, 0], [0.39473684210526316, 0.0, 0], [0.42105263157894735, 0.0, 0], [0.44736842105263153, 0.0, 0], [0.47368421052631576, 0.0, 0], [0.5, 0.0, 0]], 'gap': [0.0, 0.0, 2.2204460492503131e-16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99999999999999989, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5, 0.5]}

        self.assertFullAlmostEqual(tb_surface.get_res(), res)

    def test_warning(self):
        """ test the warning that is given when string_vec != None"""
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.em.tb.System(self.model)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            tb_surface = tb_system.surface(lambda kx: [kx / 2, 0, 0], [0, 1, 0])
            assert len(w) == 1
            assert w[-1].category == DeprecationWarning
            assert "string_vec" in str(w[-1].message)

    def test_saveload(self):
        self.createH(0.1, 0.3)
        tb_system = z2pack.em.tb.System(self.model)
        surface1 = tb_system.surface(lambda kx, ky: [kx / 2, ky, 0], pickle_file=self._build_folder + '/tb_pickle.txt')
        surface2 = tb_system.surface(lambda kx, ky: [kx / 2, ky, 0], pickle_file=self._build_folder + '/tb_pickle.txt')
        surface1.wcc_calc(verbose=False)
        surface2.load()
        self.assertFullAlmostEqual(surface1.get_res(), surface2.get_res())

    def testkwargcheck1(self):
        """ test kwarg check on wcc_calc """
        self.createH(0.1, 0.3)
        # call to Z2Pack
        tb_system = z2pack.em.tb.System(self.model)
        tb_surface = tb_system.surface(lambda kx, ky: [kx / 2, ky, 0])
        self.assertRaises(
            TypeError,
            tb_surface.wcc_calc,
            invalid_kwarg = 3)

    def testkwargcheck2(self):
        """ test kwarg check on __init__ """
        self.createH(0, 0.3)
        # call to Z2Pack
        tb_system = z2pack.em.tb.System(self.model)
        self.assertRaises(
            TypeError,
            tb_system.surface,
            1, 2, 0, invalid_kwarg = 3)

if __name__ == "__main__":
    unittest.main()
