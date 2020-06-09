import sys
import typing


def addon_disable(module: str = ""):
    '''Disable an add-on 

    :param module: Module, Module name of the add-on to disable 
    :type module: str
    '''

    pass


def addon_enable(module: str = ""):
    '''Enable an add-on 

    :param module: Module, Module name of the add-on to enable 
    :type module: str
    '''

    pass


def addon_expand(module: str = ""):
    '''Display information and preferences for this add-on 

    :param module: Module, Module name of the add-on to expand 
    :type module: str
    '''

    pass


def addon_install(overwrite: bool = True,
                  target: typing.Union[str, int] = 'DEFAULT',
                  filepath: str = "",
                  filter_folder: bool = True,
                  filter_python: bool = True,
                  filter_glob: str = "*.py;*.zip"):
    '''Install an add-on 

    :param overwrite: Overwrite, Remove existing add-ons with the same ID 
    :type overwrite: bool
    :param target: Target Path 
    :type target: typing.Union[str, int]
    :param filepath: filepath 
    :type filepath: str
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_python: Filter python 
    :type filter_python: bool
    :param filter_glob: filter_glob 
    :type filter_glob: str
    '''

    pass


def addon_refresh():
    '''Scan add-on directories for new modules 

    '''

    pass


def addon_remove(module: str = ""):
    '''Delete the add-on from the file system 

    :param module: Module, Module name of the add-on to remove 
    :type module: str
    '''

    pass


def addon_show(module: str = ""):
    '''Show add-on preferences 

    :param module: Module, Module name of the add-on to expand 
    :type module: str
    '''

    pass


def app_template_install(overwrite: bool = True,
                         filepath: str = "",
                         filter_folder: bool = True,
                         filter_glob: str = "*.zip"):
    '''Install an application-template 

    :param overwrite: Overwrite, Remove existing template with the same ID 
    :type overwrite: bool
    :param filepath: filepath 
    :type filepath: str
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_glob: filter_glob 
    :type filter_glob: str
    '''

    pass


def copy_prev():
    '''Copy settings from previous version 

    '''

    pass


def keyconfig_activate(filepath: str = ""):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param filepath: filepath 
    :type filepath: str
    '''

    pass


def keyconfig_export(all: bool = False,
                     filepath: str = "keymap.py",
                     filter_folder: bool = True,
                     filter_text: bool = True,
                     filter_python: bool = True):
    '''Export key configuration to a python script 

    :param all: All Keymaps, Write all keymaps (not just user modified) 
    :type all: bool
    :param filepath: filepath 
    :type filepath: str
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_text: Filter text 
    :type filter_text: bool
    :param filter_python: Filter python 
    :type filter_python: bool
    '''

    pass


def keyconfig_import(filepath: str = "keymap.py",
                     filter_folder: bool = True,
                     filter_text: bool = True,
                     filter_python: bool = True,
                     keep_original: bool = True):
    '''Import key configuration from a python script 

    :param filepath: filepath 
    :type filepath: str
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_text: Filter text 
    :type filter_text: bool
    :param filter_python: Filter python 
    :type filter_python: bool
    :param keep_original: Keep original, Keep original file after copying to configuration folder 
    :type keep_original: bool
    '''

    pass


def keyconfig_remove():
    '''Remove key config 

    '''

    pass


def keyconfig_test():
    '''Test key-config for conflicts 

    '''

    pass


def keyitem_add():
    '''Add key map item 

    '''

    pass


def keyitem_remove(item_id: int = 0):
    '''Remove key map item 

    :param item_id: Item Identifier, Identifier of the item to remove 
    :type item_id: int
    '''

    pass


def keyitem_restore(item_id: int = 0):
    '''Restore key map item 

    :param item_id: Item Identifier, Identifier of the item to remove 
    :type item_id: int
    '''

    pass


def keymap_restore(all: bool = False):
    '''Restore key map(s) 

    :param all: All Keymaps, Restore all keymaps to default 
    :type all: bool
    '''

    pass


def reset_default_theme():
    '''Reset to the default theme colors 

    '''

    pass


def studiolight_copy_settings(index: int = 0):
    '''Copy Studio Light settings to the Studio light editor 

    :param index: index 
    :type index: int
    '''

    pass


def studiolight_install(
        files: typing.Union[typing.List['bpy.types.OperatorFileListElement'],
                            'bpy_prop_collection'] = None,
        directory: str = "",
        filter_folder: bool = True,
        filter_glob: str = "*.png;*.jpg;*.hdr;*.exr",
        type: typing.Union[str, int] = 'MATCAP'):
    '''Install a user defined studio light 

    :param files: File Path 
    :type files: typing.Union[typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param directory: directory 
    :type directory: str
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_glob: filter_glob 
    :type filter_glob: str
    :param type: type 
    :type type: typing.Union[str, int]
    '''

    pass


def studiolight_new(filename: str = "StudioLight"):
    '''Save custom studio light from the studio light editor settings 

    :param filename: Name 
    :type filename: str
    '''

    pass


def studiolight_show():
    '''Show light preferences 

    '''

    pass


def studiolight_uninstall(index: int = 0):
    '''Delete Studio Light 

    :param index: index 
    :type index: int
    '''

    pass


def theme_install(overwrite: bool = True,
                  filepath: str = "",
                  filter_folder: bool = True,
                  filter_glob: str = "*.xml"):
    '''Load and apply a Blender XML theme file 

    :param overwrite: Overwrite, Remove existing theme file if exists 
    :type overwrite: bool
    :param filepath: filepath 
    :type filepath: str
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_glob: filter_glob 
    :type filter_glob: str
    '''

    pass
