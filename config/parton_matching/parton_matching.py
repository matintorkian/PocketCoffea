from parameters.cuts.baseline_cuts import dilepton_presel, passthrough
from lib.cut_functions import count_objects_gt
from lib.cut_definition import Cut
from config.parton_matching.functions import *

cfg =  {

    "dataset" : {
        "jsons": ["datasets/RunIISummer20UL18_local.json"],
        "filter" : {
            "samples": ["ttHTobb"],
            "samples_exclude" : [],
            "year": ["2018"]
        }
    },

    # Input and output files
    "workflow" : "parton_matching",
    "output"   : "output/mem",

    # Executor parameters
    "run_options" : {
        "executor"       : "futures",
        "workers"        : 20,
        "scaleout"       : 10,
        "partition"      : "standard",
        "walltime"       : "12:00:00",
        "mem_per_worker" : None, # GB
        "exclusive"      : True,
        "chunk"          : 50000,
        "max"            : None,
        "skipbadfiles"   : None,
        "voms"           : None,
        "limit"          : None,
    },

    # Cuts and plots settings
    "finalstate" : "dilepton",
    "preselections" : [dilepton_presel, getNjetNb_cut(4,2)],

    "categories": {
        "3bjets" :    [getNjetNb_cut(4,3)],
        "4bjets":     [getNjetNb_cut(4,4)],
        "3partonMatched" : [getNjetNb_cut(4,3),
                       Cut(name="3parton-matched",
                           params={"object": "PartonMatched", "value": 3},
                           function=count_objects_gt)],
        "4partonsMatched" : [ getNjetNb_cut(4,4),
                        Cut(name="4parton-matched",
                              params={"object": "PartonMatched", "value": 4},
                              function=count_objects_gt)],
    },
    
    "variables" : {
        "muon_pt" : {'binning' : {'n_or_arr' : 200, 'lo' : 0, 'hi' : 2000}, 'xlim' : (0,500),  'xlabel' : "$p_{T}^{\mu}$ [GeV]"},
        "muon_eta" : None,
        "muon_phi" : None,
        "electron_pt" : None,
        "electron_eta" : None,
        "electron_phi" : None,
        "jet_pt" : None,
        "jet_eta" : None,
        "jet_phi" : None,
        "nmuon" : None,
        "nelectron" : None,
        "nlep" : None,
        "nmuon" : None,
        "nelectron" : None,
        "nlep" : None,
        "njet" : None,
        "nbjet" : None,
        "nparton" : None,
        "parton_pt" : None,
        "parton_eta" : None,
        "parton_phi" : None,
        "parton_dRMatchedJet" : None,
        "parton_pdgId": None,

    },
    "variables2d" : {},
    "scale" : "log"
}
