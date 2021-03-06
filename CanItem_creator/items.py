"""
Info about all items and their options that can be used
"""
import tkinter as tk
import addwidgets

#https://tcl.tk/man/tcl8.6/TkCmd/canvas.htm
OPTIONS = {
    #Common options:
    "anchor": {
        "edit": addwidgets.AnchorEdit,
    },
    "dash": {
        "edit": addwidgets.StrEdit,
    },
    "activedash": {
        "edit": addwidgets.StrEdit,
    },
    "disableddash": {
        "edit": addwidgets.StrEdit,
    },
    "dashoffset": {
        "edit": addwidgets.IntEdit,
    },
    "fill": {
        "edit": addwidgets.ColorEdit,
    },
    "activefill": {
        "edit": addwidgets.ColorEdit,
    },
    "disabledfill": {
        "edit": addwidgets.ColorEdit,
    },
    "outline": {
        "edit": addwidgets.ColorEdit,
    },
    "activeoutline": {
        "edit": addwidgets.ColorEdit,
    },
    "disabledoutline": {
        "edit": addwidgets.ColorEdit,
    },
    "offset": {
        "edit": addwidgets.IntEdit,
    },
    "outlinestipple": {
        "edit": None, #bitmap
    },
    "activeoutlinestipple": {
        "edit": None, #bitmap
    },
    "disabledoutlinestipple": {
        "edit": None, #bitmap
    },
    "outlineoffset": {
        "edit": addwidgets.IntEdit,
    },
    "stipple": {
        "edit": None, #bitmap
    },
    "activestipple": {
        "edit": None, #bitmap
    },
    "disabledstipple": {
        "edit": None, #bitmap
    },
    "state": {
        "edit": None, #will not be used
    },
    "tags": {
        "edit": None, #will not be used
    },
    "width": {
        "edit": addwidgets.IntEdit,
    },
    "activewidth": {
        "edit": addwidgets.IntEdit,
    },
    "disabledwidth": {
        "edit": addwidgets.IntEdit,
    },
    #Item specific options:
    #Arc
    "extent": {
        "edit": addwidgets.IntEdit, #degrees
    },
    "start": {
        "edit": addwidgets.IntEdit, #degrees
    },
    "style": {
        "edit": addwidgets.StrEdit, #type - pieslice, chord, arc Should have specific edit for this
    },
    #Bitmap
    "background": {
        "edit": addwidgets.ColorEdit,
    },
    "activebackground": {
        "edit": addwidgets.ColorEdit,
    },
    "disabledbackground": {
        "edit": addwidgets.ColorEdit,
    },
    "bitmap": {
        "edit": None, #bitmap
    },
    "activebitmap": {
        "edit": None, #bitmap
    },
    "disabledbitmap": {
        "edit": None, #bitmap
    },
    "foreground": {
        "edit": addwidgets.ColorEdit,
    },
    "activeforeground": {
        "edit": addwidgets.ColorEdit,
    },
    "disabledforeground": {
        "edit": addwidgets.ColorEdit,
    },
    #Image
    "image": {
        "edit": None, #name
    },
    "activeimage": {
        "edit": None, #name
    },
    "disabledimage": {
        "edit": None, #name
    },
    #Line
    "arrow": {
        "edit": addwidgets.StrEdit, #where - none, first, last, both
    },
    "arrowshape": {
        "edit": None, #shape - must be a list with three elements
    },
    "capstyle": {
        "edit": addwidgets.StrEdit, #style - butt, projecting, or round
    },
    "joinstyle": {
        "edit": addwidgets.StrEdit, #style - bevel, miter, or round
    },
    "smooth": {
        "edit": addwidgets.StrEdit, #smoothMethod - either true, false or a method(not implemented and not planed)
    },
    "splinesteps": {
        "edit": addwidgets.IntEdit,
    },
    #Oval
    #Polygon
    #"joinstyle": {
    #    "edit": addwidgets.StrEdit, #style - bevel, miter, or round
    #},
    # "smooth": {
    #     "edit": addwidgets.StrEdit, #true, false
    # },
    #"splinesteps"...
    #Rectnagle
    #Text
    "angle": {
        "edit": addwidgets.IntEdit, #rotationDegrees
    },
    "font": {
        "edit": addwidgets.StrEdit, #fontName - should have specific widget
    },
    "justify": {
        "edit": addwidgets.StrEdit, #how - left, right, or center
    },
    "text": {
        "edit": addwidgets.StrEdit,
    },
    "underline": {
        "edit": addwidgets.IntEdit, #not sure how this works
    },
    #"width"...
    #Window - This will probably newer get implemetned but lets leave it here just in case
    "height": {
        "edit": addwidgets.IntEdit,
    },
    #"width"...
    "window": {
        "edit": None, #PathName
    }
}

ITEMS = {
    "arc": {
        "basic": ["fill", "outline", "width"],
        "all": ('dash', 'activedash', 'disableddash', 'dashoffset', 'fill', 'activefill',
                'disabledfill', 'stipple', 'activestipple', 'disabledstipple', 'state', 'tags',
                'width', 'activewidth', 'disabledwidth', 'arrow', 'arrowshape', 'capstyle',
                'joinstyle', 'smooth', 'splinesteps')
    },
    "bitmap":{#not implemented
        "basic": [],
        "all": ()
    },
    "image":{#not implemented
        "basic": [],
        "all": ()
    },
    "line": {
        "basic": ["fill", "width"],
        "all": ('dash', 'activedash', 'disableddash', 'dashoffset', 'fill', 'activefill', 'disabledfill',
                 'offset', 'outline', 'activeoutline', 'disabledoutline', 'outlineoffset', 'outlinestipple',
                 'activeoutlinestipple', 'disabledoutlinestipple', 'stipple', 'activestipple', 'disabledstipple',
                  'state', 'tags', 'width', 'activewidth', 'disabledwidth', 'extent', 'start', 'style')
    },
    "oval":{
        "basic": ["fill", "outline", "width"],
        "all": ('dash', 'activedash', 'disableddash', 'dashoffset', 'fill', 'activefill',
                'disabledfill', 'offset', 'outline', 'activeoutline', 'disabledoutline',
                'outlineoffset', 'outlinestipple', 'activeoutlinestipple', 'disabledoutlinestipple',
                'stipple', 'activestipple', 'disabledstipple', 'state', 'tags', 'width',
                'activewidth', 'disabledwidth')
    },
    "polygon":{
        "basic": ["fill", "outline", "width"],
        "all": ('dash', 'activedash', 'disableddash', 'dashoffset', 'fill', 'activefill',
                'disabledfill', 'offset', 'outline', 'activeoutline', 'disabledoutline',
                'outlineoffset', 'outlinestipple', 'activeoutlinestipple', 'disabledoutlinestipple',
                'stipple', 'activestipple', 'disabledstipple', 'state', 'tags', 'width',
                'activewidth', 'disabledwidth', 'joinstyle', 'smooth', 'splinesteps')
    },
    "rectangle":{
        "basic": ["fill", "outline", "width"],
        "all": ('dash', 'activedash', 'disableddash', 'dashoffset', 'fill', 'activefill',
                'disabledfill', 'offset', 'outline', 'activeoutline', 'disabledoutline',
                'outlineoffset', 'outlinestipple', 'activeoutlinestipple', 'disabledoutlinestipple',
                'stipple', 'activestipple', 'disabledstipple', 'state', 'tags', 'width',
                'activewidth', 'disabledwidth')
    },
    "text":{
        "basic": ["text", "font", "fill", "anchor"],
        "all": ('anchor', 'fill', 'activefill', 'disabledfill', 'stipple', 'activestipple',
                'disabledstipple', 'state', 'tags', "angle", "font", "justify", "text", "underline", "width")
    },
    "window":{#not implemented
        "basic": [],
        "all": ()
    }
}