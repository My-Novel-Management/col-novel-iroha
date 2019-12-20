# -*- coding: utf-8 -*-
"""Demo: main
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def sc_afterall(w: World):
    return w.scene("結局は", "究極的に小説の書き方はその人流を見つけるしかない",
            )


## episode
def ep_main(w: World):
    return w.episode("Demo", "小説の書き方なんてものはない",
            )
