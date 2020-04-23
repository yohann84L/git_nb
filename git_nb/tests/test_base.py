import shutil
import unittest
from pathlib import Path

import git_nb
from git_nb import cfg


class TestBase(unittest.TestCase):
    cfg.username = "yohann84L"

    def test_git_clone_public(self):
        cfg.repo_name = "git_nb_test_repo"

        path = "../../"
        git_nb.git_clone(path)

        check = False
        # Check if repo cloned
        if Path(cfg.repo_name, "README.md").exists():
            check = True
            shutil.rmtree(Path(cfg.repo_name).as_posix())

        self.assertEqual(True, check)

    def test_git_clone_private(self):
        cfg.repo_name = "git_nb_test_privaterepo"

        path = "../../"
        git_nb.git_clone(path)

        check = False
        # Check if repo cloned
        if Path(cfg.repo_name, "README.md").exists():
            check = True
            shutil.rmtree(Path(cfg.repo_name).as_posix())

        self.assertEqual(True, check)


if __name__ == '__main__':
    unittest.main()
