#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Requirements:
* pytest
* pytest-html

To run:
pytest -s --html=report.html

"""
import os
import json
from acpype_lib.acs_api import acpype_api

file_types = [
    ("file_name", 3),
    ("em_mdp", 175),
    ("AC_frcmod", 3754),
    ("AC_inpcrd", 1220),
    ("AC_lib", 4969),
    ("AC_prmtop", 24474),
    ("mol2", 3654),
    ("CHARMM_inp", 2262),
    ("CHARMM_prm", 4180),
    ("CHARMM_rtf", 9247),
    ("CNS_inp", 1431),
    ("CNS_par", 5039),
    ("CNS_top", 6583),
    ("GMX_OPLS_itp", 24582),
    ("GMX_OPLS_top", 274),
    ("GMX_gro", 1599),
    ("GMX_itp", 22723),
    ("GMX_top", 353),
    ("NEW_pdb", 2697),
    ("md_mdp", 216),
]


def test_json():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    json_output = acpype_api(
        inputFile="AAA.mol2", chargeType="gas", atomType="gaff2", debug=True, basename="AAA", chiral=False
    )
    for ft in file_types:
        assert len(json.loads(json_output)[ft[0]]) == ft[1]

test_json()
