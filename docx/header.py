# encoding: utf-8

"""
Page headers and footers.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from .blkcntnr import BlockItemContainer
from .shared import ElementProxy, lazyproperty


class _BaseHeaderFooter(ElementProxy):
    """
    Base class for header and footer objects.
    """

    __slots__ = ('_sectPr', '_type')

    def __init__(self, element, parent, type):
        super(_BaseHeaderFooter, self).__init__(element, parent)
        self._sectPr = element
        self._type = type

    def _get_reference_of_type(self):
        raise NotImplemented()

    @lazyproperty
    def body(self):
        """
        BlockItemContainer instance with contents of Header or Footer
        """
        ref = self._get_reference_of_type()
        if ref is None:
            return None
        return self.part.related_hdrftr_body(ref.rId)

    @property
    def is_linked_to_previous(self):
        """
        Boolean representing whether this Header or Footer is inherited from
        a previous section.
        """
        ref = self._get_reference_of_type()
        if ref is None:
            return True
        return False


class Header(_BaseHeaderFooter):
    """
    One of the page headers for a section.
    """

    def _get_reference_of_type(self):
        return self._sectPr.get_headerReference_of_type(self._type)


class Footer(_BaseHeaderFooter):
    """
    One of the page footers for a section.
    """

    def _get_reference_of_type(self):
        return self._sectPr.get_footerReference_of_type(self._type)


class HeaderFooterBody(BlockItemContainer):
    """
    The rich-text body of a header or footer. Supports the same rich text
    operations as a document, such as paragraphs and tables.
    """
