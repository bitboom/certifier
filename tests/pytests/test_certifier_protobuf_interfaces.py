# #####################################################################################
# Copyright (c) 2021-23, VMware Inc, and the Certifier Authors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ##############################################################################
"""
Basic pytests for Certifier Framework protobuf interfaces generated by
 $ protoc --python_out=.. ... ../certifier_service/certprotos/certifier.proto

See certifier.mak for the command issued.
"""
from inspect import getmembers, isclass, ismodule

# To resolve references to module and protobuf-python interface issues, run as:
# PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python PYTHONPATH=../.. pytest <filename>.py
import certifier_pb2 as cert_pbi

# ##############################################################################
# To see output, run: pytest --capture=tee-sys -v
def test_certifier_pb2_basic():
    """
    Basic test of generated certifier_pb2.py module.
    Verify existence of an expected list of class-names. Print list of classes.
    """

    assert ismodule(cert_pbi) is True

    pb2_classes = getmembers(cert_pbi, isclass)
    pb2_class_names = [ item[0] for item in pb2_classes]

    # Verify that some expected classes exist
    for pb_class in [  'ecc_message'
                     , 'key_message'
                     , 'rsa_message'
                     , 'protected_blob_message'
                     , 'vse_clause'
                    ]:
        assert pb_class in pb2_class_names

    print( )
    print('protobuf-generated class names in certifier_pb2.py:')
    for class_name in pb2_classes:
        print(' ', class_name)

# ##############################################################################
def test_certifier_pb2_describe_key_message():
    """
    Describe layout of 'key_message' class, verifying some expected member fields.
    """
    print('\nMember-fields in protobuf-generated class, key_message:')

    for attr in get_attrs(cert_pbi.key_message):
        print(' -', attr)

    print('\nMethods in protobuf-generated class, key_message:')
    for func in get_functions(cert_pbi.key_message):
        print(' -', func)

# ##############################################################################
def test_certifier_pb2_describe_vse_clause():
    """
    Describe layout of 'vse_clause' class, verifying some expected member fields.
    """
    print('\nMember-fields in protobuf-generated class vse_clause:')

    for attr in get_attrs(cert_pbi.vse_clause):
        print(' -', attr)

    print('\nMethods in protobuf-generated class, vse_clause:')
    for func in get_functions(cert_pbi.vse_clause):
        print(' -', func)

# ##############################################################################
def test_certifier_pb2_describe_rsa_message():
    """
    Describe layout of 'rsa_message' class, verifying some expected member fields.
    """
    print('\nMember-fields in protobuf-generated class rsa_message:')

    for attr in get_attrs(cert_pbi.rsa_message):
        print(' -', attr)

    print('\nMethods in protobuf-generated class, rsa_message:')
    for func in get_functions(cert_pbi.rsa_message):
        print(' -', func)

# ##############################################################################
def test_certifier_pb2_describe_time_point():
    """
    Describe layout of 'time_point' class, verifying some expected member fields.
    """
    print('\nMember-fields in protobuf-generated class time_point:')

    for attr in get_attrs(cert_pbi.time_point):
        print(' -', attr)

    print('\nMethods in protobuf-generated class, time_point:')
    for func in get_functions(cert_pbi.time_point):
        print(' -', func)

# ##############################################################################
def test_time_point():
    """
    Exercise class time_point() basic interfaces.
    """
    timept = cert_pbi.time_point()
    timept.year    = 2023
    timept.month   = 7
    timept.day     = 24
    timept.hour    = 17
    timept.minute  = 50
    timept.seconds = 20.23

    timept_serialized = timept.SerializeToString()
    print(timept_serialized)

    newtimept = cert_pbi.time_point.FromString(timept_serialized)
    assert newtimept == timept


# ##############################################################################
def get_attrs(klass):
    """Return a list of member-fields 'attributes' in a protobuf-generated class."""
    return [k for k in klass.__dict__.keys()
            if not k.startswith('__') and not k.endswith('__')
               and "_FieldProperty" in str(klass.__dict__[k])
          ]

# ##############################################################################
def get_functions(klass):
    """Return a list of functions in a protobuf-generated class."""
    return [k for k in klass.__dict__.keys()
            if not k.startswith('__') and not k.endswith('__')
               and "function" in str(klass.__dict__[k])
          ]