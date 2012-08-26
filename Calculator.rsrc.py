{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'size':(391, 250),
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

{'type':'Button', 
    'name':'ButtonD', 
    'position':(195, 154), 
    'label':u'.', 
    },

{'type':'Button', 
    'name':'Button00', 
    'position':(106, 154), 
    'label':u'00', 
    },

{'type':'TextField', 
    'name':'Text', 
    'position':(19, 11), 
    'size':(249, 33), 
    },

{'type':'Button', 
    'name':'ButtonA', 
    'position':(288, 14), 
    'label':u'=', 
    },

{'type':'Button', 
    'name':'ButtonE', 
    'position':(288, 154), 
    'label':u'\xf7', 
    },

{'type':'Button', 
    'name':'ButtonX', 
    'position':(288, 117), 
    'label':u'X', 
    },

{'type':'Button', 
    'name':'ButtonM', 
    'position':(288, 84), 
    'label':u'-', 
    },

{'type':'Button', 
    'name':'ButtonP', 
    'position':(288, 51), 
    'label':u'+', 
    },

{'type':'Button', 
    'name':'Button0', 
    'position':(18, 154), 
    'label':u'0', 
    },

{'type':'Button', 
    'name':'Button9', 
    'position':(195, 117), 
    'label':u'9', 
    },

{'type':'Button', 
    'name':'Button8', 
    'position':(106, 117), 
    'label':u'8', 
    },

{'type':'Button', 
    'name':'Button7', 
    'position':(17, 117), 
    'label':u'7', 
    },

{'type':'Button', 
    'name':'Button6', 
    'position':(195, 84), 
    'label':u'6', 
    },

{'type':'Button', 
    'name':'Button5', 
    'position':(106, 84), 
    'label':u'5', 
    },

{'type':'Button', 
    'name':'Button4', 
    'position':(17, 84), 
    'label':u'4', 
    },

{'type':'Button', 
    'name':'Button3', 
    'position':(195, 51), 
    'label':u'3', 
    },

{'type':'Button', 
    'name':'Button2', 
    'position':(106, 51), 
    'label':u'2', 
    },

{'type':'Button', 
    'name':'Button1', 
    'position':(17, 51), 
    'label':u'1', 
    },

] # end components
} # end background
] # end backgrounds
} }
