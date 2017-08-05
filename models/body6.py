# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Body6(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, pais: str=None, cantidad: int=None):
        """
        Body6 - a model defined in Swagger

        :param pais: The pais of this Body6.
        :type pais: str
        :param cantidad: The cantidad of this Body6.
        :type cantidad: int
        """
        self.swagger_types = {
            'pais': str,
            'cantidad': int
        }

        self.attribute_map = {
            'pais': 'Pais',
            'cantidad': 'Cantidad'
        }

        self._pais = pais
        self._cantidad = cantidad

    @classmethod
    def from_dict(cls, dikt) -> 'Body6':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_6 of this Body6.
        :rtype: Body6
        """
        return deserialize_model(dikt, cls)

    @property
    def pais(self) -> str:
        """
        Gets the pais of this Body6.

        :return: The pais of this Body6.
        :rtype: str
        """
        return self._pais

    @pais.setter
    def pais(self, pais: str):
        """
        Sets the pais of this Body6.

        :param pais: The pais of this Body6.
        :type pais: str
        """

        self._pais = pais

    @property
    def cantidad(self) -> int:
        """
        Gets the cantidad of this Body6.

        :return: The cantidad of this Body6.
        :rtype: int
        """
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad: int):
        """
        Sets the cantidad of this Body6.

        :param cantidad: The cantidad of this Body6.
        :type cantidad: int
        """

        self._cantidad = cantidad
