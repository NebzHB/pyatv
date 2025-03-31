"""Unit tests for pyatv.protocols.companion.opack.

TODO: Add integration tests using pack and unpack together.
"""

from datetime import datetime
from uuid import UUID

from deepdiff import DeepDiff
import pytest

from pyatv.support.opack import _sized_int, pack, unpack

# pack


def test_pack_unsupported_type():
    with pytest.raises(TypeError):
        pack(set())


def test_pack_boolean():
    assert pack(True) == b"\x01"
    assert pack(False) == b"\x02"


def test_pack_none():
    assert pack(None) == b"\x04"


def test_pack_uuid():
    assert (
        pack(UUID("{12345678-1234-5678-1234-567812345678}"))
        == b"\x05\x124Vx\x124Vx\x124Vx\x124Vx"
    )


def test_pack_absolute_time():
    with pytest.raises(NotImplementedError):
        pack(datetime.now())


def test_pack_small_integers():
    assert pack(0) == b"\x08"
    assert pack(0xF) == b"\x17"
    assert pack(0x27) == b"\x2f"


def test_pack_larger_integers():
    assert pack(0x28) == b"\x30\x28"
    assert pack(0x1FF) == b"\x31\xff\x01"
    assert pack(0x1FFFFFF) == b"\x32\xff\xff\xff\x01"
    assert pack(0x1FFFFFFFFFFFFFF) == b"\x33\xff\xff\xff\xff\xff\xff\xff\x01"


def test_pack_sized_integers():
    assert pack(_sized_int(0x1, 1)) == b"\x30\x01"
    assert pack(_sized_int(0x1, 2)) == b"\x31\x01\x00"
    assert pack(_sized_int(0x1, 4)) == b"\x32\x01\x00\x00\x00"
    assert pack(_sized_int(0x1, 8)) == b"\x33\x01\x00\x00\x00\x00\x00\x00\x00"


def test_pack_float64():
    assert pack(1.0) == b"\x36\x00\x00\x00\x00\x00\x00\xf0\x3f"


def test_pack_short_strings():
    assert pack("a") == b"\x41\x61"
    assert pack("abc") == b"\x43\x61\x62\x63"
    assert pack(0x20 * "a") == b"\x60" + (0x20 * b"\x61")


def test_pack_longer_strings():
    assert pack(33 * "a") == b"\x61\x21" + (33 * b"\x61")
    assert pack(256 * "a") == b"\x62\x00\x01" + (256 * b"\x61")


def test_pack_short_raw_bytes():
    assert pack(b"\xac") == b"\x71\xac"
    assert pack(b"\x12\x34\x56") == b"\x73\x12\x34\x56"
    assert pack(0x20 * b"\xad") == b"\x90" + (0x20 * b"\xad")


def test_pack_longer_raw_bytes():
    assert pack(33 * b"\x61") == b"\x91\x21" + (33 * b"\x61")
    assert pack(256 * b"\x61") == b"\x92\x00\x01" + (256 * b"\x61")
    assert pack(65536 * b"\x61") == b"\x93\x00\x00\x01\x00" + (65536 * b"\x61")


def test_pack_array():
    assert pack([]) == b"\xd0"
    assert pack([1, "test", False]) == b"\xd3\x09\x44\x74\x65\x73\x74\x02"
    assert pack([[True]]) == b"\xd1\xd1\x01"


def test_pack_endless_array():
    assert pack(15 * ["a"]) == b"\xdf\x41\x61" + 14 * b"\xa0" + b"\x03"


def test_pack_dict():
    assert pack({}) == b"\xe0"
    assert pack({"a": 12, False: None}) == b"\xe2\x41\x61\x14\x02\x04"
    assert pack({True: {"a": 2}}) == b"\xe1\x01\xe1\x41\x61\x0a"


def test_pack_endless_dict():
    assert pack(dict((chr(x), chr(x + 1)) for x in range(97, 127, 2))) == (
        b"\xef" + b"\x41" + b"\x41".join(bytes([x]) for x in range(97, 127)) + b"\x03"
    )


def test_pack_ptr():
    assert pack(["a", "a"]) == b"\xd2\x41\x61\xa0"
    assert (
        pack(["foo", "bar", "foo", "bar"])
        == b"\xd4\x43\x66\x6f\x6f\x43\x62\x61\x72\xa0\xa1"
    )
    assert (
        pack({"a": "b", "c": {"d": "a"}, "d": True})
        == b"\xe3\x41\x61\x41\x62\x41\x63\xe1\x41\x64\xa0\xa3\x01"
    )


def test_pack_more_ptr():
    data = list(chr(x).encode() for x in range(257))
    assert (
        pack(data + data)
        == b"\xdf\x71\x00\x71\x01\x71\x02\x71\x03\x71\x04\x71\x05\x71\x06\x71"
        b"\x07\x71\x08\x71\x09\x71\x0a\x71\x0b\x71\x0c\x71\x0d\x71\x0e\x71"
        b"\x0f\x71\x10\x71\x11\x71\x12\x71\x13\x71\x14\x71\x15\x71\x16\x71"
        b"\x17\x71\x18\x71\x19\x71\x1a\x71\x1b\x71\x1c\x71\x1d\x71\x1e\x71"
        b"\x1f\x71\x20\x71\x21\x71\x22\x71\x23\x71\x24\x71\x25\x71\x26\x71"
        b"\x27\x71\x28\x71\x29\x71\x2a\x71\x2b\x71\x2c\x71\x2d\x71\x2e\x71"
        b"\x2f\x71\x30\x71\x31\x71\x32\x71\x33\x71\x34\x71\x35\x71\x36\x71"
        b"\x37\x71\x38\x71\x39\x71\x3a\x71\x3b\x71\x3c\x71\x3d\x71\x3e\x71"
        b"\x3f\x71\x40\x71\x41\x71\x42\x71\x43\x71\x44\x71\x45\x71\x46\x71"
        b"\x47\x71\x48\x71\x49\x71\x4a\x71\x4b\x71\x4c\x71\x4d\x71\x4e\x71"
        b"\x4f\x71\x50\x71\x51\x71\x52\x71\x53\x71\x54\x71\x55\x71\x56\x71"
        b"\x57\x71\x58\x71\x59\x71\x5a\x71\x5b\x71\x5c\x71\x5d\x71\x5e\x71"
        b"\x5f\x71\x60\x71\x61\x71\x62\x71\x63\x71\x64\x71\x65\x71\x66\x71"
        b"\x67\x71\x68\x71\x69\x71\x6a\x71\x6b\x71\x6c\x71\x6d\x71\x6e\x71"
        b"\x6f\x71\x70\x71\x71\x71\x72\x71\x73\x71\x74\x71\x75\x71\x76\x71"
        b"\x77\x71\x78\x71\x79\x71\x7a\x71\x7b\x71\x7c\x71\x7d\x71\x7e\x71"
        b"\x7f\x72\xc2\x80\x72\xc2\x81\x72\xc2\x82\x72\xc2\x83\x72\xc2\x84"
        b"\x72\xc2\x85\x72\xc2\x86\x72\xc2\x87\x72\xc2\x88\x72\xc2\x89\x72"
        b"\xc2\x8a\x72\xc2\x8b\x72\xc2\x8c\x72\xc2\x8d\x72\xc2\x8e\x72\xc2"
        b"\x8f\x72\xc2\x90\x72\xc2\x91\x72\xc2\x92\x72\xc2\x93\x72\xc2\x94"
        b"\x72\xc2\x95\x72\xc2\x96\x72\xc2\x97\x72\xc2\x98\x72\xc2\x99\x72"
        b"\xc2\x9a\x72\xc2\x9b\x72\xc2\x9c\x72\xc2\x9d\x72\xc2\x9e\x72\xc2"
        b"\x9f\x72\xc2\xa0\x72\xc2\xa1\x72\xc2\xa2\x72\xc2\xa3\x72\xc2\xa4"
        b"\x72\xc2\xa5\x72\xc2\xa6\x72\xc2\xa7\x72\xc2\xa8\x72\xc2\xa9\x72"
        b"\xc2\xaa\x72\xc2\xab\x72\xc2\xac\x72\xc2\xad\x72\xc2\xae\x72\xc2"
        b"\xaf\x72\xc2\xb0\x72\xc2\xb1\x72\xc2\xb2\x72\xc2\xb3\x72\xc2\xb4"
        b"\x72\xc2\xb5\x72\xc2\xb6\x72\xc2\xb7\x72\xc2\xb8\x72\xc2\xb9\x72"
        b"\xc2\xba\x72\xc2\xbb\x72\xc2\xbc\x72\xc2\xbd\x72\xc2\xbe\x72\xc2"
        b"\xbf\x72\xc3\x80\x72\xc3\x81\x72\xc3\x82\x72\xc3\x83\x72\xc3\x84"
        b"\x72\xc3\x85\x72\xc3\x86\x72\xc3\x87\x72\xc3\x88\x72\xc3\x89\x72"
        b"\xc3\x8a\x72\xc3\x8b\x72\xc3\x8c\x72\xc3\x8d\x72\xc3\x8e\x72\xc3"
        b"\x8f\x72\xc3\x90\x72\xc3\x91\x72\xc3\x92\x72\xc3\x93\x72\xc3\x94"
        b"\x72\xc3\x95\x72\xc3\x96\x72\xc3\x97\x72\xc3\x98\x72\xc3\x99\x72"
        b"\xc3\x9a\x72\xc3\x9b\x72\xc3\x9c\x72\xc3\x9d\x72\xc3\x9e\x72\xc3"
        b"\x9f\x72\xc3\xa0\x72\xc3\xa1\x72\xc3\xa2\x72\xc3\xa3\x72\xc3\xa4"
        b"\x72\xc3\xa5\x72\xc3\xa6\x72\xc3\xa7\x72\xc3\xa8\x72\xc3\xa9\x72"
        b"\xc3\xaa\x72\xc3\xab\x72\xc3\xac\x72\xc3\xad\x72\xc3\xae\x72\xc3"
        b"\xaf\x72\xc3\xb0\x72\xc3\xb1\x72\xc3\xb2\x72\xc3\xb3\x72\xc3\xb4"
        b"\x72\xc3\xb5\x72\xc3\xb6\x72\xc3\xb7\x72\xc3\xb8\x72\xc3\xb9\x72"
        b"\xc3\xba\x72\xc3\xbb\x72\xc3\xbc\x72\xc3\xbd\x72\xc3\xbe\x72\xc3"
        b"\xbf\x72\xc4\x80\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab"
        b"\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb"
        b"\xbc\xbd\xbe\xbf\xc0\xc1\x21\xc1\x22\xc1\x23\xc1\x24\xc1\x25\xc1"
        b"\x26\xc1\x27\xc1\x28\xc1\x29\xc1\x2a\xc1\x2b\xc1\x2c\xc1\x2d\xc1"
        b"\x2e\xc1\x2f\xc1\x30\xc1\x31\xc1\x32\xc1\x33\xc1\x34\xc1\x35\xc1"
        b"\x36\xc1\x37\xc1\x38\xc1\x39\xc1\x3a\xc1\x3b\xc1\x3c\xc1\x3d\xc1"
        b"\x3e\xc1\x3f\xc1\x40\xc1\x41\xc1\x42\xc1\x43\xc1\x44\xc1\x45\xc1"
        b"\x46\xc1\x47\xc1\x48\xc1\x49\xc1\x4a\xc1\x4b\xc1\x4c\xc1\x4d\xc1"
        b"\x4e\xc1\x4f\xc1\x50\xc1\x51\xc1\x52\xc1\x53\xc1\x54\xc1\x55\xc1"
        b"\x56\xc1\x57\xc1\x58\xc1\x59\xc1\x5a\xc1\x5b\xc1\x5c\xc1\x5d\xc1"
        b"\x5e\xc1\x5f\xc1\x60\xc1\x61\xc1\x62\xc1\x63\xc1\x64\xc1\x65\xc1"
        b"\x66\xc1\x67\xc1\x68\xc1\x69\xc1\x6a\xc1\x6b\xc1\x6c\xc1\x6d\xc1"
        b"\x6e\xc1\x6f\xc1\x70\xc1\x71\xc1\x72\xc1\x73\xc1\x74\xc1\x75\xc1"
        b"\x76\xc1\x77\xc1\x78\xc1\x79\xc1\x7a\xc1\x7b\xc1\x7c\xc1\x7d\xc1"
        b"\x7e\xc1\x7f\xc1\x80\xc1\x81\xc1\x82\xc1\x83\xc1\x84\xc1\x85\xc1"
        b"\x86\xc1\x87\xc1\x88\xc1\x89\xc1\x8a\xc1\x8b\xc1\x8c\xc1\x8d\xc1"
        b"\x8e\xc1\x8f\xc1\x90\xc1\x91\xc1\x92\xc1\x93\xc1\x94\xc1\x95\xc1"
        b"\x96\xc1\x97\xc1\x98\xc1\x99\xc1\x9a\xc1\x9b\xc1\x9c\xc1\x9d\xc1"
        b"\x9e\xc1\x9f\xc1\xa0\xc1\xa1\xc1\xa2\xc1\xa3\xc1\xa4\xc1\xa5\xc1"
        b"\xa6\xc1\xa7\xc1\xa8\xc1\xa9\xc1\xaa\xc1\xab\xc1\xac\xc1\xad\xc1"
        b"\xae\xc1\xaf\xc1\xb0\xc1\xb1\xc1\xb2\xc1\xb3\xc1\xb4\xc1\xb5\xc1"
        b"\xb6\xc1\xb7\xc1\xb8\xc1\xb9\xc1\xba\xc1\xbb\xc1\xbc\xc1\xbd\xc1"
        b"\xbe\xc1\xbf\xc1\xc0\xc1\xc1\xc1\xc2\xc1\xc3\xc1\xc4\xc1\xc5\xc1"
        b"\xc6\xc1\xc7\xc1\xc8\xc1\xc9\xc1\xca\xc1\xcb\xc1\xcc\xc1\xcd\xc1"
        b"\xce\xc1\xcf\xc1\xd0\xc1\xd1\xc1\xd2\xc1\xd3\xc1\xd4\xc1\xd5\xc1"
        b"\xd6\xc1\xd7\xc1\xd8\xc1\xd9\xc1\xda\xc1\xdb\xc1\xdc\xc1\xdd\xc1"
        b"\xde\xc1\xdf\xc1\xe0\xc1\xe1\xc1\xe2\xc1\xe3\xc1\xe4\xc1\xe5\xc1"
        b"\xe6\xc1\xe7\xc1\xe8\xc1\xe9\xc1\xea\xc1\xeb\xc1\xec\xc1\xed\xc1"
        b"\xee\xc1\xef\xc1\xf0\xc1\xf1\xc1\xf2\xc1\xf3\xc1\xf4\xc1\xf5\xc1"
        b"\xf6\xc1\xf7\xc1\xf8\xc1\xf9\xc1\xfa\xc1\xfb\xc1\xfc\xc1\xfd\xc1"
        b"\xfe\xc1\xff\xc2\x00\x01\x03"
    )


# unpack


def test_unpack_unsupported_type():
    with pytest.raises(TypeError):
        unpack(b"\x00")


def test_unpack_boolean():
    assert unpack(b"\x01") == (True, b"")
    assert unpack(b"\x02") == (False, b"")


def test_unpack_none():
    assert unpack(b"\x04") == (None, b"")


def test_unpack_uuid():
    assert unpack(b"\x05\x124Vx\x124Vx\x124Vx\x124Vx") == (
        UUID("{12345678-1234-5678-1234-567812345678}"),
        b"",
    )


def test_unpack_absolute_time():
    # TODO: This is not implemented, it only parses the time stamp as an integer
    assert unpack(b"\x06\x01\x00\x00\x00\x00\x00\x00\x00") == (1, b"")


def test_unpack_small_integers():
    assert unpack(b"\x08") == (0, b"")
    assert unpack(b"\x17") == (0xF, b"")
    assert unpack(b"\x2f") == (0x27, b"")


def test_unpack_larger_integers():
    assert unpack(b"\x30\x28") == (0x28, b"")
    assert unpack(b"\x31\xff\x01") == (0x1FF, b"")
    assert unpack(b"\x32\xff\xff\xff\x01") == (0x1FFFFFF, b"")
    assert unpack(b"\x33\xff\xff\xff\xff\xff\xff\xff\x01") == (0x1FFFFFFFFFFFFFF, b"")


def test_unpack_sized_integers():
    assert getattr(unpack(b"\x30\x01")[0], "size") == 1
    assert getattr(unpack(b"\x31\x01\x00")[0], "size") == 2
    assert getattr(unpack(b"\x32\x01\x00\x00\x00")[0], "size") == 4
    assert getattr(unpack(b"\x33\x01\x00\x00\x00\x00\x00\x00\x00")[0], "size") == 8


def test_pack_unfloat32():
    assert unpack(b"\x35\x00\x00\x80\x3f") == (1.0, b"")


def test_unpack_float64():
    assert unpack(b"\x36\x00\x00\x00\x00\x00\x00\xf0\x3f") == (1.0, b"")


def test_unpack_short_strings():
    assert unpack(b"\x41\x61") == ("a", b"")
    assert unpack(b"\x43\x61\x62\x63") == ("abc", b"")
    assert unpack(b"\x60" + (0x20 * b"\x61")) == (0x20 * "a", b"")


def test_unpack_longer_strings():
    assert unpack(b"\x61\x21" + (33 * b"\x61")) == (33 * "a", b"")
    assert unpack(b"\x62\x00\x01" + (256 * b"\x61")) == (256 * "a", b"")


def test_unpack_short_raw_bytes():
    assert unpack(b"\x71\xac") == (b"\xac", b"")
    assert unpack(b"\x73\x12\x34\x56") == (b"\x12\x34\x56", b"")
    assert unpack(b"\x90" + (0x20 * b"\xad")) == (0x20 * b"\xad", b"")


def test_unpack_longer_raw_bytes():
    assert unpack(b"\x91\x21" + (33 * b"\x61")) == (33 * b"\x61", b"")
    assert unpack(b"\x92\x00\x01" + (256 * b"\x61")) == (256 * b"\x61", b"")
    assert unpack(b"\x93\x00\x00\x01\x00" + (65536 * b"\x61")) == (65536 * b"\x61", b"")


def test_unpack_array():
    assert unpack(b"\xd0") == ([], b"")
    assert unpack(b"\xd3\x09\x44\x74\x65\x73\x74\x02") == ([1, "test", False], b"")
    assert unpack(b"\xd1\xd1\x01") == ([[True]], b"")


def test_unpack_endless_array():
    list1 = b"\xdf\x41\x61" + 15 * b"\xa0" + b"\x03"
    list2 = b"\xdf\x41\x62" + 15 * b"\xa1" + b"\x03"
    assert unpack(list1) == (16 * ["a"], b"")
    assert unpack(b"\xd2" + list1 + list2) == ([16 * ["a"], 16 * ["b"]], b"")


def test_unpack_dict():
    assert unpack(b"\xe0") == ({}, b"")
    assert unpack(b"\xe2\x41\x61\x14\x02\x04") == ({"a": 12, False: None}, b"")
    assert unpack(b"\xe1\x01\xe1\x41\x61\x0a") == ({True: {"a": 2}}, b"")


def test_unpack_endless_dict():
    assert unpack(
        b"\xef" + b"\x41" + b"\x41".join(bytes([x]) for x in range(97, 127)) + b"\x03"
    ) == (dict((chr(x), chr(x + 1)) for x in range(97, 127, 2)), b"")


def test_unpack_ptr():
    assert unpack(b"\xd2\x41\x61\xa0") == (["a", "a"], b"")
    assert unpack(b"\xd4\x43\x66\x6f\x6f\x43\x62\x61\x72\xa0\xa1") == (
        ["foo", "bar", "foo", "bar"],
        b"",
    )
    assert unpack(b"\xe3\x41\x61\x41\x62\x41\x63\xe1\x41\x64\xa0\xa3\x01") == (
        {"a": "b", "c": {"d": "a"}, "d": True},
        b"",
    )


def test_unpack_more_ptr():
    data = list(chr(x).encode() for x in range(257))
    assert unpack(
        b"\xdf\x71\x00\x71\x01\x71\x02\x71\x03\x71\x04\x71\x05\x71\x06\x71"
        b"\x07\x71\x08\x71\x09\x71\x0a\x71\x0b\x71\x0c\x71\x0d\x71\x0e\x71"
        b"\x0f\x71\x10\x71\x11\x71\x12\x71\x13\x71\x14\x71\x15\x71\x16\x71"
        b"\x17\x71\x18\x71\x19\x71\x1a\x71\x1b\x71\x1c\x71\x1d\x71\x1e\x71"
        b"\x1f\x71\x20\x71\x21\x71\x22\x71\x23\x71\x24\x71\x25\x71\x26\x71"
        b"\x27\x71\x28\x71\x29\x71\x2a\x71\x2b\x71\x2c\x71\x2d\x71\x2e\x71"
        b"\x2f\x71\x30\x71\x31\x71\x32\x71\x33\x71\x34\x71\x35\x71\x36\x71"
        b"\x37\x71\x38\x71\x39\x71\x3a\x71\x3b\x71\x3c\x71\x3d\x71\x3e\x71"
        b"\x3f\x71\x40\x71\x41\x71\x42\x71\x43\x71\x44\x71\x45\x71\x46\x71"
        b"\x47\x71\x48\x71\x49\x71\x4a\x71\x4b\x71\x4c\x71\x4d\x71\x4e\x71"
        b"\x4f\x71\x50\x71\x51\x71\x52\x71\x53\x71\x54\x71\x55\x71\x56\x71"
        b"\x57\x71\x58\x71\x59\x71\x5a\x71\x5b\x71\x5c\x71\x5d\x71\x5e\x71"
        b"\x5f\x71\x60\x71\x61\x71\x62\x71\x63\x71\x64\x71\x65\x71\x66\x71"
        b"\x67\x71\x68\x71\x69\x71\x6a\x71\x6b\x71\x6c\x71\x6d\x71\x6e\x71"
        b"\x6f\x71\x70\x71\x71\x71\x72\x71\x73\x71\x74\x71\x75\x71\x76\x71"
        b"\x77\x71\x78\x71\x79\x71\x7a\x71\x7b\x71\x7c\x71\x7d\x71\x7e\x71"
        b"\x7f\x72\xc2\x80\x72\xc2\x81\x72\xc2\x82\x72\xc2\x83\x72\xc2\x84"
        b"\x72\xc2\x85\x72\xc2\x86\x72\xc2\x87\x72\xc2\x88\x72\xc2\x89\x72"
        b"\xc2\x8a\x72\xc2\x8b\x72\xc2\x8c\x72\xc2\x8d\x72\xc2\x8e\x72\xc2"
        b"\x8f\x72\xc2\x90\x72\xc2\x91\x72\xc2\x92\x72\xc2\x93\x72\xc2\x94"
        b"\x72\xc2\x95\x72\xc2\x96\x72\xc2\x97\x72\xc2\x98\x72\xc2\x99\x72"
        b"\xc2\x9a\x72\xc2\x9b\x72\xc2\x9c\x72\xc2\x9d\x72\xc2\x9e\x72\xc2"
        b"\x9f\x72\xc2\xa0\x72\xc2\xa1\x72\xc2\xa2\x72\xc2\xa3\x72\xc2\xa4"
        b"\x72\xc2\xa5\x72\xc2\xa6\x72\xc2\xa7\x72\xc2\xa8\x72\xc2\xa9\x72"
        b"\xc2\xaa\x72\xc2\xab\x72\xc2\xac\x72\xc2\xad\x72\xc2\xae\x72\xc2"
        b"\xaf\x72\xc2\xb0\x72\xc2\xb1\x72\xc2\xb2\x72\xc2\xb3\x72\xc2\xb4"
        b"\x72\xc2\xb5\x72\xc2\xb6\x72\xc2\xb7\x72\xc2\xb8\x72\xc2\xb9\x72"
        b"\xc2\xba\x72\xc2\xbb\x72\xc2\xbc\x72\xc2\xbd\x72\xc2\xbe\x72\xc2"
        b"\xbf\x72\xc3\x80\x72\xc3\x81\x72\xc3\x82\x72\xc3\x83\x72\xc3\x84"
        b"\x72\xc3\x85\x72\xc3\x86\x72\xc3\x87\x72\xc3\x88\x72\xc3\x89\x72"
        b"\xc3\x8a\x72\xc3\x8b\x72\xc3\x8c\x72\xc3\x8d\x72\xc3\x8e\x72\xc3"
        b"\x8f\x72\xc3\x90\x72\xc3\x91\x72\xc3\x92\x72\xc3\x93\x72\xc3\x94"
        b"\x72\xc3\x95\x72\xc3\x96\x72\xc3\x97\x72\xc3\x98\x72\xc3\x99\x72"
        b"\xc3\x9a\x72\xc3\x9b\x72\xc3\x9c\x72\xc3\x9d\x72\xc3\x9e\x72\xc3"
        b"\x9f\x72\xc3\xa0\x72\xc3\xa1\x72\xc3\xa2\x72\xc3\xa3\x72\xc3\xa4"
        b"\x72\xc3\xa5\x72\xc3\xa6\x72\xc3\xa7\x72\xc3\xa8\x72\xc3\xa9\x72"
        b"\xc3\xaa\x72\xc3\xab\x72\xc3\xac\x72\xc3\xad\x72\xc3\xae\x72\xc3"
        b"\xaf\x72\xc3\xb0\x72\xc3\xb1\x72\xc3\xb2\x72\xc3\xb3\x72\xc3\xb4"
        b"\x72\xc3\xb5\x72\xc3\xb6\x72\xc3\xb7\x72\xc3\xb8\x72\xc3\xb9\x72"
        b"\xc3\xba\x72\xc3\xbb\x72\xc3\xbc\x72\xc3\xbd\x72\xc3\xbe\x72\xc3"
        b"\xbf\x72\xc4\x80\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab"
        b"\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb"
        b"\xbc\xbd\xbe\xbf\xc0\xc1\x21\xc1\x22\xc1\x23\xc1\x24\xc1\x25\xc1"
        b"\x26\xc1\x27\xc1\x28\xc1\x29\xc1\x2a\xc1\x2b\xc1\x2c\xc1\x2d\xc1"
        b"\x2e\xc1\x2f\xc1\x30\xc1\x31\xc1\x32\xc1\x33\xc1\x34\xc1\x35\xc1"
        b"\x36\xc1\x37\xc1\x38\xc1\x39\xc1\x3a\xc1\x3b\xc1\x3c\xc1\x3d\xc1"
        b"\x3e\xc1\x3f\xc1\x40\xc1\x41\xc1\x42\xc1\x43\xc1\x44\xc1\x45\xc1"
        b"\x46\xc1\x47\xc1\x48\xc1\x49\xc1\x4a\xc1\x4b\xc1\x4c\xc1\x4d\xc1"
        b"\x4e\xc1\x4f\xc1\x50\xc1\x51\xc1\x52\xc1\x53\xc1\x54\xc1\x55\xc1"
        b"\x56\xc1\x57\xc1\x58\xc1\x59\xc1\x5a\xc1\x5b\xc1\x5c\xc1\x5d\xc1"
        b"\x5e\xc1\x5f\xc1\x60\xc1\x61\xc1\x62\xc1\x63\xc1\x64\xc1\x65\xc1"
        b"\x66\xc1\x67\xc1\x68\xc1\x69\xc1\x6a\xc1\x6b\xc1\x6c\xc1\x6d\xc1"
        b"\x6e\xc1\x6f\xc1\x70\xc1\x71\xc1\x72\xc1\x73\xc1\x74\xc1\x75\xc1"
        b"\x76\xc1\x77\xc1\x78\xc1\x79\xc1\x7a\xc1\x7b\xc1\x7c\xc1\x7d\xc1"
        b"\x7e\xc1\x7f\xc1\x80\xc1\x81\xc1\x82\xc1\x83\xc1\x84\xc1\x85\xc1"
        b"\x86\xc1\x87\xc1\x88\xc1\x89\xc1\x8a\xc1\x8b\xc1\x8c\xc1\x8d\xc1"
        b"\x8e\xc1\x8f\xc1\x90\xc1\x91\xc1\x92\xc1\x93\xc1\x94\xc1\x95\xc1"
        b"\x96\xc1\x97\xc1\x98\xc1\x99\xc1\x9a\xc1\x9b\xc1\x9c\xc1\x9d\xc1"
        b"\x9e\xc1\x9f\xc1\xa0\xc1\xa1\xc1\xa2\xc1\xa3\xc1\xa4\xc1\xa5\xc1"
        b"\xa6\xc1\xa7\xc1\xa8\xc1\xa9\xc1\xaa\xc1\xab\xc1\xac\xc1\xad\xc1"
        b"\xae\xc1\xaf\xc1\xb0\xc1\xb1\xc1\xb2\xc1\xb3\xc1\xb4\xc1\xb5\xc1"
        b"\xb6\xc1\xb7\xc1\xb8\xc1\xb9\xc1\xba\xc1\xbb\xc1\xbc\xc1\xbd\xc1"
        b"\xbe\xc1\xbf\xc1\xc0\xc1\xc1\xc1\xc2\xc1\xc3\xc1\xc4\xc1\xc5\xc1"
        b"\xc6\xc1\xc7\xc1\xc8\xc1\xc9\xc1\xca\xc1\xcb\xc1\xcc\xc1\xcd\xc1"
        b"\xce\xc1\xcf\xc1\xd0\xc1\xd1\xc1\xd2\xc1\xd3\xc1\xd4\xc1\xd5\xc1"
        b"\xd6\xc1\xd7\xc1\xd8\xc1\xd9\xc1\xda\xc1\xdb\xc1\xdc\xc1\xdd\xc1"
        b"\xde\xc1\xdf\xc1\xe0\xc1\xe1\xc1\xe2\xc1\xe3\xc1\xe4\xc1\xe5\xc1"
        b"\xe6\xc1\xe7\xc1\xe8\xc1\xe9\xc1\xea\xc1\xeb\xc1\xec\xc1\xed\xc1"
        b"\xee\xc1\xef\xc1\xf0\xc1\xf1\xc1\xf2\xc1\xf3\xc1\xf4\xc1\xf5\xc1"
        b"\xf6\xc1\xf7\xc1\xf8\xc1\xf9\xc1\xfa\xc1\xfb\xc1\xfc\xc1\xfd\xc1"
        b"\xfe\xc1\xff\xc2\x00\x01\x03"
    ) == (data + data, b"")


def test_unpack_uid():
    assert unpack(b"\xdf\x30\x01\x30\x02\xc1\x01\x03") == ([1, 2, 2], b"")
    assert unpack(b"\xdf\x30\x01\x30\x02\xc2\x01\x00\x03") == ([1, 2, 2], b"")
    assert unpack(b"\xdf\x30\x01\x30\x02\xc3\x01\x00\x00\x03") == ([1, 2, 2], b"")
    assert unpack(b"\xdf\x30\x01\x30\x02\xc4\x01\x00\x00\x00\x03") == ([1, 2, 2], b"")


def test_golden():
    data = {
        "_i": "_systemInfo",
        "_x": 1254122577,
        "_btHP": False,
        "_c": {
            "_pubID": "AA:BB:CC:DD:EE:FF",
            "_sv": "230.1",
            "_bf": 0,
            "_siriInfo": {
                "collectorElectionVersion": 1.0,
                "deviceCapabilities": {"seymourEnabled": 1, "voiceTriggerEnabled": 2},
                "sharedDataProtoBuf": 512 * b"\x08",
            },
            "_stA": [
                "com.apple.LiveAudio",
                "com.apple.siri.wakeup",
                "com.apple.Seymour",
                "com.apple.announce",
                "com.apple.coreduet.sync",
                "com.apple.SeymourSession",
            ],
            "_i": "6c62fca18b11",
            "_clFl": 128,
            "_idsID": "44E14ABC-DDDD-4188-B661-11BAAAF6ECDE",
            "_hkUID": [UUID("17ed160a-81f8-4488-962c-6b1a83eb0081")],
            "_dC": "1",
            "_sf": 256,
            "model": "iPhone10,6",
            "name": "iPhone",
        },
        "_t": 2,
    }

    packed = pack(data)
    unpacked = unpack(packed)

    assert DeepDiff(unpacked, data, ignore_order=True)
