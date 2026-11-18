from __future__ import annotations

from typing import TYPE_CHECKING

from copier_project_generic_temp_test.__main__ import main

if TYPE_CHECKING:
    from syrupy.assertion import SnapshotAssertion


def test_main() -> None:
    main()


def test_snap(snapshot: SnapshotAssertion) -> None:
    assert snapshot == "do the thing"
