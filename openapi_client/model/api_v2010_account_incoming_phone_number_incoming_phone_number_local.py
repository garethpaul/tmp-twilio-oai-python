"""
    Twilio - Api

    This is the public Twilio REST API.  # noqa: E501

    The version of the OpenAPI document: 1.8.0
    Contact: support@twilio.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('address_requirements',): {
            'NONE': "none",
            'ANY': "any",
            'LOCAL': "local",
            'FOREIGN': "foreign",
        },
        ('emergency_status',): {
            'ACTIVE': "Active",
            'INACTIVE': "Inactive",
        },
        ('sms_fallback_method',): {
            'HEAD': "head",
            'GET': "get",
            'POST': "post",
            'PATCH': "patch",
            'PUT': "put",
            'DELETE': "delete",
            'HEAD': "HEAD",
            'GET': "GET",
            'POST': "POST",
            'PATCH': "PATCH",
            'PUT': "PUT",
            'DELETE': "DELETE",
        },
        ('sms_method',): {
            'HEAD': "head",
            'GET': "get",
            'POST': "post",
            'PATCH': "patch",
            'PUT': "put",
            'DELETE': "delete",
            'HEAD': "HEAD",
            'GET': "GET",
            'POST': "POST",
            'PATCH': "PATCH",
            'PUT': "PUT",
            'DELETE': "DELETE",
        },
        ('status_callback_method',): {
            'HEAD': "head",
            'GET': "get",
            'POST': "post",
            'PATCH': "patch",
            'PUT': "put",
            'DELETE': "delete",
            'HEAD': "HEAD",
            'GET': "GET",
            'POST': "POST",
            'PATCH': "PATCH",
            'PUT': "PUT",
            'DELETE': "DELETE",
        },
        ('voice_fallback_method',): {
            'HEAD': "head",
            'GET': "get",
            'POST': "post",
            'PATCH': "patch",
            'PUT': "put",
            'DELETE': "delete",
            'HEAD': "HEAD",
            'GET': "GET",
            'POST': "POST",
            'PATCH': "PATCH",
            'PUT': "PUT",
            'DELETE': "DELETE",
        },
        ('voice_method',): {
            'HEAD': "head",
            'GET': "get",
            'POST': "post",
            'PATCH': "patch",
            'PUT': "put",
            'DELETE': "delete",
            'HEAD': "HEAD",
            'GET': "GET",
            'POST': "POST",
            'PATCH': "PATCH",
            'PUT': "PUT",
            'DELETE': "DELETE",
        },
        ('voice_receive_mode',): {
            'VOICE': "voice",
            'FAX': "fax",
        },
    }

    validations = {
        ('account_sid',): {
            'max_length': 34,
            'min_length': 34,
            'regex': {
                'pattern': r'^AC[0-9a-fA-F]{32}$',  # noqa: E501
            },
        },
        ('address_sid',): {
            'max_length': 34,
            'min_length': 34,
            'regex': {
                'pattern': r'^AD[0-9a-fA-F]{32}$',  # noqa: E501
            },
        },
        ('bundle_sid',): {
            'max_length': 34,
            'min_length': 34,
            'regex': {
                'pattern': r'^BU[0-9a-fA-F]{32}$',  # noqa: E501
            },
        },
        ('emergency_address_sid',): {
            'max_length': 34,
            'min_length': 34,
            'regex': {
                'pattern': r'^AD[0-9a-fA-F]{32}$',  # noqa: E501
            },
        },
        ('identity_sid',): {
            'max_length': 34,
            'min_length': 34,
            'regex': {
                'pattern': r'^RI[0-9a-fA-F]{32}$',  # noqa: E501
            },
        },
        ('sid',): {
            'max_length': 34,
            'min_length': 34,
            'regex': {
                'pattern': r'^PN[0-9a-fA-F]{32}$',  # noqa: E501
            },
        },
        ('sms_application_sid',): {
            'max_length': 34,
            'min_length': 34,
            'regex': {
                'pattern': r'^AP[0-9a-fA-F]{32}$',  # noqa: E501
            },
        },
        ('trunk_sid',): {
            'max_length': 34,
            'min_length': 34,
            'regex': {
                'pattern': r'^TK[0-9a-fA-F]{32}$',  # noqa: E501
            },
        },
        ('voice_application_sid',): {
            'max_length': 34,
            'min_length': 34,
            'regex': {
                'pattern': r'^AP[0-9a-fA-F]{32}$',  # noqa: E501
            },
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'account_sid': (str,),  # noqa: E501
            'address_requirements': (str,),  # noqa: E501
            'address_sid': (str,),  # noqa: E501
            'api_version': (str,),  # noqa: E501
            'beta': (bool,),  # noqa: E501
            'bundle_sid': (str,),  # noqa: E501
            'capabilities': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'date_created': (str,),  # noqa: E501
            'date_updated': (str,),  # noqa: E501
            'emergency_address_sid': (str,),  # noqa: E501
            'emergency_status': (str,),  # noqa: E501
            'friendly_name': (str,),  # noqa: E501
            'identity_sid': (str,),  # noqa: E501
            'origin': (str,),  # noqa: E501
            'phone_number': (str,),  # noqa: E501
            'sid': (str,),  # noqa: E501
            'sms_application_sid': (str,),  # noqa: E501
            'sms_fallback_method': (str,),  # noqa: E501
            'sms_fallback_url': (str,),  # noqa: E501
            'sms_method': (str,),  # noqa: E501
            'sms_url': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'status_callback': (str,),  # noqa: E501
            'status_callback_method': (str,),  # noqa: E501
            'trunk_sid': (str,),  # noqa: E501
            'uri': (str,),  # noqa: E501
            'voice_application_sid': (str,),  # noqa: E501
            'voice_caller_id_lookup': (bool,),  # noqa: E501
            'voice_fallback_method': (str,),  # noqa: E501
            'voice_fallback_url': (str,),  # noqa: E501
            'voice_method': (str,),  # noqa: E501
            'voice_receive_mode': (str,),  # noqa: E501
            'voice_url': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'account_sid': 'account_sid',  # noqa: E501
        'address_requirements': 'address_requirements',  # noqa: E501
        'address_sid': 'address_sid',  # noqa: E501
        'api_version': 'api_version',  # noqa: E501
        'beta': 'beta',  # noqa: E501
        'bundle_sid': 'bundle_sid',  # noqa: E501
        'capabilities': 'capabilities',  # noqa: E501
        'date_created': 'date_created',  # noqa: E501
        'date_updated': 'date_updated',  # noqa: E501
        'emergency_address_sid': 'emergency_address_sid',  # noqa: E501
        'emergency_status': 'emergency_status',  # noqa: E501
        'friendly_name': 'friendly_name',  # noqa: E501
        'identity_sid': 'identity_sid',  # noqa: E501
        'origin': 'origin',  # noqa: E501
        'phone_number': 'phone_number',  # noqa: E501
        'sid': 'sid',  # noqa: E501
        'sms_application_sid': 'sms_application_sid',  # noqa: E501
        'sms_fallback_method': 'sms_fallback_method',  # noqa: E501
        'sms_fallback_url': 'sms_fallback_url',  # noqa: E501
        'sms_method': 'sms_method',  # noqa: E501
        'sms_url': 'sms_url',  # noqa: E501
        'status': 'status',  # noqa: E501
        'status_callback': 'status_callback',  # noqa: E501
        'status_callback_method': 'status_callback_method',  # noqa: E501
        'trunk_sid': 'trunk_sid',  # noqa: E501
        'uri': 'uri',  # noqa: E501
        'voice_application_sid': 'voice_application_sid',  # noqa: E501
        'voice_caller_id_lookup': 'voice_caller_id_lookup',  # noqa: E501
        'voice_fallback_method': 'voice_fallback_method',  # noqa: E501
        'voice_fallback_url': 'voice_fallback_url',  # noqa: E501
        'voice_method': 'voice_method',  # noqa: E501
        'voice_receive_mode': 'voice_receive_mode',  # noqa: E501
        'voice_url': 'voice_url',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            account_sid (str): [optional]  # noqa: E501
            address_requirements (str): [optional]  # noqa: E501
            address_sid (str): [optional]  # noqa: E501
            api_version (str): [optional]  # noqa: E501
            beta (bool): [optional]  # noqa: E501
            bundle_sid (str): [optional]  # noqa: E501
            capabilities ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            date_created (str): [optional]  # noqa: E501
            date_updated (str): [optional]  # noqa: E501
            emergency_address_sid (str): [optional]  # noqa: E501
            emergency_status (str): [optional]  # noqa: E501
            friendly_name (str): [optional]  # noqa: E501
            identity_sid (str): [optional]  # noqa: E501
            origin (str): [optional]  # noqa: E501
            phone_number (str): [optional]  # noqa: E501
            sid (str): [optional]  # noqa: E501
            sms_application_sid (str): [optional]  # noqa: E501
            sms_fallback_method (str): [optional]  # noqa: E501
            sms_fallback_url (str): [optional]  # noqa: E501
            sms_method (str): [optional]  # noqa: E501
            sms_url (str): [optional]  # noqa: E501
            status (str): [optional]  # noqa: E501
            status_callback (str): [optional]  # noqa: E501
            status_callback_method (str): [optional]  # noqa: E501
            trunk_sid (str): [optional]  # noqa: E501
            uri (str): [optional]  # noqa: E501
            voice_application_sid (str): [optional]  # noqa: E501
            voice_caller_id_lookup (bool): [optional]  # noqa: E501
            voice_fallback_method (str): [optional]  # noqa: E501
            voice_fallback_url (str): [optional]  # noqa: E501
            voice_method (str): [optional]  # noqa: E501
            voice_receive_mode (str): [optional]  # noqa: E501
            voice_url (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
