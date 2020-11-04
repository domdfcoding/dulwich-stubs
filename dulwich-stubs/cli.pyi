from typing import Any, Dict, NoReturn, Optional, Type

def signal_int(signal: Any, frame: Any) -> NoReturn: ...
def signal_quit(signal: Any, frame: Any) -> None: ...

class Command:
	def run(self, args: Any) -> None: ...

class cmd_archive(Command):
	def run(self, args: Any) -> None: ...

class cmd_add(Command):
	def run(self, args: Any) -> None: ...

class cmd_rm(Command):
	def run(self, args: Any) -> None: ...

class cmd_fetch_pack(Command):
	def run(self, args: Any): ...

class cmd_fetch(Command):
	def run(self, args: Any) -> None: ...

class cmd_fsck(Command):
	def run(self, args: Any) -> None: ...

class cmd_log(Command):
	def run(self, args: Any) -> None: ...

class cmd_diff(Command):
	def run(self, args: Any) -> None: ...

class cmd_dump_pack(Command):
	def run(self, args: Any) -> None: ...

class cmd_dump_index(Command):
	def run(self, args: Any) -> None: ...

class cmd_init(Command):
	def run(self, args: Any) -> None: ...

class cmd_clone(Command):
	def run(self, args: Any) -> None: ...

class cmd_commit(Command):
	def run(self, args: Any) -> None: ...

class cmd_commit_tree(Command):
	def run(self, args: Any) -> None: ...

class cmd_update_server_info(Command):
	def run(self, args: Any) -> None: ...

class cmd_symbolic_ref(Command):
	def run(self, args: Any) -> None: ...

class cmd_show(Command):
	def run(self, args: Any) -> None: ...

class cmd_diff_tree(Command):
	def run(self, args: Any) -> None: ...

class cmd_rev_list(Command):
	def run(self, args: Any) -> None: ...

class cmd_tag(Command):
	def run(self, args: Any) -> None: ...

class cmd_repack(Command):
	def run(self, args: Any) -> None: ...

class cmd_reset(Command):
	def run(self, args: Any) -> None: ...

class cmd_daemon(Command):
	def run(self, args: Any) -> None: ...

class cmd_web_daemon(Command):
	def run(self, args: Any) -> None: ...

class cmd_write_tree(Command):
	def run(self, args: Any) -> None: ...

class cmd_receive_pack(Command):
	def run(self, args: Any) -> None: ...

class cmd_upload_pack(Command):
	def run(self, args: Any) -> None: ...

class cmd_status(Command):
	def run(self, args: Any) -> None: ...

class cmd_ls_remote(Command):
	def run(self, args: Any) -> None: ...

class cmd_ls_tree(Command):
	def run(self, args: Any) -> None: ...

class cmd_pack_objects(Command):
	def run(self, args: Any) -> None: ...

class cmd_pull(Command):
	def run(self, args: Any) -> None: ...

class cmd_push(Command):
	def run(self, args: Any) -> None: ...

class cmd_remote_add(Command):
	def run(self, args: Any) -> None: ...

class SuperCommand(Command):
	subcommands: Dict[str, Type[Command]] = ...
	def run(self, args: Any): ...

class cmd_remote(SuperCommand):
	subcommands: Any = ...

class cmd_check_ignore(Command):
	def run(self, args: Any): ...

class cmd_check_mailmap(Command):
	def run(self, args: Any) -> None: ...

class cmd_stash_list(Command):
	def run(self, args: Any) -> None: ...

class cmd_stash_push(Command):
	def run(self, args: Any) -> None: ...

class cmd_stash_pop(Command):
	def run(self, args: Any) -> None: ...

class cmd_stash(SuperCommand):
	subcommands: Any = ...

class cmd_ls_files(Command):
	def run(self, args: Any) -> None: ...

class cmd_describe(Command):
	def run(self, args: Any) -> None: ...

class cmd_help(Command):
	def run(self, args: Any) -> None: ...

commands: Any

def main(argv: Optional[Any] = ...): ...
