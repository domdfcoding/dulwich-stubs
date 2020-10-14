from dulwich._pack import apply_delta as apply_delta, bisect_find_sha as bisect_find_sha
from dulwich.errors import ApplyDeltaError as ApplyDeltaError, ChecksumMismatch as ChecksumMismatch
from dulwich.file import GitFile as GitFile
from dulwich.lru_cache import LRUSizeCache as LRUSizeCache
from dulwich.objects import ShaFile as ShaFile, hex_to_sha as hex_to_sha, object_header as object_header, sha_to_hex as sha_to_hex
from typing import Any, Iterator, Optional, Sequence, Tuple

has_mmap: bool
OFS_DELTA: int
REF_DELTA: int
DELTA_TYPES: Any
DEFAULT_PACK_DELTA_WINDOW_SIZE: int

def take_msb_bytes(read: Any, crc32: Optional[Any] = ...): ...

class PackFileDisappeared(Exception):
    obj: Any = ...
    def __init__(self, obj: Any) -> None: ...

class UnpackedObject:
    offset: Any = ...
    pack_type_num: Any = ...
    delta_base: Any = ...
    comp_chunks: Any = ...
    decomp_chunks: Any = ...
    decomp_len: Any = ...
    crc32: Any = ...
    obj_type_num: Any = ...
    obj_chunks: Any = ...
    def __init__(self, pack_type_num: Any, delta_base: Any, decomp_len: Any, crc32: Any) -> None: ...
    def sha(self): ...
    def sha_file(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

def read_zlib_chunks(read_some: Any, unpacked: Any, include_comp: bool = ..., buffer_size: Any = ...): ...
def iter_sha1(iter: Any): ...
def load_pack_index(path: Any): ...
def load_pack_index_file(path: Any, f: Any): ...
def bisect_find_sha(start: Any, end: Any, sha: Any, unpack_name: Any): ...

class PackIndex:
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __len__(self) -> None: ...
    def __iter__(self) -> Any: ...
    def iterentries(self) -> None: ...
    def get_pack_checksum(self) -> None: ...
    def object_index(self, sha: Any): ...
    def object_sha1(self, index: Any): ...
    def objects_sha1(self): ...

class MemoryPackIndex(PackIndex):
    def __init__(self, entries: Any, pack_checksum: Optional[Any] = ...) -> None: ...
    def get_pack_checksum(self): ...
    def __len__(self): ...
    def object_sha1(self, index: Any): ...
    def iterentries(self): ...

class FilePackIndex(PackIndex):
    def __init__(self, filename: Any, file: Optional[Any] = ..., contents: Optional[Any] = ..., size: Optional[Any] = ...) -> None: ...
    @property
    def path(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def close(self) -> None: ...
    def __len__(self): ...
    def iterentries(self) -> None: ...
    def check(self) -> None: ...
    def calculate_checksum(self): ...
    def get_pack_checksum(self): ...
    def get_stored_checksum(self): ...

class PackIndex1(FilePackIndex):
    version: int = ...
    def __init__(self, filename: Any, file: Optional[Any] = ..., contents: Optional[Any] = ..., size: Optional[Any] = ...) -> None: ...

class PackIndex2(FilePackIndex):
    def __init__(self, filename: Any, file: Optional[Any] = ..., contents: Optional[Any] = ..., size: Optional[Any] = ...) -> None: ...

def read_pack_header(read: Any): ...
def chunks_length(chunks: Any): ...
def unpack_object(read_all: Any, read_some: Optional[Any] = ..., compute_crc32: bool = ..., include_comp: bool = ..., zlib_bufsize: Any = ...): ...

class PackStreamReader:
    read_all: Any = ...
    read_some: Any = ...
    sha: Any = ...
    def __init__(self, read_all: Any, read_some: Optional[Any] = ..., zlib_bufsize: Any = ...) -> None: ...
    @property
    def offset(self): ...
    def read(self, size: Any): ...
    def recv(self, size: Any): ...
    def __len__(self): ...
    def read_objects(self, compute_crc32: bool = ...) -> None: ...

class PackStreamCopier(PackStreamReader):
    outfile: Any = ...
    def __init__(self, read_all: Any, read_some: Any, outfile: Any, delta_iter: Optional[Any] = ...) -> None: ...
    def verify(self) -> None: ...

def obj_sha(type: Any, chunks: Any): ...
def compute_file_sha(f: Any, start_ofs: int = ..., end_ofs: int = ..., buffer_size: Any = ...): ...

class PackData:
    pack: Any = ...
    def __init__(self, filename: Any, file: Optional[Any] = ..., size: Optional[Any] = ...) -> None: ...
    @property
    def filename(self): ...
    @property
    def path(self): ...
    @classmethod
    def from_file(cls, file: Any, size: Any): ...
    @classmethod
    def from_path(cls, path: Any): ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def __len__(self): ...
    def calculate_checksum(self): ...
    def get_ref(self, sha: Any): ...
    def resolve_object(self, offset: Any, type: Any, obj: Any, get_ref: Optional[Any] = ...): ...
    def iterobjects(self, progress: Optional[Any] = ..., compute_crc32: bool = ...) -> None: ...
    def iterentries(self, progress: Optional[Any] = ...) -> None: ...
    def sorted_entries(self, progress: Optional[Any] = ...): ...
    def create_index_v1(self, filename: Any, progress: Optional[Any] = ...): ...
    def create_index_v2(self, filename: Any, progress: Optional[Any] = ...): ...
    def create_index(self, filename: Any, progress: Optional[Any] = ..., version: int = ...): ...
    def get_stored_checksum(self): ...
    def check(self) -> None: ...
    def get_compressed_data_at(self, offset: Any): ...
    def get_object_at(self, offset: Any): ...

class DeltaChainIterator:
    def __init__(self, file_obj: Any, resolve_ext_ref: Optional[Any] = ...) -> None: ...
    @classmethod
    def for_pack_data(cls, pack_data: Any, resolve_ext_ref: Optional[Any] = ...): ...
    def record(self, unpacked: Any) -> None: ...
    def set_pack_data(self, pack_data: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def ext_refs(self): ...

class PackIndexer(DeltaChainIterator): ...
class PackInflater(DeltaChainIterator): ...

class SHA1Reader:
    f: Any = ...
    sha1: Any = ...
    def __init__(self, f: Any) -> None: ...
    def read(self, num: Optional[Any] = ...): ...
    def check_sha(self) -> None: ...
    def close(self): ...
    def tell(self): ...

class SHA1Writer:
    f: Any = ...
    length: int = ...
    sha1: Any = ...
    def __init__(self, f: Any) -> None: ...
    def write(self, data: Any) -> None: ...
    def write_sha(self): ...
    def close(self): ...
    def offset(self): ...
    def tell(self): ...

def pack_object_header(type_num: Any, delta_base: Any, size: Any): ...
def write_pack_object(f: Any, type: Any, object: Any, sha: Optional[Any] = ..., compression_level: int = ...): ...
def write_pack(filename: Any, objects: Any, deltify: Optional[Any] = ..., delta_window_size: Optional[Any] = ..., compression_level: int = ...): ...
def write_pack_header(f: Any, num_objects: Any) -> None: ...
def deltify_pack_objects(objects: Any, window_size: Optional[Any] = ...) -> None: ...
def pack_objects_to_data(objects: Sequence[Pack]) -> Tuple[int, Iterator[Tuple[Any, Any, Any, Any]]]: ...
def write_pack_objects(f: Any, objects: Any, delta_window_size: Optional[Any] = ..., deltify: Optional[Any] = ..., compression_level: int = ...): ...
def write_pack_data(f: Any, num_records: Any, records: Any, progress: Optional[Any] = ..., compression_level: int = ...): ...
def write_pack_index_v1(f: Any, entries: Any, pack_checksum: Any): ...
def create_delta(base_buf: Any, target_buf: Any): ...
def apply_delta(src_buf: Any, delta: Any): ...
def write_pack_index_v2(f: Any, entries: Any, pack_checksum: Any): ...
write_pack_index = write_pack_index_v2

class Pack:
    resolve_ext_ref: Any = ...
    def __init__(self, basename: Any, resolve_ext_ref: Optional[Any] = ...): ...
    @classmethod
    def from_lazy_objects(cls, data_fn: Any, idx_fn: Any): ...
    @classmethod
    def from_objects(cls, data: Any, idx: Any): ...
    def name(self): ...
    @property
    def data(self): ...
    @property
    def index(self): ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def check_length_and_checksum(self) -> None: ...
    def check(self) -> None: ...
    def get_stored_checksum(self): ...
    def __contains__(self, sha1: Any): ...
    def get_raw_unresolved(self, sha1: Any): ...
    def get_raw(self, sha1: Any): ...
    def __getitem__(self, sha1: Any): ...
    def iterobjects(self): ...
    pack: Any = ...
    def pack_tuples(self): ...
    def keep(self, msg: Optional[Any] = ...): ...
