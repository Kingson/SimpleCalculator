{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'size':(297, 301),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'TextField', 
    'name':'Text', 
    'position':(21, 11), 
    'size':(246, 31), 
    },

{'type':'Button', 
    'name':'ButtonA', 
    'position':(107, 185), 
    'label':'=', 
    },

{'type':'Button', 
    'name':'ButtonE', 
    'position':(196, 185), 
    'label':'\xa1\xc2', 
    },

{'type':'Button', 
    'name':'ButtonX', 
    'position':(17, 185), 
    'label':'X', 
    },

{'type':'Button', 
    'name':'ButtonM', 
    'position':(195, 150), 
    'label':'-', 
    },

{'type':'Button', 
    'name':'ButtonP', 
    'position':(17, 150), 
    'label':'+', 
    },

{'type':'Button', 
    'name':'Button0', 
    'position':(107, 150), 
    'label':'0', 
    },

{'type':'Button', 
    'name':'Button9', 
    'position':(195, 117), 
    'label':'9', 
    },

{'type':'Button', 
    'name':'Button8', 
    'position':(106, 117), 
    'label':'8', 
    },

{'type':'Button', 
    'name':'Button7', 
    'position':(17, 117), 
    'label':'7', 
    },

{'type':'Button', 
    'name':'Button6', 
    'position':(195, 84), 
    'label':'6', 
    },

{'type':'Button', 
    'name':'Button5', 
    'position':(106, 84), 
    'label':'5', 
    },

{'type':'Button', 
    'name':'Button4', 
    'position':(17, 84), 
    'label':'4', 
    },

{'type':'Button', 
    'name':'Button3', 
    'position':(195, 51), 
    'label':'3', 
    },

{'type':'Button', 
    'name':'Button2', 
    'position':(106, 51), 
    'label':'2', 
    },

{'type':'Button', 
    'name':'Button1', 
    'position':(17, 51), 
    'label':'1', 
    },

] # end components
} # end background
] # end backgrounds
} }
