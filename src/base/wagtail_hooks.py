# -*- coding: utf-8 -*-
from wagtail import hooks


@hooks.register("construct_page_action_menu")
def make_publish_default_action(menu_items, request, context):
    """
    Make publish action.
    """
    for index, item in enumerate(menu_items):
        if item.name == "action-publish":
            # move to top of list
            menu_items.pop(index)
            menu_items.insert(0, item)
            break
