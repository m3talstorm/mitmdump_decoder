# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import holoholo_shared_pb2 as holoholo__shared__pb2

from holoholo_shared_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='map.proto',
  package='PGo',
  syntax='proto3',
  serialized_pb=_b('\n\tmap.proto\x12\x03PGo\x1a\x15holoholo_shared.proto\"_\n\x12GetMapObjectsProto\x12\x0e\n\x06\x43\x65llId\x18\x01 \x01(\x05\x12\x13\n\x0bSinceTimeMs\x18\x02 \x01(\x03\x12\x11\n\tPlayerLat\x18\x03 \x01(\x01\x12\x11\n\tPlayerLng\x18\x04 \x01(\x01\"s\n\x15GetMapObjectsOutProto\x12(\n\x07MapCell\x18\x01 \x03(\x0b\x32\x17.PGo.ClientMapCellProto\x12\x30\n\x06Status\x18\x02 \x01(\x0e\x32 .PGo.GetMapObjectsOutProtoStatus\"\xb7\x03\n\x12\x43lientMapCellProto\x12\x10\n\x08S2CellId\x18\x01 \x01(\x04\x12\x12\n\nAsOfTimeMs\x18\x02 \x01(\x03\x12#\n\x04\x46ort\x18\x03 \x03(\x0b\x32\x15.PGo.PokemonFortProto\x12.\n\nSpawnPoint\x18\x04 \x03(\x0b\x32\x1a.PGo.ClientSpawnPointProto\x12\x15\n\rDeletedObject\x18\x06 \x01(\x08\x12\x17\n\x0fIsTruncatedList\x18\x07 \x01(\x08\x12\x31\n\x0b\x46ortSummary\x18\x08 \x03(\x0b\x32\x1c.PGo.PokemonSummaryFortProto\x12\x37\n\x13\x44\x65\x63imatedSpawnPoint\x18\t \x03(\x0b\x32\x1a.PGo.ClientSpawnPointProto\x12.\n\rNearbyPokemon\x18\x0b \x03(\x0b\x32\x17.PGo.NearbyPokemonProto\x12*\n\x0bWildPokemon\x18\x05 \x03(\x0b\x32\x15.PGo.WildPokemonProto\x12.\n\x10\x43\x61tchablePokemon\x18\n \x03(\x0b\x32\x14.PGo.MapPokemonProto\"\x8b\x05\n\x10PokemonFortProto\x12\x0e\n\x06\x46ortId\x18\x01 \x01(\t\x12\x16\n\x0eLastModifiedMs\x18\x02 \x01(\x03\x12\x10\n\x08Latitude\x18\x03 \x01(\x01\x12\x11\n\tLongitude\x18\x04 \x01(\x01\x12\x0f\n\x07\x45nabled\x18\x08 \x01(\x08\x12#\n\x04Team\x18\x05 \x01(\x0e\x32\x15.PGo.Custom_TeamColor\x12/\n\x0eGuardPokemonId\x18\x06 \x01(\x0e\x32\x17.PGo.Custom_PokemonName\x12\x19\n\x11GuardPokemonLevel\x18\x07 \x01(\x05\x12\x11\n\tGymPoints\x18\n \x01(\x03\x12\x12\n\nIsInBattle\x18\x0b \x01(\x08\x12,\n\x08\x46ortType\x18\t \x01(\x0e\x32\x1a.PGo.Holoholo.Rpc.FortType\x12\x1a\n\x12\x43ooldownCompleteMs\x18\x0e \x01(\x03\x12!\n\x07Sponsor\x18\x0f \x01(\x0e\x32\x10.PGo.FortSponsor\x12-\n\rRenderingType\x18\x10 \x01(\x0e\x32\x16.PGo.FortRenderingType\x12\x1a\n\x12\x41\x63tiveFortModifier\x18\x0c \x01(\x0c\x12\x44\n\x0c\x46ortLureInfo\x18\r \x01(\x0b\x32..PGo.PokemonFortProto.Custom_FortLureInfoProto\x1a\x82\x01\n\x18\x43ustom_FortLureInfoProto\x12\x0e\n\x06\x46ortId\x18\x01 \x01(\t\x12\x10\n\x08NotSure2\x18\x02 \x01(\x01\x12.\n\rActivePokemon\x18\x03 \x01(\x0e\x32\x17.PGo.Custom_PokemonName\x12\x14\n\x0cLureExpiryMs\x18\x04 \x01(\x03\"m\n\x17PokemonSummaryFortProto\x12\x15\n\rFortSummaryId\x18\x01 \x01(\t\x12\x16\n\x0eLastModifiedMs\x18\x02 \x01(\x03\x12\x10\n\x08Latitude\x18\x03 \x01(\x01\x12\x11\n\tLongitude\x18\x04 \x01(\x01\"q\n\x12NearbyPokemonProto\x12.\n\rPokedexNumber\x18\x01 \x01(\x0e\x32\x17.PGo.Custom_PokemonName\x12\x16\n\x0e\x44istanceMeters\x18\x02 \x01(\x02\x12\x13\n\x0b\x45ncounterId\x18\x03 \x01(\x01\"\xb8\x01\n\x10WildPokemonProto\x12\x13\n\x0b\x45ncounterId\x18\x01 \x01(\x01\x12\x16\n\x0eLastModifiedMs\x18\x02 \x01(\x03\x12\x10\n\x08Latitude\x18\x03 \x01(\x01\x12\x11\n\tLongitude\x18\x04 \x01(\x01\x12\x14\n\x0cSpawnPointId\x18\x05 \x01(\t\x12\"\n\x07Pokemon\x18\x07 \x01(\x0b\x32\x11.PGo.PokemonProto\x12\x18\n\x10TimeTillHiddenMs\x18\x0b \x01(\x05\"<\n\x15\x43lientSpawnPointProto\x12\x10\n\x08Latitude\x18\x02 \x01(\x01\x12\x11\n\tLongitude\x18\x03 \x01(\x01\"\xab\x01\n\x0fMapPokemonProto\x12\x14\n\x0cSpawnpointId\x18\x01 \x01(\t\x12\x13\n\x0b\x45ncounterId\x18\x02 \x01(\x01\x12.\n\rPokedexTypeId\x18\x03 \x01(\x0e\x32\x17.PGo.Custom_PokemonName\x12\x18\n\x10\x45xpirationTimeMs\x18\x04 \x01(\x03\x12\x10\n\x08Latitude\x18\x05 \x01(\x01\x12\x11\n\tLongitude\x18\x06 \x01(\x01*P\n\x1bGetMapObjectsOutProtoStatus\x12\x10\n\x0cUNSET_STATUS\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x12\n\x0eLOCATION_UNSET\x10\x02*B\n\x0b\x46ortSponsor\x12\x11\n\rUNSET_SPONSOR\x10\x00\x12\r\n\tMCDONALDS\x10\x01\x12\x11\n\rPOKEMON_STORE\x10\x02*3\n\x11\x46ortRenderingType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x11\n\rINTERNAL_TEST\x10\x01P\x00\x62\x06proto3')
  ,
  dependencies=[holoholo__shared__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_GETMAPOBJECTSOUTPROTOSTATUS = _descriptor.EnumDescriptor(
  name='GetMapObjectsOutProtoStatus',
  full_name='PGo.GetMapObjectsOutProtoStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_STATUS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_UNSET', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2000,
  serialized_end=2080,
)
_sym_db.RegisterEnumDescriptor(_GETMAPOBJECTSOUTPROTOSTATUS)

GetMapObjectsOutProtoStatus = enum_type_wrapper.EnumTypeWrapper(_GETMAPOBJECTSOUTPROTOSTATUS)
_FORTSPONSOR = _descriptor.EnumDescriptor(
  name='FortSponsor',
  full_name='PGo.FortSponsor',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_SPONSOR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MCDONALDS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_STORE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2082,
  serialized_end=2148,
)
_sym_db.RegisterEnumDescriptor(_FORTSPONSOR)

FortSponsor = enum_type_wrapper.EnumTypeWrapper(_FORTSPONSOR)
_FORTRENDERINGTYPE = _descriptor.EnumDescriptor(
  name='FortRenderingType',
  full_name='PGo.FortRenderingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_TEST', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2150,
  serialized_end=2201,
)
_sym_db.RegisterEnumDescriptor(_FORTRENDERINGTYPE)

FortRenderingType = enum_type_wrapper.EnumTypeWrapper(_FORTRENDERINGTYPE)
UNSET_STATUS = 0
SUCCESS = 1
LOCATION_UNSET = 2
UNSET_SPONSOR = 0
MCDONALDS = 1
POKEMON_STORE = 2
DEFAULT = 0
INTERNAL_TEST = 1



_GETMAPOBJECTSPROTO = _descriptor.Descriptor(
  name='GetMapObjectsProto',
  full_name='PGo.GetMapObjectsProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='CellId', full_name='PGo.GetMapObjectsProto.CellId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SinceTimeMs', full_name='PGo.GetMapObjectsProto.SinceTimeMs', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PlayerLat', full_name='PGo.GetMapObjectsProto.PlayerLat', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PlayerLng', full_name='PGo.GetMapObjectsProto.PlayerLng', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=136,
)


_GETMAPOBJECTSOUTPROTO = _descriptor.Descriptor(
  name='GetMapObjectsOutProto',
  full_name='PGo.GetMapObjectsOutProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MapCell', full_name='PGo.GetMapObjectsOutProto.MapCell', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Status', full_name='PGo.GetMapObjectsOutProto.Status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=253,
)


_CLIENTMAPCELLPROTO = _descriptor.Descriptor(
  name='ClientMapCellProto',
  full_name='PGo.ClientMapCellProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='S2CellId', full_name='PGo.ClientMapCellProto.S2CellId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AsOfTimeMs', full_name='PGo.ClientMapCellProto.AsOfTimeMs', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Fort', full_name='PGo.ClientMapCellProto.Fort', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpawnPoint', full_name='PGo.ClientMapCellProto.SpawnPoint', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DeletedObject', full_name='PGo.ClientMapCellProto.DeletedObject', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IsTruncatedList', full_name='PGo.ClientMapCellProto.IsTruncatedList', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FortSummary', full_name='PGo.ClientMapCellProto.FortSummary', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DecimatedSpawnPoint', full_name='PGo.ClientMapCellProto.DecimatedSpawnPoint', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NearbyPokemon', full_name='PGo.ClientMapCellProto.NearbyPokemon', index=8,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WildPokemon', full_name='PGo.ClientMapCellProto.WildPokemon', index=9,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CatchablePokemon', full_name='PGo.ClientMapCellProto.CatchablePokemon', index=10,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=695,
)


_POKEMONFORTPROTO_CUSTOM_FORTLUREINFOPROTO = _descriptor.Descriptor(
  name='Custom_FortLureInfoProto',
  full_name='PGo.PokemonFortProto.Custom_FortLureInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FortId', full_name='PGo.PokemonFortProto.Custom_FortLureInfoProto.FortId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NotSure2', full_name='PGo.PokemonFortProto.Custom_FortLureInfoProto.NotSure2', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ActivePokemon', full_name='PGo.PokemonFortProto.Custom_FortLureInfoProto.ActivePokemon', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LureExpiryMs', full_name='PGo.PokemonFortProto.Custom_FortLureInfoProto.LureExpiryMs', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1219,
  serialized_end=1349,
)

_POKEMONFORTPROTO = _descriptor.Descriptor(
  name='PokemonFortProto',
  full_name='PGo.PokemonFortProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FortId', full_name='PGo.PokemonFortProto.FortId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastModifiedMs', full_name='PGo.PokemonFortProto.LastModifiedMs', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Latitude', full_name='PGo.PokemonFortProto.Latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Longitude', full_name='PGo.PokemonFortProto.Longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Enabled', full_name='PGo.PokemonFortProto.Enabled', index=4,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Team', full_name='PGo.PokemonFortProto.Team', index=5,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GuardPokemonId', full_name='PGo.PokemonFortProto.GuardPokemonId', index=6,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GuardPokemonLevel', full_name='PGo.PokemonFortProto.GuardPokemonLevel', index=7,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GymPoints', full_name='PGo.PokemonFortProto.GymPoints', index=8,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IsInBattle', full_name='PGo.PokemonFortProto.IsInBattle', index=9,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FortType', full_name='PGo.PokemonFortProto.FortType', index=10,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CooldownCompleteMs', full_name='PGo.PokemonFortProto.CooldownCompleteMs', index=11,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Sponsor', full_name='PGo.PokemonFortProto.Sponsor', index=12,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RenderingType', full_name='PGo.PokemonFortProto.RenderingType', index=13,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ActiveFortModifier', full_name='PGo.PokemonFortProto.ActiveFortModifier', index=14,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FortLureInfo', full_name='PGo.PokemonFortProto.FortLureInfo', index=15,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_POKEMONFORTPROTO_CUSTOM_FORTLUREINFOPROTO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=698,
  serialized_end=1349,
)


_POKEMONSUMMARYFORTPROTO = _descriptor.Descriptor(
  name='PokemonSummaryFortProto',
  full_name='PGo.PokemonSummaryFortProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FortSummaryId', full_name='PGo.PokemonSummaryFortProto.FortSummaryId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastModifiedMs', full_name='PGo.PokemonSummaryFortProto.LastModifiedMs', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Latitude', full_name='PGo.PokemonSummaryFortProto.Latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Longitude', full_name='PGo.PokemonSummaryFortProto.Longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1351,
  serialized_end=1460,
)


_NEARBYPOKEMONPROTO = _descriptor.Descriptor(
  name='NearbyPokemonProto',
  full_name='PGo.NearbyPokemonProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PokedexNumber', full_name='PGo.NearbyPokemonProto.PokedexNumber', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DistanceMeters', full_name='PGo.NearbyPokemonProto.DistanceMeters', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EncounterId', full_name='PGo.NearbyPokemonProto.EncounterId', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1462,
  serialized_end=1575,
)


_WILDPOKEMONPROTO = _descriptor.Descriptor(
  name='WildPokemonProto',
  full_name='PGo.WildPokemonProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='EncounterId', full_name='PGo.WildPokemonProto.EncounterId', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastModifiedMs', full_name='PGo.WildPokemonProto.LastModifiedMs', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Latitude', full_name='PGo.WildPokemonProto.Latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Longitude', full_name='PGo.WildPokemonProto.Longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpawnPointId', full_name='PGo.WildPokemonProto.SpawnPointId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pokemon', full_name='PGo.WildPokemonProto.Pokemon', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeTillHiddenMs', full_name='PGo.WildPokemonProto.TimeTillHiddenMs', index=6,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1578,
  serialized_end=1762,
)


_CLIENTSPAWNPOINTPROTO = _descriptor.Descriptor(
  name='ClientSpawnPointProto',
  full_name='PGo.ClientSpawnPointProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Latitude', full_name='PGo.ClientSpawnPointProto.Latitude', index=0,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Longitude', full_name='PGo.ClientSpawnPointProto.Longitude', index=1,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1764,
  serialized_end=1824,
)


_MAPPOKEMONPROTO = _descriptor.Descriptor(
  name='MapPokemonProto',
  full_name='PGo.MapPokemonProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SpawnpointId', full_name='PGo.MapPokemonProto.SpawnpointId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EncounterId', full_name='PGo.MapPokemonProto.EncounterId', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PokedexTypeId', full_name='PGo.MapPokemonProto.PokedexTypeId', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ExpirationTimeMs', full_name='PGo.MapPokemonProto.ExpirationTimeMs', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Latitude', full_name='PGo.MapPokemonProto.Latitude', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Longitude', full_name='PGo.MapPokemonProto.Longitude', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1827,
  serialized_end=1998,
)

_GETMAPOBJECTSOUTPROTO.fields_by_name['MapCell'].message_type = _CLIENTMAPCELLPROTO
_GETMAPOBJECTSOUTPROTO.fields_by_name['Status'].enum_type = _GETMAPOBJECTSOUTPROTOSTATUS
_CLIENTMAPCELLPROTO.fields_by_name['Fort'].message_type = _POKEMONFORTPROTO
_CLIENTMAPCELLPROTO.fields_by_name['SpawnPoint'].message_type = _CLIENTSPAWNPOINTPROTO
_CLIENTMAPCELLPROTO.fields_by_name['FortSummary'].message_type = _POKEMONSUMMARYFORTPROTO
_CLIENTMAPCELLPROTO.fields_by_name['DecimatedSpawnPoint'].message_type = _CLIENTSPAWNPOINTPROTO
_CLIENTMAPCELLPROTO.fields_by_name['NearbyPokemon'].message_type = _NEARBYPOKEMONPROTO
_CLIENTMAPCELLPROTO.fields_by_name['WildPokemon'].message_type = _WILDPOKEMONPROTO
_CLIENTMAPCELLPROTO.fields_by_name['CatchablePokemon'].message_type = _MAPPOKEMONPROTO
_POKEMONFORTPROTO_CUSTOM_FORTLUREINFOPROTO.fields_by_name['ActivePokemon'].enum_type = holoholo__shared__pb2._CUSTOM_POKEMONNAME
_POKEMONFORTPROTO_CUSTOM_FORTLUREINFOPROTO.containing_type = _POKEMONFORTPROTO
_POKEMONFORTPROTO.fields_by_name['Team'].enum_type = holoholo__shared__pb2._CUSTOM_TEAMCOLOR
_POKEMONFORTPROTO.fields_by_name['GuardPokemonId'].enum_type = holoholo__shared__pb2._CUSTOM_POKEMONNAME
_POKEMONFORTPROTO.fields_by_name['FortType'].enum_type = holoholo__shared__pb2._HOLOHOLO_RPC_FORTTYPE
_POKEMONFORTPROTO.fields_by_name['Sponsor'].enum_type = _FORTSPONSOR
_POKEMONFORTPROTO.fields_by_name['RenderingType'].enum_type = _FORTRENDERINGTYPE
_POKEMONFORTPROTO.fields_by_name['FortLureInfo'].message_type = _POKEMONFORTPROTO_CUSTOM_FORTLUREINFOPROTO
_NEARBYPOKEMONPROTO.fields_by_name['PokedexNumber'].enum_type = holoholo__shared__pb2._CUSTOM_POKEMONNAME
_WILDPOKEMONPROTO.fields_by_name['Pokemon'].message_type = holoholo__shared__pb2._POKEMONPROTO
_MAPPOKEMONPROTO.fields_by_name['PokedexTypeId'].enum_type = holoholo__shared__pb2._CUSTOM_POKEMONNAME
DESCRIPTOR.message_types_by_name['GetMapObjectsProto'] = _GETMAPOBJECTSPROTO
DESCRIPTOR.message_types_by_name['GetMapObjectsOutProto'] = _GETMAPOBJECTSOUTPROTO
DESCRIPTOR.message_types_by_name['ClientMapCellProto'] = _CLIENTMAPCELLPROTO
DESCRIPTOR.message_types_by_name['PokemonFortProto'] = _POKEMONFORTPROTO
DESCRIPTOR.message_types_by_name['PokemonSummaryFortProto'] = _POKEMONSUMMARYFORTPROTO
DESCRIPTOR.message_types_by_name['NearbyPokemonProto'] = _NEARBYPOKEMONPROTO
DESCRIPTOR.message_types_by_name['WildPokemonProto'] = _WILDPOKEMONPROTO
DESCRIPTOR.message_types_by_name['ClientSpawnPointProto'] = _CLIENTSPAWNPOINTPROTO
DESCRIPTOR.message_types_by_name['MapPokemonProto'] = _MAPPOKEMONPROTO
DESCRIPTOR.enum_types_by_name['GetMapObjectsOutProtoStatus'] = _GETMAPOBJECTSOUTPROTOSTATUS
DESCRIPTOR.enum_types_by_name['FortSponsor'] = _FORTSPONSOR
DESCRIPTOR.enum_types_by_name['FortRenderingType'] = _FORTRENDERINGTYPE

GetMapObjectsProto = _reflection.GeneratedProtocolMessageType('GetMapObjectsProto', (_message.Message,), dict(
  DESCRIPTOR = _GETMAPOBJECTSPROTO,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.GetMapObjectsProto)
  ))
_sym_db.RegisterMessage(GetMapObjectsProto)

GetMapObjectsOutProto = _reflection.GeneratedProtocolMessageType('GetMapObjectsOutProto', (_message.Message,), dict(
  DESCRIPTOR = _GETMAPOBJECTSOUTPROTO,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.GetMapObjectsOutProto)
  ))
_sym_db.RegisterMessage(GetMapObjectsOutProto)

ClientMapCellProto = _reflection.GeneratedProtocolMessageType('ClientMapCellProto', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTMAPCELLPROTO,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.ClientMapCellProto)
  ))
_sym_db.RegisterMessage(ClientMapCellProto)

PokemonFortProto = _reflection.GeneratedProtocolMessageType('PokemonFortProto', (_message.Message,), dict(

  Custom_FortLureInfoProto = _reflection.GeneratedProtocolMessageType('Custom_FortLureInfoProto', (_message.Message,), dict(
    DESCRIPTOR = _POKEMONFORTPROTO_CUSTOM_FORTLUREINFOPROTO,
    __module__ = 'map_pb2'
    # @@protoc_insertion_point(class_scope:PGo.PokemonFortProto.Custom_FortLureInfoProto)
    ))
  ,
  DESCRIPTOR = _POKEMONFORTPROTO,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.PokemonFortProto)
  ))
_sym_db.RegisterMessage(PokemonFortProto)
_sym_db.RegisterMessage(PokemonFortProto.Custom_FortLureInfoProto)

PokemonSummaryFortProto = _reflection.GeneratedProtocolMessageType('PokemonSummaryFortProto', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONSUMMARYFORTPROTO,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.PokemonSummaryFortProto)
  ))
_sym_db.RegisterMessage(PokemonSummaryFortProto)

NearbyPokemonProto = _reflection.GeneratedProtocolMessageType('NearbyPokemonProto', (_message.Message,), dict(
  DESCRIPTOR = _NEARBYPOKEMONPROTO,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.NearbyPokemonProto)
  ))
_sym_db.RegisterMessage(NearbyPokemonProto)

WildPokemonProto = _reflection.GeneratedProtocolMessageType('WildPokemonProto', (_message.Message,), dict(
  DESCRIPTOR = _WILDPOKEMONPROTO,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.WildPokemonProto)
  ))
_sym_db.RegisterMessage(WildPokemonProto)

ClientSpawnPointProto = _reflection.GeneratedProtocolMessageType('ClientSpawnPointProto', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTSPAWNPOINTPROTO,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.ClientSpawnPointProto)
  ))
_sym_db.RegisterMessage(ClientSpawnPointProto)

MapPokemonProto = _reflection.GeneratedProtocolMessageType('MapPokemonProto', (_message.Message,), dict(
  DESCRIPTOR = _MAPPOKEMONPROTO,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.MapPokemonProto)
  ))
_sym_db.RegisterMessage(MapPokemonProto)


# @@protoc_insertion_point(module_scope)
