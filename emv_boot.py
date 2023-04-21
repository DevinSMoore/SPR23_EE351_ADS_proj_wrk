# -*- coding: utf-8 -*-

import empro.toolkit.adv as adv

def main():
	path=r"C:/SPR23_EE351_ADS_proj_wrk"
	lib=r"SPR23_EE351_ADS_proj1_lib"
	subst=r"SPR23_EE351_ADS_proj1_lib/substrate1.subst"
	substlib=r"SPR23_EE351_ADS_proj1_lib"
	substname=r"substrate1"
	cell=r"HD1"
	view=r"layout"
	libS3D=r"simulation/SPR23_EE351_ADS_proj1_lib/%H%D1/_3%D%Viewer/extra/0/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	adv.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, cell=cell, view=view, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary)
