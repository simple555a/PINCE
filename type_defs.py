# -*- coding: utf-8 -*-
# IMPORTANT: Any constant involving only PINCE.py should be declared in PINCE.py

class PATHS:
    PINCE_IPC_PATH = "/tmp/PINCE-connection/"
    INITIAL_INJECTION_PATH = "/Injection/InitialCodeInjections.so"
    IPC_FROM_PINCE_PATH = "/from_PINCE_file"
    IPC_TO_PINCE_PATH = "/to_PINCE_file"


class INFERIOR_STATUS:
    INFERIOR_RUNNING = 0
    INFERIOR_STOPPED = 1


class INFERIOR_ARCH:
    ARCH_32 = 0
    ARCH_64 = 1


class INJECTION_METHOD:
    NO_INJECTION = 0
    SIMPLE_DLOPEN_CALL = 1
    LINUX_INJECT = 2


class INJECTION_RESULT:
    INJECTION_SUCCESSFUL = 1
    INJECTION_FAILED = 0
    NO_INJECTION_ATTEMPT = -1


# represents the indexes of value types
# Also used in PINCE's value comboboxes
class VALUE_INDEX:
    INDEX_BYTE = 0
    INDEX_2BYTES = 1
    INDEX_4BYTES = 2
    INDEX_8BYTES = 3
    INDEX_FLOAT = 4
    INDEX_DOUBLE = 5
    INDEX_STRING = 6
    INDEX_AOB = 7  # Array of Bytes


# Represents the texts at indexes in combobox
index_to_text_dict = {
    VALUE_INDEX.INDEX_BYTE: "Byte",
    VALUE_INDEX.INDEX_2BYTES: "2 Bytes",
    VALUE_INDEX.INDEX_4BYTES: "4 Bytes",
    VALUE_INDEX.INDEX_8BYTES: "8 Bytes",
    VALUE_INDEX.INDEX_FLOAT: "Float",
    VALUE_INDEX.INDEX_DOUBLE: "Double",
    VALUE_INDEX.INDEX_STRING: "String",
    VALUE_INDEX.INDEX_AOB: "AoB"
}

text_to_index_dict = {
    "Byte": VALUE_INDEX.INDEX_BYTE,
    "2 Bytes": VALUE_INDEX.INDEX_2BYTES,
    "4 Bytes": VALUE_INDEX.INDEX_4BYTES,
    "8 Bytes": VALUE_INDEX.INDEX_8BYTES,
    "Float": VALUE_INDEX.INDEX_FLOAT,
    "Double": VALUE_INDEX.INDEX_DOUBLE
}

# A dictionary used to convert value_combobox index to gdb/mi x command
# Check GDB_Engine for an exemplary usage
index_to_gdbcommand_dict = {
    VALUE_INDEX.INDEX_BYTE: "db",
    VALUE_INDEX.INDEX_2BYTES: "dh",
    VALUE_INDEX.INDEX_4BYTES: "dw",
    VALUE_INDEX.INDEX_8BYTES: "dg",
    VALUE_INDEX.INDEX_FLOAT: "fw",
    VALUE_INDEX.INDEX_DOUBLE: "fg",
    VALUE_INDEX.INDEX_STRING: "xb",
    VALUE_INDEX.INDEX_AOB: "xb"
}

# first value is the length and the second one is the type
# Check ScriptUtils for an exemplary usage
index_to_valuetype_dict = {
    VALUE_INDEX.INDEX_BYTE: [1, "b"],
    VALUE_INDEX.INDEX_2BYTES: [2, "h"],
    VALUE_INDEX.INDEX_4BYTES: [4, "i"],
    VALUE_INDEX.INDEX_8BYTES: [8, "q"],
    VALUE_INDEX.INDEX_FLOAT: [4, "f"],
    VALUE_INDEX.INDEX_DOUBLE: [8, "d"],
    VALUE_INDEX.INDEX_STRING: [None, None],
    VALUE_INDEX.INDEX_AOB: [None, None]
}

# Check ScriptUtils for an exemplary usage
index_to_struct_pack_dict = {
    VALUE_INDEX.INDEX_BYTE: "B",
    VALUE_INDEX.INDEX_2BYTES: "H",
    VALUE_INDEX.INDEX_4BYTES: "I",
    VALUE_INDEX.INDEX_8BYTES: "Q",
    VALUE_INDEX.INDEX_FLOAT: "f",
    VALUE_INDEX.INDEX_DOUBLE: "d"
}
