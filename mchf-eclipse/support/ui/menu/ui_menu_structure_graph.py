#!/usr/bin/python

"""
support program to document the menu structure of mcHF amateur radio SDR TRX

relies upon module  ui_menu_structure.py  in the same directory (generated by build of mcHF FW)

"""


from ui_menu_structure import MENU_DESCRIPTOR
# MENU_DESCRIPTOR is a list of dicts with entries "MENU_ID" "ME_KIND" "NR" "ID" "LABEL"
# e.g.  [ ... { 'MENU_ID': "TOP",
#               'ME_KIND': "GROUP",
#               'NR': "MENU_BASE",
#               'ID': "STD",
#               'LABEL': "Standard Menu" },
#         ...]
        


from datetime import datetime

TS_NOW = datetime.now().replace(microsecond=0).isoformat()


BUILD_ID = "<${BUILD_ID}>"


#-----------------------------------------------------


# preface/header
print(r"""
    #  
    #  WARNING: generated data!  DO NOT EDIT MANUALLY ! ! !
    #  
    #  {GEN_SENTENCE}
    #  
    #  mcHF SDR TRX - Menu Structure Diagram in DOT-language
    #  
    #  (see <http://www.graphviz.org/content/dot-language> )
    #  
    digraph mcHF_menus {{
       
        graph [ fontsize = 14,
                label = "\nmcHF - Menus Overview\n{GEN_SENTENCE}",
              ];
       
        rankdir=LR
        nodesep=.05
       
    """.format(
        GEN_SENTENCE="generated from  {0}  at  {1}  by  ui_menu_structure_graph.py".format(BUILD_ID, TS_NOW)
    )
)


print("""
    #  -  -  -  -
""")


# artificial node for MENU_TOP
print("""
    "MENU_TOP" [
        shape = none
        image = "mcHF-logo.png"
        label = ""
        ];

""")


# body - nodes

for md in MENU_DESCRIPTOR:
    
    if((0 != md['NR']) and ('MEK_STOP' != md['ME_KIND'])):
        # declare a node for id
        print("""\
        "{NR}" [
             label = "{NR} ({ID}) | {LABEL}"
             shape = record
             ];
        """.format(**md).replace('<', '\<').replace('>', '\>'))


print("""
    #  -  -  -  -
""")


# body - edges

for mId in set([md['MENU_ID'] for md in MENU_DESCRIPTOR]):
    # start subgraph for every "parent"
    print("""
    subgraph "{0}" {{
            label = "{0} beef.0f.dead.e5e1"
    """.format(mId))

    for md in MENU_DESCRIPTOR:
        if((0 != md['NR']) and ('MEK_STOP' != md['ME_KIND']) and (mId ==  md['MENU_ID'])):
            # ...add an edge
            print("""\
            {MENU_ID} -> {NR}""".format(**md))

    print("""
    }}  ## END subgraph {MENU_ID}
    """.format(**md))

    
print("""
    #  -  -  -  -
""")

# footer
print("""
}

#EOFILE
""")


#EOFILE