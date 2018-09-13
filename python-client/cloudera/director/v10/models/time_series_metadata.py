# coding: utf-8

"""
Licensed to Cloudera, Inc. under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  Cloudera, Inc. licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import pprint
import re  # noqa: F401

import six


class TimeSeriesMetadata(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'alias': 'str',
        'attributes': 'dict(str, str)',
        'end_time': 'int',
        'entity_name': 'str',
        'expression': 'str',
        'metric_collection_frequency_ms': 'int',
        'metric_name': 'str',
        'rollup_used': 'str',
        'start_time': 'int',
        'unit_denominators': 'list[str]',
        'unit_numerators': 'list[str]'
    }

    attribute_map = {
        'alias': 'alias',
        'attributes': 'attributes',
        'end_time': 'endTime',
        'entity_name': 'entityName',
        'expression': 'expression',
        'metric_collection_frequency_ms': 'metricCollectionFrequencyMs',
        'metric_name': 'metricName',
        'rollup_used': 'rollupUsed',
        'start_time': 'startTime',
        'unit_denominators': 'unitDenominators',
        'unit_numerators': 'unitNumerators'
    }

    def __init__(self, alias=None, attributes=None, end_time=None, entity_name=None, expression=None, metric_collection_frequency_ms=None, metric_name=None, rollup_used=None, start_time=None, unit_denominators=None, unit_numerators=None):  # noqa: E501
        """TimeSeriesMetadata - a model defined in Swagger"""  # noqa: E501

        self._alias = None
        self._attributes = None
        self._end_time = None
        self._entity_name = None
        self._expression = None
        self._metric_collection_frequency_ms = None
        self._metric_name = None
        self._rollup_used = None
        self._start_time = None
        self._unit_denominators = None
        self._unit_numerators = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if attributes is not None:
            self.attributes = attributes
        self.end_time = end_time
        self.entity_name = entity_name
        self.expression = expression
        if metric_collection_frequency_ms is not None:
            self.metric_collection_frequency_ms = metric_collection_frequency_ms
        self.metric_name = metric_name
        self.rollup_used = rollup_used
        self.start_time = start_time
        if unit_denominators is not None:
            self.unit_denominators = unit_denominators
        if unit_numerators is not None:
            self.unit_numerators = unit_numerators

    @property
    def alias(self):
        """Gets the alias of this TimeSeriesMetadata.  # noqa: E501

        Alias  # noqa: E501

        :return: The alias of this TimeSeriesMetadata.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this TimeSeriesMetadata.

        Alias  # noqa: E501

        :param alias: The alias of this TimeSeriesMetadata.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def attributes(self):
        """Gets the attributes of this TimeSeriesMetadata.  # noqa: E501

        Attributes  # noqa: E501

        :return: The attributes of this TimeSeriesMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this TimeSeriesMetadata.

        Attributes  # noqa: E501

        :param attributes: The attributes of this TimeSeriesMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._attributes = attributes

    @property
    def end_time(self):
        """Gets the end_time of this TimeSeriesMetadata.  # noqa: E501

        End time  # noqa: E501

        :return: The end_time of this TimeSeriesMetadata.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TimeSeriesMetadata.

        End time  # noqa: E501

        :param end_time: The end_time of this TimeSeriesMetadata.  # noqa: E501
        :type: int
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def entity_name(self):
        """Gets the entity_name of this TimeSeriesMetadata.  # noqa: E501

        Entity name  # noqa: E501

        :return: The entity_name of this TimeSeriesMetadata.  # noqa: E501
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this TimeSeriesMetadata.

        Entity name  # noqa: E501

        :param entity_name: The entity_name of this TimeSeriesMetadata.  # noqa: E501
        :type: str
        """
        if entity_name is None:
            raise ValueError("Invalid value for `entity_name`, must not be `None`")  # noqa: E501

        self._entity_name = entity_name

    @property
    def expression(self):
        """Gets the expression of this TimeSeriesMetadata.  # noqa: E501

        Expression  # noqa: E501

        :return: The expression of this TimeSeriesMetadata.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this TimeSeriesMetadata.

        Expression  # noqa: E501

        :param expression: The expression of this TimeSeriesMetadata.  # noqa: E501
        :type: str
        """
        if expression is None:
            raise ValueError("Invalid value for `expression`, must not be `None`")  # noqa: E501

        self._expression = expression

    @property
    def metric_collection_frequency_ms(self):
        """Gets the metric_collection_frequency_ms of this TimeSeriesMetadata.  # noqa: E501

        Metric collection frequency in milliseconds  # noqa: E501

        :return: The metric_collection_frequency_ms of this TimeSeriesMetadata.  # noqa: E501
        :rtype: int
        """
        return self._metric_collection_frequency_ms

    @metric_collection_frequency_ms.setter
    def metric_collection_frequency_ms(self, metric_collection_frequency_ms):
        """Sets the metric_collection_frequency_ms of this TimeSeriesMetadata.

        Metric collection frequency in milliseconds  # noqa: E501

        :param metric_collection_frequency_ms: The metric_collection_frequency_ms of this TimeSeriesMetadata.  # noqa: E501
        :type: int
        """

        self._metric_collection_frequency_ms = metric_collection_frequency_ms

    @property
    def metric_name(self):
        """Gets the metric_name of this TimeSeriesMetadata.  # noqa: E501

        Metric name  # noqa: E501

        :return: The metric_name of this TimeSeriesMetadata.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this TimeSeriesMetadata.

        Metric name  # noqa: E501

        :param metric_name: The metric_name of this TimeSeriesMetadata.  # noqa: E501
        :type: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

    @property
    def rollup_used(self):
        """Gets the rollup_used of this TimeSeriesMetadata.  # noqa: E501

        Rollup used  # noqa: E501

        :return: The rollup_used of this TimeSeriesMetadata.  # noqa: E501
        :rtype: str
        """
        return self._rollup_used

    @rollup_used.setter
    def rollup_used(self, rollup_used):
        """Sets the rollup_used of this TimeSeriesMetadata.

        Rollup used  # noqa: E501

        :param rollup_used: The rollup_used of this TimeSeriesMetadata.  # noqa: E501
        :type: str
        """
        if rollup_used is None:
            raise ValueError("Invalid value for `rollup_used`, must not be `None`")  # noqa: E501

        self._rollup_used = rollup_used

    @property
    def start_time(self):
        """Gets the start_time of this TimeSeriesMetadata.  # noqa: E501

        Start time  # noqa: E501

        :return: The start_time of this TimeSeriesMetadata.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TimeSeriesMetadata.

        Start time  # noqa: E501

        :param start_time: The start_time of this TimeSeriesMetadata.  # noqa: E501
        :type: int
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def unit_denominators(self):
        """Gets the unit_denominators of this TimeSeriesMetadata.  # noqa: E501

        Unit denominators  # noqa: E501

        :return: The unit_denominators of this TimeSeriesMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._unit_denominators

    @unit_denominators.setter
    def unit_denominators(self, unit_denominators):
        """Sets the unit_denominators of this TimeSeriesMetadata.

        Unit denominators  # noqa: E501

        :param unit_denominators: The unit_denominators of this TimeSeriesMetadata.  # noqa: E501
        :type: list[str]
        """

        self._unit_denominators = unit_denominators

    @property
    def unit_numerators(self):
        """Gets the unit_numerators of this TimeSeriesMetadata.  # noqa: E501

        Unit numerators  # noqa: E501

        :return: The unit_numerators of this TimeSeriesMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._unit_numerators

    @unit_numerators.setter
    def unit_numerators(self, unit_numerators):
        """Sets the unit_numerators of this TimeSeriesMetadata.

        Unit numerators  # noqa: E501

        :param unit_numerators: The unit_numerators of this TimeSeriesMetadata.  # noqa: E501
        :type: list[str]
        """

        self._unit_numerators = unit_numerators

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimeSeriesMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other