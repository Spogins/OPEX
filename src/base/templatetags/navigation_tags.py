# -*- coding: utf-8 -*-
from django import template
from wagtail.models import Page, Site

register = template.Library()
# https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    return Site.find_for_request(context["request"]).root_page


def has_menu_children(page):
    # This is used by the top_menu property
    # get_children is a Treebeard API thing
    # https://tabo.pe/projects/django-treebeard/docs/4.0.1/api.html
    return page.get_children().live().in_menu().exists()


def has_children(page):
    # Generically allow index pages to list their children
    return page.get_children().live().exists()


def is_active(page, current_page):
    # To give us active state on main navigation
    return current_page.url_path.startswith(page.url_path) if current_page else False


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the Foundation menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag("includes/menu_item.html", takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    names = []
    for menuitem in menuitems:
        field_value = getattr(menuitem.specific, "name_in_navbar", None)
        names.append({"nav_name": field_value, "page": menuitem})
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = calling_page.url_path.startswith(menuitem.url_path) if calling_page else False

    return {
        "calling_page": calling_page,
        "menuitems": menuitems,
        "names": names,
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }


# Register tag for display url page in lower block
@register.inclusion_tag("includes/footer_item.html", takes_context=True)
def footer_top_menu(context, parent):
    footer_items = parent.get_children().live().in_menu()  # get pages which have show in navbar
    names = []  # list for save name page and page
    for item in footer_items:
        field_value = getattr(item.specific, "name_in_navbar", None)
        names.append({"footer_name": field_value, "page": item})

    return {"names": names, "request": context["request"]}


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag("includes/menu_children.html", takes_context=True)
def top_menu_children(context, parent, calling_page=None):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    child_names = []
    for menuitem in menuitems_children:
        menuitem.has_dropdown = has_menu_children(menuitem)
        field_value = getattr(menuitem.specific, "name_in_navbar", None)
        child_names.append({"child_name": field_value, "child_page": menuitem})
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = calling_page.url_path.startswith(menuitem.url_path) if calling_page else False
        menuitem.children = menuitem.get_children().live().in_menu()
    return {
        "parent": parent,
        "menuitems_children": menuitems_children,
        "child_names": child_names,
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the Foundation menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag("includes/mobile_menu_item.html", takes_context=True)
def mobile_top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    names = []
    for menuitem in menuitems:
        field_value = getattr(menuitem.specific, "name_in_navbar", None)
        names.append({"nav_name": field_value, "page": menuitem})
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = calling_page.url_path.startswith(menuitem.url_path) if calling_page else False

    return {
        "calling_page": calling_page,
        "menuitems": menuitems,
        "names": names,
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag("includes/mobile_menu_children.html", takes_context=True)
def mobile_top_menu_children(context, parent, calling_page=None):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    child_names = []
    for menuitem in menuitems_children:
        menuitem.has_dropdown = has_menu_children(menuitem)
        field_value = getattr(menuitem.specific, "name_in_navbar", None)
        child_names.append({"child_name": field_value, "child_page": menuitem})
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = calling_page.url_path.startswith(menuitem.url_path) if calling_page else False
        menuitem.children = menuitem.get_children().live().in_menu()
    return {
        "parent": parent,
        "menuitems_children": menuitems_children,
        "child_names": child_names,
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }


@register.inclusion_tag("tags/breadcrumbs.html", takes_context=True)
def breadcrumbs(context):
    self = context.get("self")
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(self, inclusive=True).filter(depth__gt=1)
    return {
        "ancestors": ancestors,
        "request": context["request"],
    }
