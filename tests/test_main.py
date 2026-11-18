import tempfile
import unittest
from pathlib import Path
from main import deduplicate

class JsonlDeduperTests(unittest.TestCase):
    def test_deduplicates_by_selected_nested_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/"in.jsonl"; target=root/"out.jsonl"
            source.write_text('{"user":{"id":1},"event":"open"}\n{"event":"close","user":{"id":1}}\n{"user":{"id":2},"event":"open"}\n',encoding="utf-8")
            self.assertEqual(deduplicate(source,target,["user.id"]),(2,1,0))
            self.assertEqual(len(target.read_text(encoding="utf-8").splitlines()),2)

if __name__=="__main__": unittest.main()
