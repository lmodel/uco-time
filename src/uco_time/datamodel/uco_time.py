# Auto generated from uco_time.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-04-12T12:20:50
# Schema: uco-time
#
# id: https://w3id.org/lmodel/uco-time
# description: Time classes for Unified Cyber Ontology
# license: https://www.apache.org/licenses/LICENSE-2.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace


metamodel_version = "1.7.0"
version = "1.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://example.org/UNKNOWN/NCIT/')
WIKIDATA = CurieNamespace('WIKIDATA', 'http://identifiers.org/wikidata/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LM_CORE = CurieNamespace('lm_core', 'https://w3id.org/lmodel/core/')
SUMO = CurieNamespace('sumo', 'https://w3id.org/sumo/kb/')
TIME = CurieNamespace('time', 'https://w3id.org/lmodel/uco-time/')
DEFAULT_ = TIME


# Types

# Class references



class Time(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME.Time
    class_class_curie: ClassVar[str] = "time:Time"
    class_name: ClassVar[str] = "Time"
    class_model_uri: ClassVar[URIRef] = TIME.Time


class TimeRange(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME.TimeRange
    class_class_curie: ClassVar[str] = "time:TimeRange"
    class_name: ClassVar[str] = "TimeRange"
    class_model_uri: ClassVar[URIRef] = TIME.TimeRange


class TimeStamp(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME.TimeStamp
    class_class_curie: ClassVar[str] = "time:TimeStamp"
    class_name: ClassVar[str] = "TimeStamp"
    class_model_uri: ClassVar[URIRef] = TIME.TimeStamp


# Enumerations


# Slots
class slots:
    pass

